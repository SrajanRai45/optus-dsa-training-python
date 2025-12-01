from rich.console import Console
from rich.panel import Panel

console = Console()


def checkPrime(num:int)-> bool:
    if num in [0,1,2,3]:
        return True
    if num % 2 == 0 or num %3 == 0:
        return False
    for i in range(5,11,2):
        if num % i == 0:
            return False 
    for i in range(17,num,6):
        if num % i == 0:
            return False
    return True

console.print(Panel("enter the number below"))
a = int(input())
if checkPrime(a):
    console.print(Panel(f" the number is prinme"))
else:
    console.print(Panel(f" the number is not a prime"))


