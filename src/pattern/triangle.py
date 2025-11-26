from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

# right angle triangle
def rightAngleTriangle(size: int)->string:
    result = ""
    for i in range(size):
        for j in range(size):
            if i >= j:
                result += "*"
            else:
                result += " "
        result += "\n"
    return result


def triangle(size:int):
    mid = size//2 + 1
    result = ""
    for row in range(mid, -1,-1):
        for column in range(size , -1 ,-1):
            if column >= row and column <= size - row - 1:
                result += "*"
            else:
                result += " "
        result += "\n"
    return result

console.rule("[bold cyan]Right Angle Triangle[/bold cyan]" , style="dim")
console.print(Panel(rightAngleTriangle(11)))

rightAngleTriangle(11)

console.rule("[bold cyan]Triagle[/bold cyan]", style="dim")

console.print(Panel("here is an equilateral triangle"))
console.print(Panel(triangle(11)))
