
Q1. 
The full absolute path of my current working directory,the exact location in the filesystem where my terminal is at right now.

Q2. 
It showed the hidden files or folders, anything starting with a dot, like '.' , '..' etc. Plain 'ls' shows only the visible files and folders.

Q3. 
The first column is a 10-character permissions string. The very first character is the file type (`-` = regular file, `d` = directory). The next 9 characters are three groups of three (read/write/execute) for the user.

Q4. 
It works because the path is given relative to my current directory  the shell resolves `coding-cafe/week02` starting from wherever I currently am, without needing `cd` first. This is a relative path (it doesn't start with /). An absolute path would instead start from the root, e.g. /home/adhirajsinghchaudhri/coding-cafe/week02.

Q5. 
First, 'mv README-backup.md week01/' moved the file into a different folder. Second, 'mv README-backup.md old-readme.md' renamed the file in place without changing the location. `mv` basically does the work of moving and renaming.


Q6. 
I ran 'echo $PATH' and counted.That's 12 folders on my PATH. Counting the colon-separated entries:
/usr/local/bin
/System/Cryptexes/App/usr/bin
/usr/bin
/bin
/usr/sbin
/sbin
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
/pkg/env/global/bin
/Library/Apple/usr/bin
/opt/homebrew/bin

Q7. 
'which python3' printed the full path-- '/usr/bin/python3' 

Q8. 
It is different because it depends on various factors like how they installed python, using homebrew or something else. It also depends upon how the user installed the packages and files for python. Another reason could be that it depends on how the system read the files like in which order.

Q9. 
It said 'zsh: command not found: pyton3'. This means the shell searched every folder listed in my PATH, in order, and found no executable file named exactly 'pyton3' in any of them — it's not that Python is missing, it's that no folder on the PATH contains a program with that exact (misspelled) name.

Q10. 
Because '.venv' starts with a dot, which makes it a hidden folder by the same rule from Section 1 — plain 'ls' doesn't show anything starting with '.'. Running 'ls -a' reveals it.

Q11.
After 'source .venv/bin/activate', the prompt gained a '(.venv)' prefix at the start of the line, signalling that this shell session is now "inside" the virtual environment.

Q12. 
No, inside the venv, 'which python3' points to a Python inside the 'coding-cafe/.venv'  This shows that 'activate' didn't install a new Python — it simply pushed the venv's own 'bin/' folder to the front of PATH, so the shell finds that copy first before it ever gets to the system folders.

Q13.
The second list includes 'requests' that got pulled in by 'pip install requests'. The first list only had the bare minimum packages that ship with a fresh venv.

Q14. 
Back to the same system path from Q7 — 'deactivate' removes the venv's 'bin/' folder from the front of PATH, so the shell goes back to finding the original system Python first.


Q15. 
It makes file sizes shown by 'ls -l' "human-readable" — instead of printing raw byte counts.

Q16. 
Ctrl+C sends an interrupt signal that forcibly stops whatever is currently running (it says "stop right now"). Ctrl+D sends an end-of-input signal, telling the program there's no more input coming — for the Python REPL, this reads as "nothing more to type," so it exits gracefully. Ctrl+C halts a stuck process; Ctrl+D signals a clean end of input.
