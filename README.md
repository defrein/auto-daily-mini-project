# Daily Mini Project Generator

An automated system that generates, commits, and pushes a new mini web project every day using the DeepSeek API.

## Features

- 🤖 **AI-Powered Generation**: Uses DeepSeek API to create unique project ideas and code
- 📅 **Daily Automation**: Automatically generates projects at a scheduled time
- 🚀 **Auto Git Operations**: Commits and pushes projects to your repository
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

## Setup Instructions

### 1. Clone and Setup

```bash
cd d:\Code\Python\daily-mini-project
```

### 2. Install Dependencies

Dependencies are already installed:
- `requests` - For API calls
- `gitpython` - For git operations  
- `python-dotenv` - For environment variables
- `schedule` - For daily automation

### 3. Configure Environment

1. Copy the example environment file:
```bash
copy .env.example .env
```

2. Edit `.env` file and add your DeepSeek API key:
```
DEEPSEEK_API_KEY=your_actual_deepseek_api_key_here
```

### 4. Get DeepSeek API Key

1. Visit [DeepSeek Platform](https://platform.deepseek.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

### 5. Configure Git (Optional)

If you want to push to a remote repository:

```bash
git remote add origin https://github.com/yourusername/daily-mini-projects.git
```

## Usage

### Run Once (Generate Immediate Project)

```bash
python daily_project_generator.py
```

This will:
1. Generate a project idea using DeepSeek API
2. Create complete project code (HTML, CSS, JS, README)
3. Save files in organized directory structure
4. Commit and push to git

### Start Daily Scheduler

When you run the script, it will ask if you want to start the daily scheduler:

```
Do you want to start the daily scheduler? (y/n): y
```

The scheduler will:
- Generate a new project every day at 9:00 AM
- Run continuously in the background
- Log all activities to `daily_projects.log`

### Manual Project Generation

You can also generate projects manually by running:

```bash
python -c "from daily_project_generator import DailyProjectGenerator; DailyProjectGenerator().generate_daily_project()"
```

## Project Structure

```
daily-mini-project/
├── daily_project_generator.py    # Main automation script
├── .env                         # Environment variables (create from .env.example)
├── .env.example                # Example environment file
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── daily_projects.log          # Activity logs
├── .gitignore                  # Git ignore rules
└── projects/                   # Generated projects directory
    ├── 2025-08-15-Interactive-Color-Palette/
    │   ├── index.html
    │   ├── style.css
    │   ├── script.js
    │   └── readme.md
    ├── 2025-08-16-Memory-Card-Game/
    │   ├── index.html
    │   ├── style.css
    │   ├── script.js
    │   └── readme.md
    └── ...
```

## Example Generated Projects

The system can generate various types of projects:

- 🎨 **Interactive Color Palette Generator**
- 🌦️ **Animated Weather Dashboard**  
- 🎮 **Memory Card Matching Game**
- ⏰ **Digital Clock with Multiple Timezones**
- 🖌️ **Interactive Drawing Canvas**
- 💭 **Random Quote Generator with Animations**
- 🧮 **Themed Calculator**
- ✅ **To-Do List with Local Storage**
- 🖼️ **Image Slider/Gallery**
- ✨ **Interactive Particle System**

## Scheduling Options

### Default Schedule
- **Time**: 9:00 AM daily
- **Timezone**: System timezone

### Custom Schedule
Edit the script to change the schedule:

```python
# Change this line in start_scheduler() method
schedule.every().day.at("14:30").do(self.generate_daily_project)  # 2:30 PM
```

### Run as Windows Service
To run continuously as a service, you can use tools like:
- **NSSM** (Non-Sucking Service Manager)
- **Windows Task Scheduler**
- **Python service frameworks**

## Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   ValueError: DEEPSEEK_API_KEY environment variable not set
   ```
   **Solution**: Make sure `.env` file exists with valid API key

2. **Git Remote Error**
   ```
   Could not push to remote
   ```
   **Solution**: Configure git remote or ignore the warning (projects still save locally)

3. **API Rate Limits**
   - DeepSeek has rate limits
   - The script includes error handling and fallback projects

4. **Network Issues**
   - Script includes timeout handling
   - Falls back to template projects if API fails

### Logs

Check `daily_projects.log` for detailed information:

```bash
type daily_projects.log
```

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEEPSEEK_API_KEY` | Your DeepSeek API key | Required |
| `GIT_USER_NAME` | Git username | Optional |
| `GIT_USER_EMAIL` | Git email | Optional |
| `DAILY_TIME` | Schedule time (HH:MM) | 09:00 |
| `PROJECTS_DIR` | Projects directory | projects |

### Code Customization

You can customize the project generation by modifying:

- **Project prompts** in `generate_project_idea()` and `generate_project_code()`
- **Fallback templates** in `create_fallback_project()`
- **Schedule timing** in `start_scheduler()`
- **File structure** in `parse_and_save_project()`

## API Usage

The script uses DeepSeek's chat completion API:

- **Model**: `deepseek-chat`
- **Temperature**: 0.7-0.8 (for creativity)
- **Max Tokens**: 4000 (for complete projects)
- **Timeout**: 60 seconds

## Security Notes

- Keep your `.env` file secure and never commit it
- The `.gitignore` file excludes sensitive files
- API keys are loaded from environment variables only

## Contributing

Feel free to improve the project:

1. Add new project templates
2. Improve error handling
3. Add more customization options
4. Enhance the scheduling system
5. Add project validation

## License

This project is open source. Use it freely for your daily coding practice!

---

**Happy Daily Coding! 🚀**
