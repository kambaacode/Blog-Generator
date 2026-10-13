from src.states.blog_state import BlogState, Blog

class BlogNode:
    """A class to reperesent the blog node"""
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """Create title for the blog"""

        prompt ="""
                    You're an expert blog content writer. Generate a blog title for
                    this topic {topic}. This title should be creative and SEO friendly.
                    Return only the title text, with no quotes, no numbering and no markdown. 
                """

        system_message = prompt.format(topic = state["topic"])
        response = self.llm.invoke(system_message)

        return {"blog": Blog(title= response.content , content= "") }

    def content_generator(self, state: BlogState):
            """Generates content for topic"""
            system_prompt ="""
                    You're an expert blog content writer. Use markdown formatting. Generate a detailed blog content
                    with detailed breakdown for this topic {topic} and this title {title}. 
                    """
            system_message = system_prompt.format(topic = state["topic"], title = state["blog"].title)

            response = self.llm.invoke(system_message)
            return {"blog": Blog(title= state["blog"].title , content= response.content) }