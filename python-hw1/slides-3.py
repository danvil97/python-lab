# Нарисовать рамочку шириной w символов и
# высотой h символов.
def draw1(w,h):
    for i in range(0, h):
        if (i == 0) | (i == h-1):
            print(w*"*")
        else:
            print("*" + (w - 2) * " " + "*")


draw1(10, 5)
print("\n")

# Пускай символ, которым рисуется рамочка –
# тоже входной параметр.

def draw2(w, h, symb):
    for i in range(0, h):
        if (i == 0) | (i == h-1):
            print(w*symb)
        else:
            print(symb + (w - 2) * " " + symb)


draw2(10, 5, "x")
print("\n")

# Нарисовать рамочку шириной w символов и
# высотой h символов, и толщиной f символов.
# (оформить в виде функции)


def draw3(w, h, f):
    for _ in range(0, f):
        print(w * "*")
    for _ in range(0, h - f * 2):
        print(f * "*" + (w - 2 * f) * " " + f * "*")
    for _ in range(0, f):
        print(w * "*")


draw3(7, 6, 2)
print("\n")
