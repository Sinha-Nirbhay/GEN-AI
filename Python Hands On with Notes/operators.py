print("\n___________________________ Arithmetic Operators ________________\n")
a = 10
b = 3

# Addition
print("a + b =", a + b)

# Subtraction
print("a - b =", a - b)

# Multiplication
print("a * b =", a * b)

# Division
print("a / b =", a / b)

# Floor Division
print("a // b =", a // b)

# Modulus
print("a % b =", a % b)

# Exponentiation
print("a ** b =", a ** b)


print("\n___________________________ Comparisonal/Relational Operators ________________\n")

# Equal to
print("a == b =", a == b)

# Not equal to
print("a != b =", a != b)

# Greater than
print("a > b =", a > b)

# Less than
print("a < b =", a < b)

# Greater than or equal to
print("a >= b =", a >= b)

# Less than or equal to
print("a <= b =", a <= b)

print("\n___________________________ Logical Operators ________________\n")

# and → looks for the first FALSE value
# or  → looks for the first TRUE value
# not → reverses TRUE/FALSE

# a and b    If a is truthy → return b else return a
# a or b    If a is truthy → return a else return b
# not a    Reverse truthiness    False

a=3
b=10


# Logical AND
print("a and b =", a and b)

# Logical OR
print("a or b =", a or b)

# Logical NOT
print("not a =", not a)


print("\n___________________________ Assignment Operators ________________\n")

a , b , c = 1, 2 ,3

# Assignment
c = a
print("c =", c)

# Add AND assignment
c += b
print("c += b =", c)

# Subtract AND assignment
c -= b
print("c -= b =", c)

# Multiply AND assignment
c *= b
print("c *= b =", c)

# Divide AND assignment
c /= b
print("c /= b =", c)

# Floor Divide AND assignment
c //= b
print("c //= b =", c)

# Modulus AND assignment
c %= b
print("c %= b =", c)

# Exponent AND assignment
c **= b
print("c **= b =", c) 

print("\n___________________________ Bitwise Operators ________________\n")

a = 10
b = 3

# Bitwise AND
print("a & b =", a & b)

# Bitwise OR
print("a | b =", a | b)

# Bitwise XOR
print("a ^ b =", a ^ b)

# Bitwise NOT
print("~a =", ~a)

# Bitwise Left Shift
print("a << b =", a << b)

# Bitwise Right Shift
print("a >> b =", a >> b)

print("\n___________________________ Membership Operators ________________\n")

my_list = [1, 2, 3, 4, 5]

# Membership - in
print("3 in my_list =", 3 in my_list)

# Membership - not in
print("6 not in my_list =", 6 not in my_list)


print("\n___________________________ Identity Operators ________________\n")    

a = 10
b = 10

# Identity - is
print("a is b =", a is b)

# Identity - is not

a=288
b=288
print("a is not b =", a is not b)

print("\n___________________________ Other Operators ________________\n")
# x if condition else y ternary (conditional) operator
x = 5
y = 10
max_value = x if x > y else y
print("max_value =", max_value)

# * and ** unpacking operators
def my_function(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

my_list = [1, 2, 3]
my_function(*my_list)  # Unpacking list into function arguments

my_dict = {"a": 4, "b": 5, "c": 6}
my_function(**my_dict)  # Unpacking dictionary into function arguments

#packing
def my_packing_function(*args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)

my_packing_function(1, 2, 3, a=4, b=5)