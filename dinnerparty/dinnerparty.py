import random

count = int(input("Enter the number of friends joining (including you):\n> "))

if count <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(count):
        name = input("> ")
        friends[name] = 0

    total_amount = float(input("Enter the total amount:\n> "))
    split_amount = round(total_amount / count, 2)

    for name in friends:
        friends[name] = split_amount

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')

    if lucky_choice == "Yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")

        new_split = round(total_amount / (count - 1), 2)
        for name in friends:
            if name == lucky_person:
                friends[name] = 0
            else:
                friends[name] = new_split
    else:
        print("No one is going to be lucky")

    print(friends)