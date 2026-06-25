n = int(input("Enter the number: "))
def find_sum (n) :
    total = 0 
    for i in range(1, n + 1):
        total =  total + i
    print("sum" , total)
    
find_sum(n)
    
