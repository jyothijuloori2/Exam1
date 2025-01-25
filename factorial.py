def factorial(n):
    fact=1
    if n<0:
        return False
    for i in range(1,n+1):
        fact*=i
    print(f"factorial of {n} is {fact}")
def main():
    factorial(n)
n=int(input())
main()


