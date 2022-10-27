from itertools import chain, product, repeat, cycle
num = input("Tu número: ")
print(num)
if len(num) != 4:
    print("Tu número no es válido")
else:
    for c in range(3, -1, -1):
        res = num[c]
        if c == 0:
            n ="1000"
            m = n.replace("1", res)
            print(m, "milenas")
        elif c == 1:
            n ="0100"
            m = n.replace("1", res)
            print(m, "centenas")
        elif c == 2:
            n ="0010"
            m = n.replace("1", res)
            print(m, "decenas")
        elif c == 3:
            n ="0001"
            m = n.replace("1", res)
            print(m, "unidades")