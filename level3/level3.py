def solution(nums):
    list_result = []
    for num in range(3, nums + 1):
        if num == 3 or num == 4:
            list_result.append({num - 1: 1})
        else:
            limit = num // 2 + 1
            first_n = {}
            for i in range(1, num - limit + 1):
                first_n[num - i] = 1
            list_result.append(first_n)
            list_result = add_lower_nums(list_result, num)

    return sum(list_result[-1].values())


def add_lower_nums(list_result, num, i=3):
    if num - i > 3 or num - i == i:

        if num - i >= i:
            s = sum(list_result[i - 3].values())
            n_ = num - i

            if n_ in list_result[-1].keys():
                value_n = list_result[-1].get(n_)
                list_result[-1].update({n_: s + value_n})
            else:
                list_result[-1].update({n_: s})

        else:
            dif = (i - num) + i
            if len(list_result[i - 3]) > dif:
                num_lower = check_lower_num(list_result[i - 3], num - i - 1)
                list_result[-1].update({num - i: num_lower})
            else:
                return list_result

        i = i + 1
        return add_lower_nums(list_result, num, i)

    return list_result


def check_lower_num(second_list, start_num):
    count = 0
    for k, v in second_list.items():
        if k <= start_num:
            count += v
    return count


