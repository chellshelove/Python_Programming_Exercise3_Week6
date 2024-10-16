# Get 5 integers from the user and store them in a list
numbers = [int(input(f"Enter integer {i+1}: ")) for i in range(5)]

# Sort the list in descending order
sorted_numbers = sorted(numbers, key=lambda x: -x)

# Print the sorted list
print("Sorted list in descending order:", sorted_numbers)