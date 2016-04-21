
import org.anderes.edu.python.PythonicCardDesk

def showsample():
    beer_card = org.anderes.edu.python.PythonicCardDesk.Card('7', 'diamonds')
    print(beer_card)

    deck = org.anderes.edu.python.PythonicCardDesk.FrenchDeck()
    print(len(deck))
    
    print(deck[0])
    
    print(deck[-1])
    
    print(deck[1:3])
    
    for card in deck:
        print(card)
        
    print(org.anderes.edu.python.PythonicCardDesk.Card('Q', 'hearts') in deck)
    
    print('Sortierte Ausgabe: -----------------------')
    for card in sorted(deck, key=deck.spades_high): 
        print(card)
    print('/-----------------------------------------')

if __name__ == '__main__':
    showsample()