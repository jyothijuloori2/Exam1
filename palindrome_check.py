s=input("enter a string or number: ")
def is_palindrome(s):
    s=str(s)
    if (s==s[::-1]):
        print("Yes it is palindrome")
    else:
        print("Not a palindrome")
def main():
    is_palindrome(s)
main()

