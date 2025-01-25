weight=int(input("enter your weight in kgs: "))
height=float(input("enter your height in mts:"))
def cal_bmi(weight,height):
    x=weight/(float(height*height))
    if x<18.5:
        print("underweight")
    if x>18.5 and x<25:
        print("Normal")
    if x>25 and x<30:
        print("overweight")
    if x>30:
        print("obesity")
def main():
    cal_bmi(weight,height)
main()
