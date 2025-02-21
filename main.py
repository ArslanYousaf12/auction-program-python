import os
from art import logo
bider_info = {}
biders = []
print(logo)
print("Welcome to the Secret Auction Program")
end_of_auction = True
highest_bider_name = ""
highest_bid_amount = 0
while end_of_auction:
    bidder_name = input("what is your name ")
    bid_amount = int(input("what is your bid "))


    bider_info = {"name": bidder_name, "amount": bid_amount}

    biders.append(bider_info)

    result = input("Is there any bidder 'yes' or 'no' ")
    if result == "yes":
        os.system('clear')
    else:
        end_of_auction = False

print(biders)

highest_bider_name = biders[0]["name"]
highest_bid_amount = biders[0]["amount"]
for bidder in biders:
    amount = bidder["amount"]
    name = bidder["name"]
    if amount > highest_bid_amount:
        highest_bid_amount = amount
        highest_bider_name = name

print(f"Highest bidder is {highest_bider_name} and bid is {highest_bid_amount}")



