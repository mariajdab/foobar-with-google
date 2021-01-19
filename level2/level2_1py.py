def solution(h, q, p=None):
    if p is None:
        p = []

    n_f = 2 ** h - 1

    if n_f == q[0]:
        p.append(-1)
    else:
        n_r = n_f - 1
        n_l = n_r // 2

        for level in range(h - 2, -1, -1):
            if q[0] == n_l or q[0] == n_r:
                p.append(n_f)
                break
            if q[0] > n_l:
                n_f, n_r, n_l = set_nodes(n_r, level)
            else:
                n_f, n_r, n_l = set_nodes(n_l, level)

    if len(q) > 1:
        q.pop(0)
        return solution(h, q, p)
    return p


def set_nodes(nodef_r_l, level):
    n_f = nodef_r_l
    n_r = n_f - 1
    n_l = n_r - 2**level + 1
    return n_f, n_r, n_l
