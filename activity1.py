num = int(input('Enter your number : '))

temp = num
revnum = 0 

while temp > 0 :
    digit=temp % 10
    revnum = revnum * 10 + digit
    temp = temp // 10

if(num == revnum):
    print(num,' is palindrome')
else:
    print(num,'is not  palindrome')