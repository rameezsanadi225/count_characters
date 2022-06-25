x=input("Enter the string: ")
a=x.split(' ')
count=0
upper_count=0
lower_count=0
digit_count=0
symbol_count=0
for i in a:
    for j in i:
        if j.islower():
            lower_count+=1
        elif j.isdigit():
            digit_count+=1
        elif j.isupper():
            upper_count+=1
        else:
            symbol_count+=1
count= upper_count+digit_count+lower_count+symbol_count
print("The number of words in the string is",len(a))
print("The number of letters in the string is",count)
print("The number of digits in the string is",digit_count)
print("The number of symbols in the string is",symbol_count)
print("The number of upper-case letters in the string is",upper_count)
print("The number of lower-case letters in the string is",lower_count)