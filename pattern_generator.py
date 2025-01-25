n=int(input("enter no.of rows"))
your_inp=input("enter yes if you want to print reverse pattern and no if you dont want")

def pattern_reverse(n):
    for i in range(n,0,-1):
         print("*" * i)

def pattern_generator(n):
    for i in range(1,n+1):
        print("*" * i)

def main():
    if your_inp=='yes':
        pattern_reverse(n)
    if your_inp=='no':
        pattern_generator(n)
main() 