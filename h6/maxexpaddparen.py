# Maximum expression by adding parentheses 

def maxexpressionaddingparen(expression):
    expression = expression.strip().replace(" ", "").replace("−", "-")

    numbers, operators, num = [], [], ""
    for ch in expression:
        if ch in "+-":
            if num != "":
                numbers.append(int(num))
                operators.append(ch)
                num = ""
            else:
                if ch == "-":
                    num = "-"
        else:
            num += ch
    if num != "":
        numbers.append(int(num))

    n = len(numbers)
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')

            for k in range(i, j):
                op = operators[k]
                left_max, left_min = dp_max[i][k], dp_min[i][k]
                right_max, right_min = dp_max[k + 1][j], dp_min[k + 1][j]

                if op == '+':
                    max_val = left_max + right_max
                    min_val = left_min + right_min
                else:  # restricted subtraction
                    max_val = left_max - right_max
                    min_val = left_min - right_min

                dp_max[i][j] = max(dp_max[i][j], max_val)
                dp_min[i][j] = min(dp_min[i][j], min_val)

    return dp_max[0][n - 1]


if __name__ == '__main__':
    expression_input = input().strip()
    print("input expression:", expression_input)
    result = maxexpressionaddingparen(expression_input)
    print("max possible value:", result)
