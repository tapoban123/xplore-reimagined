from datetime import datetime

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
import io
import uuid

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Spacer, FrameBreak
from PyPDF2 import PdfWriter, PdfReader
from sqlmodel import select

from ...entities.entities import Student, StudentPsychometrics
from ...utils.constants import API_KEYS, LLM_MODELS
from ...utils.helper import get_age_from_dob
from .output_parser_models import AllQuestionsModel, CareersOutputModel
from .prompts import GENERATE_PSYCHOMETRIC_QUESTIONS_PROMPT, GENERATE_CAREERS_PROMPT
from ...utils.pdf_generation_manager import PDFComponentGenerationManager
from ...database.core import db_dependency


def get_llm() -> ChatGoogleGenerativeAI:
    """Returns the Google Gemini LLM instance."""
    llm = ChatGoogleGenerativeAI(
        google_api_key=API_KEYS.GOOGLE_GEMINI_API_KEY,
        model=LLM_MODELS.GOOGLE_GEMINI_MODEL,
    )
    return llm


def get_questions():
    """Generates 20 psychometric questions for the user to answer."""
    llm = get_llm()
    pydantic_parser = PydanticOutputParser(pydantic_object=AllQuestionsModel)
    prompt = PromptTemplate(
        template=f"""{GENERATE_PSYCHOMETRIC_QUESTIONS_PROMPT}\n\n{{format_instructions}}""",
        partial_variables={
            "format_instructions": pydantic_parser.get_format_instructions()
        },
    )

    chain = prompt | llm | pydantic_parser
    questions = chain.invoke({})

    return questions


def get_careers(questions: list):
    """Generates 3 most suitable careers for the student as per their psychometrics."""
    llm = get_llm()
    careers_parser = PydanticOutputParser(pydantic_object=CareersOutputModel)

    prompt = PromptTemplate(
        template=f"""{GENERATE_CAREERS_PROMPT}\n\n{{qna}}\n\n\n{{format_instructions}}""",
        input_variables=["qna"],
        partial_variables={
            "format_instructions": careers_parser.get_format_instructions()
        },
    )

    chain = prompt | llm | careers_parser
    careers = chain.invoke({"qna": questions})
    return careers


def generate_pdf(user: Student, careers_output: CareersOutputModel) -> tuple:
    """Generate psychometric analysis report in PDF format."""
    new_pdf_buffer = io.BytesIO()
    file_name = f"report_{user.id}.pdf"
    document_title = "Psychometric Analysis Report"

    # -------- Creating user info -----------
    user_info = PDFComponentGenerationManager()
    user_info.create_frame(x1=50, y1=A4[1] - 430, width=500, height=120,
                           leftPadding=30, )
    user_info_style = user_info.get_paragraph_style(leftIndent=100)

    user_info.content.append(Paragraph(user.name, user_info_style))
    user_info.content.append(Spacer(height=8, width=0))
    user_info.content.append(Paragraph(str(get_age_from_dob(datetime.now(), user.date_of_birth)), user_info_style))
    user_info.content.append(Spacer(height=8, width=0))
    user_info.content.append(Paragraph(user.institution, user_info_style))
    user_info.prepare_pdf()

    # -------- Creating psychometric chart & careers -----------
    charts_and_careers = PDFComponentGenerationManager()
    charts_and_careers.create_frame(x1=0, y1=385, width=A4[0], height=A4[1] - (A4[1] / 2),
                                    leftPadding=140, )
    charts_and_careers.create_frame(x1=0, y1=0, width=A4[0], height=330,
                                    leftPadding=60, rightPadding=20, )
    psychometrics_chart = charts_and_careers.create_horizontal_bar_chart(
        psychometrics_len=len(careers_output.psychometrics),
        category_names=[x.parameter for x in careers_output.psychometrics],
        data=[tuple([x.score for x in careers_output.psychometrics])],
        x=0,
        y=-200,
        minValue=0,
        maxValue=10,
        lables_dx=-10,
    )
    charts_and_careers_style = charts_and_careers.get_paragraph_style(
        fontSize=16,
        leading=20,
        bulletFontSize=20,
        textColor=HexColor(0x222222)
    )
    careers = [f"<bullet>&bull;</bullet> <b>{x.career}:</b> {x.explanation}" for x in careers_output.careers]
    charts_and_careers.content.extend([psychometrics_chart, FrameBreak()])

    for i in range(len(careers)):
        charts_and_careers.content.append(Paragraph(careers[i], charts_and_careers_style))

        if i != len(careers) - 1:
            spacer = charts_and_careers.create_spacer()
            charts_and_careers.content.append(spacer)

    charts_and_careers.prepare_pdf()

    # --------- Generating new pdf ----------
    new_page1 = PdfReader(user_info.buffer)
    new_page3 = PdfReader(charts_and_careers.buffer)
    report_pdf = PdfReader(open("static/documents/Psychometric_Test_Report.pdf", mode="rb"))
    output = PdfWriter()

    page1 = report_pdf.pages[0]
    page2 = report_pdf.pages[1]
    page3 = report_pdf.pages[2]

    page1.merge_page(new_page1.pages[0])
    page3.merge_page(new_page3.pages[0])

    output.add_page(page1)
    output.add_page(page2)
    output.add_page(page3)

    output.write(new_pdf_buffer)
    return (file_name, new_pdf_buffer.getvalue())


