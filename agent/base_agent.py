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
        base_url = ""
        api_key = ""
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature = 0,openai_api_key=api_key,base_url=base_url )

    @abstractmethod
    def run(self, input: str) -> str:
        pass

    def invoke(self, input: str) -> str:
        return self.llm.invoke(input)