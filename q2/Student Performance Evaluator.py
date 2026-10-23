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
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print("Average: ", average)
print("Performance: ", performance)
print("Eligible for Challenge: ", eligible)
