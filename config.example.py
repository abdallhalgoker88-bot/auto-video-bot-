# Configuration file for Auto Video Bot
# Copy this file to config.py and modify as needed

import os
from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent

# Video Settings
VIDEO_CONFIG = {
    'resolution': '1920x1080',
    'fps': 30,
    'bitrate': '5000k',
    'format': 'mp4',
    'codec': 'libx264',
    'preset': 'medium',
}

# AI Settings
AI_CONFIG = {
    'model': 'gpt-4',
    'temperature': 0.7,
    'max_tokens': 2000,
    'api_key': os.getenv('OPENAI_API_KEY', ''),
}

# Processing Settings
PROCESSING_CONFIG = {
    'max_workers': 4,
    'timeout': 300,
    'retry_attempts': 3,
    'chunk_size': 1024 * 1024,
}

# Paths
PATHS = {
    'input': PROJECT_ROOT / 'input',
    'output': PROJECT_ROOT / 'output',
    'logs': PROJECT_ROOT / 'logs',
    'temp': PROJECT_ROOT / 'temp',
    'cache': PROJECT_ROOT / 'cache',
}

for path in PATHS.values():
    path.mkdir(parents=True, exist_ok=True)

# Logging Configuration
LOGGING = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': PATHS['logs'] / 'app.log',
    'max_size': 10485760,
    'backup_count': 5,
}

# Database
DATABASE = {
    'engine': 'sqlite',
    'url': f"sqlite:///{PROJECT_ROOT / 'data.db'}",
}

# Redis
REDIS = {
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': int(os.getenv('REDIS_PORT', 6379)),
    'db': 0,
}

# Email
EMAIL = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'sender': os.getenv('EMAIL_SENDER', ''),
    'password': os.getenv('EMAIL_PASSWORD', ''),
}

# API Keys
API_KEYS = {
    'openai': os.getenv('OPENAI_API_KEY', ''),
    'huggingface': os.getenv('HUGGINGFACE_API_KEY', ''),
    'aws': {
        'access_key': os.getenv('AWS_ACCESS_KEY', ''),
        'secret_key': os.getenv('AWS_SECRET_KEY', ''),
    },
}

# Feature Flags
FEATURES = {
    'enable_ai_processing': True,
    'enable_async_processing': True,
    'enable_caching': True,
    'enable_notifications': False,
    'enable_analytics': True,
}

# Environment
ENV = os.getenv('ENV', 'development')
DEBUG = ENV == 'development'

# Security
SECURITY = {
    'secret_key': os.getenv('SECRET_KEY', 'your-secret-key-change-in-production'),
    'allowed_origins': ['http://localhost:3000', 'http://localhost:5000'],
}