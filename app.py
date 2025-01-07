from dotenv import load_dotenv
import os 
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
import streamlit as st


load_dotenv()


GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')




@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b."""
    print("function is called")
    return a * b

tools = [multiply]


llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp" , api_key=GOOGLE_API_KEY)


agent = initialize_agent(tools, llm , agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION )
st.title("Langchain toolcalling with Multiply Function")
st.write("welcome to my app")
user_input = st.text_input("enter your prompt")

if st.button("submit"):
    response = agent.invoke(user_input)
    st.write(response["output"])
    