# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

heights_sum = 0
heights_len = 0
for i in student_heights :
    heights_sum += i
    heights_len += 1

average_heights = round(heights_sum / heights_len)
print(average_heights)

