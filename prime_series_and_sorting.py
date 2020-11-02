n= int(input('enter a number:'))
for i in range(1,n+1):
    count = 0
    cur_no = i
    for j in range(1,cur_no+1):
        if cur_no % j == 0:
            count += 1
    if count==2:
            print(cur_no)
a = []
limit = int(input("enter limit: "))
print("Enter elements:")
for i in range(1,limit+1):
    value = int(input())
    a.append(value)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
            
print("The decending order:" ,a)
print("the ascending order: ",a[::-1])

