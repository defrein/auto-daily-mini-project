#!/usr/bin/env python3
"""
Configuration helper for Daily Mini Project Generator
"""

import os
import sys

def configure_api_key():
    """Interactive API key configuration"""
    print("🔧 Daily Mini Project Generator - API Configuration")
    print("=" * 50)
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found. Please run setup.py first.")
        return False
    
    print("📝 To get your DeepSeek API key:")
    print("1. Visit: https://platform.deepseek.com/")
    print("2. Sign up or log in")
    print("3. Navigate to API Keys section") 
    print("4. Create a new API key")
    print("5. Copy the key")
    print()
    
    # Get API key from user
    api_key = input("🔑 Enter your DeepSeek API key (or press Enter to skip): ").strip()
    
    if not api_key:
        print("⏭️  Skipped API key configuration")
        return False
    
    # Read current .env file
    with open('.env', 'r') as f:
        lines = f.readlines()
    
    # Update API key line
    updated_lines = []
    key_updated = False
    
    for line in lines:
        if line.startswith('DEEPSEEK_API_KEY='):
            updated_lines.append(f'DEEPSEEK_API_KEY={api_key}\n')
            key_updated = True
        else:
            updated_lines.append(line)
    
    # If key line doesn't exist, add it
    if not key_updated:
        updated_lines.append(f'DEEPSEEK_API_KEY={api_key}\n')
    
    # Write updated .env file
    with open('.env', 'w') as f:
        f.writelines(updated_lines)
    
    print("✅ API key configured successfully!")
    return True

def configure_git():
    """Configure git settings"""
    print("\n🔧 Git Configuration (Optional)")
    print("-" * 30)
    
    git_name = input("Enter your Git username (or press Enter to skip): ").strip()
    git_email = input("Enter your Git email (or press Enter to skip): ").strip()
    
    if git_name or git_email:
        # Read current .env file
        with open('.env', 'r') as f:
            lines = f.readlines()
        
        # Update git lines
        updated_lines = []
        name_updated = False
        email_updated = False
        
        for line in lines:
            if line.startswith('GIT_USER_NAME=') and git_name:
                updated_lines.append(f'GIT_USER_NAME={git_name}\n')
                name_updated = True
            elif line.startswith('GIT_USER_EMAIL=') and git_email:
                updated_lines.append(f'GIT_USER_EMAIL={git_email}\n')
                email_updated = True
            else:
                updated_lines.append(line)
        
        # Add missing lines
        if git_name and not name_updated:
            updated_lines.append(f'GIT_USER_NAME={git_name}\n')
        if git_email and not email_updated:
            updated_lines.append(f'GIT_USER_EMAIL={git_email}\n')
        
        # Write updated .env file
        with open('.env', 'w') as f:
            f.writelines(updated_lines)
        
        print("✅ Git configuration updated!")
    else:
        print("⏭️  Skipped Git configuration")

def show_next_steps():
    """Show next steps to user"""
    print("\n🎉 Configuration Complete!")
    print("=" * 50)
    print("📋 Next Steps:")
    print("1. Run tests: python test.py")
    print("2. Generate first project: python daily_project_generator.py")
    print("3. (Optional) Set up git remote for auto-pushing")
    print()
    print("💡 Quick Commands:")
    print("   • Windows: run.bat")
    print("   • Windows Tests: test.bat")
    print("   • Manual: python daily_project_generator.py")
    print()
    print("📚 Check README.md for detailed documentation")

def main():
    """Main configuration function"""
    try:
        # Configure API key
        api_configured = configure_api_key()
        
        # Configure git (optional)
        configure_git()
        
        # Show next steps
        show_next_steps()
        
        if api_configured:
            # Ask if user wants to run a test
            print("\n" + "=" * 50)
            test_now = input("🧪 Run tests now? (y/n): ").strip().lower()
            if test_now in ['y', 'yes']:
                print("\n🧪 Running tests...")
                os.system(f"{sys.executable} test.py")
        
    except KeyboardInterrupt:
        print("\n\n⛔ Configuration cancelled by user")
    except Exception as e:
        print(f"\n❌ Error during configuration: {e}")

if __name__ == "__main__":
    main()
