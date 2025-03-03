def generate_parentheses(n):
    if n == 0:  # Edge case handling
        return []

    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result

n = int(input("Enter the Number of Pairs of Parentheses: "))

if 1 <= n <= 8:
    print(generate_parentheses(n))
else:
    print("Please Enter a Value Between 1 and 8.")
