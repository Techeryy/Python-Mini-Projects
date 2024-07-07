# A relatively simplistic password strength checker algorithm
# which takes a password input and provides a score based on 
# it's stregth alongside any criteria which was not met,
# part of Techeryy/Python-Mini-Projects
# Programmed By: Stephen Adams

prohibited = ['Password','Password1','1234','Qwerty','12345678','Birthday']

def length(password):
    return len(password) >= 8

def capitalLetters(password):
    return any(65 <= ord(i) <= 90 for i in password)

def specialCharacters(password):
    return any((33 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126) for i in password)

def numericCharacters(password):
    return any(48 <= ord(i) <= 57 for i in password)

def prohibitedPasswords(password):
    return not any(password == invalid for invalid in prohibited)

password = input("Please Enter A Strong Password: ")
if password == input("Please Re-Enter Your Password: "):
    checks = [("Length", length), ("Capital Letters", capitalLetters), ("Special Characters", specialCharacters), ("Numeric Characters", numericCharacters), ("Prohibited Passwords", prohibitedPasswords)]
    low_scores = []
    for item in checks:
        if item[1](password) == False:
            low_scores.append(item[0])
    score = (len(checks)-len(low_scores))*20
    print(f"Your password received an overall strength score of {score}/100")
    if score < 100:
        print(f"This is considered a weak password, the following criteria were not met: {', '.join(low_scores)}") 
else:
    print("Passwords Don't Match")
