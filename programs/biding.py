print("Welcome to the secreat action program.")
bid_details = {}
while True:
    name = input("What is your name ?")
    bid = int(input("Wht's your bid ?"))
    bid_details[name] = bid
    is_other = input("Are there any other bidders ? Type (yes) or (no)")
    if is_other == "no":
        break
    elif is_other == "yes":
        print("\n" * 20)
    else:
        raise "Entered a invalid value"

max_bid =max(bid_details.items(), key=lambda x: x[1])
print(f"Winner is {max_bid[0]} with bid of {max_bid[1]}")