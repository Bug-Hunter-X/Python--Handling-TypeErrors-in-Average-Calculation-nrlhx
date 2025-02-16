def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) # This will return 0
print(f"The average of empty list is: {average_empty}")

my_list_with_zero = [1, 2, 0, 4, 5]
average_zero = calculate_average(my_list_with_zero) # this will work properly
print(f"The average of list with zeros is: {average_zero}")

my_list_with_strings = [1, 2, 'a', 4, 5]
average_string = calculate_average(my_list_with_strings) # this will raise TypeError
print(f"The average of list with string is: {average_string}")