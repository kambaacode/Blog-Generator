from langgraph.graph import START, END, StateGraph
from src.llms.groq_llm import GroqModel
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
            Build a graph to generate blogs based on topic
        """

        blog_node = BlogNode(self.llm)
        # Nodes
        self.graph.add_node("title_creation", blog_node.title_creation)
        self.graph.add_node("content_generation", blog_node.content_generator)

        # Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)
        