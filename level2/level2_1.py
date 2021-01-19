def solution(n, b, result=None):
    if result is None:
        result = []

    y = sorted(n)
    x = y[::-1]
    len_n = len(n)

    if b == 10:
        subtract_x_y = int(''.join(x)) - int(''.join(y))
        s = str(subtract_x_y)
        len_after = len_n - len(s)

        if len_after == 0:
            if s in result:
                return len(result) - result.index(s)
            result.append(s)
            return solution(s, b, result)

        zeros_remain = str(subtract_x_y * 10 ** len_after)
        if zeros_remain in result:
            return len(result) - result.index(zeros_remain)
        result.append(zeros_remain)
        return solution(zeros_remain, b, result)

    else:
        if result == []:
            x = list(map(int, x))
            y = x[::-1]

        s = []
        for i in range(len_n - 1, -1, -1):
            if x[i] >= y[i]:
                s.append(x[i] - y[i])
            else:
                s.append(x[i] - y[i] + b)
                x[i - 1] = x[i - 1] - 1

        if s[::-1] in result:
            return len(result) - result.index(s[::-1])

        result.append(s[::-1])
        return solution(s, b, result)


print(solution('210022', 3))
print(solution('1211', 10))
