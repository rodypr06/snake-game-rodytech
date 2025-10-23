"""
Simple Flask web server to host the Snake game on port 2025
"""

from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    """Redirect to the game"""
    return redirect('/game.html')


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('static', path)


def main():
    """Start the web server"""
    print("🎮 Snake Game Server Starting...")
    print("=" * 60)
    print(f"🌐 Server running at: http://localhost:2025")
    print(f"🎯 Open your browser and visit: http://localhost:2025")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server\n")

    app.run(host='0.0.0.0', port=2025, debug=True)


if __name__ == '__main__':
    main()
