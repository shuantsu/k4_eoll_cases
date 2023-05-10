import itertools, pprint

combinations = list(itertools.product(range(2), repeat=8))
legal_wings = lambda a: sum(a[1::2]) == sum(a[::2])
result = list(filter(legal_wings, combinations))

def get_symmetries(case):
    symmetries = []
    i = list(case)
    for n in range(4):
        i = i[-2:] + i[:-2]
        symmetries.append(i[:])
    return str(sorted(symmetries))

cases = map(get_symmetries, result)
cases = list(map(eval, set([o[0] for o in [list(set([str(ii) for ii in eval(i)])) for i in cases]])))

pprint.pprint(cases)
input()