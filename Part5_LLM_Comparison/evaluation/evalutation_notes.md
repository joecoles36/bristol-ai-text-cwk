## Evaluation Notes

We evaluated Gemini outputs by comparing predicted descriptions to ground truth labels.

### Matching Strategy
- Matching was based on keyword presence rather than exact sentence equality
- This accounts for variation in phrasing (e.g. "centrally displayed" vs "in the center")

### Normalisation Rules
- "dark red" was treated as equivalent to "brown"
- "light grey" and "gray" were treated as equivalent
- "top row" was treated as equivalent to "top-left, top-center, top-right"

### Scoring
- Each attribute (shape, colour, size, position, background) was scored independently
- Final accuracy is reported as proportion of correctly identified attributes

### Limitations
- Small sample size (20 shapes, 8 numbers, 8 tic-tac-toe)
- Gemini responses sometimes included additional descriptive language
- Occasional API unavailability due to high usage (rate limiting)

These decisions ensure fair comparison between CNN outputs (which are structured) and LLM outputs (which are free-form text).
