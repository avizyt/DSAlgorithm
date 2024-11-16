import subprocess
import os


def automate_git_commit(repo_path, commit_message, branch="main"):
    """
    Automates the process of adding, committing, and optionally pushing changes to a Git repository.

    Parameters:
        repo_path (str): Path to the local Git repository.
        commit_message (str): Commit message.
        branch (str): Branch to push changes (default is 'main').
    """
    try:
        # Change the working directory to the repository path
        os.chdir(repo_path)

        # Run `git add .` to stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Run `git commit -m <message>` to commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Run `git push origin <branch>` to push changes
        subprocess.run(["git", "push", "origin", branch], check=True)

        print(f"Changes committed and pushed to branch '{branch}' successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Example usage
if __name__ == "__main__":
    repo_path = "/path/to/your/repo"  # Replace with the path to your Git repository
    commit_message = "Automated commit using Python script"
    branch_name = "main"  # Replace with the branch you want to push to

    automate_git_commit(repo_path, commit_message, branch_name)
