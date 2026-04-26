'''1.Create a list of even numbers from 2 to 2000.
get two numbers, x and y, which are positions (1-based) in this list.
Calculate the sum of the numbers from position x to position y (inclusive).
Print the sum.

def solution():
    nums =[]
    x ,y = map(int, input("Enter starting and ending Index: ").split())
    sum = 0
    for i in range(2 ,2001 ,2):
        nums.append(i)

    extract = nums[ x -1:y]

    for i in range(len(extract)):
        sum += extract[i]

    print(sum)
# Call the function
solution() '''

'''2.Given an array of integers, calculate and return the sum of its elements. 
Input Format:
The first line contains an integer , denoting the size of the array.
The second line contains space-separated integers representing the array's elements

def solution(n):
    nums = list(map(int, input("Enter Array Elements: ").split()))
    arr_sum = 0
    for i in range(len(nums)):
        arr_sum += nums[i]

    print(arr_sum)

solution( n= int(input("Enter a number "))) '''

'''3.Balanced Parentheses using Stack
Every opening bracket must be closed in correct order
The last opened bracket must be closed first'''

def isvalid(s):
    stack=[]
    mapping={')':'(','}':'{',']':'['}

    for char in s:
        if char in mapping:
            if not stack or stack[-1]!= mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack)==0

print(isvalid('{[()]}'))

'''4.Find the frequency of a given character in a given string.'''

s='programming'

def count_of_character(s,target):
    count=0
    for char in s.lower():
        if char==target:
            count+=1
    return count

print(count_of_character(s,'g'))

'''5.Inserting a element inside a sorted list'''

def insert_sort(arr,val):
    for i in range(len(arr)):
        if val<arr[i]:
            arr.insert(i,val)
            return arr
    arr.append(val)
    return arr
print(insert_sort([1,3,5,7],6))

'''6.Left View of Binary Tree (Using BFS)'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque

def leftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(leftView(root))

'''7.Reversing a string'''

s='programming'
rev=''
print(s[::-1])
for char in s:
    rev=char+rev
print(rev)

'''8.Merging two sorted linked list'''

class Node:
    def __init__(self,value):
        self.value=value
        self.next_node=None

def build_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next_node = Node(val)
        current = current.next_node

    return head

def merge_sorted_list(first_list,second_list):
    merge_head = Node(0)
    current_position=merge_head

    while first_list and second_list:
        if first_list.value < second_list.value:
            current_position.next_node=first_list
            first_list=first_list.next_node

        else:
            current_position.next_node=second_list
            second_list=second_list.next_node

        current_position=current_position.next_node

    if first_list:
        current_position.next_node=first_list
    else:
        current_position.next_node=second_list

    return merge_head.next_node


def print_linked_list(head):
    current = head

    while current:
        print(current.value, end=" -> ")
        current = current.next_node

    print("None")

list1 = build_linked_list([1,2,3])
list2 = build_linked_list([4,5,6])

merged=merge_sorted_list(list1, list2)
print_linked_list(merged)