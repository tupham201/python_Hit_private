

def e(x, n):
    ans = tu = mau =1.0
    for i in range(1, n + 1):
        tu *= x
        mau *= i
        ans += tu / mau
    return ans


def f(n):
    ans = 0.0
    t = 1
    for i in range(2, n + 2):
        ans += t
        t = t/i
    return ans


x = float(input())
n = int(input())

print(f"e^{x} = {e(x, 5)}")
print(f"f(n) = {f(n)}")