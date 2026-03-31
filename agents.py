from typing import TypedDict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import list_directory, read_file, search_codebase
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

class AgentState(TypedDict):
    issue_text: str
    investigation_plan: List[str]
    checked_files: List[str]
    final_pathway: str

# langchain    

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

agent_tools = [list_directory, read_file, search_codebase]

llm_with_tools = llm.bind_tools(agent_tools)

# langgraph

graph_builder = StateGraph(AgentState)

graph_builder.add_node("brain", run_brain)

graph_builder.add_node("tools", ToolNode(agent_tools))

graph_builder.set_entry_point("brain")

graph_builder.add_edge("tools", "brain")

graph_builder.add_conditional_edges("brain", tools_condition)

investigator_agent = graph_builder.compile()

if __name__ == "__main__":
    bug_report = """
    Issue #402: When a user adds a duplicate item to the cart, 
    the total price does not update, even though the item count increases.
    """

    initial_state = {"issue_text": bug_report}

    print("Agent is starting its investigation... \n")
    final_state = investigator_agent.invoke(initial_state)

    print("Investigation Complete! Here is your roadmap: /n")
    print(final_state.get("final_pathway", "No pathway generated."))