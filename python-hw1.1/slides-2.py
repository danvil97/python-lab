# Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...
def find1(n):
    res1 = 1
    res2 = 1
    for _ in range(2, n):
        res1, res2 = res2, res1 + res2
    return res2


# Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17...
def find2(n):
    res1 = 1
    res2 = 1
    res3 = 1
    for _ in range(3, n):
        res1, res2, res3 = res2, res3, res1
        res3 += res2 + res1
    return res3


# Вычислить сумму и произведение всех натуральных чисел от А до В
# включительно.
def idksm(A, B):
    sum_res = 0
    multiply_res = 1
    for i in range(A, B + 1):
        sum_res += i
        multiply_res *= i
    return [sum_res, multiply_res]


# Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые
# между ними, потом все нечётные (генератором/ами списков)
def idk5(A, B):
    tmp1 = [i for i in range(A, B + 1) if i % 2 == 0]
    tmp2 = [i for i in range(A, B + 1) if i % 2 != 0]
    return tmp1 + tmp2


def idk6(l):
    tmp1 = [i for i in l if i >= 0]
    tmp2 = [i for i in l if i < 0]
    return [tmp1, tmp2]


l1 = [find1(n) for n in range(1, 10)]
print(l1)

l2 = [find2(n) for n in range(1, 10)]
print(l2)

# Вывести квадраты нечетных чисел до N. (генератором списков)
n = 11
l3 = [i**2 for i in range(1, n, 2)]
print(l3)

l4 = idksm(1, 2)
print("Сумма:", l4[0], "Произведение:", l4[1])

l5 = idk5(1, 10)
print(l5)

l6 = idk6([1, -2, -5, 3, -2, 10, 2, -4, 20, 30, -230])
print("Положительные:", l6[0], "\n", "Отрицательные:", l6[1])
