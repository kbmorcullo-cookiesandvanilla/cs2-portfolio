# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Your Name
**Section:** Your Section
**Quarter:** 1
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number:** 3
**Case Title:** Suspicious Download
> A pop-up says the student's device is infected and tells them to download an unknown security
application.

---
### 1. What cybersecurity threat is shown?
> It shows that a random pop up is trying to trick the person into thinking that theres a virus and asks them to give their personal information
### 2. What warning signs make the situation suspicious?
> It’s a random pop-up
### 3. What may be affected?
Check or describe all that apply:
- Data(yes)
- Account(yes)
- Application(yes)
- Device(yes)
- Network(maybe)
- Financial information(yes)
> Because with personal information all of these could be accessed and used.
### 4. What information could be exposed or misused?
> Personal information
### 5. What should the user do to reduce the risk?
> Ignore it or report it.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | | | Collect, so that they know who is registering where.
| Section | | | Collect, to verify stuff.
| Club Choice | | | Collect, so they know which club you're trying to register in.
| School Email | | | Collect, so that when they need to send you documents for things they can do it via email
| Attendance Status | | | Collect, so that they know when you're actually present.
| Password | | | Don’t Collect, because it’s just a club registration form. Why would we need to input that information?
| OTP | | | Don’t Collect, because it’s just a club registration form. Why would we need to input that information?
| Home Address | | | Don’t Collect, because it’s just a club registration form why would we need to input that information.

| Parent Bank Account | | |Don’t Collect, because it’s just a club registration form. Why would we need to input that information?

---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> So that there isn’t a chance to disclose private information.
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | | | | | |
| Section | | | | | |
| Club Choice | | | | | |
| School Email | | | | | |
| Attendance Status | | | | | |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> Student Name, Section, Club Choice, School Email, Attendance Status

### 2. What should your program reject?
> Password
OTP, Home Address, Banking Information
### 3. How do your validation rules help reduce incorrect or unsafe input?
> Write your answer here.
---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email

- Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
#first 1
name = input("What is your name? ")

while not name:
  print("")
  print("Error: Student name is required.")
  name = input("What is your name? ").strip()

#to make it prettier hshshsh
print("")

#section part
section = input("What is your section? ").strip().title()

while section != "Dahlia":
   section = input("What is your section? ").strip().title()

print("Next,")
print("")

#next club part
leclub = input("What is your club? ").strip().title()

while leclub not in ["Robotics", "Science", "Mathematics", "Programming"]:
   print("Error: Please choose a valid club.")
   leclub = input("What is your club? ").strip().title()

print("")

# emaiillll
email = input("What is your email? ").strip()

while "@" not in email or "." not in email:
  print("")
  print("Either wrong format or something's missing, anyway go again")
  print("")
  email = input("What is your email? ").strip()

print("")

#last, attendance!!!
uder = input("What's your attendance status? ").strip().title()
while uder not in ["Present", "Absent", "Late"]:
   print("")
   print("This is not allowed, it's either present late or absent, go again")

print("")

#final resultsss
print("-" * 32)
print("REGISTRATION ACCEPTED")
print("-" * 32)
print("Student:", name)
print("Section:", section)
print("Club:", leclub)
print("Email:", email)
print("Attendance:", uder)


```
---
## Security Practices Applied
### Required Input
> Explain how you handled blank input.
### Allowed Values
> Explain which fields accept only predefined values.
### Format Check
> Explain your simple email validation rule.
### Error Messages
> Explain why clear error messages are useful.
### Data Minimization
> Explain what information you intentionally did NOT collect and why.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | | | |
| 2 | Blank student name | | | |
| 3 | Invalid section | | | |

| 4 | Invalid club choice | | | |
| 5 | Email missing `@` | | | |
| 6 | Email missing `.` | | | |
| 7 | Invalid attendance status | | | |
| 8 | Different valid inputs | | | |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> Write your answer here.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Write your answer here.
### 3. How can validation rules improve the security of user input?
> Write your answer here.
### 4. Why should a program avoid collecting unnecessary personal information?
> Write your answer here.
### 5. How did SG7's input validation concepts become security practices in SG8?
> Write your answer here.



