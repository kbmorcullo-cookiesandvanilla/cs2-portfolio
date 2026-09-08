Input: What information does the program need?
-It needs 

Boundary: What is the minimum valid score?
-0

Boundary: What is the maximum valid score?
-100

Possible Outputs: What outcomes can the program produce?
-Outstanding, Very Satisfactory, Satisfactory, Needs Improvement, Invalid Score

Selection Pattern: Which part uses a boundary condition?
-range validation check

Selection Pattern: Which part uses multiple decision paths?
-The if or elif parts


**Pseudocode:**
Start
Ask for the score
Then determine which category it falls into
If its above 101 or equal to then diplay "Invalid Score"
If its below -1 or equal to then diplay "Invalid Score"
If its above 90 or equal to then diplay "Outstanding"
If its above 80 or equal to then diplay "Very Satisfactory"
If its above 75 or equal to then diplay "Satisfactory"
If its anything else then diplay "Needs Improvement"
End

**Testing reflections**
Why is it important to test the values 0 and 100?
To get the exact output you want and need

Why did you also test -1 and 101?
So that it doesnt go below or over what the range of results possible

Which test helped you understand boundary conditions the most?
Testing for satisfactory and very satisfactory, shows me that 75 cuts in for very satisfactory and 74 starts the satisfactory

Did any of your tests initially fail? If yes, what did you change in your program?
None

**General Reflections**
How did selection structures make the program more useful?
Helped by making it more organized and easier

How did proper comments and readable formatting improve your program?
It let the person understand the steps I did and hopefully the reason why too

Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
It let me fix the logic behind it first before I create the code itself
