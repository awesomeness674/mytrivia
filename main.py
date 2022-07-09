score=0
total_questions=10
print('Welcome to Krish Arora triva lets see if you know anything about me')
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
