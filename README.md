# Snake Game - CrewAI Proof of Concept

A simple web-based Snake game built using CrewAI multi-agent collaboration.

## Overview

This project demonstrates CrewAI's multi-agent collaboration capabilities by having three specialized agents work together to build a complete Snake game:

- 🎨 **Designer Agent**: Creates game specifications and architecture
- 💻 **Developer Agent**: Implements the game based on specifications
- 🧪 **Tester Agent**: Tests and validates the implementation

## Setup

1. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API key**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

## Usage

### Step 1: Build the Game with CrewAI

Run the CrewAI crew to collaboratively build the game:

```bash
python crew.py
```

This will:
- Designer agent creates game specifications
- Developer agent implements the game in `static/game.html`
- Tester agent validates the implementation

### Step 2: Run the Web Server

Start the Flask server on port 2025:

```bash
python server.py
```

### Step 3: Play the Game

Open your browser and navigate to:
```
http://localhost:2025
```

## Game Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Space**: Restart after game over

## Project Structure

```
snake-game-python/
├── crew.py              # CrewAI multi-agent system
├── server.py            # Flask web server (port 2025)
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API key)
├── static/
│   └── game.html       # Generated Snake game (created by CrewAI)
└── README.md           # This file
```

## CrewAI Agent Workflow

```
Designer Agent
    ↓ (creates specifications)
Developer Agent
    ↓ (implements game)
Tester Agent
    ↓ (validates & provides feedback)
Complete Game
```

## Technologies

- **Backend**: Python 3.8+, Flask
- **AI Framework**: CrewAI
- **Frontend**: HTML5, CSS3, JavaScript (Canvas API)
- **LLM**: OpenAI GPT (via CrewAI)

## License

MIT License
