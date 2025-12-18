"""
Python Error Test App
This app will fail immediately on startup due to missing required environment variable
Used to test error handling and logging in Hostany deployment
"""
import os
import sys
from datetime import datetime


def get_timestamp():
    """Get formatted timestamp"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def main():
    """Main application - will fail immediately"""
    print(f"[{get_timestamp()}] Starting application...")
    print(f"[{get_timestamp()}] Checking required environment variables...")
    
    # Try to access a required environment variable that doesn't exist
    required_var = os.getenv('REQUIRED_API_KEY')
    
    if not required_var:
        print(f"[{get_timestamp()}] ERROR: Required environment variable 'REQUIRED_API_KEY' is not set!")
        print(f"[{get_timestamp()}] ERROR: Application cannot start without this variable.")
        print(f"[{get_timestamp()}] ERROR: Please set REQUIRED_API_KEY environment variable.")
        sys.exit(1)
    
    print(f"[{get_timestamp()}] INFO: Application started successfully")
    print(f"[{get_timestamp()}] INFO: API Key: {required_var[:8]}...")


if __name__ == '__main__':
    main()


