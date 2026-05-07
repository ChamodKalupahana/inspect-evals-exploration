from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import exact
from inspect_ai.solver import generate

from dotenv import load_dotenv
load_dotenv()

@task
def hello_world():
    return Task(
        dataset=[
            Sample(
                input="Just reply with hello world bro",
                target="hello world bro",
            )
        ],
        solver=[generate()],
        scorer=exact(),
    )