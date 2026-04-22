\# Dataset 3 — Tic-Tac-Toe Dataset



\## Overview

This dataset contains automatically generated sentences describing tic-tac-toe board states. Each sentence describes the positions of X and O pieces on the board at a given game state.



\## Board Layout

The board has 9 positions arranged as follows:

top-left     | top-center     | top-right

middle-left  | center         | middle-right

bottom-left  | bottom-center  | bottom-right



\## Vocabulary



\### Positions (9)

top-left, top-center, top-right,

middle-left, center, middle-right,

bottom-left, bottom-center, bottom-right



\### Players (2)

X, O



\## Sentence Templates (5)

1\. `X is in {x\_pos}, O is in {o\_pos}`

2\. `X has played in {x\_pos}, O has played in {o\_pos}`

3\. `X occupies {x\_pos}, O occupies {o\_pos}`

4\. `X is placed in {x\_pos}, O is placed in {o\_pos}`

5\. `X marks {x\_pos}, O marks {o\_pos}`



\## Dataset Information

\- Total unique sentences: 3419

\- Generation method: Random sampling with duplicate removal

\- Output file: sentence\_dataset\_tictactoe.csv



\## CSV Columns

| Column | Description |

|---|---|

| sentence\_id | Unique identifier for each sentence |

| sentence | The generated sentence |

| board\_state | 9-character board state using \\| as separator (e.g. X\\|O\\|\_\\|X\\|\_\\|\_\\|O\\|\_\\|\_) |

| x\_count | Total number of X pieces on the board |

| x\_positions | Comma separated list of X piece positions |

| o\_count | Total number of O pieces on the board |

| o\_positions | Comma separated list of O piece positions |

| template\_id | ID of the template used (1-5) |



\## Board State Format

The board state is represented as 9 values separated by | reading 

left to right, top to bottom:

\- X = X piece

\- O = O piece

\- \_ = empty square



Example: `X|O|\_|X|\_|\_|O|\_|\_` represents:

X | O | \_

X | \_ | \_

O | \_ | \_



\## Design Decisions

\- X always goes first so X count is always equal to or one more than O count

\- When x\_count = 5, o\_count is always 4

\- X and O positions never overlap

\- When O has no pieces yet, o\_positions is described as "none"

\- Positions are listed in natural English (e.g., "the center, the top-left, and the bottom-right")

