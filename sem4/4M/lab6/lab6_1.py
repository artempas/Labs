import numpy as np
from random import randint




def print_system(A, f):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j == 0 and A[i][j] > 0:
                print(' ', end='')
            if A[i][j] >= 0 and j != 0:
                print('+{:0.3f}'.format(A[i][j].round(3))+chr(j + 97), end='')
            else:
                print('{:0.3f}'.format(A[i][j].round(3))+chr(j + 97), end='')
        print('=', end='')
        if f[i] >= 0:
            print(' ', end='')
        print(f'{f[i].round(3)}')


def print_solution(solution):
    for i in range(len(solution)):
        print(f'{chr(i + 97)} = {solution[i]}')


def kramer(A:np.ndarray, f:np.ndarray)->np.ndarray:
    if not np.linalg.det(A):
        raise ValueError('Unable to solve due to matrix singularity')
    solution=np.array(f,np.float64)
    delta=np.linalg.det(A)
    for col in range(len(f)):
        Ai=A.copy()
        Ai[:,col]=f
        solution[col]=np.linalg.det(Ai)/delta
    return solution


if __name__ == '__main__':
    A = np.array([[randint(-9, 9) for _ in range(3)],
                  [randint(-9, 9) for _ in range(3)],
                  [randint(-9, 9) for _ in range(3)]])
    f = np.array([randint(-9, 9) for _ in range(3)])
    f = f.transpose()
    print_system(A, f)
    print('-' * 24)
    print_solution(kramer(A, f))
