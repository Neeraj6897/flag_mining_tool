import streamlit as st
from src.user_interface.streamlit.load_ui import LoadStreamlitUI
from src.LLMs.groqllm import GroqLLM
from src.graph.graph_builder import GraphBuilder
from src.user_interface.streamlit.display_result import DisplayResultStreamlit

def load_flag_mining_tool():
    """
    Loads and runs the flag mining tool on the provided error message and compiler flags.
    This function intializes the UI, handles the user input, configure the llm model,
    sets up the graph based on the selected use case and displays the output while implementing
    exception handling for robustness.
    """

    #Load UI
    user_interface = LoadStreamlitUI()
    user_input = user_interface.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load the user input from the UI")
        return
    
    #Text input from user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe

    else:
        user_message = st.chat_input("Enter your error message")

    if user_message:
        #try:
        #Configure LLM
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if not model:
            st.error("Error: LLM model could not be initialized")
            return
        
        #Initialize and setup the graph based on the use case
        usecase = user_input.get('selected_usecase')
        if not usecase:
            st.error("Error: No usecase selected")
            return
        
        #Graph builder
        graph_builder = GraphBuilder(model)
        try:
            graph = graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

        except Exception as e:
            st.error(f"Error: Graph setup failed due to {e}")
'''
        except Exception as e:
            raise ValueError(f"Error occurred with Exception: {e}")
'''