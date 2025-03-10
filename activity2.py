numlarger = int(input('Enter the largest number : '))
numsmall = int(input('Enter the smallest number : '))

while numsmall:
    numstore=numsmall
    numsmall = numlarger % numsmall
    numlarger = numstore

print('HCF is : ', numlarger)
