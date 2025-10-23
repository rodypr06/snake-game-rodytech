# 🐍 Modern Snake Game

A stunning, modern implementation of the classic Snake game featuring realistic 3D graphics, glassmorphism UI design, progressive difficulty, and CrewAI-powered enhancements.

![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

---

## ✨ Features

### 🎮 Gameplay
- **Progressive Difficulty**: Starts slow (150ms) and speeds up as you score (down to 60ms)
- **Large Playing Field**: 600x600 pixel canvas with 900 tiles
- **Smart Controls**: Arrow keys for movement, Space to restart
- **Score Persistence**: High scores saved in browser localStorage
- **Smooth Animations**: 60 FPS rendering for fluid gameplay

### 🎨 Visual Design
- **Glassmorphism UI**: Modern frosted glass effect with backdrop blur
- **Retro Grid Background**: Animated grid pattern inspired by MagicUI
- **3D Realistic Snake**: Detailed head with moving eyes, textured scales, shadows
- **Animated Apple**: Pulsing fruit with stem, leaf, and glow effects
- **Particle System**: Explosion effects when eating food
- **Modern Color Palette**: Indigo (#6366f1), Purple (#8b5cf6), Pink (#ec4899)

### 🤖 AI-Powered Development
- **CrewAI Integration**: Multi-agent collaboration for game enhancement
- **Intelligent Design**: AI-designed difficulty curves and mechanics
- **Quality Assurance**: Automated testing and validation

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone or download the project**
   ```bash
   cd snake-game-python
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server**
   ```bash
   python server.py
   ```

5. **Play the game**
   - Local: http://localhost:2025
   - Network: http://YOUR_IP:2025 (shown in terminal)

---

## 🎯 How to Play

### Controls
- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Space**: Restart game after game over

### Objective
- Eat the red apples to grow and score points
- Avoid hitting the walls or your own body
- The game gets progressively faster as you score more points

### Scoring
- **+10 points** per apple eaten
- High score is automatically saved
- Speed increases by 4ms per apple (max speed: 60ms)

---

## 🏗️ Project Structure

```
snake-game-python/
├── static/
│   └── game.html          # Main game (single-page application)
├── venv/                  # Python virtual environment
├── server.py              # Flask web server with IP detection
├── crew.py                # Original CrewAI game creation workflow
├── enhance_game.py        # CrewAI enhancement workflow
├── requirements.txt       # Python dependencies
├── PROGRESS.md            # Development progress documentation
├── CLAUDE.md              # AI assistant project instructions
└── README.md              # This file
```

---

## 🛠️ Technical Details

### Frontend
- **HTML5 Canvas**: For game rendering
- **CSS3**: Glassmorphism effects, animations, gradients
- **Vanilla JavaScript**: Game logic, physics, particle system
- **LocalStorage API**: High score persistence

### Backend
- **Flask 3.0.0**: Lightweight web server
- **Python Socket**: Network IP detection
- **Auto-reload**: Debug mode for development

### AI Framework
- **CrewAI**: Multi-agent collaboration
- **Agents**: Game Designer, Developer, QA Tester
- **Sequential Process**: Structured workflow

---

## 🎨 Design System

### Color Palette
```css
Primary:    #6366f1  /* Indigo */
Secondary:  #8b5cf6  /* Purple */
Accent:     #ec4899  /* Pink */
Background: #0a0a0a  /* Deep Black */
Glass:      rgba(15, 15, 25, 0.7)
```

### Visual Effects
- **Backdrop Blur**: 20px for glassmorphism
- **Grid Animation**: Infinite scrolling at 20s cycle
- **Gradient Text**: Indigo → Purple → Pink
- **Shadows**: Multi-layered with glow
- **Transitions**: 0.3s ease for smooth interactions

---

## 🚀 Advanced Usage

### Running with CrewAI

**Initial Game Creation**:
```bash
python crew.py
```
Creates the base game using AI agents (Designer → Developer → Tester)

**Enhancement Workflow**:
```bash
python enhance_game.py
```
Applies progressive difficulty and canvas enlargement using CrewAI

### Custom Configuration

Edit `server.py` to change:
- **Port**: Default 2025 (line 32)
- **Debug Mode**: Default True (line 32)
- **Host**: Default 0.0.0.0 (line 32)

Edit `static/game.html` to modify:
- **Canvas Size**: Line 156 (width/height)
- **Grid Size**: Line 177 (gridSize variable)
- **Initial Speed**: Line 194 (gameSpeed variable)
- **Speed Increment**: Line 293 (decrease value)
- **Colors**: Lines 14-262 (CSS styles)

---

## 📊 Performance

### Metrics
- **FPS**: 60 frames per second
- **Game Loop**: 150ms → 60ms (progressive)
- **Canvas**: 600x600 pixels
- **Grid**: 30x30 tiles (20px each)
- **Max Particles**: 15 per food consumption
- **Network Latency**: <5ms (local)

### Optimization
- Hardware-accelerated blur effects
- Efficient particle lifecycle management
- Minimal DOM manipulation
- Canvas-only rendering (no external images)

---

## 🌐 Network Access

The server binds to `0.0.0.0`, making it accessible from:
- **Localhost**: http://127.0.0.1:2025
- **LAN Devices**: http://YOUR_LAN_IP:2025
- **Other Devices**: Same network required

The terminal displays your network IP automatically on startup.

---

## 🔧 Development

### Adding New Features

1. **Modify Game Logic**: Edit JavaScript in `static/game.html`
2. **Update Styles**: Edit CSS in `<style>` section
3. **Server Changes**: Modify `server.py` (auto-reloads in debug mode)

### Code Structure

```javascript
// Game state variables (lines 179-195)
let snake, dx, dy, food, score, gameSpeed...

// Core functions
draw()           // Main game loop
generateFood()   // Random food placement
endGame()        // Game over handling
restartGame()    // Reset game state
startGame()      // Initialize game loop

// Rendering
// Background, grid, snake, food, particles

// Classes
Particle         // Explosion effect particles
```

---

## 📱 Browser Compatibility

### Tested Browsers
- ✅ Chrome/Chromium 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Required Features
- CSS backdrop-filter (for glassmorphism)
- HTML5 Canvas API
- LocalStorage API
- ES6 JavaScript

---

## 🎓 Learning Resources

This project demonstrates:
- **Canvas API**: 2D graphics and animations
- **Game Development**: Game loops, collision detection, physics
- **Modern CSS**: Glassmorphism, gradients, animations
- **Flask**: Python web framework basics
- **AI Integration**: CrewAI multi-agent systems

---

## 🤝 Contributing

This is an educational project, but suggestions are welcome!

### Ideas for Contribution
- Mobile touch controls
- Sound effects and music
- Additional themes/skins
- Multiplayer mode
- Power-ups system
- Different game modes

---

## 📝 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Credits

**Created by**: RodyTech
**AI Assistant**: Claude (Anthropic)
**Framework**: CrewAI
**Inspired by**: MagicUI, Modern Glassmorphism Trends

### Technologies Used
- HTML5 Canvas API
- CSS3 Glassmorphism
- JavaScript ES6
- Python Flask
- CrewAI Framework

---

## 📞 Support

For issues or questions:
1. Check the code documentation in files
2. Review `PROGRESS.md` for development history
3. Examine `CLAUDE.md` for project context

---

## 🔄 Version History

### v1.3.0 (Current)
- Modern glassmorphism design
- Retro grid background
- RodyTech branding
- Enhanced color scheme

### v1.2.0
- Progressive speed system
- CrewAI enhancement workflow
- Larger 600x600 canvas

### v1.1.0
- Realistic 3D graphics
- Particle effects
- Animated apple

### v1.0.0
- Initial release
- Basic Snake game
- Flask server setup

---

## 🎯 Future Roadmap

- [ ] Mobile responsive design
- [ ] PWA capabilities
- [ ] Global leaderboard
- [ ] Theme selector
- [ ] Sound effects
- [ ] Multiplayer mode
- [ ] Docker support
- [ ] Production deployment guide

---

**Made with ❤️ by RodyTech**

*Last Updated: October 23, 2025*
