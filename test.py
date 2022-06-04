def maskify(cc):
    l = len(cc)
    if l <= 4: print(cc)
    print((l - 4) * '#' + cc[-4:])

maskify("12345678901122")

def is_narcissistic(n):
    num = str(n)
    length = len(num)
    print(sum(int(a) ** length for a in num) == n)

is_narcissistic(153)