def get_card_value(card):
    # Simulating a complex/heavy calculation
    values = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 15}
    return values.get(card, 0) 

hand = ['7', 'Jack', '3', 'Ace', '9', 'King']

# THE CHALLENGE: Refactor this line below!
high_value_scores = [y for card in hand if (y:= get_card_value(card)) > 10]

print(high_value_scores)
# Output: [11, 15, 13]