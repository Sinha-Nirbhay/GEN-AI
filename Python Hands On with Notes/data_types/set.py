
print("\n_____________________ CREATING SETS ________________\n")

my_set = {1 , 2 , "Hello" , 3.14 , (1,2)} # only immutable (hashable) items allowed
print("my_set :", my_set)

empty_set = set() # {} creates a dict, not a set
print("empty_set :", empty_set)
print("Type of {} :", type({})) # <class 'dict'>
print("Type of set() :", type(empty_set)) # <class 'set'>

dup_set = {1 , 2 , 2 , 3 , 3 , 3} # {1, 2, 3} duplicates removed
print("dup_set :", dup_set)

true_set = {1 , True , 0 , False} # {0, 1} True is treated as 1 and False as 0
print("true_set :", true_set)

my_set_ii = set("hello") # {'h', 'e', 'l', 'o'} (order may vary)
print("my_set_ii :", my_set_ii)

my_set_iii = set([1,2,2,3]) # {1, 2, 3}
print("my_set_iii :", my_set_iii)

my_set_iv = set((1,2,3)) # {1, 2, 3}
print("my_set_iv :", my_set_iv)

my_set_v = set({ "name" : "Yeyy" , "Age" : 26 }) # {'name', 'Age'} only keys (order may vary)
print("my_set_v :", my_set_v)

my_set_vi = set({ "name" : "Yeyy" , "Age" : 26 }.values()) # {'Yeyy', 26}
print("my_set_vi :", my_set_vi)

my_set_vii = set(range(5)) # {0, 1, 2, 3, 4}
print("my_set_vii :", my_set_vii)

my_set_viii = {val * 3 for val in range(8)} # {0, 3, 6, 9, 12, 15, 18, 21}
print("my_set_viii :", my_set_viii)

try:
    bad_set = {[1,2] , 3} # List is mutable, so not allowed in set
except Exception as e:
    print("Error: Mutable Item", e) # unhashable type: 'list'




print("\n___________________ ACCESSING SET ELEMENTS ________________\n")

st = {10 , 20 , 30 , 40 , 50}
print("st :", st)

20 in st # True
print("Is 20 in set:", 20 in st)

99 in st # False
print("Is 99 in set:", 99 in st)

try:
    st[0] # No indexing in set
except Exception as e:
    print("Error: Indexing not allowed", e) # 'set' object is not subscriptable

for item in st: # Order is not guaranteed
    print(f"Item: {item}" , end=" | ")

print()

sorted(st) # [10, 20, 30, 40, 50] (list)
print("Sorted set:", sorted(st))






print("\n___________________ ADD REMOVE SET ELEMENTS ________________\n")
st = {1,2,3,4,5}

st.add(6)
print("After add(6):", st)

st.add(3) # Duplicate ignored, no change
print("After add(3):", st)

st.update([7 , 8])
print("After update([7 , 8]):", st)

st.update({9} , (10 , 11)) # update can take many iterables
print("After update({9} , (10 , 11)):", st)

st |= {12 , 13}
print("After |= {12 , 13}:", st)

st = {1,2,3,4,5,6,7,8,9,10}

st.remove(10)
print("After remove(10):", st)

try:
    st.remove(99)
except Exception as e:
    print("Error: Not in the Set", e) # KeyError: 99

st.discard(99) # No error if item is not in the set
print("After discard(99):", st)

item = st.pop() # Removes a random item
print("Popped item:", item)
print("After pop():", st)

st.clear()
print("After clear():", st) # set()






print("\n___________________ SET OPERATIONS ________________\n")
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print("a :", a)
print("b :", b)

a.union(b) # {1, 2, 3, 4, 5, 6, 7, 8}
print("Union:", a.union(b))
print("Union using |:", a | b)

a.intersection(b) # {4, 5}
print("Intersection:", a.intersection(b))
print("Intersection using &:", a & b)

a.difference(b) # {1, 2, 3}
print("Difference (a - b):", a.difference(b))
print("Difference using -:", a - b)

a.symmetric_difference(b) # {1, 2, 3, 6, 7, 8}
print("Symmetric difference:", a.symmetric_difference(b))
print("Symmetric difference using ^:", a ^ b)

c = a.copy()
c.intersection_update(b) # Changes c itself
print("After intersection_update:", c) # {4, 5}

c = a.copy()
c.difference_update(b)
print("After difference_update:", c) # {1, 2, 3}

c = a.copy()
c.symmetric_difference_update(b)
print("After symmetric_difference_update:", c) # {1, 2, 3, 6, 7, 8}

{1,2}.issubset(a) # True
print("Is {1,2} subset of a:", {1,2}.issubset(a))

a.issuperset({1,2}) # True
print("Is a superset of {1,2}:", a.issuperset({1,2}))

a.isdisjoint({10,11}) # True (no common items)
print("Is a disjoint with {10,11}:", a.isdisjoint({10,11}))






print("\n_____________________ BUILT IN FUNCTIONS FOR SETS ________________\n")
nums = {4, 1, 7}
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

sorted(nums)   # [1, 4, 7] (list)
print("Sorted nums:", sorted(nums))

list(set([1,2,2,3,3,3])) # [1, 2, 3]
print("Remove duplicates from list:", list(set([1,2,2,3,3,3])))

try:
    reversed(nums) # Set has no order
except Exception as e:
    print("Error: Set is not reversible", e) # 'set' object is not reversible