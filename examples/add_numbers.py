from pydantic import Field

from lazyopenai import generate
from lazyopenai.types import LazyTool


class AddNumbers(LazyTool):
    a: float = Field(..., description="The first integer")
    b: float = Field(..., description="The second integer")

    def __call__(self) -> str:
        print("function called")
        return str(self.a + self.b)


def main() -> None:
    resp = generate(
        "100 + 10 = ?",
        tools=[AddNumbers],
    )
    print(resp)


if __name__ == "__main__":
    main()
