def caculator(s):
    def expr(s, i, n):
        if i == n:
            return 0

        left = i
        while i < n and '0' <= s[i] <= '9':
            i += 1
        val = int(s[left:i])

        if i == n:
            return val

        op = s[i]
        i += 1

        def get_val(s, i):
            left = i
            while i < n and '0' <= s[i] <= '9':
                i += 1
            val = int(s[left:i])
            return val, i

        while op == '*' or op == '/':
            next_val, i = get_val(s, i)
            if op == '*':
                val *= next_val
            else:
                val /= next_val
            if i == n:
                return val
            op = s[i]
            i += 1

        if op == '+':
            return val + expr(s, i, n)

        if op == '-':
            return val - expr(s, i, n)


    return expr(s, 0, len(s))

if __name__ == "__main__":
    print(caculator("1+2*3"))
    print(caculator(""))
    print(caculator("0"))
    print(caculator("10"))
    print(caculator("10-2+3*3-4"))


