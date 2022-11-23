def BlackjackHighest(strArr):
    
    cards = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

    highest_card_value = {k: i for i, k in enumerate(cards)}

    cards_value = {k: i+1 for i, k in enumerate(cards[:10])}
    for i in cards[10:]:
        cards_value[i] = 10
    
    input_cards = sorted(strArr, reverse=True)
    
    score = 0
    hand_cards_value = {}
    is_ace = False
    
    for i in input_cards:
        if (i == 'ace') & (score < 11) & (len(hand_cards_value) == len(input_cards)-1):
            score +=  11
            is_ace = True
        else:
            score += cards_value[i] 
            hand_cards_value[i] = highest_card_value[i]
            
    if is_ace:
        highest_card = 'ace'
    else:
        highest_card = max(hand_cards_value, key=hand_cards_value.get)
    
    if score < 21:
        return f'above {highest_card}'
    elif score == 21:
        return f'blackjack {highest_card}' 
    else:
        return f'belove {highest_card}' 
