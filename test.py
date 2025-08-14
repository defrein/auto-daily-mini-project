#!/usr/bin/env python3
"""
Test script for Daily Mini Project Generator
"""

import os
import sys
from daily_project_generator import DailyProjectGenerator

def test_setup():
    """Test the basic setup"""
    print("🧪 Testing Daily Mini Project Generator Setup...")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found. Please run setup.py first.")
        return False
    
    # Check if API key is set
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key or api_key == 'your_deepseek_api_key_here':
        print("❌ DeepSeek API key not configured. Please edit .env file.")
        return False
    
    print("✅ Environment configuration looks good")
    return True

def test_fallback_project():
    """Test fallback project generation"""
    print("🔧 Testing fallback project generation...")
    
    try:
        generator = DailyProjectGenerator()
        
        # Test fallback project creation
        files = generator.create_fallback_project("Test Project")
        
        if all(files.values()) and len(files) == 4:
            print("✅ Fallback project generation works")
            return True
        else:
            print("❌ Fallback project generation failed")
            return False
            
    except Exception as e:
        print(f"❌ Error testing fallback: {e}")
        return False

def test_api_connection():
    """Test API connection (if key is configured)"""
    print("🌐 Testing API connection...")
    
    try:
        generator = DailyProjectGenerator()
        
        # Try to generate a simple idea
        idea = generator.generate_project_idea()
        
        if idea and len(idea) > 10:
            print("✅ API connection successful")
            print(f"📝 Sample idea: {idea[:100]}...")
            return True
        else:
            print("❌ API connection failed or returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ API connection error: {e}")
        return False

def run_tests():
    """Run all tests"""
    print("=" * 50)
    print("Daily Mini Project Generator - Test Suite")
    print("=" * 50)
    
    tests = [
        test_setup,
        test_fallback_project,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            print()
    
    # Only test API if basic setup works
    if passed == total:
        print("🌐 Running API test (optional)...")
        try:
            if test_api_connection():
                passed += 1
            total += 1
            print()
        except Exception as e:
            print(f"⚠️  API test skipped: {e}")
            print()
    
    print("=" * 50)
    print(f"Tests Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\n🚀 You can now run: python daily_project_generator.py")
    else:
        print("❌ Some tests failed. Please check the setup.")
        if passed < 2:
            print("💡 Try running: python setup.py")
    
    print("=" * 50)

if __name__ == "__main__":
    run_tests()
