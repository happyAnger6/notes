def pow(num, n):
    if n < 0:
        return 1 / pow(num, -n)

    if n == 0:
        return 1

    if n == 1:
        return num

    if n % 2 == 0:
        s = pow(num, n//2)
        return s * s

    if n % 2 != 0:
        s = pow(num, n//2)
        return s * s * num


if __name__ == "__main__":
    print(pow(2, 3))
    print(pow(2, 5))
    print(pow(3, 3))
    print(pow(3, 5))
