from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import ToolNode
from src.vectorstore.faiss_vectordb import build_vectorstore_retriever

urls = [
    "https://clang.llvm.org/docs/UsersManual.html",
    "https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-amdgpu-arch-tool",
    "https://github.com/llvm/llvm-project/issues/131281"
]

retriever = build_vectorstore_retriever(urls)

def build_retriever_tool(retriever):
    return create_retriever_tool(retriever=retriever)