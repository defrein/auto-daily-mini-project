#!/usr/bin/env python3
"""
Demo script to showcase the Daily Mini Project Generator
"""

import os
import sys
from datetime import datetime

def print_banner():
    """Print a nice banner"""
    print("=" * 60)
    print("🎨 DAILY MINI PROJECT GENERATOR - DEMO")
    print("=" * 60)
    print()

def show_file_structure():
    """Show the project structure"""
    print("📁 Project Structure:")
    print("├── 📜 daily_project_generator.py    # Main automation")
    print("├── ⚙️ configure.py                  # Easy setup")
    print("├── 🧪 test.py                       # Testing")
    print("├── 📖 README.md                     # Documentation")
    print("├── 🚀 QUICKSTART.md                 # Quick guide")
    print("├── 🔐 .env                          # Your config")
    print("├── 📂 projects/                     # Generated projects")
    print("└── 📊 daily_projects.log            # Activity logs")
    print()

def show_sample_project():
    """Show the sample project that was created"""
    sample_dir = "projects/2025-08-15-Interactive-Demo-Project"
    
    if os.path.exists(sample_dir):
        print("🎯 Sample Project Created:")
        print(f"📁 {sample_dir}/")
        
        files = ["index.html", "style.css", "script.js", "readme.md"]
        for file in files:
            file_path = os.path.join(sample_dir, file)
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                print(f"   ├── 📄 {file} ({size} bytes)")
        print()
        
        # Show a snippet of HTML
        html_path = os.path.join(sample_dir, "index.html")
        if os.path.exists(html_path):
            print("📝 Sample HTML Preview:")
            with open(html_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()[:10]  # First 10 lines
                for line in lines:
                    print(f"   {line.rstrip()}")
                print("   ...")
            print()

def show_next_steps():
    """Show what to do next"""
    print("🔑 NEXT STEPS:")
    print("1. Get DeepSeek API key: https://platform.deepseek.com/")
    print("2. Configure: python configure.py")
    print("3. Test: python test.py")
    print("4. Generate: python daily_project_generator.py")
    print()
    
    print("💡 QUICK COMMANDS:")
    print("   • Windows Config: configure.bat")
    print("   • Windows Test: test.bat")
    print("   • Windows Run: run.bat")
    print()

def show_project_examples():
    """Show examples of projects that can be generated"""
    print("🎨 EXAMPLE PROJECTS THE AI WILL CREATE:")
    
    examples = [
        "🌈 Interactive Color Palette Generator",
        "🎮 Memory Card Matching Game", 
        "⏰ Multi-Timezone Digital Clock",
        "🖌️ Canvas Drawing Application",
        "📝 Smart To-Do List with Local Storage",
        "🎲 Animated Random Quote Generator",
        "🧮 Scientific Calculator with Themes",
        "🖼️ Responsive Image Gallery Slider",
        "✨ Interactive Particle Animation System",
        "📊 Real-time Data Visualization Dashboard"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"   {i:2d}. {example}")
    print()

def show_automation_info():
    """Show information about automation"""
    print("🤖 AUTOMATION FEATURES:")
    print("   • 📅 Generates new project daily at 9:00 AM")
    print("   • 🔄 Auto-commits to git repository")
    print("   • 📊 Logs all activities")
    print("   • 🛡️ Fallback templates if API fails")
    print("   • 📱 All projects are mobile-responsive")
    print("   • 💻 Uses only pure HTML, CSS, JavaScript")
    print()

def main():
    """Main demo function"""
    print_banner()
    
    print("🎉 Welcome to your Daily Mini Project Generator!")
    print("This system automatically creates a new web project every day.")
    print()
    
    show_file_structure()
    show_sample_project()
    show_project_examples()
    show_automation_info()
    show_next_steps()
    
    print("📚 DOCUMENTATION:")
    print("   • README.md - Complete documentation")
    print("   • QUICKSTART.md - Simple setup guide")  
    print("   • SETUP_COMPLETE.md - Summary of everything")
    print()
    
    print("🎊 Ready to start your daily coding journey!")
    print("=" * 60)

if __name__ == "__main__":
    main()
