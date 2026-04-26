'''1.WAP to print all the substribgs with length 3 from the given string.
s=input("Enter a string:\n")
for i in range(0,len(s)-2):
    print(s[i:i+3]) '''

'''2.WAP to print all the characters of a string except first and last characters
s=input("Enter a string:\n")
print(s[1:len(s)-1]) '''

'''3.WAP to print all the characters of a string in reverse order except first and last character
s=input("Enter a string:\n")
print(s[len(s)-2:0:-1])'''

'''4.WAP to check whether given string is palindrome.
if s==s[::-1]:
    print("It's palindrome")
else:
    print("It's not a palindrome") 

# Approach 2
s=input("Enter a string:\n")
rev=''
for i in s:
    rev = i+rev
if rev==s:
    print("It's palindrome")
else:
    print("It's not a palindrome") '''

'''5.WAP to reverse the second half of the string '''
s=input("Enter the string: ")
first=s[0:len(s)//2]
last=s[len(s):(len(s)//2)-1:-1]
print(first+last)
