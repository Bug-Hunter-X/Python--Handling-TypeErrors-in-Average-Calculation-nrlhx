def calculate_average(numbers):
    try:
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    except TypeError:
        print("Error: List contains non-numeric values.")
        return None
    except ZeroDivisionError:
        print("Error: List is empty.")
        return 0

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1, 2, 0, 4, 5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zeros is: {average_zero}")

my_list_with_strings = [1, 2, 'a', 4, 5]
average_string = calculate_average(my_list_with_strings)
print(f"The average of a list with strings is: {average_string}") 