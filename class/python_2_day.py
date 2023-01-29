# Data Types, Numbers, Operations, Type Conversion, f-Strings

# String, Integer, Float, Boolean
print("Hello"[0])
print("Hello"[-1])

# Integer
print(1_000_000+2_000)

# Float
print(1_000.0)
print(3.14159)

# Boolean
# True or False
print("------------------------")
# Numbers
num_char = len(input("What is your name?"))
print(type(num_char))
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has "+ new_num_char+ " charaters.")
# str can not combine with int
print("------------------------")
# Mathmatical Operater
print("Mathmatical Operater")
print("7-3 :",7-3)
print("7+3 :",7+3)
print("100*3 :", 100*3)
print("100**3 :",100**3)
print("100/3  :",100/3,"(auto float type translate)")
print("100//3 :",100//3)
print("100%3 :",100%3)
print("순서 : 괄호 > 지수(**) > 곱셈,나눗셈(*,/) > 덧셈,뺄셈(+,-)")


# mathmatic 
print("8/3 =", 8/3)
print("int(8/3) = ",int(8/3))
print("round(8/3) = ", round(8/3))
print("round(8/3, 2) = ", round(8/3, 2), "소수점 3번째에서 반올림")
print("------------------------")

# F-string
score = 0
height = 1.8
iswinning = True
print(f"your score is {score} (int), your height is {height}(float), you are winning is {iswinning}(boolean)")
print("f-String은 {}안에 변수를 넣으면 되며, 다른 Data type을 문자열로 처리하는 작업이 수월하다.")


