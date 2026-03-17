people = [
    {"name": "Ashok", "age": 30},
    {"name": "Suresh", "age": 25},
    {"name": "Ramesh", "age": 35},
    {"name": "Naresh", "age": 28}   
]



people.sort(key=lambda person: person["age"])

print(people)
