'''1: Take the input from the user and remove all the duplicates from it.

lst=input().split()
print(lst) # ['python', 'java', 'python', 'html', 'css', 'java']
print(set(lst)) # {'java', 'python', 'css', 'html'} '''

'''2: Write a program to print the number of duplicate elements in the list
lst=input().split()
print(lst)
print(f"Number of duplicate elements:{len(lst)-len(set(lst))}") '''

'''3: Given 3 set of roll numbers of students who play hockey,football and cricket. Print the roll numbers according to the below conditions.
a) Who play any game
b) Who play all 3 games
c) Who play only hockey
d) Who play either football or cricket but not both '''

h={1,9,12,7,14}
c={2,4,9,3,5,13}
f={6,9,8,10,5,11,12,13,15}

print(h|c|f)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(h&c&f)  # {9}
print(h-c-f)  # {1, 14, 7}
print(f^c)    # {2, 3, 4, 6, 8, 10, 11, 12, 15}
