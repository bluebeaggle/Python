#Write your code below this row 👇
sum = 0
for i in range(1,101) :
    if i %2 == 0 :
        sum += i
    else :
        continue
print(sum)
sum = 0
for i in range(2,101,2) :
    sum += i
print(sum)