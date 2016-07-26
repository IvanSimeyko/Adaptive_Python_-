
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


def snail():
    """
    Snail creeps up the vertical pole of height H feets. Per day it goes A feets up,
    and per night it goes B feets down. In which day the snail will reach the top of the pole?
    """
    h = int(input('Enter the height: '))
    a = int(input('Enter the day feets: '))
    b = int(input('Enter the night feets: '))
    i = a
    n = 1
    while i < h:
        i -= b
        n += 1
        i += a
    return n

if __name__ == '__main__':
    print(snail())
    #print(squirrels())
