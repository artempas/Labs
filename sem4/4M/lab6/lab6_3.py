from lab6_1 import kramer, print_system
from lab6_2 import gauss
from prettytable import PrettyTable
import numpy as np


def table_footer(tbl, text, dc):
    res = f"{tbl._vertical_char} {text}{' ' * (tbl._widths[0] - len(text))} {tbl._vertical_char}"

    for idx, item in enumerate(tbl.field_names):
        if idx == 0:
            continue
        if not item in dc.keys():
            res += f"{' ' * (tbl._widths[idx] + 1)} {tbl._vertical_char}"
        else:
            res += f"{' ' * (tbl._widths[idx] - len(str(dc[item])))} {dc[item]} {tbl._vertical_char}"

    res += f"\n{tbl._hrule}"
    return res


if __name__ == '__main__':
    A = np.random.rand(20, 20)
    X = np.random.rand(20, 1).T[0]
    f = A.dot(X)
    while np.linalg.cond(A) < 1000:
        A = np.random.rand(20, 20)
    print_system(A, f)
    print(f'cond(A)={np.linalg.cond(A)}')
    kramer_solution = kramer(A, f)
    gauss_solution = gauss(A, f)
    simpleAF_solution=np.linalg.inv(A).dot(f)
    t = PrettyTable()
    t.add_column('Premade', X)
    t.add_column('Gauss', gauss_solution)
    t.add_column('Gauss difference', tuple(abs(gauss_solution[i] - X[i]) for i in range(len(gauss_solution))))
    t.add_column('Kramer', kramer_solution)
    t.add_column('Kramer difference', tuple(abs(kramer_solution[i] - X[i]) for i in range(len(kramer_solution))))
    t.add_column('A^(-1)*f', simpleAF_solution)
    t.add_column('A^(-1)*f difference', tuple(abs(simpleAF_solution[i] - X[i]) for i in range(len(simpleAF_solution))))
    print(t)
    print(table_footer(t, 'Max',
                       {'Kramer difference': max(abs(kramer_solution[i] - X[i]) for i in range(len(kramer_solution))),
                        'Gauss difference': max(abs(gauss_solution[i] - X[i]) for i in range(len(gauss_solution))),
                        'A^(-1)*f difference':max(abs(simpleAF_solution[i] - X[i]) for i in range(len(simpleAF_solution)))}))
