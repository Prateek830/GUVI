s=input()
ar=['a','e','i','o','u']
if s.isalpha():
    if s in ar:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")