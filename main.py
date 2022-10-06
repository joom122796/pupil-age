#Write a pseudocode algorithm to include a validation Rule: Read a pupil age and output a message “Valid pupil age” if it is at least 10 and less than 19 years old. Otherwise output the message “Invalid input: enter a value from 11 to 18”. 
age = int(input('Enter pupil age: '))
while age < 10 or age > 19:
  age = int(input('Invalid input: enter a value from 11 to 18: '))
else:
  print('Valid pupil age')
