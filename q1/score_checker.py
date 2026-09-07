#ask for score
#determine its category
s=int(input("score:"))

if s>=101:
  print("Invalid Score") 
  
elif s<= -1:
  print("Invalid Score")
  
elif  s>=90:
  print("Outstanding")
  
elif s>=80:
  print("Very Satisfactory")
  
elif s>=75:
  print("Satisfactory")
  
else : 
  print("Needs Improvement")
