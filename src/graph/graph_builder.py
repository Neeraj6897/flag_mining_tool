from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.state.state_schema import State
from src.nodes.basic_chatbot_node import BasicChatbotNode
from src.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.tools.search_tool import get_tools, create_tool_node
#from src.tools.retriever_tool import build_retriever_tool
#from src.nodes.flag_mining_with_tool_node import FlagMiningWithToolNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """

        ##Define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools)

        ##Define LLM
        llm = self.llm

        ##Define chatbot node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        ##Add nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        ##Define conditional and directional edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
    '''
    def flag_mining_with_vectordb_tools_build_graph(self):
        """Builds a chatbot with getting information from vector retriever first and then using LLM"""
        tools = build_retriever_tool()
        tool_node = FlagMiningWithToolNode.agent(tools)

        llm = self.llm

        self.graph_builder.add_node("tool", tool_node)

    '''
    def setup_graph(self, usecase: str):
        """Sets us the graph for the selected use case"""

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()