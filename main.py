import tkinter
import random
from PIL import Image, ImageTk

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.root.geometry("800x600")
        self.root.configure(bg='green')
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda e: self.root.attributes('-fullscreen', False))
        self.root.bind("<F11>", lambda e: self.root.attributes('-fullscreen', True))
        
        
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.side_deck = [
            "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA",
            "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA",
            "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA",
            "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA"
        ]
        
        # Štatistiky
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
        # obrazky kariet a aktualny screen
        self.card_images = {}
        self.card_back_image = None
        self.nacitat_card_obrazky()
        self.game_over = False
        self.dealer_cards_hidden = True
        self.current_screen = "lobby"
        
        self.vytvorit_lobby()
    
    def nacitat_card_obrazky(self):
        
        card_size = (100, 140)
        
        # nacitanie zadnej karty
        try:
            back_img = Image.open("cards/back_card.png").resize(card_size, Image.Resampling.LANCZOS)
            self.card_back_image = ImageTk.PhotoImage(back_img)
        except:
            try:
                back_img = Image.open("cards/card_back.png").resize(card_size, Image.Resampling.LANCZOS)
                self.card_back_image = ImageTk.PhotoImage(back_img)
            except:
                back_img = Image.new('RGB', card_size, color='blue')
                self.card_back_image = ImageTk.PhotoImage(back_img)
        
        # nacitanie kartiet (normalne z predu)
        for card in self.side_deck:
            try:
                filename = self.ziskat_card_meno(card)
                img = Image.open(f"cards/{filename}").resize(card_size, Image.Resampling.LANCZOS)
                self.card_images[card] = ImageTk.PhotoImage(img)
            except:
                img = Image.new('RGB', card_size, color='white')
                self.card_images[card] = ImageTk.PhotoImage(img)
    
    def ziskat_card_meno(self, card):
        #prevedenie karty na meno suboru
        suits = {'s': 'spades', 'd': 'diamonds', 'c': 'clubs', 'h': 'hearts'}
        values = {'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
        
        suit = suits[card[0]]
        value = values.get(card[1:], card[1:])
        
        return f"{suit}_{value}.png"
    
    def vycistit_obrazovku(self):
        #vycistenie obrazovky
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def vytvorit_lobby(self):
        #vyrobenie lobby
        self.vycistit_obrazovku()
        self.current_screen = "lobby"
        
        frame = tkinter.Frame(self.root, bg='darkgreen')
        frame.pack(fill=tkinter.BOTH, expand=True)
        
        # popis
        tkinter.Label(frame, text="♠ BLACKJACK CASINO ♠", 
                font=("Arial", 32, "bold"), bg='darkgreen', fg='gold').pack(pady=50)
        
        # Štatistiky
        stats_frame = tkinter.Frame(frame, bg='black', relief=tkinter.RAISED, bd=3)
        stats_frame.pack(pady=30)
        
        tkinter.Label(stats_frame, text="YOUR STATISTICS", 
                font=("Arial", 14, "bold"), bg='black', fg='gold').pack(pady=10)
        
        self.stats_label = tkinter.Label(stats_frame, 
                                   text=f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}", 
                                   font=("Arial", 12), bg='black', fg='white')
        self.stats_label.pack(pady=5)
        
        if self.wins + self.losses > 0:
            win_rate = (self.wins / (self.wins + self.losses)) * 100
            tkinter.Label(stats_frame, text=f"Win Rate: {win_rate:.1f}%", 
                    font=("Arial", 10), bg='black', fg='lightgreen').pack(pady=(0, 10))
        
        # Buttony
        button_frame = tkinter.Frame(frame, bg='darkgreen')
        button_frame.pack(pady=50)
        
        tkinter.Button(button_frame, text="🎮 PLAY BLACKJACK", font=("Arial", 18, "bold"), 
                 command=self.start_nova_hra, bg='red', fg='white', 
                 width=20, height=2, relief=tkinter.RAISED, bd=5).pack(pady=15)
        
        tkinter.Button(button_frame, text="🔄 RESET STATISTICS", font=("Arial", 12), 
                 command=self.reset_statistik, bg='orange', fg='black', 
                 width=20, height=1, relief=tkinter.RAISED, bd=3).pack(pady=10)
        
        tkinter.Button(button_frame, text="❌ QUIT GAME", font=("Arial", 12), 
                 command=self.root.quit, bg='gray', fg='white', 
                 width=20, height=1, relief=tkinter.RAISED, bd=3).pack(pady=10)
    
    def reset_statistik(self):
        #resetovanie statistik
        self.wins = self.losses = self.ties = 0
        self.update_statistik()
    
    def update_statistik(self):
        # update stastistik
        if hasattr(self, 'stats_label') and self.stats_label.winfo_exists():
            self.stats_label.config(text=f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}")
    
    def start_nova_hra(self):
        #spustenie novej hry
        self.hra_config()
        self.zacat_hru()
    
    def hra_config(self):
        #confing hry
        self.vycistit_obrazovku()
        self.current_screen = "game"
        
        frame = tkinter.Frame(self.root, bg='green')
        frame.pack(fill=tkinter.BOTH, expand=True)
        
        # popis hry a statistiky
        tkinter.Label(frame, text="BLACKJACK", font=("Arial", 24, "bold"), 
                bg='green', fg='white').pack(pady=10)
        tkinter.Label(frame, text=f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}", 
                font=("Arial", 10), bg='green', fg='lightgray').pack()
        
        # Dealer sekcia
        dealer_frame = tkinter.Frame(frame, bg='green')
        dealer_frame.pack(pady=15)
        tkinter.Label(dealer_frame, text="🎩 DEALER", font=("Arial", 16, "bold"), 
                bg='green', fg='white').pack()
        self.dealer_value_label = tkinter.Label(dealer_frame, text="Value: ?", 
                                          font=("Arial", 12), bg='green', fg='white')
        self.dealer_value_label.pack()
        self.dealer_cards_frame = tkinter.Frame(dealer_frame, bg='green')
        self.dealer_cards_frame.pack()
        
        # Player sekcia
        player_frame = tkinter.Frame(frame, bg='green')
        player_frame.pack(pady=20)
        tkinter.Label(player_frame, text="🧑 PLAYER", font=("Arial", 16, "bold"), 
                bg='green', fg='white').pack()
        self.player_value_label = tkinter.Label(player_frame, text="Value: 0", 
                                          font=("Arial", 12), bg='green', fg='white')
        self.player_value_label.pack()
        self.player_cards_frame = tkinter.Frame(player_frame, bg='green')
        self.player_cards_frame.pack()
        
        # Buttony
        button_frame = tkinter.Frame(frame, bg='green')
        button_frame.pack(pady=20)
        
        self.hit_button = tkinter.Button(button_frame, text="🎯 HIT", font=("Arial", 14, "bold"), 
                                   command=self.hit, bg='red', fg='white', width=10,
                                   relief=tkinter.RAISED, bd=3)
        self.hit_button.pack(side=tkinter.LEFT, padx=10)
        
        self.stand_button = tkinter.Button(button_frame, text="✋ STAND", font=("Arial", 14, "bold"), 
                                     command=self.stand, bg='orange', fg='white', width=10,
                                     relief=tkinter.RAISED, bd=3)
        self.stand_button.pack(side=tkinter.LEFT, padx=10)
        
        tkinter.Button(button_frame, text="🏠 LOBBY", font=("Arial", 12), 
                 command=self.vytvorit_lobby, bg='blue', fg='white', width=10,
                 relief=tkinter.RAISED, bd=3).pack(side=tkinter.LEFT, padx=10)
        
        self.status_label = tkinter.Label(frame, text="", font=("Arial", 16, "bold"), 
                                    bg='green', fg='yellow')
        self.status_label.pack(pady=10)
    
    def vysledky_obrazovka(self, result_type, message):
        #zobrazienie vysledkov
        self.vycistit_obrazovku()
        self.current_screen = "result"
        
        colors = {
            "win": ('darkgreen', 'gold', '🎉'),
            "lose": ('darkred', 'lightcoral', '😞'),
            "tie": ('navy', 'lightblue', '🤝')
        }
        bg_color, accent_color, emoji = colors[result_type]
        
        frame = tkinter.Frame(self.root, bg=bg_color)
        frame.pack(fill=tkinter.BOTH, expand=True)
        
        # obrazovka vysledkov
        tkinter.Label(frame, text=emoji, font=("Arial", 80), 
                bg=bg_color, fg=accent_color).pack(pady=30)
        tkinter.Label(frame, text=message, font=("Arial", 28, "bold"), 
                bg=bg_color, fg='white').pack(pady=20)
        
        # detaily akurat odohranej hry a statistiky
        details_frame = tkinter.Frame(frame, bg='black', relief=tkinter.RAISED, bd=3)
        details_frame.pack(pady=20)
        
        tkinter.Label(details_frame, text="GAME SUMMARY", font=("Arial", 16, "bold"), 
                bg='black', fg=accent_color).pack(pady=10)
        tkinter.Label(details_frame, text=f"Your Hand: {self.vypocitat_value_ruky(self.player_hand)}", 
                font=("Arial", 14), bg='black', fg='white').pack(pady=5)
        tkinter.Label(details_frame, text=f"Dealer Hand: {self.vypocitat_value_ruky(self.dealer_hand)}", 
                font=("Arial", 14), bg='black', fg='white').pack(pady=5)
        tkinter.Label(details_frame, text=f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}", 
                font=("Arial", 12), bg='black', fg='lightgray').pack(pady=(10, 15))

        # Buttony
        button_frame = tkinter.Frame(frame, bg=bg_color)
        button_frame.pack(pady=30)
        
        tkinter.Button(button_frame, text="🎮 PLAY AGAIN", font=("Arial", 16, "bold"), 
                 command=self.start_nova_hra, bg='green', fg='white', 
                 width=15, height=2, relief=tkinter.RAISED, bd=5).pack(pady=10)
        tkinter.Button(button_frame, text="🏠 BACK TO LOBBY", font=("Arial", 14), 
                 command=self.vytvorit_lobby, bg='blue', fg='white', 
                 width=15, height=1, relief=tkinter.RAISED, bd=3).pack(pady=10)
    
    def zamiesat_balik(self):
        #zamiesanie balika
        side_deck_copy = self.side_deck.copy()
        self.deck = []
        
        while side_deck_copy:
            card = side_deck_copy.pop(random.randint(0, len(side_deck_copy) - 1))
            self.deck.append(card)
    
    def rozdanie_card(self, who):
        #rozdanie kariet
        if who == "start":
            for _ in range(2):
                self.player_hand.append(self.deck.pop(0))
                self.vykresit_kartu(self.player_hand[-1], "player")
                
                self.dealer_hand.append(self.deck.pop(0))
                self.vykresit_kartu(self.dealer_hand[-1], "dealer")
        elif who == "player":
            card = self.deck.pop(0)
            self.player_hand.append(card)
            self.vykresit_kartu(card, "player")
        elif who == "dealer":
            card = self.deck.pop(0)
            self.dealer_hand.append(card)
            self.vykresit_kartu(card, "dealer")
    
    def vykresit_kartu(self, card, who):
        #pridaj kartu na obrazovku
        if who == "player":
            frame = self.player_cards_frame
            image = self.card_images[card]
        else:  # dealer
            frame = self.dealer_cards_frame
            if len(self.dealer_hand) == 1 or not self.dealer_cards_hidden:
                image = self.card_images[card]
            else:
                image = self.card_back_image
        
        tkinter.Label(frame, image=image, bg='green').pack(side=tkinter.LEFT, padx=2)
        self.update_display(who)
    
    def update_display(self, who):
        #update hodnoty ruky
        if who == "player":
            value = self.vypocitat_value_ruky(self.player_hand)
            self.player_value_label.config(text=f"Value: {value}")
        else:  # dealer
            if self.dealer_cards_hidden and len(self.dealer_hand) > 1:
                first_card_value = self.ziskat_value_karty(self.dealer_hand[0])
                self.dealer_value_label.config(text=f"Value: {first_card_value} + ?")
            else:
                value = self.vypocitat_value_ruky(self.dealer_hand)
                self.dealer_value_label.config(text=f"Value: {value}")
    
    def vycistit_karty(self):
        #vycistenie obrazovky (karty)
        for frame in [getattr(self, 'player_cards_frame', None), 
                     getattr(self, 'dealer_cards_frame', None)]:
            if frame and frame.winfo_exists():
                for widget in frame.winfo_children():
                    widget.destroy()
    
    def ukaza_dealer_karty(self):
        #zobrazit dealerove karty
        self.dealer_cards_hidden = False
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()
        for card in self.dealer_hand:
            tkinter.Label(self.dealer_cards_frame, image=self.card_images[card], 
                    bg='green').pack(side=tkinter.LEFT, padx=2)
        self.update_display("dealer")
    
    def zacat_hru(self):
        #spustenie novej hry
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.dealer_cards_hidden = True
        
        self.vycistit_karty()
        if hasattr(self, 'status_label'):
            self.status_label.config(text="")
        
        if hasattr(self, 'hit_button'):
            self.hit_button.config(state=tkinter.NORMAL)
            self.stand_button.config(state=tkinter.NORMAL)
        
        self.zamiesat_balik()
        self.rozdanie_card("start")
        
        if self.vypocitat_value_ruky(self.player_hand) == 21:
            if hasattr(self, 'status_label'):
                self.status_label.config(text="BLACKJACK!")
            self.root.after(2000, self.stand)
    
    def ziskat_value_karty(self, card):
        #ziskanie hodnoty karty
        value = card[1:]
        if value == 'A':
            return 11
        elif value in ['J', 'Q', 'K']:
            return 10
        else:
            return int(value)
    
    def vypocitat_value_ruky(self, hand):
        #vypocitanie hodnoty ruky
        value = 0
        aces = 0
        
        for card in hand:
            if card[1:] == 'A':
                aces += 1
            else:
                value += self.ziskat_value_karty(card)
        
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        
        return value
    
    def hit(self):
        # Player hits
        if self.game_over:
            return
            
        self.rozdanie_card("player")
        
        if self.vypocitat_value_ruky(self.player_hand) > 21:
            self.game_over = True
            self.ukaza_dealer_karty()
            self.losses += 1
            self.hit_button.config(state=tkinter.DISABLED)
            self.stand_button.config(state=tkinter.DISABLED)
            self.root.after(2000, lambda: self.vysledky_obrazovka("lose", "BUST! You Lose!"))
    
    def stand(self):
        # Player stands
        if self.game_over:
            return
            
        self.game_over = True
        self.ukaza_dealer_karty()
        self.dealer_ai()
        
        if hasattr(self, 'hit_button'):
            self.hit_button.config(state=tkinter.DISABLED)
            self.stand_button.config(state=tkinter.DISABLED)
    
    def dealer_ai(self):
        # Dealer AI
        dealer_value = self.vypocitat_value_ruky(self.dealer_hand)
        
        while dealer_value < 17:
            self.rozdanie_card("dealer")
            dealer_value = self.vypocitat_value_ruky(self.dealer_hand)
            self.root.update()
            self.root.after(1000)
        
        self.root.after(1500, self.vyherca)
    
    def vyherca(self):
        #rozhodnutie o vitazovi
        player_value = self.vypocitat_value_ruky(self.player_hand)
        dealer_value = self.vypocitat_value_ruky(self.dealer_hand)
        
        if dealer_value > 21:
            self.wins += 1
            self.vysledky_obrazovka("win", "Dealer Busts! You Win!")
        elif player_value > dealer_value:
            self.wins += 1
            self.vysledky_obrazovka("win", "You Win!")
        elif player_value < dealer_value:
            self.losses += 1
            self.vysledky_obrazovka("lose", "Dealer Wins!")
        else:
            self.ties += 1
            self.vysledky_obrazovka("tie", "It's a Tie!")


root = tkinter.Tk()
game = BlackjackGame(root)
root.mainloop()

