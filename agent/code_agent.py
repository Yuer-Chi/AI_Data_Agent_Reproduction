from base_agent import BaseAgent
# from tools.basetool import execute_code, execute_command,read_document

class Code(BaseAgent):
    def __init__(self):
        super().__init__("Code Agent", "A code agent that specializes in data processing and analysis.")

    def run(self, user_message: str) -> str:
        # tools = [read_document, execute_code, execute_command]
        prompt = f"""
        You are an expert Python programmer specializing in data processing and analysis. 
        Generate Python code based on the following user request:

        User Request: {user_message}

        Your main responsibilities include:
        1. Writing clean, efficient Python code for data manipulation, cleaning, and transformation.
        2. Implementing statistical methods and machine learning algorithms as needed.
        3. Debugging and optimizing existing code for performance improvements.
        4. Adhering to PEP 8 standards and ensuring code readability with meaningful variable and function names.

        Constraints:
        - Focus solely on data processing tasks; do not generate visualizations or write non-Python code.
        - Provide only valid, executable Python code, including necessary comments for complex logic.
        - Avoid unnecessary complexity; prioritize readability and efficiency.
        """

        intent_response = self.invoke(prompt)
        return intent_response.content

