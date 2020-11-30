def Plus(pyx1, pyx2, pyx3, pyx4):
    pyy1 = (pyx1+pyx2)
    pyy2 = (pyx1+pyx3)
    pyy3 = (pyx1+pyy1)
    pyyA, pyyB, pyyC = (pyx2+pyx3), (pyx2+pyx4), (pyx3+pyx4)
    
    y1, y2, y3 = (pyy1+pyyA), (pyy2+pyyB), (pyy3+pyyC)

    ans = y1+y2+y3
    return ans


def Minus(x1, x2):
    if x1 > x2:
        ans = x1-x2
    elif x2 > x1:
        ans = x2-x1
    return ans


def Multi(x1, x2, x3):
    my1, my2, my3 = (x1*x2), (x1*x3), (x2*x3)

    ans = (my1*my2*my3)
    
    return ans


def Division(x1, x2, x3):
    dy1, dy2, dy3 = (x1/x2), (x1/x3), (x2/x3)

    ans = ((dy1/dy2)/dy3)
    return ans


def Exponentiation(x1, x2):
    ans = (x1)**(x2)
    return ans


def EvenOROdd(x):
    if x%2 == 0:
        return 0
    else:
        return 1


def Factorial(x):
    cnt, answer = 1, 1
    if x > 1:
        while cnt <= x:
            answer *= cnt
            cnt += 1
        return answer
    else:
        return answer

