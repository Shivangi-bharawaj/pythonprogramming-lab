def check_even_or_not(a):
    if a%2==0:
        return 'Entered number is even number '
    else:
        return 'Entered number id odd number '
num=int(input('Enter the number : '))
out=check_even_or_not(num)
print(out)