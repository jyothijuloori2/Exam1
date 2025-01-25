salary=int(input("enter your salary per month"))
age=int(input("enter your age"))
credit_score=float(input("enter your credit score"))
def eligibility():
    if salary>40000 and age<50 and credit_score>4:
        print("Your loan can be approved")
    elif salary>40000 and age>50 and credit_score>4:
        print("Your loan application is rejected ,due to age limit")
    elif salary>40000 and age<50 and credit_score<4:
        print("Your loan application is rejected ,due to less credit score")
    else:
          print("Your loan application is rejected ,due to less salary amount")
def main():
    eligibility()
main()