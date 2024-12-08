numbers = list(range(1,100 + 1))

sum_of_squares = sum([x ** 2 for x in numbers])
square_of_sum = sum(numbers) ** 2

print(square_of_sum - sum_of_squares)
