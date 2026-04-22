\# Dataset 1 — Shapes Dataset



\## Overview

This dataset contains automatically generated sentences describing simple 2D scenes with two geometric shapes. Each sentence describes two objects with their size, colour, and spatial relationship.



\## Vocabulary



\### Shapes (8)

circle, square, triangle, rectangle, oval, pentagon, hexagon, diamond



\### Colours (9)

red, blue, green, yellow, orange, purple, pink, brown, grey



\### Sizes (3)

small, medium, large



\### Spatial Relations (6)

above, below, to the left of, to the right of, next to, inside



\## Sentence Templates (6)

1\. `a {size} {colour} {shape} is {relation} a {size} {colour} {shape}`

2\. `there is a {size} {colour} {shape} {relation} a {size} {colour} {shape}`

3\. `one {size} {colour} {shape} is {relation} one {size} {colour} {shape}`

4\. `{article} {colour} {shape} is {relation} {article} {colour} {shape}`

5\. `a {size} {shape} is {relation} a {size} {shape}`

6\. `a {size} {colour} {shape} is positioned {relation} a {size} {colour} {shape}`



\## Dataset Information

\- Total unique sentences: 3895

\- Generation method: Random sampling with duplicate removal

\- Output file: sentence\_dataset\_shapes.csv



\## CSV Columns

| Column | Description |

|---|---|

| sentence\_id | Unique identifier for each sentence |

| sentence | The generated sentence |

| obj1\_shape | Shape of the first object |

| obj1\_colour | Colour of the first object |

| obj1\_size | Size of the first object |

| relation | Spatial relationship between the two objects |

| obj2\_shape | Shape of the second object |

| obj2\_colour | Colour of the second object |

| obj2\_size | Size of the second object |

| template\_id | ID of the template used (1-6) |



\## Example Sentences

\- "a large red circle is above a small blue square"

\- "there is a medium pink triangle next to a large brown oval"

\- "an orange oval is to the right of a purple rectangle"

\- "a small diamond is below a large hexagon"



\## Design Decisions

\- Only 2D shapes are used to ensure visual clarity and ease in generating images

\- The "inside" relation enforces size constraints: obj1 must always be smaller than obj2 (small inside medium, small inside large, medium inside large)

\- Article "a/an" is handled automatically based on the first letter of the following colour (Used only in Template 4)

