# percent-choice

Fast percentage-based random choice for Python.

## Installation

```bash
pip install percent-choice
Usage
from percent_choice import Percent

chance = Percent(
    ["green", "blue", "red"],
    [10, 30, 60]
)

print(chance.get())

For cryptographically secure randomness:

print(chance.get_secure())