from lyzr_automata import Task
from lyzr_automata.ai_models.openai import OpenAIModel
from emails import send_email
import os

api = os.getenv("OPENAI_API_KEY")
open_ai_text_completion_model = OpenAIModel(
    api_key=api,
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def email_task(email):
    se = send_email(rec_email=email)

    Task(
        name="Send Email",
        tool=se,
        model=open_ai_text_completion_model,
        instructions=f"""Just write Below Script:
        Hello user,
        Your Music Is generated.Please Review that.
        """
    ).execute()

