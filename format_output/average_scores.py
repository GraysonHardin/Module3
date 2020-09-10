"""
1.  Write tests to read one person's information: Include first & last name, age, and find the average of three numbers 0-100 (store within a variable)
2. Create a project named Module 3, add directories test and format_output
3. Within the test directory, add a unit test called 'test_average_scores.py
4. Within the format_output directory, add average_scores.py

"""


def average():
    score1 = int(input("Enter first number here:"))
    score2 = int(input("Enter second number here:"))
    score3 = int(input("Enter third number here:"))
    average_scores = (score1 + score2 + score3) / 3
    return average_scores
