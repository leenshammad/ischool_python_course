# Lesson 1: Solving on Loops

## Key Concepts

### Loops
to let the code to repeat itself. don't let programmers copy same code again and again

```py
fruit_list = ["Orange", "Banana", "Strawberry"]
for fruit in fruit_list:
    print(fruit)
```

### range() function

create sequence to control the loop runs
1,2,3,4,5           : range(1,6) # ends at n-1
1,3,5,7             : range(1,8,2) #start, end, and step
7,8,9               : range(7,10)
0,1,2               : range(3)

```py
for i in range(1,6):
    print(i)        # will print from 1 to 5
```

### Control statements

break, continue, pass
control how code behaves

```py
i = 0
while True:
    i = i+1
    if i > 5 :
        break

for i in range(1,5):
    if i == 3:
        continue
    print(i)        # print 1,2,4

def draw_star:
    pass

```

### Nested loop

to have a loop inside another loop

```py
count = 0
for i in range(8):
    for j in range(3):
        print(count)
        count += 1  # print 0 - 23

```

# Lession 2: 

## Key Concepts

### concept #1
