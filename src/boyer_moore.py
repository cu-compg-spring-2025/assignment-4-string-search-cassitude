def get_shift_match_table(P):
    m = len(P)
    shift_match_table = {}

    for shift in range(m - 1, 0, -1):
        p_1 = m - 1
        p_2 = m - shift - 1

        while p_2 >= 0:
            if P[p_2] == P[p_1]:
                p_1 -= 1
                p_2 -= 1
                if p_2 < 0:
                    shift_match_table[shift] = m - shift
                    break
            else:
                shift_match_table[shift] = m - shift - p_2 - 1
                break
    shift_match_table[m] = 0
    return shift_match_table


def get_good_suffix_table(P):
    m = len(P)

    good_suffix_table = {}
    good_suffix_table[0] = 1

    shift_match_table = get_shift_match_table(P)

    for i in range(1, m + 1):
        good_suffix_table[i] = i + m

    for i in range(m, 0, -1):
        if shift_match_table[i] > 0:
            good_suffix_table[shift_match_table[i]] = i + shift_match_table[i]

    for i in range(m, 0, -1):
        if shift_match_table[i] + i == m:
            for j in range(shift_match_table[i] + 1, m + 1):
                good_suffix_table[j] = min(good_suffix_table[j], j + i)
    return good_suffix_table


def get_bad_char_table(P):
    bad_char_table = {}

    for i in range(len(P)):
        bad_char_table[P[i]] = i

    return bad_char_table


def boyer_moore_search(T, P):
    occurrences = []
    n, m = len(T), len(P)

    if m == 0 or n == 0 or m > n:
        return occurrences

    bad_char_table = get_bad_char_table(P)
    good_suffix_table = get_good_suffix_table(P)

    text_pointer = 0
    while text_pointer <= n - m:
        pattern_pointer = m - 1

        while (
            pattern_pointer >= 0
            and P[pattern_pointer] == T[text_pointer + pattern_pointer]
        ):
            pattern_pointer -= 1

        if pattern_pointer < 0:
            occurrences.append(text_pointer)
            bad_char_shift = pattern_pointer - bad_char_table.get(
                T[text_pointer + pattern_pointer], -1
            )
            good_suffix_shift = good_suffix_table.get(pattern_pointer - 1, m)
            text_pointer += (
                max(bad_char_shift, good_suffix_shift) if text_pointer + m < n else 1
            )
        else:
            bad_char_shift = pattern_pointer - bad_char_table.get(
                T[text_pointer + pattern_pointer], -1
            )
            good_suffix_shift = good_suffix_table.get(pattern_pointer - 1, m)
            text_pointer += max(bad_char_shift, good_suffix_shift)

    return occurrences
