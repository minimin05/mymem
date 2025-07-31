def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) 
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

number = [5, 10, 15, 20, 25]
total, avg, max_val, min_val = calculate_stats(number)

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum Value: {max_val}")
print(f"Minimum Value: {min_val}")