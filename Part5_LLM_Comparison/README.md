# Part 5 - LLM Comparison

This section evaluates a commercial LLM (Gemini 2.5 Flash) on the same synthetic datasets used for CNN evaluation.

## Domains Tested
- Shapes (N = 20)
- Numbers (N = 8)
- Tic-tac-toe (N = 8)

## Method
Each image was passed to Gemini using a structured prompt designed to extract:

- objects / numbers  
- colours  
- sizes  
- spatial relationships / positions  

## Prompts
See `gemini_eval/prompts.py` for the exact prompts used per domain.

## Reproduction
To reproduce the results:

1. Generate images using `image_generators/`
2. Run `gemini_eval/gemini_eval.py` to collect model outputs
3. Score responses using `evaluation/score_responses.py`

## Limitations
- Small sample sizes (subset of full test data)
- API rate limits (“try again later” errors)
- Minor variation in LLM wording (affects exact-match metrics)
