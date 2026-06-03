# Conditional Statements Practice
# Conditional statements allow us to execute certain blocks of code based on specific conditions.

# 1. If Statement
# The if statement is used to execute a block of code if a specified condition is true.
is_student = True

if is_student :
    print("Student.")

# 2. If-Else Statement
# The if-else statement is used to execute if statement if the condition is true and else statement if the condition is false.
is_student = False

if is_student :
    print("Student.")
else :
    print("Not a student.")

# 3. If-Elif_Else Staement
# The if-elif-else statement is used to execute one block of code among multiple conditions.
marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

# 4. Nested If Statement.
# A nested if statement is an if statement that is inside another if statement.
marks = 85

if marks >= 35:
    print("Passed")

    if marks >= 75:
        print("Distinction")

# 5. Logical Operators in Conditional Statements.
# Logical operators (and, or, not) are used to combine multiple conditions in an if statement.

# And Operator gives True if both conditions are true.
marks = 85

if marks >= 35 and marks <= 100:
    print("Valid marks")

# Or Operator gives True if at least one condition is true.
marks = 105
if marks < 35 or marks > 100:
    print("Invalid marks")

# Not Operator gives True if the condition is false and vice versa.
is_raining = False
if not is_raining:
    print("It's not raining.")

