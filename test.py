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
                input="what's the answer to the universe",
                target="42",
            )
        ],
        solver=[generate()],
        scorer=exact(),
    )