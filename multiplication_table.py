n=int(input("enter the table you want:"))
N=int(input("enter the range:"))
def table(n):
    for i in range(0,N+1,1):
        print(f"{n}*{i}=",n*i)
def main():
   table(n)
main()

