"""
Simple Flask web server to host the Snake game on port 2025
"""

from flask import Flask, send_from_directory, redirect
import os
import socket

app = Flask(__name__, static_folder='static')


def get_ip_address():
    """Get the server's IP address"""
    try:
        # Create a socket to determine the IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"


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
    ip_address = get_ip_address()

    print("🎮 Snake Game Server Starting...")
    print("=" * 60)
    print(f"🌐 Server running on all interfaces (0.0.0.0:2025)")
    print(f"")
    print(f"🎯 Access the game at:")
    print(f"   • Local:    http://localhost:2025")
    print(f"   • Network:  http://{ip_address}:2025")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server\n")

    app.run(host='0.0.0.0', port=2025, debug=True)


if __name__ == '__main__':
    main()
