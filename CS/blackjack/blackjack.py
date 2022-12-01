from random import shuffle
from cs1graphics import *

img_path = "/Users/hailhwan/Code/python_learning/CS/blackjack/images/"

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# >>> len(face_names) == len(value) -> True

bj_board = Canvas(600,400,'dark green','Blackjack')

class Card:
    def __init__(self, suit: list, face: list, value: list, image:str = None, hidden: bool = False):
        """Card class의 생성자."""
        self.suit = suit
        self.face = face
        self.value = value
        self.image = Image(img_path + suit + '_' + face + '.png')
        self.hidden = hidden
  
    def string(self):  # card_string()의 메소드화. -> card.string()
        return self.face + ' of ' + self.suit
    
    def add(self, x_pos, y_pos):
        if self.hidden == True: addImage = Image(img_path + 'back.png')
        else: addImage = self.image
        addImage.moveTo(x_pos, y_pos)
        bj_board.add(addImage)

class Hand:
    def __init__(self):
        self.deck = []
    def append(self, card):
        self.deck.append(card)
    def value(self):
      return sum(x.value for x in self.deck)

def create_deck():
    ###############################################################
    # Create a list("deck") of all 52 cards, shuffle them and return the list.
    # The list 'deck' have to include Card objects
    # A Card is represented by a object with five attributes: suit, face, value, image, and hidden
    # You should declare those five attributes to define class 'Card'   
    ###############################################################
    deck = []  # deck은 Card 객체를 담는 리스트
    # 리스트에 주어진 순서대로 카드를 추가 
    for suit_name in suit_names:  # 리스트에 제공된대로 suit_names를 순회
      for idx, face_name in enumerate(face_names):  # 리스트에 제공된대로 face_names를 순회  #TODO 원래 face_name과 value를 같이 뽑아오도록 for face_name, val in face_names, value 이렇게 될 줄 알았는데 안돼서 일단 멈춤 나중에 알아보기
          deck.append(Card(suit_name, face_name, value[idx]))  # Card 객체를 생성하여 deck에 추가   
          print(suit_name, face_name, value[idx])
    shuffle(deck)  # deck을 섞음
    return deck  # deck을 반환
      
# def hand_value(hand):
#   ###############################################################
#   # hand is a list including card objects
#   # Return the value of the cards in the list "hand"   
#   ###############################################################
  
#   pass

# def card_string(card):
#   ###############################################################
#   # Parameter "card" is a Card object
#   # Return a nice string to represent a card
#   # (sucn as "King of Spades" or "Ace of Diamonds")
#   ###############################################################
#   pass
    
def ask_yesno(prompt:str = 'None'):
    ###############################################################
    # Display the text prompt and let's the user enter a string.
    # If the user enters "y", the function returns "True",
    # and if the user enters "n", the function returns "False"
    # If the user enters anything else, the function prints "I beg your pardon!",
    # and asks again, repreting this until the user has entered a correct string.
    ###############################################################
    print(prompt)  # prompt를 출력
    user_input = input()  # 사용자의 입력을 받음
    while True:  # 무한 루프
      if user_input == 'y':  # 사용자의 입력이 y라면
        return True  # True를 반환
      elif user_input == 'n':  # 사용자의 입력이 n이라면
        return False  # False를 반환
      else:  # 사용자의 입력이 y나 n이 아니라면
        print("I beg your pardon!")  # I beg your pardon!을 출력
        print(prompt)  # prompt를 출력
        user_input = input()  # 사용자의 입력을 받음

def draw_card(dealer, player):
    ###############################################################
    # This funuction add the cards of dealer and player to canvas, bj_board
    # In Blackjack, the first card of dealer is hidden.
    # If the attribute 'hidden' of each Card object is true,
    # then you have to show the hidden card image(Back.png).
    # The parameter dealer and player are List objects including Card Objects
    # The start position of dealer's card is (100,100)
    # The start position of player's card is (100,300)
    # You can use the following methods for positioning images and text:
    # Image() Object, Text() Object, moveTo() method, setDepth() method
    ###############################################################
    depth = 100  # 첫번째 카드의 Depth
    x0, y0 = 100, 100  # 딜러의 첫번째 카드의 위치
    x1, y1 = 100, 300  # 플레이어의 첫번째 카드의 위치
    offset = 30 # 출력될 카드의 위치를 조정하기 위한 변수
    
    bj_board.clear()  # canvas 초기화
    for i in range(len(dealer.deck)):  # 딜러의 카드 개수만큼 반복
        dealer.deck[i].add(x0 + (i * offset), y0)
        
    for i in range(len(player.deck)):  # 플레이어의 카드 개수만큼 반복
        player.deck[i].add(x1 + (i * offset), y1)
        
    bj_board.add(Text(f"Dealer", centerPt=Point(x0 - 15, y0 - 65))) # Player의 카드의 총합을 출력
    bj_board.add(Text(f"Player", centerPt=Point(x1 - 15, y1 - 65))) # Player의 카드의 총합을 출력
    
    if dealer.deck[0].hidden == False:  # 딜러가 패를 공개했을 경우 = 게임이 끝날 경우
      bj_board.add(Text(f"The dealer's Total : {dealer.value()}", centerPt=Point(x0 + 300, y0))) # dealer의 카드의 총합을 출력
      
    bj_board.add(Text(f"Your Total : {player.value()}", centerPt=Point(x1 + 300, y1))) # Player의 카드의 총합을 출력

###############################################
# DO NOT MODIFY THE FOLLOWING CODES
###############################################


def main():
  deck = []

  while True:
    print("Welcome to Blackjack World!\n")
    if len(deck) < 12:
      deck = create_deck()

    # create two hands of dealer and player
    dealer = Hand()
    player = Hand()

    # initial two dealings
    card = deck.pop()
    print("You are dealt " + card.string())
    player.append(card)

    card = deck.pop()
    print("Dealer is dealt a hidden card\n")
    card.hidden = True
    dealer.append(card)

    card = deck.pop()
    print("You are dealt " + card.string())
    player.append(card)

    card = deck.pop()
    print("Dealer is dealt " + card.string() + "\n")
    dealer.append(card)

    print("Your total is", player.value(), "\n")
    draw_card(dealer, player)

    # player's turn to draw cards
    while player.value() < 21 and ask_yesno("Would you like another card? (y/n) "):
      # draw a card for the player
      card = deck.pop()
      print("You are dealt " + card.string())
      player.append(card)
      print("Your total is", player.value(), "\n")

      draw_card(dealer, player)
    # if the player's score is over 21, the player loses immediately.
    if player.value() > 21:
      print("You went over 21! You lost.")
      dealer.deck[0].hidden = False
      draw_card(dealer, player)
    else:
        # draw cards for the dealer while the dealer's score is less than 17
      print("The dealer's hidden card was " + dealer.deck[0].string())
      while dealer.value() < 17:
          card = deck.pop()
          print("Dealer is dealt " + card.string())
          dealer.append(card)
          print("The dealer's total is", dealer.value(), "\n")

      dealer.deck[0].hidden = False
      draw_card(dealer, player)
      # summary
      player_total = player.value()
      dealer_total = dealer.value()
      print("Your total is", player_total)
      print("The dealer's total is", dealer_total)

      if dealer_total > 21:
        print("The dealer went over 21! You win!")
      else:
        if player_total > dealer_total:
          print("You win!")
        elif player_total < dealer_total:
          print("You lost!")
        else:
          print("You have a tie!")

    if not ask_yesno("Play another round? (y/n) "):
      bj_board.close()
      break

main()
# create_deck()