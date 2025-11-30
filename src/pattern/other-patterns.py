from rich.console import Console
from rich.panel import Panel

console = Console()


def diamond1(size: int) -> string:
    mid = size // 2 + 1
    result = []
    for row in range(mid, -1, -1):
        for column in range(size - 1, -1, -1):
            if column >= row and column <= size - row - 1:
                result.append(" ")
            else:
                result.append("*")
        result.append("\n")
    for row in range(mid):
        for column in range(size):
            if column >= row and column <= size - row - 1:
                result.append(" ")
            else:
                result.append("*")
        result.append("\n")

    return "".join(result)

def diamond2(size: int) -> string:
    mid = size // 2 + 1
    result = []
    for row in range(mid):
        for column in range(size):
            if column >= row and column <= size - row - 1:
                result.append(" ")
            else:
                result.append("*")
        result.append("\n")
    for row in range(mid, -1, -1):
        for column in range(size - 1, -1, -1):
            if column >= row and column <= size - row - 1:
                result.append(" ")
            else:
                result.append("*")
        result.append("\n")

    return "".join(result)


# right angle triangle
def rightAngleTriangle(size: int) -> string:
    result = []
    for i in range(size):
        pos = i + 1
        factor = i
        for j in range(size):
            if i >= j:
                result.append(f"{pos + (factor * size)} ")
                factor -= 1
            else:
                result.append(" ")
        result.append("\n")
    return "".join(result)

def rightAngleTriangle2(size: int) -> string:
    result = []
    for i in range(size -1,-1,-1):
        for j in range(size):
            if i >= j:
                result.append(f"{size - j} ")
            else:
                result.append(" ")
        result.append("\n")
    return "".join(result)


console.print(Panel(diamond1(11)))
console.print(Panel(diamond2(11)))
console.print(Panel(rightAngleTriangle(11)))
console.print(Panel(rightAngleTriangle2(11)))

