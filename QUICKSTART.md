# 🚀 Quick Start Guide

Welcome to the Daily Mini Project Generator! Follow these simple steps to get started.

## Step 1: Get Your DeepSeek API Key 🔑

1. Visit **[DeepSeek Platform](https://platform.deepseek.com/)**
2. **Sign up** or **log in** to your account
3. Navigate to **"API Keys"** section
4. Click **"Create New Key"**
5. **Copy** the generated API key (keep it safe!)

## Step 2: Configure the System ⚙️

### Option A: Use Configuration Script (Recommended)
```bash
python configure.py
```
Or on Windows, double-click: **`configure.bat`**

### Option B: Manual Configuration
1. Open `.env` file in a text editor
2. Replace `your_deepseek_api_key_here` with your actual API key:
   ```
   DEEPSEEK_API_KEY=sk-your-actual-key-here
   ```

## Step 3: Test the Setup 🧪

```bash
python test.py
```
Or on Windows, double-click: **`test.bat`**

You should see: `✅ All tests passed!`

## Step 4: Generate Your First Project 🎨

```bash
python daily_project_generator.py
```
Or on Windows, double-click: **`run.bat`**

The system will:
1. ✨ Generate a creative project idea
2. 💻 Create complete HTML, CSS, JS files
3. 📁 Save in organized folder structure
4. 🔄 Commit to git automatically

## Step 5: Start Daily Automation 📅

When prompted:
```
Do you want to start the daily scheduler? (y/n): y
```

This will generate a new project every day at 9:00 AM!

## 🎯 What You Get

Each project includes:
- **`index.html`** - Main page structure
- **`style.css`** - Beautiful styling
- **`script.js`** - Interactive functionality  
- **`readme.md`** - Project documentation

## 📁 Project Structure

```
projects/
├── 2025-08-15-Interactive-Color-Palette/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── readme.md
├── 2025-08-16-Memory-Card-Game/
│   └── ... (same files)
└── ... (new projects daily)
```

## 🔧 Troubleshooting

### ❌ API Key Issues
- Make sure you copied the key correctly
- Check that `.env` file exists and has the right format
- Run `python configure.py` to reconfigure

### ❌ Git Issues  
- Git errors are usually non-critical
- Projects still save locally even if git fails
- Configure git remote to enable pushing

### ❌ Network Issues
- Script includes fallback projects if API fails
- Check your internet connection
- DeepSeek API might have rate limits

## 🎨 Example Projects Generated

- 🌈 Interactive Color Palette Generator
- 🎮 Memory Card Matching Game
- ⏰ Multi-Timezone Digital Clock
- 🖌️ Canvas Drawing App
- 📝 Smart To-Do List
- 🎲 Random Quote Generator
- 🧮 Themed Calculator
- 🖼️ Image Gallery Slider

## 🚀 Ready to Start?

1. Get your API key from DeepSeek
2. Run: `python configure.py`
3. Run: `python daily_project_generator.py`
4. Enjoy your daily coding projects!

**Happy Coding! 🎉**
