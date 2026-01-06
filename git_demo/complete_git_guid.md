 GIT COMPLETE NOTES FOR DEVOPS (LINUX / UBUNTU)

## GIT INSTALLATION

sudo apt update
sudo apt upgrade
sudo apt install git
git --version


## GIT CONFIGURATION

git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list


## BASIC GIT WORKFLOW

Working Directory → Staging Area → Local Repository → Remote Repository

- git add     → move changes to staging
- git commit → save changes locally
- git push   → upload changes to remote


## GIT CLONE & STATUS

git clone <repository_url>    # copy remote repo
git status                   # check file status

File states:
- untracked  → new file
- modified  → changed file
- staged    → ready to commit
- unmodified→ no change


## GIT ADD & COMMIT

git add <file_name>           # add single file
git add .                     # add all files
git commit -m "message"       # save changes


## GIT INIT (NEW REPOSITORY)

git init                      # create git repository
git branch                    # check branch
git branch -M main             # rename branch
git remote add origin <url>    # add remote
git remote -v                 # verify remote
git push -u origin main        # first push


## GIT PUSH & PULL

git push origin main          # upload code
git fetch origin              # download changes only
git pull origin main          # download + merge


## BRANCH COMMANDS

git branch                    # list branches
git checkout <branch>         # switch branch
git checkout -b <branch>      # create & switch
git branch -d <branch>        # delete branch


## MERGING CODE

git diff <branch>             # compare branches
git merge <branch>            # merge branches

Pull Request:
- request to merge code using GitHub


## MERGE CONFLICTS

- Happens when Git cannot auto-merge changes
- Must be fixed manually, then commit


## GIT LOG & DIFF

git log                       # full history
git log --oneline             # short history
git log --graph --all         # branch graph

git diff                      # unstaged changes
git diff --staged             # staged changes


## UNDOING CHANGES

git reset <file>              # unstage file
git reset HEAD~1              # undo last commit
git reset --hard <hash>       # delete commits permanently

git checkout -- <file>        # discard local changes
git revert <hash>             # safe undo commit


## GIT STASH

git stash                     # save work temporarily
git stash apply               # restore stash
git stash pop                 # restore & delete


## FORK & UPSTREAM

- Fork = copy of repository
- Used in open-source projects

git remote add upstream <url> # add original repo
git fetch upstream            # get updates
git merge upstream/main       # sync fork


# ===============================
# DEVOPS MUST-KNOW GIT CONCEPTS
# ===============================

## GIT REBASE
Rewrites commit history to keep it clean (used before merging PRs).
git rebase main
git rebase -i HEAD~3


## GIT CHERRY-PICK
Apply a specific commit to another branch (used for hotfixes).
git cherry-pick <commit_hash>


## GIT TAGS (RELEASES)
Marks a specific commit as a release version.
git tag v1.0
git tag -a v1.1 -m "release"
git push --tags


## .gitignore
Prevents unwanted files from being tracked by Git.
Examples:
node_modules/
.env
*.log


## GIT HOOKS
Scripts that run automatically on git actions (pre-commit, pre-push).
Location:
.git/hooks/


## SHALLOW CLONE
Downloads only recent commit history (faster CI/CD).
git clone --depth=1 <repo_url>


## GIT SUBMODULE
Includes another repository inside a project.
git submodule add <repo_url>
git submodule update --init


## GIT CLEAN
Removes untracked files (used in CI/CD cleanup).
git clean -n   # preview
git clean -f   # delete


## DETACHED HEAD
Occurs when checking out commits or tags directly.
git checkout <commit_hash>


## GIT AUTHENTICATION (SSH)
Secure way to connect Git with servers.
ssh-keygen
ssh -T git@github.com


## IMPORTANT DEVOPS NOTES

- Rebase preferred over merge for clean history
- Tags are used for production releases
- Never push secrets (use .gitignore)
- Always pull before push
- git revert is safer than reset

## END OF FILE
