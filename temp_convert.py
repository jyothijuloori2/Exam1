
def convert_C_to_F():
    C=float(input())
    ans1=(9/5)*C +32
    return ans1
    
       
def convert_C_to_K():
    C=float(input())
    ans2=C+273.15
    return ans2
    
        
def convert_F_to_C():
    F=float(input())
    ans3=(F-32)*(5/9)
    return ans3

        
def convert_F_to_K():
    F=float(input())
    ans4=(F-32)*(5/9)-273.15
    return ans4
    
        
def convert_K_to_C():
    K=float(input())
    ans5=K-273.15
    return ans5
    
def convert_K_to_F():
    K=float(input())
    ans6=(K-273.15)*(9/5)+32
    return ans6
def main():
    choice=input()
    if choice=='A':
          print(convert_C_to_F())
    if choice=='B':
          print(convert_C_to_K())
    if choice=='C':
          print(convert_F_to_C())
    if choice=='D':
          print(convert_F_to_K())
    if choice=='E':
         print(convert_K_to_C())
    if choice=='F':
         print(convert_K_to_F())
    
main()

   