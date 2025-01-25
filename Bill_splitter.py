total_amount=int(input("enter total amount:"))
n=int(input("enter number of people:"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
def bill_splitter():
    tip_amount = (tip_percentage / 100) * total_amount
    total_with_tip=total_amount+tip_amount
    amount=total_with_tip/n
    return amount
def main():
    print(bill_splitter())

main()
