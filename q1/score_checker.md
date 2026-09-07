Input: What information does the program need?
-It needs 

Boundary: What is the minimum valid score?
-0

Boundary: What is the maximum valid score?
-100

Possible Outputs: What outcomes can the program produce?
-Outstanding, Very Satisfactory, Satisfactory, Needs Improvement, Invalid Score

Selection Pattern: Which part uses a boundary condition?
-

Selection Pattern: Which part uses multiple decision paths?
-The if or elif parts


Pseudocode:
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
