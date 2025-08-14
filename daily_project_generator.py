#!/usr/bin/env python3
"""
Daily Mini Project Generator
Automatically generates, commits, and pushes a new mini web project every day using DeepSeek API.
"""

import os
import json
import requests
import schedule
import time
import argparse
from datetime import datetime
from git import Repo
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('daily_projects.log'),
        logging.StreamHandler()
    ]
)

class DailyProjectGenerator:
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY')  # Will work with OpenAI key too
        # Detect API provider based on key format
        if self.api_key and (self.api_key.startswith('sk-proj-') or self.api_key.startswith('sk-')):
            self.api_url = "https://api.openai.com/v1/chat/completions"
            self.model = "gpt-3.5-turbo"
            logging.info("Using OpenAI API")
        else:
            self.api_url = "https://api.deepseek.com/chat/completions"
            self.model = "deepseek-chat"
            logging.info("Using DeepSeek API")
            
        self.projects_dir = os.path.join(os.getcwd(), 'projects')
        self.repo_path = os.getcwd()
        
        if not self.api_key:
            raise ValueError("API key not set in environment variable")
        
        # Ensure projects directory exists
        os.makedirs(self.projects_dir, exist_ok=True)
        
        # Initialize git repo if not already initialized
        self.init_git_repo()
    
    def init_git_repo(self):
        """Initialize git repository if not already initialized"""
        try:
            self.repo = Repo(self.repo_path)
            logging.info("Git repository found")
        except:
            self.repo = Repo.init(self.repo_path)
            logging.info("Git repository initialized")
            
            # Create .gitignore
            gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log

# OS
.DS_Store
Thumbs.db
"""
            with open(os.path.join(self.repo_path, '.gitignore'), 'w') as f:
                f.write(gitignore_content.strip())
    
    def generate_project_idea(self):
        """Generate a creative project idea using DeepSeek API"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        prompt = f"""Generate a creative, small web project idea for {current_date}. The project should be:

1. Completable with one HTML, one CSS, and one JavaScript file
2. Functional, creative, and visually appealing
3. Use only pure HTML, CSS, and JavaScript (no frameworks)
4. Be engaging and interactive
5. Have a clear purpose or theme

Please suggest a unique project idea with a catchy title. Examples of good projects:
- Interactive color palette generator
- Animated weather dashboard
- Memory card matching game
- Digital clock with multiple timezones
- Interactive drawing canvas
- Random quote generator with animations
- Simple calculator with themes
- To-do list with local storage
- Image slider/gallery
- Interactive particle system

Respond with just the project title and a brief 2-sentence description."""

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.8,
            "max_tokens": 200
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        except Exception as e:
            logging.error(f"Error generating project idea: {e}")
            return f"Interactive Web App - A creative web application for {current_date}"
    
    def generate_project_code(self, project_description):
        """Generate complete project code using DeepSeek API"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        prompt = f"""Create a complete web project based on this description: {project_description}

Requirements:
1. Create exactly 4 files: index.html, style.css, script.js, and readme.md
2. The project must be functional, creative, and visually appealing
3. Use only pure HTML, CSS, and JavaScript (no external frameworks)
4. Include proper linking between files
5. Add clear comments in the code
6. Make it responsive and mobile-friendly
7. Use modern CSS features (flexbox, grid, animations, etc.)
8. Include interactive JavaScript functionality

Please provide the complete code for all 4 files in the following format:

---
Title: {current_date} - [Project Title]

index.html:
```html
[Complete HTML code]
```

style.css:
```css
[Complete CSS code]
```

script.js:
```javascript
[Complete JavaScript code]
```

readme.md:
```markdown
[Complete README with project description, features, and how to run]
```
---