def store_psychometrics_to_db(db: db_dependency, careers_output: CareersOutputModel, report_url: str, student_id: str):
    """Store the psychometric scores of the student to database along with the generated report url."""
    query = select(StudentPsychometrics).where(StudentPsychometrics.student_id == student_id)
    user = db.exec(query).first()

    psychometrics = {x.parameter: x.score for x in careers_output.psychometrics}

    if not user:
        metrics_id = uuid.uuid4().hex
        metrics = StudentPsychometrics(
            id=metrics_id,
            student_id=student_id,
            report_url=report_url,
            Analytical_Thinking=psychometrics["Analytical Thinking"],
            Creativity=psychometrics["Creativity"],
            Emotional_Intelligence=psychometrics["Emotional Intelligence"],
            Leadership=psychometrics["Leadership"],
            Communication_Skills=psychometrics["Communication Skills"],
            Risk_taking=psychometrics["Risk-taking"],
            Attention_to_Detail=psychometrics["Attention to Detail"],
            Problem_solving=psychometrics["Problem-solving"],
            Empathy=psychometrics["Empathy"],
            Teamwork=psychometrics["Teamwork"],
            Independence=psychometrics["Independence"],
            Decision_making=psychometrics["Decision-making"],
            STEM_Interest=psychometrics["STEM Interest"],
            Humanities_Interest=psychometrics["Humanities Interest"],
            Business_Interest=psychometrics["Business Interest"],
            Design_or_Arts=psychometrics["Design/Arts Interest"],
            Social_Work_Interest=psychometrics["Social Work Interest"]
        )
        db.add(metrics)
        db.commit()

    else:
        user.report_url = report_url
        user.Analytical_Thinking = psychometrics["Analytical Thinking"]
        user.Creativity = psychometrics["Creativity"]
        user.Emotional_Intelligence = psychometrics["Emotional Intelligence"]
        user.Leadership = psychometrics["Leadership"]
        user.Communication_Skills = psychometrics["Communication Skills"]
        user.Risk_taking = psychometrics["Risk-taking"]
        user.Attention_to_Detail = psychometrics["Attention to Detail"]
        user.Problem_solving = psychometrics["Problem-solving"]
        user.Empathy = psychometrics["Empathy"]
        user.Teamwork = psychometrics["Teamwork"]
        user.Independence = psychometrics["Independence"]
        user.Decision_making = psychometrics["Decision-making"]
        user.STEM_Interest = psychometrics["STEM Interest"]
        user.Humanities_Interest = psychometrics["Humanities Interest"]
        user.Business_Interest = psychometrics["Business Interest"]
        user.Design_or_Arts = psychometrics["Design/Arts Interest"]
        user.Social_Work_Interest = psychometrics["Social Work Interest"]

        db.add(user)
        db.commit()
