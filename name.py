name = input("What is your name: ")
age = int(input("How old are you: "))
bd = input("Did you have your birthday this year?: ")
year = 2023-age
if bd == 'no':
    year=year-1
print(name + ", you are born in " + str(year))
