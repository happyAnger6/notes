def get_last(N):
    return N%10

def last_number(N, n):
    if n == 0:
        return 1

    if n == 1:
        return get_last(N)

    s = last_number(N, n//2) 
    if n % 2 == 0:
        return get_last(s*s)

    return get_last(s*s*get_last(N))

if __name__ == "__main__":
    print(last_number(3, 3))
    print(last_number(4, 4))
    print(last_number(1, 0))
    print(last_number(0, 1))

    