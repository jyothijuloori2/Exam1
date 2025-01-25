arr=list(map(int,input().split()))
even_list=[]
odd_list=[]
def sep_odd_even():
    for i in arr:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)
def main():
    sep_odd_even()
main()
