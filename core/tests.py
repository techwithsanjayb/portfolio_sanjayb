# Assignment 1 

# Q1 
User_Score  = int(input("Enter a number between 0 and 100"))

if User_Score >= 0 and User_Score <= 100:
    if User_Score >= 90:
        Grade = "A"
    elif User_Score >= 80 and User_Score <=89:
        Grade = "B"
    elif User_Score >= 70 and User_Score <=79:
        Grade = "C"
    elif User_Score >= 60 and User_Score <=69:
        Grade = "D"
    else:
        Grade = "F"
    print("Your score is " + Grade)
else:
    print("Please enter a number between 0 and 100")

# Q2 
sum = 0
for i in range(2,102,2):
    sum = sum+i
print("Sum of even number from 0 to 100 is ", +sum)


# Q3 
user_input_year = int(input("Enter a Year"))

if user_input_year % 4 == 0:
    if user_input_year % 100 == 0:
        if user_input_year % 400 == 0:
            print("Year is Leap Year")
        else:
            print("Year is not a Leap Year")
    else:
        print("Year is a Leap Year")
else:
    print("Year is not a Leap Year")


# Q4 
user_input = int(input("Enter a User input number"))

for i in range(1,11):
    print(f"{user_input} x {i} = {user_input*i}")