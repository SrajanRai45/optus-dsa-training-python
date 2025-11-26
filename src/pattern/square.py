# square
def square(size: int):
    for i in range(size):
        for j in range(size):
            if i in [0, size - 1] or j in [0, size - 1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()


square(5)
