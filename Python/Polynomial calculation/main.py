input_line1 = input().strip().split()
n = int(input_line1[0])
x = int(input_line1[1])

coefficients = list(map(int, input().strip().split()))

result = 0
power = n - 1

for coef in coefficients:
    result += coef * (x ** power)
    power -= 1

print(result)
