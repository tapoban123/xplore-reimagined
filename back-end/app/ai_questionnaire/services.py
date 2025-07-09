from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from ..utils.env_secrets import API_KEYS, LLM_MODELS
from .output_parser_models import AllQuestionsModel, CareersOutputModel
from .prompts import GENERATE_PSYCHOMETRIC_QUESTIONS_PROMPT, GENERATE_CAREERS_PROMPT


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
        template=f"""{GENERATE_PSYCHOMETRIC_QUESTIONS_PROMPT}\n\n{{format_instructions}}""",
        partial_variables={"format_instructions": pydantic_parser.get_format_instructions()},
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
        partial_variables={"format_instructions": careers_parser.get_format_instructions()},
    )

    chain = prompt | llm | careers_parser
    careers = chain.invoke({"qna": questions})
    return careers
