def check_power_of_three(n):
    while n:
        if n % 3 == 1 or n % 3 == 0:
            n //= 3
        else:
            return False
    return True

if __name__ == "__main__":
    print(check_power_of_three(12))
    print(check_power_of_three(21))
    print(check_power_of_three(91))
    print(check_power_of_three(11))
    print(check_power_of_three(19842))
    print(check_power_of_three(67343))
            

