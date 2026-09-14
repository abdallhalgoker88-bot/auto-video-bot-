# 🎬 Auto Video Bot

> An intelligent bot that automatically generates and processes videos with AI capabilities.

## ✨ Features

- 🤖 Automatic video generation
- 🎯 AI-powered content processing
- ⚡ Fast and efficient processing
- 📝 Customizable output options
- 🔧 Easy to configure and deploy

## 📋 Requirements

- Python 3.8+
- FFmpeg
- Required Python packages (see `requirements.txt`)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/abdallhalgoker88-bot/auto-video-bot-.git
cd auto-video-bot-
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure settings
```bash
cp config.example.py config.py
# Edit config.py with your settings
```

## 💻 Usage

### Basic usage
```python
from auto_video_bot import VideoBot

bot = VideoBot()
bot.generate_video(input_file="content.txt", output_file="video.mp4")
```

### Command line
```bash
python main.py --input content.txt --output video.mp4
```

### Advanced options
```bash
python main.py \
  --input content.txt \
  --output video.mp4 \
  --quality 1080p \
  --fps 30 \
  --bitrate 5000k
```

## 🔧 Configuration

Edit `config.py` to customize:
- Video resolution
- Frame rate
- Output format
- AI model settings
- Processing parameters

## 📚 Project Structure

```
auto-video-bot-/
├── src/
│   ├── __init__.py
│   ├── bot.py
│   ├── processor.py
│   ├── generator.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   └── test_processor.py
├── config.py
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🧪 Testing

```bash
python -m pytest tests/ -v
```

## 📝 Logging

Logs are stored in `logs/` directory. Configure logging in `config.py`.

## 🐛 Troubleshooting

### FFmpeg not found
Install FFmpeg:
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Windows**: Download from https://ffmpeg.org/download.html

### Memory issues
- Reduce video resolution in `config.py`
- Process smaller chunks
- Increase available RAM

### Processing errors
- Check log files in `logs/` directory
- Verify input file format
- Ensure all dependencies are installed

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abdallah Algoker**
- GitHub: [@abdallhalgoker88-bot](https://github.com/abdallhalgoker88-bot)
- 📧 Contact: abdallhalgoker88@gmail.com

## 🙏 Acknowledgments

- FFmpeg community
- Python community
- Contributors and testers

## 📞 Support

For support, open an issue on [GitHub Issues](https://github.com/abdallhalgoker88-bot/auto-video-bot-/issues).

---

**Made with ❤️ by Abdallah Algoker**