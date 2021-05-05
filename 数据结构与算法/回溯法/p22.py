def gen_parenthesis(n):
    results = []
    def gen(left, right, result=None):
        nonlocal results

        if result is None:
            result = []

        if right == 0:
            results.append("".join(result))
            return
        
        if left:
            result.append("(")
            gen(left-1, right, result)
            result.pop()
        
        if right > left:
            result.append(")")
            gen(left, right-1, result)
            result.pop()
    gen(n, n)
    return results

if __name__ == "__main__":
    print(gen_parenthesis(3))
    print(gen_parenthesis(1))