# Lazy OpenAI

Lazy OpenAI is a Python library that simplifies interaction with OpenAI's API. It provides easy-to-use functions to generate text and structured outputs using Pydantic models.

## Installation

To install Lazy OpenAI, run the following command:

```sh
pip install lazyopenai
```

## Usage

```python
from lazyopenai import generate

print(generate("Hi"))
```

### Structured Outputs

```python
from pydantic import BaseModel
from rich import print

from lazyopenai import generate


class Step(BaseModel):
    explanation: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


# https://platform.openai.com/docs/guides/structured-outputs?context=ex1#chain-of-thought
resp = generate("how can I solve 8x + 7 = -23", response_format=MathReasoning)
print(resp)
```

### Function Calling

```python
from pydantic import Field

from lazyopenai import generate
from lazyopenai.types import BaseTool


class AddNumbers(BaseTool):
    a: float = Field(..., description="First number to add")
    b: float = Field(..., description="Second number to add")

    def __call__(self) -> float:
        print("function called")
        return self.a + self.b


resp = generate(
    "100 + 10 = ?",
    tools=[AddNumbers],
)
print(resp)
```

## TODO

- [x] Function calling
- [ ] Memory
- [ ] Async
