
input_line1 = input().strip().split()
n = int(input_line1[0])
x = int(input_line1[1])


coefficients = list(map(int, input().strip().split()))

result = 0
power = n - 1
polynomial_str = "P(x) = "
evaluation_str = ""

for i, coef in enumerate(coefficients):

    x_to_the_power = 1
    for _ in range(power):
        x_to_the_power *= x

    term_value = coef * x_to_the_power
    result += term_value

    if i > 0:
        polynomial_str += " + " if coef >= 0 else " - "
        evaluation_str += " + " if term_value >= 0 else " - "

    polynomial_str += f"{abs(coef)} × {x}^{power}"
    evaluation_str += f"{abs(term_value)}"

    power -= 1

print(result)
print(f"{polynomial_str} = {evaluation_str} = {result}")
