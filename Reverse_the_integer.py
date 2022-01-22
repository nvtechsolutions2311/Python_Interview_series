##### Reverse the integer entered by the user #####
## Input = Integer     Output = Reverse of Integer
## 1000+200+30+4 =1234 Input
## 4000+300+20+1=4321 Output

### CLASSICAL METHOD
number = int(input("Enter The Number For Classical Method : "))
reverse = 0
while number != 0:
    reverse= reverse*10 + number%10
    number=number//10

print(f"Reversed integer is : {reverse}")

### ITERATIVE METHOD
num=int(input("Enter the Number For Iterative Method : "))
new_num=str(num)
for i in range (1,len(new_num)+1):
    print(new_num[-i],end="")
print("")

### DIRECT METHOD
n=int(input("Enter the Number For Direct Method : "))
str_num=str(n)
print(str_num[::-1])