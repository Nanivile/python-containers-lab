# Exercise 1: 

students = ['Jay', 'John', 'Martha', 'Pepper']
print(students[1])
print(students[-1])

# Exercise 2:

foods = 'pizza', 'rice', 'noodles', 'burger'
for food in foods:
    print(f"{food} is a good food.")

# Exercise 3:

for food in foods[2:4]:
    print(food)

# Exercise 4:

home_town = {
    'city': 'Stockton',
    'state': 'California',
    'population': 254999
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5:

for key in home_town:
    print(f"{key} = {home_town[key]}")

# Exercise 6:
    
cohort = []

for idx, student in enumerate(students):
    cohort += [{'student': student, 'fav_food': foods[idx]}]

for person in cohort:
    print(person)

# Exercise 7:
    
awesome_students = []
for student in students:
    awesome_students.append(f"{student} is awesome!")

for student in awesome_students:
    print(student)

# Exercise 8:
    
for food in foods:
    if 'a' in food:
        print(food)