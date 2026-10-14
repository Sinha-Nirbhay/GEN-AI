print("_______________ Integer _______________\n")

a = 18
print("Value of a :", a)
print("Type of a :", type(a))

print("\n_______________ Float _______________\n")

b = 10.5
print("Value of b :", b)
print("Type of b :", type(b))

x = 2 + 3.5
print("Value of x :", x)
print("X = 2 + 3.5, Type of x :", type(x))

print("\n_______________ Boolean _______________\n")

d = True
print("Value of d :", d)
print("Type of d :", type(d))

print("True==1" , True==1)
print("False==0" , False==0)
print("2 + True" , 2 + True)
print("2 + False" , 2 + False)

x = 2 + True
print("Value of x :", x)
print("X = 2 + True, Type of x :", type(x))

print("\n_______________ String _______________\n")

c = "Hello"
print("Value of c :", c)
print("Type of c :", type(c))


print("\n_______________ String Immutability _______________\n")

str = "Hello"

print("Initial value of str :", str)
print("Trying to modify the first character of str...")

try:
    str[0] = "J"          # modify in place
except TypeError as e:
    print("Error:", e)

print("Final value of str :", str)