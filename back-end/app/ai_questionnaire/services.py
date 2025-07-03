from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from ..utils.env_secrets import API_KEYS, LLM_MODELS
from .output_parser_models import AllQuestionsModel, CareersOutputModel


def get_llm() -> ChatGoogleGenerativeAI:
    """Returns the Google Gemini LLM instance."""
    llm = ChatGoogleGenerativeAI(
        google_api_key=API_KEYS.GOOGLE_GEMINI_API_KEY.value,
        model=LLM_MODELS.GOOGLE_GEMINI_MODEL,
    )
    return llm


def get_questions():
    """Generates 20 psychometric questions for the user to answer."""
    llm = get_llm()
    pydantic_parser = PydanticOutputParser(pydantic_object=AllQuestionsModel)
    prompt = PromptTemplate(
        template="""Generate me 20 psychometric questions with 4 choices for each. The user will answer those psychometric questions and 
        you will have to analyse the best 3 career choices for the user from the answers to those questions.
        \n\n{format_instructions}  
        """,
        partial_variables={"format_instructions": pydantic_parser.get_format_instructions()},
    )
    chain = prompt | llm | pydantic_parser
    questions = chain.invoke({})

    return questions


def get_careers(questions: list):
    llm = get_llm()
    careers_parser = PydanticOutputParser(pydantic_object=CareersOutputModel)

    prompt = PromptTemplate(
        template="""You are a professional Career Counselor cum Psychiatrist. 
        Provided below is are 20 questions and their answers as answered by the user. 
        I want you to,
        1. Analyse the answers well
        2. Understand the intellect and other psychometrics' level of the student.
        3. Return me 3 most suitable career options for the user.
        The career choices to be returned must be appropriate and practical for an Indian user.
        
        \n{qna}
        \n\n{format_instructions}
        """,
        input_variables=["qna"],
        partial_variables={"format_instructions": careers_parser.get_format_instructions()},
    )

    chain = prompt | llm | careers_parser
    careers = chain.invoke({"qna": questions})
    return careers
