from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
load_dotenv()


def main():
    print("Hello from langchain-course!")

    prompt_template = """You are an expert of this topic: {topic}. 
    Provide a detailed explanation about it.
    """

    template = PromptTemplate(
        input_variables=["topic"],
        template=prompt_template
    )
    
    llm = ChatOpenAI(
    temperature= 0.7,
    model="gpt-3.5-turbo"
    )

    chain = template | llm
    response = chain.invoke({"topic": "Artificial Intelligence"})
    print(response.content)

if __name__ == "__main__":
    main()
