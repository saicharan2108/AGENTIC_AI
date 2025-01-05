import typer
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.model.groq import Groq


import os 
from dotenv import load_dotenv 
load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    # urls=["https://www.beiruteyecenter.com/uploads/3794_1008_4334.pdf"],
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes",db_url=db_url),
    model=Groq(id="llama-3.1-70b-versatile"),
    )

knowledge_base.load()


storage = PgAssistantStorage(
        table_name="pdf_assistant",
        db_url=db_url,
    )


def pdf_assistant(new:bool=False, user:str="user"):
    run_id: Optional[str] = None
    if not new:
        existing_run_ids: List[str] = storage.get_all_run_ids(user)
        if existing_run_ids:
            run_id = existing_run_ids[0] 
    Assistant = Assistant(
        model=Groq(id="llama-3.1-70b-versatile"),
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        show_tool_calls=True,
        search_knowledge=True,
        read_chat_history=True,

        )
    if run_id is None:
        run_id=Assistant.run_id
        print(f"Started run id: {run_id}")
    else:
        print(f"Continuing run id: {run_id}")

        assistant.cli_app(markdown=True)
if __name__ == "__main__":    
    typer.run(pdf_assistant)
