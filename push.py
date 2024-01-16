#!/usr/local/bin/python3
import subprocess
import schedule
import time

def commit_and_push():
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'])
        
        # Commit changes
        subprocess.run(['git', 'commit', '-m', 'Automated commit'])
        
        # Push to the default remote branch
        subprocess.run(['git', 'push'])
        
        print("Commit and push successful.")
    except Exception as e:
        print(f"Error: {e}")

# Schedule the job to run every minute
schedule.every(1).minutes.do(commit_and_push)

while True:
    schedule.run_pending()
    time.sleep(1)
