GIT INSTALLATION (Ubuntu/Linux)

1. Update system packages
   # sudo apt update
   # sudo apt upgrade

2. Install Git
   # sudo apt install git

3. Verify installation
   # git --version


GIT CONFIGURATION

1. Configure Git user identity (global)
   # git config --global user.name "Your Name"
   # git config --global user.email "your@email.com"

2. Verify configuration
   # git config --list

GIT CLONE & STATUS

1. Clone (clone repository into local form github)
    # git clone <url (https or ssh )>

2. Status(Check status)
    # git status

    a) untracked -> new file that git doesn't yet track
    b) modified -> changed
    c) staged -> file is ready to be committed 
    d) unmodified -> unchanged 

GIT ADD & TRACK

1. Add ( adds new or changed files in your working directory to the git staging area)
   # git add <file_name> or
   # git add . (to add multiple files or record)
2. commit (it is the record of change)
   # git commit -m "message"

GIT PUSH (upload local repo content to remote repo)
# git push origin main

GIT INIT (used to create a new repo)

# git init (to track the file )
# git remote add origin < add file or folder in remore repo link>
# git branch ( cheks branch )
# git remote -v ( verifes remote)
# git branch -M main    ( )
# git push origin main /or 
## git push -u origin main ( to work countiniously in same project and next time it tells the system git push instead of origin main)

BRANCH COMMANDS
# git branch (to check branch)
# git branch -M main ( to rename branch)
# git checkout <branch_name> ( to navigate)
# git checkout -b < branch_name> ( to create new branch)
# git git branch -d <branch_name > (to delete branch)