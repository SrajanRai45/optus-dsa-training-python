from rich.console import Console
from rich.panel import Panel

console = Console()


def diamond(size: int) -> string:
    mid = size // 2 + 1
    result = []
    for row in range(mid, -1, -1):
        for column in range(size - 1, -1, -1):
            if column >= row and column <= size - row - 1:
                result.append("*")
            else:
                result.append(" ")
        result.append("\n")
    for row in range(mid):
        for column in range(size):
            if column >= row and column <= size - row - 1:
                result.append("*")
            else:
                result.append(" ")
        result.append("\n")

    return "".join(result)


console.print(Panel(diamond(11)))
