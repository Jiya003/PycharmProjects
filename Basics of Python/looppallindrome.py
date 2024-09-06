string=input('Enter a String')
rev=""
for i in string:
    rev=i+rev
print(rev)

if (rev==string):
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')