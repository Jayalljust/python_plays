people = [
    {"name": "Seva", "job": "PM"},
    {"name": "Tema", "job": "business-analytic"},
    {"name": "Dima", "job": "programmer"}
]

#defining such function the same as using built-in lambda function
#def f(person):
    #return person["name"]

people.sort(key=lambda person: person["name"])

print(people)