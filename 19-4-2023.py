1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
i=1
j=1
x=int(input("Enter a number:))
for i in range(1,x+1)
    for j in range(i,i+1)
        print(i,end="")
    print()    
  
Palindrome
num=int(input("Enter a number:"))
x=num
rev=0            
while num!=0:
            rem=num%10
            rev=rev*10+rem
            num=num//10
if x == rev:
    print("Given number is palindrome")
else:
    print("Not a palindrome")            
            
