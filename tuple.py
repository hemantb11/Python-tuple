# Tuple Creation and Type Check
x=(10,20,30)
print(x,type(x))

# Access Tuple Element using Index
print(x[2])

# Traverse Tuple using for loop
for i in x:
    print(i)


# Membership Operator in Tuple
x=("red","pink","black")

# Check element exists in tuple
print("red" in x)
print("grey" in x)


# Identity Operator (is)
x=(10,20)
y=(10,20,30)
z=x

print(x is y)   # False (different objects)
print(x is z)   # True  (same reference)


# Tuple Functions and Slicing
x=(10,20,30)

print(len(x))        # Length of tuple
print(x.count(20))   # Count occurrences
print(x.index(30))   # Index of element

print(x[1:])         # Slicing from index 1 to end
print(x[1:2])        # Slicing single element tuple


# Nested Tuple Traversal
x=((10,20),30,(40,50),"hii")

for i in x:
    if type(i)==tuple:
        for j in i:
            print(j)
        continue
    print(i)


# List and Tuple Mixed Traversal
x=[10,[20,30],40,(50,60)]

for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            print(j)
        continue
    print(i)


# Deep Nested Structure Traversal
x=(90,"hi",("red",[10,20]),[100,200])

for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==list:
                for k in j:
                    print(k)
                continue
            print(j)
        continue
    print(i)


# Convert Tuple to List and Add Element
x=(10,20)

print(x,type(x))

y=list(x)     # Convert tuple to list

y.append(90)  # Add new element

print(y,type(y))

x=tuple(y)    # Convert list back to tuple

print(x,type(x))