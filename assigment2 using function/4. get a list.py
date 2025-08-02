def get_adults(people):
    return [person for person in people if person['age'] > 18]

people = [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 17}]
adults = get_adults(people)
print(adults)  
