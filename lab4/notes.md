Question 1: Meaning of --global in git config and omitting it
The --global flag applies user details across all Git repositories on your system by storing them in ~/.gitconfig. Omitting it applies the configuration only to the current repository locally (in .git/config).

Question 2: Contents of .git revealed by ls -a
Running ls -a reveals the hidden .git folder. It contains Git's internal metadata, tracking data, configuration options, object store, and commit history for the repository.

Question 3: Approximate untracked file count and identifying untracked code
Before creating .gitignore, Git offered to track .DS_Store, Python/, notes.md, and week02/, spanning thousands of files when including dependencies like .venv/. Code you did not write includes virtual environment files inside .venv/ and system files like .DS_Store.

Question 4: Difference in git status after creating .gitignore
After adding .gitignore, hidden virtual environment files and OS junk like .DS_Store were ignored by Git. The .gitignore file itself showed up under untracked files while .DS_Store disappeared.

Question 5: Why .gitignore itself should be committed rather than ignored
.gitignore must be committed so that everyone who clones or reviews the repository shares the exact same rules for ignoring temporary build files and virtual environments.

Question 6: Movement of README.md across sections in git status (three-places model)
Running git add README.md moves the file from Untracked files (Working Directory) to Changes to be committed (Staging Area/Index).

Question 7: Output produced by git commit and count of changed files
Git printed [main (root-commit) 7f6aab4] Lab work so far along with mode creation details for each file. It reported that 13 files changed with 4498 insertions(+).

Question 8: Name and purpose of the first seven characters of a commit hash
The first seven characters (e.g., 7f6aab4) are called the short commit hash. They serve as a unique abbreviated identifier for referencing that specific commit.

Question 9: The 4 steps of the repetitive Git loop
Edit: Modify or create files in the working directory.

Status Check: Run git status to see unstaged/untracked changes.

Stage: Run git add <file> to move changes to the staging area.

Commit: Run git commit -m "message" to record a permanent snapshot.

Question 10: Special purpose and placement of README.md
README.md is placed in the root directory because Git hosting platforms automatically render it as the main landing page documentation for anyone viewing the repository.

Question 11: How gh auth login eliminates future password prompts
gh auth login authenticates via OAuth in the browser and configures GitHub CLI as a secure credential helper, storing a persistent token so password prompts are no longer needed.

Question 12: File rendered on GitHub's front page and the reason why
README.md is rendered on the front page of the repository because GitHub is hardcoded to parse Markdown files with that name as the primary overview for visitors.

Question 13: Effect of git push on local history
Running git push uploads your local commits to the remote repository. It updates remote tracking references without modifying your local commit history.

Question 14: Distinction between a private repository vs. no repository on GitHub
A private repository exists on GitHub's servers but limits access exclusively to you and explicitly added collaborators. If no repository exists, the URL returns a 404 error and remote operations like git push fail completely.
