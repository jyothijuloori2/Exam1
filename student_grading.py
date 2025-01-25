name=input()
max_marks=int(input())
n=int(input("enter no.of subjects:"))
total=0
for i in range(n):
    N=int(input("enter marks for {i}"))
    total+=N
print(total)

def grade():
    P=((total)/(max_marks))*100
    print(P)
    if P<60:
        print("grade:D")
    if P>60 and P<70:
        print("grade:C")
    if P>70 and P<80:
        print("grade:B")
    if P>80 and P<100:
        print("grade:A")
def main():
    grade()
main()

