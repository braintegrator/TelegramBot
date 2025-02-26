
```markdown
# PositiveInputsBot

Telegram bot for instant delivery of positive content. Designed to boost mood and inspire.

## Key Features
- 🎨 **Random Images**: Get uplifting pictures from a curated collection
- 🎥 **Motivational Videos**: Watch inspiring video clips
- 📜 **Wise Quotes**: Read quotes from great minds
- 🔄 **Smart Randomization**: Unique content every request
- 📱 **Persistent Interface**: Control buttons always visible at screen bottom

## Technologies Used
- **Telegram Bot API** - for user interaction
- **Aiogram 3.18** - modern async framework for Telegram bots
- **Python 3.10+** - main programming language
- **FSInputFile** - secure media file handling
- **Randomization Algorithms** - for unbiased content selection

## Setup and Launch
1. Clone repository:
```bash
git clone https://github.com/braintegrator/TelegramBot.git
cd PositiveInputsBot
```

2. Install dependencies:
```bash
pip install aiogram==3.18.0 python-dotenv
```

3. Create `.env` file:
```env
BOT_TOKEN=your_telegram_bot_token
```

4. Prepare content:
```
├── images/          # Image files (jpg, png)
├── videos/          # Video files (mp4, mov)
└── quotes.txt       # Text file with quotes (one per line)
```

5. Run the bot:
```bash
python bot.py
```

## Usage Guide
1. Start conversation: `/start`
2. Use bottom buttons:
   - "Get Image" - random uplifting photo
   - "Get Video" - motivational video
   - "Get Quote" - inspirational quote
3. Each button press delivers new content

## Implementation Details
- Persistent keyboard using Telegram's `is_persistent` feature
- Automatic content validation in folders
- Graceful error handling for missing files
- Full Unicode support for quotes
- Telegram API limits respected:
  - Images: up to 20 MB
  - Videos: up to 50 MB

## License
MIT License - free to use and modify for any purpose.

## Credits
- Main developer: [Begemot](https://t.me/photon_of_freedom)
- Development assistant: [Qwen](https://example.com/qwen_avatar.jpg)  [AI developer from Alibaba Cloud](https://www.alibabacloud.com/product/qwen?spm=5aebb161.6b324b01.0.0.4c58c921lM5tWn)

## Contact
For collaboration inquiries: [hfwddm@gmail.com](mailto:hfwddm@gmail.com)

```
