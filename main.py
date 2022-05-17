loop = True


def OR(A, B):
    if A == 1 or B == 1:
        print(1, end=" ")
        return 1
    else:
        print(0, end=" ")
        return 0


def AND(A, B):
    if A == 1 and B == 1:
        print(1, end=" ")
        return 1
    else:
        print(0, end=" ")
        return 0


def NAND(A, B):
    if A == 0 and B == 0:
        print(1, end=" ")
        return 1
    else:
        print(0, end=" ")
        return 0


def NOT(A):
    if A == 0:
        print(1, end=" ")
        return 1

    if A == 1:
        print(0, end=" ")
        return 0


def Lhelp():
    print("basic gates example:"
          "OR(1,0)")


if __name__ == '__main__':

    while loop:
        exec(input("\nPrint your logic gates "))

    pass
