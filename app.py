"""
Simple Python Logger App
Continuously prints current time for testing Hostany deployment
"""
import time
from datetime import datetime


def main():
    """Main application loop"""
    print("Python Logger App Started")
    print("Printing current time every second...")
    print("-" * 50)

    try:
        while True:
            # Print current time
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(current_time)
            
            # Wait 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nApplication stopped gracefully")


if __name__ == '__main__':
    main()
