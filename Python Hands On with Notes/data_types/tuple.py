
print("\n_____________________ CREATING TUPLES ________________\n")

my_tuple = (1 , 2 , "Hello" , True , 3.14 , [1,2] , (1,2) , {"name" : "Yeyy"})
print("my_tuple :", my_tuple)

empty_tuple = ()
print("empty_tuple :", empty_tuple)

single_tuple = (1,) # trailing comma needed for single item tuple
print("single_tuple :", single_tuple , type(single_tuple)) # <class 'tuple'>

not_a_tuple = (1) # this is just an int
print("not_a_tuple :", not_a_tuple , type(not_a_tuple)) # <class 'int'>

no_bracket_tuple = 1 , 2 , 3 # packing, brackets are optional
print("no_bracket_tuple :", no_bracket_tuple)

my_tuple_ii = tuple("abcde") # ('a', 'b', 'c', 'd', 'e')
print("my_tuple_ii :", my_tuple_ii)

my_tuple_iii = tuple([1,2,3]) # (1, 2, 3)
print("my_tuple_iii :", my_tuple_iii)

my_tuple_iv = tuple({ "name" : "Yeyy" , "Age" : 26 }) # ('name', 'Age')
print("my_tuple_iv :", my_tuple_iv)

my_tuple_v = tuple({ "name" : "Yeyy" , "Age" : 26 }.values()) # ('Yeyy', 26)
print("my_tuple_v :", my_tuple_v)

my_tuple_vi = tuple({1, 2, 3}) # (1, 2, 3) (order may vary)
print("my_tuple_vi :", my_tuple_vi)

my_tuple_vii = tuple(range(5)) # (0, 1, 2, 3, 4)
print("my_tuple_vii :", my_tuple_vii)

my_tuple_viii = tuple(val * 3 for val in range(8)) # (0, 3, 6, 9, 12, 15, 18, 21) no tuple comprehension, generator inside tuple()
print("my_tuple_viii :", my_tuple_viii)




print("\n___________________ ACCESSING TUPLE ELEMENTS ________________\n")

tup = (1,2,3,4,5,6,7,8,9,10)

tup[0] # First element
print("First element:", tup[0])

tup[-1] # Last element
print("Last element:", tup[-1])

tup[2:5:1]  # Elements from index 2 to 4
print("Elements from index 2 to 4:", tup[2:5:1])

tup[::2] # Every second element
print("Every second element:", tup[::2])

tup[::-1]  # Reversed tuple
print("Reversed tuple:", tup[::-1])

tup = (1,2,3,2,4,2)

tup.count(2) # 3
print("Count of 2:", tup.count(2))

tup.index(2) # 1 (first match)
print("Index of first 2:", tup.index(2))

try:
    tup.index(99)
except Exception as e:
    print("Error: Not in the Tuple", e) # tuple.index(x): x not in tuple






print("\n___________________ TUPLE IS IMMUTABLE ________________\n")
tup = (1,2,3,4,5)
print("tup :", tup)

try:
    tup[0] = 100 # Update not allowed
except Exception as e:
    print("Error: Update not allowed", e) # 'tuple' object does not support item assignment

try:
    del tup[0] # Delete not allowed
except Exception as e:
    print("Error: Delete not allowed", e) # 'tuple' object doesn't support item deletion

print("Tuple has append :", hasattr(tup, "append")) # False

# To change a tuple : convert to list -> change -> convert back to tuple
lst = list(tup)
lst.append(6)
lst[0] = 100
tup = tuple(lst)
print("After changing using list:", tup) # (100, 2, 3, 4, 5, 6)

tup = (1,2,3)

tup + (4,5) # New tuple
print("Concatenate with + :", tup + (4,5))

tup * 2 # New tuple
print("Repeat with * :", tup * 2)

print("Original tuple:", tup) # No change

tup = (1 , [2,3])
tup[1].append(4) # Mutable item inside tuple can still change
print("Mutable item inside tuple:", tup) # (1, [2, 3, 4])

del tup # Deletes the whole tuple variable
try:
    print(tup)
except Exception as e:
    print("Error: Tuple deleted", e) # name 'tup' is not defined






print("\n___________________ PACKING AND UNPACKING ________________\n")

a , b , c = (1 , 2 , 3) # Unpacking
print("a , b , c :", a , b , c)

first , *rest = (1 , 2 , 3 , 4)
print("first :", first) # 1
print("rest :", rest) # [2, 3, 4] (rest is a list)

a , b = b , a # Swap using tuple
print("After swap a , b :", a , b)






print("\n_____________________ BUILT IN FUNCTIONS FOR TUPLES ________________\n")
nums = (4, 1, 7)
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

sorted(nums)   # [1, 4, 7] (list, not tuple)
print("Sorted nums:", sorted(nums))

reversed(nums) # <reversed object at 0x...>
print("Reversed nums:", tuple(reversed(nums))) # (7, 1, 4)






