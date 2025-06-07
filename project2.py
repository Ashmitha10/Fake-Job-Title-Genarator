import random

adjectives=['cheif','global','dynamic','senior','innovative']
roles=['visionary','happiness','vibe','synergy','disruption']
suffixes=['officers','manager','coordinator','consultant','ninja']

adj=random.choice(adjectives)
role=random.choice(roles)
suffix=random.choice(suffixes)

fake_jobtitle=adj+""+role+""+suffix
print("fake_jobtitle is:",fake_jobtitle)

while True:
    again = input("Do you want another title? (yes/no): ").strip().lower()
    if again == "yes":
        adj = random.choice(adjectives)
        role = random.choice(roles)
        suffix = random.choice(suffixes)
        fake_title = adj + " " + role + " " + suffix
        print("Your new fake job title is:", fake_title)
    else:
        print("Thanks for playing!")
        break
