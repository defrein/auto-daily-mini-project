#!/usr/bin/env python3
"""
Quick setup script for Daily Mini Project Generator
"""

import os
import subprocess
import sys

def setup_project():
    """Setup the daily mini project generator"""
    print("🚀 Setting up Daily Mini Project Generator...")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("📝 Creating .env file from template...")
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as src, open('.env', 'w') as dst:
                dst.write(src.read())
            print("✅ .env file created. Please edit it with your DeepSeek API key.")
        else:
            print("❌ .env.example not found!")
            return False
    
    # Initialize git if not already initialized
    if not os.path.exists('.git'):
        print("🔧 Initializing Git repository...")
        try:
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', 'Initial commit: Daily Mini Project Generator setup'], check=True, capture_output=True)
            print("✅ Git repository initialized")
        except subprocess.CalledProcessError:
            print("⚠️  Git initialization failed (git might not be installed)")
    
    # Create projects directory
    os.makedirs('projects', exist_ok=True)
    print("📁 Projects directory created")
    
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your DeepSeek API key")
    print("2. Run: python daily_project_generator.py")
    print("3. (Optional) Configure git remote for pushing projects")
    
    return True

if __name__ == "__main__":
    setup_project()
