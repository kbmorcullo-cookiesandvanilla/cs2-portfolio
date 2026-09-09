# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Kaithlynn Brielle M. Orcullo
**Section:** Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Kaithlynn Brielle M. Orcullo | | | | | |
| 13 | | | | | |
| 8 | | | | | |
| Kbmorcullo@brc.pshs.edu.ph | | | | | |
| Registration Code | | | | | |
---
## Validation Questions
### 1. Why should the student name not be blank?
>Because it is a requirement
### 2. Why should age be checked for both data type and range?
>Because we need to see if its in the specific range required and if it's 
### 3. Why should grade level only accept specific values?
>Because if it's in the worng grade then it's invalid
### 4. What format requirements did you use for the email address?
>It needs to have a "@" along with a "."
### 5. What length requirement did you use for the registration code?
> 6
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Flowchart
Insert your flowchart below.
![Workshop Validator Flowchart](workshop_validator_flowchart.png)
OR
## Pseudocode

```text
START
start
    input name
    input age
    input grade
    input email
    input code

    if name is empty then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Student name is required."
    else if age is not numeric then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Age must be a number"
    else if age <= 11 or age >= 18 then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Age must be from 11 to 18"
    else if grade is not in ["7", "8", "9", "10", "11", "12"] then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Invalid level"
    else if "@" not in email or "." not in email then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Invalid format"
    else if length(code) != 6 then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Code should only have 6 characters"
    else
        print "------------------------------"
        print "REGISTRATION ACCEPTED"
        print "------------------------------"
        print "Student:", name
        print "Age:", age
        print "Grade Level:", grade
        print "Email:", email
        print "Registration Code:", code
    endif
end


END
```

Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```# --------------------- USER INPUTS --------------------------
name = input("Enter student name: ")
age = input("Enter age: ")
grade = input("Enter grade level: ")
email = input("Enter email address: ")
code = input("Enter registration code: ")

print("")

# ----------------- VALIDATION LOGIC -----------------
if name == "":
    print("------------------------------")
    print("REGISTRATION NOT ACCEPTED")
    print("------------------------------")
    print("Reason: Student name is required.")

elif not age.isdigit():
    print("------------------------------")
    print("REGISTRATION NOT ACCEPTED")
    print("------------------------------")
    print("Reason: Age must be a number")

# Checks if age is outside the 11-18 range (11 and 18 are allowed)
elif int(age) < 11 or int(age) > 18:
    print("------------------------------")
    print("REGISTRATION NOT ACCEPTED")
    print("------------------------------")
    print("Reason: Age must be from 11 to 18")

elif grade not in ["7", "8", "9", "10", "11", "12"]:
    print("------------------------------")
    print("REGISTRATION NOT ACCEPTED")
    print("------------------------------")
    print("Reason: Invalid level")

elif "@" not in email or "." not in email:
    print("------------------------------")
    print("REGISTRATION NOT ACCEPTED")
    print("------------------------------")
    print("Reason: Invalid format")

elif len(code) != 6:
    print("------------------------------")
    print("REGISTRATION NOT ACCEPTED")
    print("------------------------------")
    print("Reason: Code should only have 6 characters")

else:
    print("------------------------------")
    print("REGISTRATION ACCEPTED")
    print("------------------------------")
    print("Student:", name)
    print("Age:", age)
    print("Grade Level:", grade)
    print("Email:", email)
    print("Registration Code:", code)
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | | | |
| 2 | Blank student name | Presence | | | |
| 3 | Age = `fourteen` | Data type | | | |
| 4 | Age = `11` | Minimum boundary | | | |
| 5 | Age = `18` | Maximum boundary | | | |
| 6 | Age = `10` | Range | | | |
| 7 | Grade Level = `13` | Acceptable value | | | |
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | |
| 9 | Registration Code = `ABC` | Length | | | |
| 10 | Registration Code = `CS2026` | Valid length | | | |
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.

**PASS**
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.
11
```
**Expected Output:**
```text
Write the expected output here.
No, too young, go again
```
**Actual Output:**
```text
Write the actual output here.
REGISTRATION NOT ACCEPTED
```
**Result:** PASS / FAIL
PASS
**Explanation:**
> Explain why the output is correct or incorrect.
Because it had worked
---
## Verification Test 2
**Input:**
```text
Write the input here.
18
```
**Expected Output:**
```text
Write the expected output here.
Too old, unc, go again
```
**Actual Output:**
```text
Write the actual output here.
REGISTRATION NOT ACCEPTED
```
**Result:** PASS / FAIL
PASS
**Explanation:**
Because it worked
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
10
```
**Expected Output:**
```text
Write the expected output here.
REGISTRATION NOT ACCEPTED
```
**Actual Output:**

```text
Write the actual output here.
REGISTRATION NOT ACCEPTED
```
**Result:** PASS / FAIL
PASS
**Explanation:**
Because it worked
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> To see if the what was inputted before it runs so that theres no errors
### 2. What is the difference between input validation and output verification?
> Input verfication verifies the input and output verfication verifies the output too see if they work
### 3. Which validation technique was easiest for you to implement? Why?
> Name, because it had the least lines needed to code
### 4. Which validation technique was most challenging? Why?
>The registration code because I had to have ai help me (creds po kay ai)
### 5. How did testing invalid inputs help you improve your program?
> Helped me know when they worked
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used
---

[← Back to Main Portfolio](../README.md)
