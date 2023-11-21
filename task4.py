n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

odd = 0
even = 0

for num in numbers:
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"Numbers: {numbers}")
print(f"Sum of odd numbers: {odd}")
print(f"Sum of even numbers: {even}")
