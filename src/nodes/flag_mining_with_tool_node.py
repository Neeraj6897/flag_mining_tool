from src.state.state_schema import State
#from src.tools.retriever_tool import build_retriever_tool

#tools = build_retriever_tool()

class FlagMiningWithToolNode:
    """FlagMining with enhanced tool integration"""

    def __init__(self, model):
        self.llm = model

    def agent(self, tools):
        """Returns a chatbot node function"""

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State) -> dict:
            """Chatbot logic for processing the input state and returning a response"""

            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node