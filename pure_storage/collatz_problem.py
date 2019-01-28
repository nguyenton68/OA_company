def collatz(n):
    count = 0
    m = {}
    while n != 1:
        if n in m:
            print("here")
            return count + m[n]
        else:
            m[n] = count
        if n % 2 == 1:
            n = n*3 + 1
        else:
            n = n//2
        count += 1
        print(n)
    return count

def collatz2(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return 1 + collatz(n*3 +1)
    else:
        return 1 + collatz(n//2)

x = collatz(15)
print(x)