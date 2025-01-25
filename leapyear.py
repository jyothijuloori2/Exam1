def leapcheck():
    year=int(input("enter the year"))
    if (year%4==0 and year%100!=0 or year%400==0):
        print("It is a leap Year")
    else:
        print("It is not a leap Year")
def main():
    leapcheck()
main()
