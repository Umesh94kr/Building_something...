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

if __name__ == "__main__":
    quest = invoke_ASR()
    # using LLM to correct words spoken by human
    template = "Correct the words spoken by user raw voice input : {raw_voice_input}, and you need to convert it to clean voice input of user.  " \
    "Examples : quest -> i AM GOD, what are u doin" \
    "Clean voice input -> I am good, what are you doing?"
    prompt = PromptTemplate(
        template=template,
        input_variables=['quest']
    )

    chain = prompt | llm 
    question = chain.invoke(quest)
    print(f"Question : {question}")

    answer = "Hey Buddy! I'm doing good."
    invoke_TTS(answer)