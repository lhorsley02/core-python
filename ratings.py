"""Restaurant rating lister."""


# put your code here
scores = open("scores.txt")

restaurants = {}

for line in scores:
    line = line.rstrip("\n").split(":")
    restaurants[line[0]] = int(line[1])


# sort
def sort_items():
    items = restaurants.items()
    sorted_items = sorted(items)
    for x in sorted_items:
        print(x[0], "is rated a", x[1])
    rate_again = input("Would you like to add another restaurant? Type y or n:")
    if rate_again == "y":
        user_input()


# user input
def user_input():
    new_rest = input("Enter Restaurant Name: ")
    new_rating = input("Enter Restaurant Rating Out of 5: ")
    restaurants[new_rest] = new_rating
    sort_items()

sort_items()
