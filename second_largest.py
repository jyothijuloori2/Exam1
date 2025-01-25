def find_second_largest(numbers):
    largest = second_largest = float('-inf')  
    for num in numbers:
        if num > largest:
            second_largest = largest  
            largest = num  
        elif num > second_largest and num != largest:
            second_largest = num  
    if second_largest == float('-inf'):
        return "No second largest number found"  
    return second_largest
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Second largest number is:", find_second_largest(numbers))

