score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
completed_tasks = int(input("Completed Tasks: "))

def calculate_average(score1, score2, score3):
 return (score1 + score2 + score3) / 3
  
def get_performance(average):
 if average >= 85:
   return "Mastery"
 elif average >= 70:
   return "Developing"
 else:
   return "Needs Review"
   
def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
   return True 
  else:
   return False

average = calculate_average(score1, score2, score3)

#1. Which function returns a number, which returns a string, and which returns a Boolean?
 #calculate_average returns a number
 #get_performance returns a string
 #is_eligible returns a boolean
#2. Explain how the average moves from calculate_average() into get_performance().
 #Its stored into the variable 'average' to be used again in get_performance().
#3. What happens when a student has a high average but has completed fewer than three tasks?
 #The student will not be eligble.
#4. Why is return more appropriate than simply printing the result inside each function?
 #Return stores the result to be used again.

performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print("Average: ", average)
print("Performance: ", performance)
print("Eligible for Challenge: ", eligible)
