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

# class StructuredOutput(BaseModel):
#     clean_voice : Annotated[str, Field(description="Raw voice input cleaned by LLM.")]

# function to find whether 'quit', 'exit', or 'end' like keywords are in the user question 
def check_exit(user_question):
    exit_words = ['quit', 'exit', 'end', 'stop', 'goodbye', 'bye']
    user_words = user_question.split()
    for word in user_words:
        if word.lower() in exit_words:
            return True 
    return False

if __name__ == "__main__":
    chat_history = []
    user_question = invoke_ASR()

    chat_history.append("User question: " + user_question)
    while check_exit(user_question) == False:

        chat_template = "Given a user_question and chat_history, you need to answer it like a second human. user question : {user_question}, chat_history : {chat_history}"

        chat_prompt = PromptTemplate(
            template=chat_template,
            input_variables=['user_question', 'chat_history']
        )

        chain = chat_prompt | llm 
        response = chain.invoke({'user_question' : user_question, 'chat_history' : chat_history})
        invoke_TTS(response.content)
        chat_history.append("AI response: " + response.content)
        user_question = invoke_ASR()
        chat_history.append("User question: " + user_question)