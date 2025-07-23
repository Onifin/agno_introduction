from agno.agent import Agent
from agno.tools.website import WebsiteTools
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

load_dotenv(override=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"), 
    tools=[
        WebsiteTools(),
        ReasoningTools(add_instructions=True)
    ], 
    instructions=[
        "Resuma a página como se fossem minhas anotações de um estudante."
        "O resumo deve ser escrito em parágrafos."
    ],
    show_tool_calls=True
)
agent.print_response("https://www.anthropic.com/news/model-context-protocol", stream=True, show_full_reasoning=True, markdown=True)