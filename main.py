from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv(override=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[]
)

agent.print_response("Me diga um node de um estado brasileiro que não possui a letra a", stream=True)