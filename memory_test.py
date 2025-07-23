from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from dotenv import load_dotenv

load_dotenv(override = True)

bd = SqliteStorage(table_name = "sessions", db_file = "history/sessions.db")
memory = Memory(
    db = SqliteMemoryDb(table_name = "memory", db_file = "history/memory.db"),
    model = OpenAIChat(id="gpt-4o-mini")
)
agent = Agent(
    session_id = "s_01340",
    user_id = "u_010",
    model = OpenAIChat(id="gpt-4o-mini"), 
    add_history_to_messages = True,
    storage = bd,
    memory = memory,
    enable_agentic_memory = True
)

#agent.print_response("Oi, meu nome é Onifin", stream=True, markdown=True)
#agent.print_response("Como é meu nome?", stream=True, markdown=True)

agent.print_response("Você ainda lembra meu nome?", stream=True, markdown=True)