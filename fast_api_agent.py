from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from fastapi import FastAPI
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv(override = True)

app = FastAPI()

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

class Body(BaseModel):
    message: str

@app.post("/invoke")
async def run(body: Body):
    response = agent.run(body.message)
    return {"response": response.content}
