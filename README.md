# Daily Mini Project Generator

An automated system that generates, commits, and pushes a new mini web project every day using the DeepSeek API.

## Features

- 🤖 **AI-Powered Generation**: Uses DeepSeek API to create unique project ideas and code
- 📅 **Daily Automation**: Automatically generates projects at a scheduled time (9:00 AM)
- 🚀 **Auto Git Operations**: Commits and pushes projects to GitHub
- 📁 **Organized Structure**: Creates well-organized project directories
- 🎨 **Creative Projects**: Generates functional, visually appealing web projects
- 📱 **Responsive Design**: All projects are mobile-friendly
- 💻 **Pure Web Tech**: Uses only HTML, CSS, and JavaScript (no frameworks)

## Project Requirements

Each generated project follows strict rules:

1. ✅ Small enough to complete within one HTML, one CSS, and one JavaScript file
2. ✅ Functional, creative, and visually appealing
3. ✅ Clear title for the project
4. ✅ Provides: index.html, style.css, script.js, readme.md
5. ✅ Proper file linking
6. ✅ No external frameworks (pure HTML, CSS, JS only)
7. ✅ Clean, readable, well-commented code

## Usage

### Run Once (Generate Immediate Project)
```bash
python daily_project_generator.py
```

### Start Daily Scheduler
When prompted, choose 'y' to start the daily scheduler:
```
Do you want to start the daily scheduler? (y/n): y
```

The scheduler will generate a new project every day at 9:00 AM.

## Project Structure

```
daily-mini-project/
├── daily_project_generator.py    # Main automation script
├── run.bat                      # Windows shortcut
├── .env                         # Environment variables (not tracked)
├── .env.example                # Example environment file
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── daily_projects.log          # Activity logs
└── projects/                   # Generated projects directory
    ├── 2025-08-15-Project-Name/
    │   ├── index.html
    │   ├── style.css
    │   ├── script.js
    │   └── readme.md
    └── ...
```

## Configuration

The `.env` file contains:
```
DEEPSEEK_API_KEY=your_api_key_here
GIT_USER_NAME=your_username
GIT_USER_EMAIL=your_email@example.com
```

## Example Generated Projects

- � Interactive Color Palette Generator
-  Memory Card Matching Game
- ⏰ Multi-Timezone Digital Clock
- 🖌️ Canvas Drawing Application
- 📝 Smart To-Do List with Local Storage
- 🎲 Animated Random Quote Generator
- 🧮 Scientific Calculator with Themes
- 🖼️ Responsive Image Gallery Slider
- ✨ Interactive Particle Animation System
- 📊 Real-time Data Visualization Dashboard

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure `.env` file exists with valid DeepSeek API key
2. **Git Remote Error**: The script will commit locally even if push fails
3. **Network Issues**: Script includes fallback projects if API is unavailable

### Logs
Check `daily_projects.log` for detailed activity information.

## License

Open source - use freely for your daily coding practice!

---

**Happy Daily Coding! 🚀**
