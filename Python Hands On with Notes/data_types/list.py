
print("\n________________ CREATING LISTS ________________\n")

my_list = [1 , 2 , "Hello" , True , 3.14 , [1,2] , (1,2) , {"name" : "Yeyy"}]
print("my_list :", my_list)

empty_list = []
print("empty_list :", empty_list)

my_list_ii = list("abcde") # ['a', 'b', 'c', 'd', 'e']
print("my_list_ii :", my_list_ii)

my_list_iii = list((1,2,3)) # [1, 2, 3]
print("my_list_iii :", my_list_iii)

my_list_iv = list({ "name" : "Yeyy" , "Age" : 26 }) # ['name', 'Age']
print("my_list_iv :", my_list_iv)

my_list_v = list({ "name" : "Yeyy" , "Age" : 26 }.values()) # ['Yeyy', 26]
print("my_list_v :", my_list_v)

my_list_vi = list({1, 2, 3}) # [1, 2, 3] (order may vary)
print("my_list_vi :", my_list_vi)

my_list_vii = list(range(5))  # [0, 1, 2, 3, 4]
print("my_list_vii :", my_list_vii)

my_list_viii = [val * 3 for val in range(8)] # [0, 3, 6, 9, 12, 15, 18, 21]
print("my_list_viii :", my_list_viii)




print("\n___________________ ACCESSING LIST ELEMENTS ________________\n")

lst = [1,2,3,4,5,6,7,8,9,10]

lst[0] # First element
print("First element:", lst[0])

lst[-1] # Last element
print("Last element:", lst[-1])


lst[2:5:1]  # Elements from index 2 to 4
print("Elements from index 2 to 4:", lst[2:5:1])


lst[::2] # Every second element
print("Every second element:", lst[::2])

lst[::-1]  # Reversed list
print("Reversed list:", lst[::-1])






print("\n___________________ ADD REMOVE UPDATE LIST ELEMENTS ________________\n")
lst = [1,2,3,4,5,6,7,8,9,10]
lst_i = [11,12,13]

lst.append(25)
print("Append :" , lst)

lst.insert(0 , -25)
print("Insert at beginning:", lst)

lst += lst_i
print("After += lst_i:", lst)

lst.extend(lst_i)
print("After extend(lst_i):", lst)

lst.extend([-50 , -51])
print("After extend([-50 , -51]):", lst)

lst = [1,2,3,4,5,6,7,8,9,10]
lst_i = [11,12,13]

lst.remove(10)
print("After remove(10):", lst)

try:
    lst.remove(12)
except ValueError as e:
    print("Error:", e)
print("After remove(12):", lst) # Error Not in the List

lst.pop()
print("After pop():", lst)

lst.pop(0)
print("After pop(0):", lst) 

del lst[0]
print("After del lst[0]:", lst)

lst.clear()
print("After clear():", lst)


lst = [1,2,3,4,5,6,7,8,9,10]

lst[1] = 25
print("After updating index 1 to 25:", lst)

lst[2:6] = [30, 31, 32, 33]
print("After updating index 2 to 5:", lst)

print("\n_____________________BUILT IN FUNCTIONS FOR LISTS ________________\n")
nums = [4, 1, 7]
len(nums)      # 3
print("Length of nums:", len(nums))
    
sum(nums)      # 12
print("Sum of nums:", sum(nums))

min(nums)      # 1
print("Minimum of nums:", min(nums))

max(nums)      # 7
print("Maximum of nums:", max(nums))

any(nums)      # True
print("Any of nums:", any(nums))

all(nums)      # True
print("All of nums:", all(nums))

sorted(nums)   # [1, 4, 7]
print("Sorted nums:", sorted(nums))

reversed(nums) # <list_reverseiterator object at 0x...>
print("Reversed nums:", list(reversed(nums)))

list(reversed(nums)) # [7, 1, 4]    
print("Reversed nums:", list(reversed(nums)))
