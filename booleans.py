my_list = ["a", "b", "c"]
some_other_list = [1, 2, 3, 4]

print(len(my_list) > len(some_other_list))
print(len(my_list) < len(some_other_list))
print(len(my_list) == len(some_other_list))
print(len(my_list) != len(some_other_list))


print("hello" == "Hello")

a = [1, 2, 3]
b = {1, 2, 3}

print(a == b)

x = ["a", "b", "c"]
y = ["a", "b", "c"]

print(x == y)

# the same object in memory
print(x is y)
print(x is not y)


# and(return false value), or(returns truthy value), not(returns the opposite
# value)
a = False
b = True
c = False

print("a and b is: ", a and b)
print("a or b is: ", a or b)
print("not a or b is: ", not a or b)
print("a and (b or c)is: ", a and (b or c))
