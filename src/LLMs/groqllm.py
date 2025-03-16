import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        #try:
        groq_api_key = self.user_controls_input['GROQ_API_KEY']
        selected_groq_model = self.user_controls_input['selected_groq_model']
        print(f"Selected Model is: {selected_groq_model}")
        print(f"Groq api key: {groq_api_key}")
        print(os.environ.get("SSL_CERT_FILE"))
        if groq_api_key =='' and os.environ['GROQ_API_KEY'] =='':
            st.error("Please enter the Groq API Key")

        llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        #except Exception as e:
            #raise ValueError(f"Error occurred with Exception as {e}")
        
        return llm