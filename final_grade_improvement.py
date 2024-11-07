###########################################################################################
# Program: Final Grade Improvement
# Author: Jayce Baxter
# Date: November 5th, 2024
# Description: Improving final_grade by adding functions, a menu, and overall optimization
###########################################################################################

# Setting the weights of each grade as a constant, multiplied by the amount of each activity. For example 2 tests * weight of 6.
CLASS_EXERCISE_WEIGHT = 12
ASSIGNMENT_WEIGHT = 10
TEST_WEIGHT = 12
QUIZ_WEIGHT = 15

# Initializing the user_input variable. Unsure if this is necessary. Sometimes it gives me an error saying it's undefined.
user_input = 0

# Initializing my lists
grade = []
assignment = []
test = []
class_exercise = []
quiz = []

# Setting all the prompts as constants
PROMPT_1 = ("Please enter your grade for Class Exercise 1 - Planning an Application: ")
PROMPT_2 = ("Please enter your grade for Class Exercise 2 - Numeric and String Data: ")
PROMPT_3 = ("Please enter your grade for Class Exercise 3 - Selection: ")
PROMPT_4 = ("Please enter your grade for Class Exercise 4 - Iteration: ")
PROMPT_5 = ("Please enter your grade for Test 1 - Theory: ")
PROMPT_6 = ("Please enter your grade for Test 1 - Practical: ")
PROMPT_7 = ("Please enter your grade for Assignment 1 - Iteration: ")
PROMPT_8 = ("Please enter your grade for Quiz 1 - Planning an Application: ")
PROMPT_9 = ("Please enter your grade for Quiz 2 - Numeric and String Data: ")
PROMPT_10 = ("Please enter your grade for Quiz 3 - Selection: ")
PROMPT_11 = ("Please enter your grade for Quiz 4 - Iteration: ")
PROMPT_12 = ("Please enter your grade for Quiz 5 - Arrays: ")


# Defining a function that will ask the user for their grade, loop until input is appropriate, and give errors if necessary
def get_grade(prompt):
    while True:
        # Ensuring input is numeric
        try:
            user_input = float(input(prompt))
            
            # Checking that input is between 0 and 100
            if float(user_input) < 0 or float(user_input) > 100:
                print("Input must be between 0 and 100.")

            # Checking that input is not null
            elif user_input == None:
                print("Input cannot be null.")

            else:
                return user_input
            
        except ValueError:
            print("Input must be numeric.")

# Defining a function that will append class exercises to the appropriate lists
def CE_append():
    grade.append(user_input)
    class_exercise.append(user_input)

# Defining a function that will append tests to the appropriate lists
def test_append():
    grade.append(user_input)
    test.append(user_input)

# Defining a function that will append assignments to the appropriate lists
def assignment_append():
    grade.append(user_input)
    assignment.append(user_input)

# Defining a function that will append quizzes to the appropriate lists
def quiz_append():
    grade.append(user_input)
    quiz.append(user_input)


# Getting input for Class Exercise 1 - Planning an Application and appending to grade list and class exercise list
user_input = get_grade(PROMPT_1)
CE_append()

# Getting input for Class Exercise 2 - Numeric and String Data and appending to grade list and class exercise list
user_input = get_grade(PROMPT_2)
CE_append()

# # Getting input for Class Exercise 3 - Selection and appending to grade list and class exercise list
user_input = get_grade(PROMPT_3)
CE_append()

# # Getting input for Class Exercise 4 - Iteration and appending to grade list and class exercise list
user_input = get_grade(PROMPT_4)
CE_append()

# Getting input for Test 1 - Theory and appending to grade list and test list
user_input = get_grade(PROMPT_5)
test_append()

# Getting input for Test 1 - Practical and appending to grade list and test list
user_input = get_grade(PROMPT_6)
test_append()

# Getting input for Assignment 1 - Iteration and appending to grade list and assignment list
user_input = get_grade(PROMPT_7)
assignment_append()


# Getting input for Quiz 1 - Planning an Application and appending to grade list and quiz list
user_input = get_grade(PROMPT_8)
quiz_append()


# Getting input for Quiz 2 - Numeric and String Data and appending to grade list and quiz list
user_input = get_grade(PROMPT_9)
quiz_append()



# Getting input for Quiz 3 - Selection and appending to grade list and quiz list
user_input = get_grade(PROMPT_10)
quiz_append()



# Getting input for Quiz 4 - Iteration and appending to grade list and quiz list
user_input = get_grade(PROMPT_11)
quiz_append()


# Getting input for Quiz 5 - Arrays and appending to grade list and quiz list
user_input = get_grade(PROMPT_12)
quiz_append()



# Calculating the average of all assignments (there is only 1)
assignment_calc = float(sum(assignment))

# Calculating the average of all tests
test_calc = float((sum (test) / 200)) * 100

# Calculating the average of all class exercises    
class_exercise_calc = float((sum (class_exercise) / 400)) * 100

# Calculating the average of all quizzes
quiz_calc = float((sum(quiz) / 500)) * 100

# Calculating the grade * weight of all activities so we can use this as the numerator 
total_activities = 12 * (class_exercise_calc/100) + 12 * (test_calc/100) + 10 * (assignment_calc/100) + 15 * (quiz_calc/100)

# Calculating the weight of all activities so we can use this as the denominator
total_weight = CLASS_EXERCISE_WEIGHT + TEST_WEIGHT + ASSIGNMENT_WEIGHT + QUIZ_WEIGHT

# Calculating final grade
final_grade = (total_activities / total_weight)*100

# Printing final grades
print(f"""\nYour final grade is {round(final_grade, 2)}%
Class Exercise Average: {round(class_exercise_calc, 2)}%
Test Average: {round(test_calc, 2)}%
Assignment Average: {round(assignment_calc, 2)}%
Quiz Average: {round(quiz_calc, 2)}%
""")