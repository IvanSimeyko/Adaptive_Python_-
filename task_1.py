
def squirrels():
    """
    N squirrels found K nuts and decided to divide them equally.
    Determine how many nuts each squirrel will get.
    """
    i = 0
    a = []
    while i < 2:
        inp = int(input("Enter number: "))
        a.append(inp)
        i += 1
    ans = a[1]//a[0]
    return ans


if __name__ == '__maim__':

    print(squirrels())



