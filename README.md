## User-Profile-Validation
### Description
This program helps us to validate the user profile details
It checks whether the user input such as name, phone number, and other details meet the required validation rules.
### Purpose
The main purpose of this project is to practice input validation in Python
### How the Code Works
- The program takes user input from the console.
- It validates each field using conditional statements.
- If the input is valid, it displays a User Profile is Valid.
- If the input is invalid, it shows User Profile is InValid.
Files in This Project:
  UserNameValidationSystem.py : Contains the Python code for user profile validation.
Output:
The program displays whether the entered user details are valid or not based on the given conditions
  
## Student Profile Approval System

### Description
This program helps us to  validate student profile details using Python.
It checks whether the entered ID, email, password, and referral code follow the required format and validation rules.

### Purpose
The main purpose of this project is to practice string validation, conditional logic etc

### How the Code Works
- The program takes student details as input 
- It validates student ID format.
- It verifies email 
- It checks password strength rules.
- It validates the referral code.
- If all inputs are correct, it displays "APPROVED". or else"REJECTED"

### Validation Rules
- Student ID must start with `CSE-` followed by digits.
- Email must contain one `@` and end with `.edu`.
- Password must be at least 8 characters, start with an uppercase letter, and contain a digit.
- Referral code must start with `REF`, contain digits, and end with `@`.



### Output
The program prints whether the student profile is APPROVED OR REJECTED based on the validation conditions.



## Student Performance Analyzer

### Description
This program analysis the student performace
It classifies activity scores into different risk levels and also we will applying the personalization rules.

### Purpose
The purpose of this project is to practice using of lists loops, conditional statements etc

### How the Code Works
- The program asks for a student registration number.
- It takes activity scores as input.
- Each score is categorised into risk group based on the conditions
- Negative values are considered as invalid and we will be ignoring those values
- A personalization rule is applied  depending on the registration number.
- if the registration number is divided by 3 then i will removing th lowrisk values
- parallely i will be counting no.of totalValid scores are there and no.of ignored scores and also we will be counting no.of scores are removed due to personalization
- The program prints final categorized result.

### Risk Classification Range
- Critical risk: score > 100
- High risk: 61 – 100
- Medium risk: 31 – 60
- Low risk: 1 – 30
- Ignored: ≤ 0

### Personalization Rule
- If registration number is divisible by 3  low risk scores are removed
- Else → critical risk scores are removed


### Output
The program displays:
- Risk category lists
- After applying personalization list
- Total valid scores
- Total ignored scores
- Number of scores removed due to personalization

