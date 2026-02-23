from ASR.main import invoke_ASR 
from TextToSpeech.main import invoke_TTS
from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate

# llm 
llm = ChatOllama(
    model='llama3.2',
    verbose=True,
    temperature=0.2
)

from pydantic import BaseModel, Field
from typing import Annotated

class StructuredOutput(BaseModel):
    clean_voice : Annotated[str, Field(description="Raw voice input cleaned by LLM.")]

if __name__ == "__main__":
    quest = invoke_ASR()
    # using LLM to correct words spoken by human
    template = "Correct the words spoken by user raw voice input : {raw_voice_input}, and you need to convert it to clean voice input of user.  " \
    "Examples : Raw voice input -> i AM GOD, what are u doin" \
    "Clean voice input -> I am good, what are you doing?"
    prompt = PromptTemplate(
        template=template,
        input_variables=['raw_voice_input']
    )

    llm_str = llm.with_structured_output(StructuredOutput)
    chain = prompt | llm_str
    question = chain.invoke({'raw_voice_input' : quest})
    print(f"Question : {question.clean_voice}")

    answer = "Hey Buddy! I'm doing good."
    invoke_TTS(answer)