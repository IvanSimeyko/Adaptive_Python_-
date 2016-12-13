
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


def mkad():
    """
    The length of the Moscow Ring Road (MKAD) is 109 kilometers. Biker Vasya starts from the zero kilometer
    of MKAD and drives with a speed of V kilometers per hour. On which mark will he stop after T hours?
    """
    v, t = abs(int(input('Enter value v: '))), int(input('Enter value t: '))
    def mark(dist, len_mkad = 109):
        if len_mkad > dist:
            return dist
        else:
            return mark(dist-len_mkad,)

    return mark(v*t, )

def calc_expr(a, b, c):
    """
    Write a function to compute the value of the following expression:
    """
    x = (a+b*c)/5
    y = a**3
    z = (a+c/3)/4
    return x-y+z


if __name__ == '__main__':
    print(calc_expr(1, 2, -3))
    #print(mkad())
    #print(snail())
    #print(squirrels())