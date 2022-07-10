score=0
total_questions=10
mark=0
print('Welcome to Krish Arora triva!')
ans=input('Are you ready to play(yes/no)')
if ans.lower() == 'yes':
  ans = input('What is my favorite food')
  if ans.lower() == 'palak paneer':
    print('Correct')
    score +=1
    ans = input('What is my favorite color')
  else:
    print('incorrect')
    ans = input('What is my favorite color')
  if ans.lower() == 'teal':
    print('Correct')
    score +=1
  ans = input('What is my favorite hobby?')
else:
    print('incorrect')
    ans = input('What is my favorite hobby?')
    if ans.lower() == 'basketball':
      print('Correct')
      score +=1
    ans = input('Which grade am I going to?')
else:
print('incorrect')
ans = input('Which grade am I going to?')
if ans.lower() == '6th grade':
      print('Correct')
score +=1
ans = input('What animal do I want as a pet')
else:
print('Incorrect')
ans = input('What animal do I want as a pet')
if ans.lower() == 'dog':
  print('Correct')
score +=1
ans = input('Do I prefer Noise or Quiet')
else:
print('Incorrect')
ans = input('Do I prefer Noise or Quiet')
if ans.lower() == 'noise':
  print('Correct')
score +=1
ans = input('What is my favorite english song?')
else:
print('Incorrect')
ans = input('What is my favorite english song?')
if ans.lower() == 'beliver':
  print('Correct')
score +=1
ans = input('What is my favorite english song?')
else:
print('Incorrect')
ans = input('What is my favorite english song?')
if ans.lower() == 'believer':
  print('Correct')
score +=1
ans = input('What is my favorite hindi song?')
else:
print('Incorrect')
ans = input('What is my favorite hindi song?')
if ans.lower() == 'swag se swagat':
  print('Correct')
score +=1
ans = input('What is my favorite book?')
else:
print('Incorrect')
ans = input('What is my favorite book?')
if ans.lower() == 'harry potter':
  print('Correct')
score +=1
ans = input('What do I want to be when I grow up(2 words)')
else:
print('Incorrect')
ans = input('What do I want to be when I grow up(2 words)')
if ans.lower() == 'software engineer':
  print('Correct')
score +=1
else:
print('Incorrect')



      
print('Thank you for playing you got',score,"questions correct") 
mark=(score/total_questions)* 100
print("mark:",mark,)
      print('goodbye')