from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.thinking import ThinkingTools
from dotenv import load_dotenv

load_dotenv(override=True)

agent = Agent(
    model = OpenAIChat(id="gpt-4o-mini"),
    tools = [
        ThinkingTools(add_instructions=True)
    ],
    instructions = [
        "Você deve prestar atenção, pois certas vezes as letras são as mesmas, porém com acentuação diferente"
        "Note que você pode excluir um a um os estados que possuem a letra até que sobre somente 1 na lista"
    ],
    markdown = True
)

agent.print_response("Me diga o nome de um estado brasileiro que não possui a letra a", stream=True)