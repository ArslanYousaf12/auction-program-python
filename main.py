import os
from art import logo

print(logo)
print("Welcome to the Secret Auction Program")
end_of_auction = True

bid = {}

def find_highest_bidder(bid):
    highest_bider_amount = 0
    winner = ""
    for bidder in bid:
        amount = bid[bidder]
        if amount > highest_bider_amount:
            highest_bider_amount = amount
            winner = bidder
    print(f"higest bider is {winner} and highest bid is {highest_bider_amount}")
while end_of_auction:
    bidder_name = input("what is your name ")
    bid_amount = int(input("what is your bid "))
    bid[bidder_name] = bid_amount
    result = input("Is there any bidder 'yes' or 'no' ")
    if result == "yes":
        os.system('clear')
    else:
        end_of_auction = False
        find_highest_bidder(bid=bid)

print(bid)


# print(f"Highest bidder is {highest_bider_name} and bid is {highest_bid_amount}")



