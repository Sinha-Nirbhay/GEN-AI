
print("\n_____________________ CREATING DICTS ________________\n")
my_dict = {"Name":"Yeyy" , "Age":26 , "Hobby":"Cricket"}
print("my_dict :", my_dict)

my_dict = {}
print("Empty my_dict :", my_dict)

my_dict_ii = dict(name = "Yeyy" , Age = 26) # {'name': 'Yeyy', 'Age': 26}
print("my_dict_ii :", my_dict_ii)

my_dict_iii = dict([("name" , "Yeyy") , ("Age" , 26)]) # {'name': 'Yeyy', 'Age': 26}
print("my_dict_iii :", my_dict_iii)

my_dict_iv = dict(zip(["name" , "Age"] , ["Yeyy" , 26])) # {'name': 'Yeyy', 'Age': 26}
print("my_dict_iv :", my_dict_iv)

my_dict_v = dict.fromkeys(["a" , "b" , "c"] , 0) # {'a': 0, 'b': 0, 'c': 0}
print("my_dict_v :", my_dict_v)

my_dict_vi = { val : val * val for val in range(5) } # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print("my_dict_vi :", my_dict_vi)

dup_key_dict = { "a" : 1 , "a" : 2 } # {'a': 2} duplicate key, last value wins
print("dup_key_dict :", dup_key_dict)

try:
    bad_dict = { [1,2] : "list as key" } # Key must be immutable
except Exception as e:
    print("Error: Mutable Key", e) # unhashable type: 'list'


print("\n_____________________ ACCESSING DICT ELEMENTS ________________\n")



my_dict = {"Name":"Yeyy" , "Age":26 , "Hobby":"Cricket" , "Country":"India" , "Profession":"Engineer"}

print("my_dict :", my_dict)

Name = my_dict["Name"]
print("Accessing 'Name' using my_dict[key]:", Name)

try:
    Val = my_dict["InvalidKey"]
except Exception as e:
    print("Error: Key not found", e)

Name = my_dict.get("Name")
print("Accessing 'Name' using get():", Name)

InavildKey = my_dict.get("InvalidKey" , "Key Not Present")
print("Accessing 'InvalidKey' using get() with default value:", InavildKey)

keys = my_dict.keys()
print("All keys in my_dict:", keys)
print("Type of keys object:", type(keys))

values = my_dict.values()
print("All values in my_dict:", values)
print("Type of values object:", type(values))

items = my_dict.items()
print("All items in my_dict:", items)
print("Type of items object:", type(items))

print("\n_____________________ ITERATING OVER DICTS ________________\n")

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}" , end=" | ")

print()

for key in my_dict:    
    print(f"Key: {key}, Value: {my_dict[key]}" , end=" | ")


print("\n______________________ UPDATE DICTS ________________________\n")

my_dict = {"Name":"Yeyy" , "Age":26 , "Hobby":"Cricket" , "Country":"India" , "Profession":"Engineer"}

my_dict["State"] = "Bihar"
print("Updated my_dict with new 'State' key:", my_dict)

my_dict["State"] = "Karnataka"
print("Updated 'State' key in my_dict:", my_dict)

my_dict.update({"Age": 27, "Hobby": "Football" , "Champion": "Yes"})
print("Updated my_dict using update():", my_dict)


try:
    val_i = my_dict.pop("Champion")
    print("Popped 'Champion' value:", val_i)

    val_ii = my_dict.pop("InvalidKey")
    print("Popped 'InvalidKey' value:", val_ii)
except Exception as e:
    print("Error: Pop failed - No Such Keys", e)

print("\n_____________________BUILT IN FUNCTIONS FOR DICTIONARIES ________________\n")

my_dict = {"Name":"Yeyy" , "Age":27 , "Hobby":"Football" , "Country":"India" , "Profession":"Engineer" , "State":"Karnataka"}

len(my_dict)              # 6
print("Length of my_dict:", len(my_dict))

min(my_dict)              # 'Age' (smallest key)
print("Minimum key:", min(my_dict))

max(my_dict)              # 'State' (largest key)
print("Maximum key:", max(my_dict))

sum([value for value in my_dict.values() if isinstance(value, (int, float))])     # 54
print("Sum of numeric values:", sum([value for value in my_dict.values() if isinstance(value, (int, float))]))

sorted(my_dict)           # ['Age', 'Country', 'Hobby', 'Name', 'Profession', 'State'] (sorted keys)
print("Sorted keys:", sorted(my_dict))

list(my_dict)             # ['Name', 'Age', 'Hobby', 'Country', 'Profession', 'State'] (keys)
print("Keys as list:", list(my_dict))


any(my_dict)
print("Any of my_dict:", any(my_dict))    # True
             
all(my_dict)
print("All of my_dict:", all(my_dict))              # True
 
 
    
