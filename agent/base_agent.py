from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

#抽象基类
class BaseAgent(ABC):
    #构造方法
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        #加载环境变量/获得API
        load_dotenv()
        self.llm = ChatOpenAI(model="o4-mini")

    @abstractmethod
    def run(self, input: str) -> str:
        pass

    def invoke(self, input: str) -> str:
        return self.llm.invoke(input)