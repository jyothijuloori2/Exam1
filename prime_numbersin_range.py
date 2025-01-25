import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers_in_range(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

def main():
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))
        
    if start > end:
        print("The starting number should be less than or equal to the ending number.")
    else:
        print_prime_numbers_in_range(start, end)
   
main()