Make sure the project is fully functional and engaging!"""

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 4000
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        except Exception as e:
            logging.error(f"Error generating project code: {e}")
            return None
    
    def parse_and_save_project(self, generated_content):
        """Parse the generated content and save files"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H-%M")
        
        try:
            if generated_content:
                # Extract title
                title_lines = [line for line in generated_content.split('\n') if line.startswith('Title:')]
                if title_lines:
                    title = title_lines[0].replace('Title:', '').strip()
                else:
                    title = f"{current_date} - AI Generated Project"
                
                # Create project directory
                safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                project_dir = os.path.join(self.projects_dir, f"{current_date}-{safe_title.replace(' ', '-')}")
                
                # If directory exists, add time to make it unique
                if os.path.exists(project_dir):
                    project_dir = os.path.join(self.projects_dir, f"{current_date}-{current_time}-{safe_title.replace(' ', '-')}")
                
                os.makedirs(project_dir, exist_ok=True)
                
                # Extract and save files
                files = {
                    'index.html': self.extract_code_block(generated_content, 'html'),
                    'style.css': self.extract_code_block(generated_content, 'css'),
                    'script.js': self.extract_code_block(generated_content, 'javascript'),
                    'readme.md': self.extract_code_block(generated_content, 'markdown')
                }
                
                # If extraction fails, create basic template
                if not files['index.html']:
                    files = self.create_fallback_project(title)
            else:
                # No generated content, create fallback project
                title = f"{current_date} - Fallback Project"
                project_dir = os.path.join(self.projects_dir, f"{current_date}-{current_time}-Fallback-Project")
                os.makedirs(project_dir, exist_ok=True)
                files = self.create_fallback_project(title)
            
            # Save files
            for filename, content in files.items():
                if content:
                    with open(os.path.join(project_dir, filename), 'w', encoding='utf-8') as f:
                        f.write(content)
            
            logging.info(f"Project created: {project_dir}")
            return project_dir
            
        except Exception as e:
            logging.error(f"Error parsing and saving project: {e}")
            # Create emergency fallback
            try:
                fallback_dir = os.path.join(self.projects_dir, f"{current_date}-{current_time}-Emergency-Fallback")
                os.makedirs(fallback_dir, exist_ok=True)
                files = self.create_fallback_project(f"{current_date} - Emergency Fallback Project")
                for filename, content in files.items():
                    with open(os.path.join(fallback_dir, filename), 'w', encoding='utf-8') as f:
                        f.write(content)
                logging.info(f"Emergency fallback project created: {fallback_dir}")
                return fallback_dir
            except Exception as e2:
                logging.error(f"Failed to create emergency fallback: {e2}")
                return None
    
    def extract_code_block(self, content, language):
        """Extract code block for specific language"""
        try:
            lines = content.split('\n')
            start_markers = [f'```{language}', f'{language}:']
            
            for i, line in enumerate(lines):
                if any(marker in line.lower() for marker in start_markers):
                    # Find the start of the code block
                    start_idx = i + 1
                    if '```' in line:
                        # Already at code block start
                        pass
                    else:
                        # Look for next ```
                        for j in range(i + 1, len(lines)):
                            if lines[j].strip().startswith('```'):
                                start_idx = j + 1
                                break
                    
                    # Find the end of the code block
                    end_idx = len(lines)
                    for j in range(start_idx, len(lines)):
                        if lines[j].strip() == '```' or lines[j].strip().startswith('```'):
                            end_idx = j
                            break
                    
                    return '\n'.join(lines[start_idx:end_idx])
            
            return None
        except Exception:
            return None
    
    def create_fallback_project(self, title):
        """Create a fallback project if API generation fails"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>{title}</h1>
            <p>Generated on {current_date}</p>
        </header>
        <main>
            <div class="content">
                <p>This is a fallback project created when API generation failed.</p>
                <button id="click-btn">Click Me!</button>
                <div id="message"></div>
            </div>
        </main>
    </div>
    <script src="script.js"></script>
</body>
</html>'''

        css_content = '''/* Fallback Project Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.container {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    text-align: center;
    max-width: 500px;
    width: 90%;
}

header h1 {
    color: #333;
    margin-bottom: 0.5rem;
}

header p {
    color: #666;
    margin-bottom: 2rem;
}

.content {
    margin: 2rem 0;
}

#click-btn {
    background: linear-gradient(45deg, #667eea, #764ba2);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 25px;
    font-size: 1rem;
    cursor: pointer;
    transition: transform 0.3s ease;
}

#click-btn:hover {
    transform: translateY(-2px);
}

#message {
    margin-top: 1rem;
    padding: 1rem;
    border-radius: 10px;
    background: #f8f9fa;
    color: #333;
    min-height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}'''

        js_content = '''// Fallback Project JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('click-btn');
    const messageDiv = document.getElementById('message');
    
    const messages = [
        "Hello! 👋",
        "This is a fallback project! 🚀",
        "Generated automatically! 🤖",
        "Have a great day! ☀️",
        "Keep coding! 💻"
    ];
    
    let clickCount = 0;
    
    button.addEventListener('click', function() {
        clickCount++;
        const messageIndex = (clickCount - 1) % messages.length;
        messageDiv.textContent = messages[messageIndex];
        
        // Add some animation
        messageDiv.style.transform = 'scale(0.9)';
        setTimeout(() => {
            messageDiv.style.transform = 'scale(1)';
        }, 150);
    });
    
    // Initial message
    messageDiv.textContent = "Click the button to see messages!";
});'''

        readme_content = f'''# {title}

Generated on {current_date}

## Description
This is a fallback project created by the Daily Mini Project Generator when the main API generation encountered issues.

## Features
- Clean, responsive design
- Interactive button with messages
- Smooth animations and transitions
- Mobile-friendly layout

## How to Run
1. Open `index.html` in a web browser
2. Click the button to see different messages
3. Enjoy the simple interaction!

## Files
- `index.html` - Main HTML structure
- `style.css` - Styling and animations
- `script.js` - Interactive functionality
- `readme.md` - This documentation

## Technologies Used
- Pure HTML5
- CSS3 with gradients and animations
- Vanilla JavaScript
'''

        return {
            'index.html': html_content,
            'style.css': css_content,
            'script.js': js_content,
            'readme.md': readme_content
        }
    
    def commit_and_push(self, project_dir):
        """Commit and push the new project to git"""
        try:
            # Add all files
            self.repo.git.add(A=True)
            
            # Get project name for commit message
            project_name = os.path.basename(project_dir)
            commit_message = f"Add daily project: {project_name}"
            
            # Commit
            self.repo.index.commit(commit_message)
            logging.info(f"Committed: {commit_message}")
            
            # Push to GitHub
            try:
                # Check if origin remote exists
                if 'origin' in [remote.name for remote in self.repo.remotes]:
                    origin = self.repo.remote(name='origin')
                    # Push to the current branch (master in this case)
                    origin.push()
                    logging.info("Successfully pushed to GitHub repository")
                else:
                    logging.warning("No 'origin' remote configured. Please add remote manually.")
                    logging.info("To add remote: git remote add origin https://github.com/defrein/auto-daily-mini-project.git")
            except Exception as e:
                logging.error(f"Failed to push to GitHub: {e}")
                logging.info("Project committed locally but not pushed to remote")
            
        except Exception as e:
            logging.error(f"Error committing: {e}")
    
    def generate_daily_project(self):
        """Main function to generate daily project"""
        logging.info("Starting daily project generation...")
        
        try:
            # Generate project idea
            project_idea = self.generate_project_idea()
            logging.info(f"Generated idea: {project_idea}")
            
            # Generate project code
            project_code = self.generate_project_code(project_idea)
            
            # Parse and save project
            project_dir = self.parse_and_save_project(project_code)
            
            if project_dir:
                # Commit and push
                self.commit_and_push(project_dir)
                logging.info(f"Daily project generated successfully: {project_dir}")
                return True
            else:
                logging.error("Failed to create project")
                return False
                
        except Exception as e:
            logging.error(f"Error in daily project generation: {e}")
            return False
    
    def start_scheduler(self):
        """Start the daily scheduler"""
        # Schedule daily project generation at 9:00 AM
        schedule.every().day.at("09:00").do(self.generate_daily_project)
        
        logging.info("Scheduler started. Daily projects will be generated at 9:00 AM")
        logging.info("Press Ctrl+C to stop the scheduler")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Daily Mini Project Generator')
    parser.add_argument('--now', action='store_true', 
                       help='Generate and push a project immediately without starting the scheduler')
    args = parser.parse_args()
    
    try:
        generator = DailyProjectGenerator()
        
        if args.now:
            # Generate project immediately and exit
            print("🚀 Generating project immediately...")
            success = generator.generate_daily_project()
            
            if success:
                print("✅ Project generated and pushed successfully!")
            else:
                print("❌ Failed to generate project")
            
            # Exit without starting scheduler
            exit(0 if success else 1)
        
        # Default behavior: generate initial project and ask about scheduler
        print("Generating initial project...")
        success = generator.generate_daily_project()
        
        if success:
            print("✅ Initial project generated successfully!")
        else:
            print("❌ Failed to generate initial project")
        
        # Ask user if they want to start the scheduler
        response = input("\nDo you want to start the daily scheduler? (y/n): ")
        if response.lower() in ['y', 'yes']:
            generator.start_scheduler()
        else:
            print("Scheduler not started. Run this script again to start it.")
            print("💡 Tip: Use --now flag to generate projects immediately without the scheduler")
            
    except KeyboardInterrupt:
        print("\nScheduler stopped by user")
    except Exception as e:
        print(f"Error: {e}")
