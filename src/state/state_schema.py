from typing import Annotated, Literal, Optional
from typing import Sequence
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages, BaseMessage
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """
    messages: Annotated[list, add_messages]

class AgentState(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """
    messages: Annotated[Sequence[BaseMessage], add_messages]