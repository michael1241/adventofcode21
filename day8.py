#! /usr/bin/env python3


with open('./day8in') as f:
    lines = [r.split(' | ') for r in f.read().splitlines()]


# part 1
# inp, out = zip(*lines)
# out_joined = " ".join(out).split()
# _1_4_7_8 = list(filter(lambda x: len(x) in {2, 3, 4, 7}, out_joined))
# print(len(_1_4_7_8))

total = 0
for line in lines:
    digits, code = line
    digits = [set(d) for d in digits.split(' ')]
    code = [set(d) for d in code.split(' ')]
    _1 = [_ for _ in digits if len(_) == 2][0]
    _4 = [_ for _ in digits if len(_) == 4][0]
    _7 = [_ for _ in digits if len(_) == 3][0]
    _8 = [_ for _ in digits if len(_) == 7][0]

    lookups = {2: '1', 4: '4', 3: '7', 7: '8'}
    decode = []
    for c in code:
        l = len(c)
        if l in (2, 4, 3, 7):  # unique lengths
            decode.append(lookups[l])
        elif l == 5:
            if not _7 - c:  # 7 is completely overlaid by 3
                decode.append('3')
            elif len(c & _4) == 3:  # _4 and and 5 have 3 intersections
                decode.append('5')
            else:
                decode.append('2')
        elif l == 6:
            if not _4 - c:  # 9 is completely overlaid by 4
                decode.append('9')
            elif not _7 - c:  # 7 is completely overlaid by 0
                decode.append('0')
            else:
                decode.append('6')
    total += int("".join(decode))

print(total)
