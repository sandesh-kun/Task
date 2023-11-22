a = 48
b = 18

while b != 0:
    a, b = b, a % b

gcd_result = a

if gcd_result == 1:
    print(f"The numbers {a} and {b} are coprime.")
else:
    print(f"The GCD of {a} and {b} is {gcd_result}.")
