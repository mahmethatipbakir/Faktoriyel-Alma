"""Faktoriyel alma programı"""

def fact(sayi):
    if sayi <= 1:
        return 1
    else:
        return sayi * fact(sayi - 1)


if __name__ == '__main__':
    sayi = int(input("Faktoriyel almak istediğiniz sayıyı yazınız: "))

    print(fact(sayi))
