import subprocess
import datetime

def auto_git_update(commit_message=None):
    if not commit_message:
        commit_message = f"Automated repo update: {datetime.date.today()}"
        
    try:
        # 1. Add all changes
        subprocess.run(["git", "add", "."], check=True)
        
        # 2. Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 3. Push to GitHub
        subprocess.run(["git", "push"], check=True)
        print(" Repository successfully updated on GitHub!")
        
    except subprocess.CalledProcessError as e:
        print(f" Git automation failed: {e}")
    except FileNotFoundError:
        print("Error: Git is not installed or not in your system PATH.")

if __name__ == "__main__":
    auto_git_update()
