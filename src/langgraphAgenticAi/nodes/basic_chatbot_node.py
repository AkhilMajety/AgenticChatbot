from src.langgraphagenticai.state.state import State

class BasicChatBotNode:

    "Basic chat bot"

    def __init__(self,model):
        self.llm =  model

    def process(self,state:State)->dict:
        "process the input state and generate the response"

        return {"messages": self.llm.invoke(state['messages'])}