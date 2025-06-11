
def calculate_love_score(name1: str, name2: str):
    true_count = sum(1 for word in name1+name2 if word in "TRUEtrue")
    love_count = sum(1 for word in name1+name2 if word in "LOVElove")
    return str(true_count) + str(love_count)

your_name = input("Enter your name")
your_lover_name = input("Enter your lover name")
love_score = calculate_love_score(your_name, your_lover_name)
print(f"Your love score is {love_score}")