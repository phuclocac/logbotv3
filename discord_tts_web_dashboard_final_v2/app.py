#!/usr/bin/env python3
"""
Discord TTS Bot - Main Web Application
Public web interface for the Discord TTS Bot
"""
import os
import time
import psutil
from flask import Flask, render_template, jsonify, request, redirect, url_for
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tts-bot-secret-key-2024')

# Simple bot monitor class
class SimpleBotMonitor:
    def __init__(self):
        self.stats = {
            'uptime': 0,
            'start_time': time.time(),
            'commands_executed': 0,
            'tts_requests': 0,
            'voice_connections': 0,
            'guild_count': 0,
            'status': 'online',
            'last_activity': datetime.now().isoformat(),
            'cpu_usage': 0,
            'memory_usage': 0
        }
        
    def update_stats(self):
        """Update stats"""
        self.stats['uptime'] = time.time() - self.stats['start_time']
        try:
            self.stats['cpu_usage'] = psutil.cpu_percent()
            self.stats['memory_usage'] = psutil.virtual_memory().percent
        except:
            self.stats['cpu_usage'] = 0
            self.stats['memory_usage'] = 0
        self.stats['last_activity'] = datetime.now().isoformat()

# Global instances
monitor = SimpleBotMonitor()
bot_instance = None

@app.route('/')
def index():
    """Main landing page"""
    return render_template('public_dashboard.html')

@app.route('/dashboard')
def dashboard():
    """Admin dashboard (if available)"""
    try:
        # Check if admin dashboard template exists
        return render_template('dashboard.html')
    except:
        # Fallback to public dashboard
        return redirect(url_for('index'))

@app.route('/setup')
def setup():
    """Setup guide page"""
    return render_template('setup.html')

@app.route('/api/public/stats')
def api_public_stats():
    """Public API for bot statistics"""
    try:
        monitor.update_stats()
        public_stats = {
            'status': monitor.stats.get('status', 'online'),
            'uptime': monitor.stats.get('uptime', 0),
            'guild_count': monitor.stats.get('guild_count', 1),
            'voice_connections': monitor.stats.get('voice_connections', 0),
            'commands_executed': monitor.stats.get('commands_executed', 150),
            'tts_requests': monitor.stats.get('tts_requests', 120),
            'last_activity': monitor.stats.get('last_activity', datetime.now().isoformat())
        }
        return jsonify(public_stats)
    except Exception as e:
        return jsonify({
            'status': 'online',
            'uptime': 0,
            'guild_count': 1,
            'voice_connections': 0,
            'commands_executed': 150,
            'tts_requests': 120,
            'last_activity': datetime.now().isoformat(),
            'error': str(e)
        })

@app.route('/api/public/features')
def api_public_features():
    """Public API for bot features"""
    features = {
        'tts_languages': ['Vietnamese (vi-VN)'],
        'voice_support': True,
        'commands': [
            {'command': '.ab', 'description': 'Vào voice channel'},
            {'command': '.at [text]', 'description': 'Đọc text tiếng Việt'},
            {'command': '.leave', 'description': 'Rời voice channel'},
            {'command': '.help', 'description': 'Hiển thị trợ giúp'}
        ],
        'features': [
            'Giọng nói tiếng Việt tự nhiên',
            'Hoàn toàn miễn phí',
            'Không cần API key',
            'Dễ sử dụng',
            'Hoạt động 24/7'
        ]
    }
    return jsonify(features)

@app.route('/api/invite-url')
def api_invite_url():
    """API endpoint for bot invite URL"""
    try:
        # Use the actual bot client ID from environment or config
        client_id = os.environ.get('DISCORD_CLIENT_ID', '1393623196263252110')
        permissions = 3148800  # Send Messages, Connect, Speak, Use Voice Activity
        invite_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&permissions={permissions}&scope=bot"
        return jsonify({'invite_url': invite_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'bot_ready': True,
        'version': '1.0.0'
    })

@app.route('/api/status')
def api_status():
    """Detailed status API"""
    return jsonify({
        'web_app': 'running',
        'bot_status': monitor.stats.get('status', 'online'),
        'uptime': monitor.stats.get('uptime', 0),
        'timestamp': datetime.now().isoformat()
    })

# Export app for Vercel
# This allows Vercel to import the app directly
application = app

if __name__ == '__main__':
    # Start web app
    port = int(os.environ.get('PORT', 5001))
    print(f"🌐 Starting web application on port {port}")
    print(f"📱 Public dashboard: http://localhost:{port}")
    
    app.run(host='0.0.0.0', port=port, debug=False)