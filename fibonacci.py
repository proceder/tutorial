def fib_rek(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rek(n-1) + fib_rek(n-2)

def fib_for(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0, f1 = 0, 1
    fn = f0 + f1
    for i in range(2,n+1):
        print("i: ", i)
        fn = f0 + f1
        f0 = f1
        f1 = fn
        print("f0: %s, f1: %s" % (f0, f1) )

    return f1;

def fib_while(n):

    f0, f1 = 0, 1
    i = 1
    while(i != n):
        i += 1
        f0 = f1
        f1 = f0 + f1
        # print("f0: %s, f1: %s" % (f0, f1) )
    return f1


# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

ile = int(input())
for i in range(ile):
    n = int(input())
    print(fibonacci(n))


