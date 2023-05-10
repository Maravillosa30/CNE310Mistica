# A code that takes a number between 0-100 and determines if a user has a grade of ‘A’ or not.
number_grade = int(input("Enter your grade here"))
letter_grade = 'F'
letter_grade = 'Not A'
if number_grade > 90:
    print('letter_grade is A')
elif number_grade >= 87:
    print('letter_grade is B+')
elif number_grade >= 80:
    print('letter_grade is  B')
elif number_grade >= 77:
    print('letter_grade is C+')
elif number_grade >= 70:
    print('letter_grade is C')
elif number_grade >= 67:
    print('letter_grade is D+')
elif number_grade >= 60:
    print('letter_grade is D')
else:
    print('letter_grade is F')




