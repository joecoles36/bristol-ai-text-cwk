\# Dataset 2 — Numbers Dataset



\## Overview

This dataset contains automatically generated sentences describing numbers of varying digit lengths, sizes, and colours. Each sentence describes a single number with its visual properties.



\## Vocabulary



\### Colours (9)

red, blue, green, yellow, orange, purple, pink, brown, grey



\### Sizes (3)

small, medium, large



\### Number Ranges (4 digit lengths)

\- 1-digit: 1 to 9

\- 2-digit: 10 to 99

\- 3-digit: 100 to 999

\- 4-digit: 1000 to 9999



\## Sentence Templates (5)

1\. `a {size} {colour} {number}`

2\. `the number {number} in {colour} colour and {size} size`

3\. `{article} {colour} number {number} of {size} size`

4\. `a {size} {number} in {colour} colour`

5\. `a {size} {colour} number {number}`



\## Dataset Information

\- Total unique sentences: 3634

\- Generation method: Random sampling with duplicate removal

\- Output file: sentence\_dataset\_numbers.csv



\## CSV Columns

| Column | Description |

|---|---|

| sentence\_id | Unique identifier for each sentence |

| sentence | The generated sentence |

| number | The number described in the sentence |

| num\_digits | Number of digits (1, 2, 3, or 4) |

| colour | Colour of the number |

| size | Size of the number |

| template\_id | ID of the template used (1-5) |



\## Example Sentences

\- "a large blue 67"

\- "the number 1337 in red colour and small size"

\- "an orange number 42 of medium size"

\- "a small 9 in green colour"

\- "a medium purple number 573"



\## Design Decisions

\- Numbers are evenly sampled across all 4 digit lengths

\- 1-digit numbers produce fewer unique sentences due to smaller pool (only 9 possible values)

\- Article "a/an" is handled automatically based on the first letter of the following colour (used only in 3rd template)

