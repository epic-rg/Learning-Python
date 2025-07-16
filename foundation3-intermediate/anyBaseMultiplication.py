num1 = 4234
num2 = 43
base = 5

def addBaseN(num1, num2, base):
    result = 0
    carry = 0
    x = 0

    while num1 > 0 or num2 > 0 or carry > 0:
        q1 = num1 % 10
        q2 = num2 % 10

        s = q1 + q2 + carry
        carry = 1 if s >= base else 0
        s = s % base

        result += s * (10 ** x)
        x += 1

        num1 //= 10
        num2 //= 10

    return result

def digitMultiply(num, digit, base):
    result = 0
    carry = 0
    x = 0

    while num > 0 or carry > 0:
        q = num % 10
        product = q * digit + carry
        carry = product // base
        digit_result = product % base

        result += digit_result * (10 ** x)
        x += 1

        num //= 10

    return result

def baseNMultiply(num1, num2, base):
    final_result = 0
    x = 0

    while num2 > 0:
        d = num2 % 10
        partial_product = digitMultiply(num1, d, base)
        shifted_product = partial_product * (10 ** x)

        final_result = addBaseN(final_result, shifted_product, base)

        num2 //= 10
        x += 1

    return final_result

print("-------------------------------------------------")
print(f"Multiplication of {num1} and {num2} in base {base}:")
print(baseNMultiply(num1, num2, base))
print("-------------------------------------------------")