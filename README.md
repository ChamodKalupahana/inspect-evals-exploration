for a single model
`inspect eval test.py --model "openrouter/poolside/laguna-m.1:free"`

# evals
inspect eval inspect_evals/agentic_misalignment --model openrouter/poolside/laguna-m.1:free
inspect eval inspect_evals/hle --model openrouter/poolside/laguna-m.1:free
inspect eval inspect_evals/humaneval --model openrouter/poolside/laguna-m.1:free

none of these run on my crappy laptop tho :(