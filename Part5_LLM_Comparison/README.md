# Part 5 - LLM Comparison

This section evaluates a commercial LLM (Gemini 2.5 Flash) on the same synthetic datasets used for CNN evaluation.

## Domains tested
- Shapes (N=20)
- Numbers (N=8)
- Tic-tac-toe (N=8)

## Method
Each image was passed to Gemini using a structured prompt asking for:
- objects / numbers
- colours
- sizes
- spatial relationships / positions

## Prompts
See `gemini_eval/prompts.py`.

## Reproduction
1. Generate images using `image_generators/`
2. Run `gemini_eval/gemini_eval.py`
3. Score outputs using `evaluation/score_responses.py`

## Limitations
- Small sample size (not full test split)
- API rate limits ("try again later" errors)
- LLM outputs vary slightly in wording
