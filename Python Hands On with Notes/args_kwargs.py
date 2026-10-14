print("____________________________ *args ___________________________________")

# Variable argument * allows to pass a variable number of positional arguments to a function
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

def sum_ii(*val):
    total = 0
    for num in val:
        total += num
    return total

print("Sum : ", sum(1,2,3,4,5))
print("Sum II : ", sum_ii(1,2,3,4,5,6))


print("____________________________ **kwargs ___________________________________")


def kwargs_practice(**kwargs):
    for key, value in kwargs.items():
        print("Key :" , key ,  "Value :" , value)

kwargs_practice(name="HEYY", Village="JOJO" , Age = 26)