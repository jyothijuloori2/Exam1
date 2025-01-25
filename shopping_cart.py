def shopping():
    cost=0
    n=int(input("enter number of items"))
    for i in range(n):
        
        costofitem=int(input())
        cost+=costofitem
    return cost
def main():
    print(shopping())
main()