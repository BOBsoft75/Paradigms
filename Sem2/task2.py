from string import ascii_uppercase, digits

DIGITS = digits + ascii_uppercase


def bin_octa(num, prod):
    result = []
    while num > 0:
        temp = num % prod
        result.append(DIGITS[temp])
        num //= prod
    return "".join(result[::-1])


number = int(input("Введите число: "))
res = bin_octa(number, 16)
print(res)
