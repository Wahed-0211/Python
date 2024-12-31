
# Initial list
my_list = [
    {'name': 'A', 'age': 25},
    {'name': 'B', 'age': 30},
    {'name': 'C', 'age': 22}
]

# Print header and separator
print(f"{'Name':<10} {'Age':<5}")
print('-' * 15)

# View the list
for person in my_list:
    print(f"{person['name']:<10} {person['age']:<5}")

# Update: Change age of 'A' to 26
my_list[0]['age'] = 26

# Delete: Remove person with name 'B'
my_list = [person for person in my_list if person['name'] != 'B']

# Add: Add a new person
my_list.append({'name': 'D', 'age': 28})

# Print updated list
print("\nUpdated list:")
print(f"{'Name':<10} {'Age':<5}")
print('-' * 15)
for person in my_list:
    print(f"{person['name']:<10} {person['age']:<5}")
