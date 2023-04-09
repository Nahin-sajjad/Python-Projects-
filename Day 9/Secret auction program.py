from art import logo
print(logo)

bids={}

bids_finnished=False
while not bids_finnished:
    name=input("Start bidding by writting your name: ")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bids_finnished=True
    elif should_continue == "yes":
        clear()    
        highest_bid=0
        winner=""
        for bidder in bids:
            bid_amount=bids[bidder]
            if bid_amount > highest_bid:
                highest_bid=bid_amount
                winner=bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}.")        
                

