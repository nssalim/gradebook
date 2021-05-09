# Lists - Python3
# Project 1 - Gradebook
#Organize subjects and grades

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# classes being taken: 
subjects = ["physics", "calculus", "poetry", "history"]

# class grades:
grades = [98, 97, 85, 88]

# two-dimensional list combining subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
# print(gradebook)

# Add a subject:
gradebook.append(["computer science", 100])
# print(gradebook)

# Add another subject:
gradebook.append(["visual art", 93])
# print(gradebook)

# Modify the Gradebook:
# Award an extra 5 points for our visual arts class.
gradebook[-1][-1] = 98
# print(gradebook)

# Switch from a numerical grade value to a Pass/Fail option for our poetry class
# Step 1
# Find the grade value in the gradebook for the poetry class and use the .remove() method to delete it.
gradebook[2].remove(85)
# print(gradebook)

# Step 2
# Use the .append() method to then add a new "Pass" value to the sublist where the poetry class is located.
gradebook[2].append("Pass")
# print(gradebook)

# One Big Gradebook!
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

