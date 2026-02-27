<div align="center">

# ♠️ BLACKJACK CASINO ♦️

### *Experience the thrill of Vegas in your desktop!*

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

</div>

## 🎮 About The Game

Welcome to **Blackjack Casino** - a fully-featured, GUI-based Blackjack game that brings the excitement of the casino directly to your computer! Built with Python and Tkinter, this game features stunning card graphics, real-time statistics tracking, and an immersive casino atmosphere.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Beautiful GUI** | Smooth, casino-style interface with professional card graphics |
| 📊 **Statistics Tracking** | Track your wins, losses, ties, and win rate |
| 🖥️ **Fullscreen Mode** | Immersive fullscreen gameplay (F11 to toggle) |
| 🃏 **Full Deck** | Complete 52-card deck with all suits (♠️ ♥️ ♦️ ♣️) |
| 🤖 **Smart Dealer AI** | Follows official casino rules (stands on 17+) |
| 🎯 **Classic Gameplay** | Hit, Stand, and compete against the dealer |
| 🏆 **Results Screen** | Detailed game summaries after each round |
| 🔄 **Quick Restart** | Jump back into the action with one click |

## 📸 Game Screens

### 🏠 Lobby
- View your overall statistics
- Check your win rate
- Start a new game or reset stats

### 🎲 Game Table
- Clear display of dealer and player hands
- Real-time hand value calculation
- Hit or Stand buttons for decision-making

### 🎉 Results Screen
- Animated result announcements
- Hand comparison details
- Updated statistics

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blackjack.git
   cd blackjack
   ```

2. **Install required dependencies**
   ```bash
   pip install pillow
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Starting the Game**
   - Launch the game and click "🎮 PLAY BLACKJACK" from the lobby
   - You and the dealer are dealt 2 cards each
   - One of the dealer's cards is hidden

2. **Your Turn**
   - **Hit (🎯)**: Draw another card
   - **Stand (✋)**: Keep your current hand and end your turn

3. **Dealer's Turn**
   - Dealer reveals hidden card
   - Dealer must hit until reaching 17 or higher

4. **Winning**
   - Get closer to 21 than the dealer without going over
   - Dealer busts (over 21) = You win! 🎉
   - You bust = You lose 😞
   - Same value = Tie 🤝

## 🃏 Blackjack Rules

| Hand Value | Description |
|------------|-------------|
| **21** (Blackjack) | Best possible hand! |
| **2-10** | Face value |
| **J, Q, K** | Worth 10 points |
| **Ace** | Worth 11 or 1 (automatically adjusted) |

### Winning Conditions
- ✅ Your hand is closer to 21 than the dealer's
- ✅ Dealer busts (goes over 21)
- ❌ You bust (go over 21)
- ❌ Dealer's hand is closer to 21
- 🤝 Both have the same value (Push/Tie)

## 🎮 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `F11` | Toggle Fullscreen Mode |
| `ESC` | Exit Fullscreen Mode |

## 🛠️ Technical Details

### Built With
- **Python 3.8+** - Core programming language
- **Tkinter** - GUI framework
- **PIL/Pillow** - Image processing for card graphics
- **Random** - Card shuffling and deck management

### Project Structure
```
Blackjack/
├── main.py              # Main game file
├── README.md           # This file
└── cards/              # Card images folder
    ├── back_card.png   # Card back design
    ├── spades_*.png    # Spades suit (♠️)
    ├── hearts_*.png    # Hearts suit (♥️)
    ├── diamonds_*.png  # Diamonds suit (♦️)
    └── clubs_*.png     # Clubs suit (♣️)
```

### Key Classes & Methods
- `BlackjackGame` - Main game class
  - `vytvorit_lobby()` - Creates the lobby screen
  - `zacat_hru()` - Starts a new game
  - `hit()` - Player draws a card
  - `stand()` - Player stands
  - `dealer_ai()` - Dealer's automated play
  - `vypocitat_value_ruky()` - Calculates hand value

## 📊 Statistics Tracking

The game automatically tracks:
- 🏆 **Wins** - Games you've won
- 😞 **Losses** - Games you've lost
- 🤝 **Ties** - Games that ended in a draw
- 📈 **Win Rate** - Your winning percentage

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is licensed under the MIT License - feel free to use it for your own projects!

## 🎨 Credits

- Card images: Classic playing card design
- Game concept: Traditional Blackjack rules
- Developer: Your Name

## 💬 Support

If you enjoy this game, give it a ⭐ star!

---

<div align="center">

### 🎲 *Good Luck at the Tables!* 🎰

Made with ❤️ and Python

</div>