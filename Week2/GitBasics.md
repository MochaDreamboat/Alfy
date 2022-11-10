Initializing Git

1. input "git init" in command line
(optional: remove hidden directory with rm -rf .git ... careful)

2. create .gitignore file (filter out dependencies, logs, etc.)
    - Write filepaths of what you want ignored

Staging files
git add .

Unstaging files
git reset . (--hard flag also deletes file forever ... careful)

* Make many small commits
- Helps prevent catastrophic losses of code
- Makes code changes easier to follow

Commiting files
git commit -m "Insert message here"
(can be multiline)

Branching

Creating new branch
git checkout -b *branch name*

Saving changes w/out commit:
git stash -u Save
git stash pop Returns to changes

Merging branches
while in main branch i.e.:
git merge *branch you want to merge*

*Make sure to occasionally merge master branch into feature branch*

Merging branches when you have a lot of commits (but want to condense)
git merge *branch with a lot of commits* --squash

Connecting remote repo
git add origin *HTTP or SSH*
git push -u origin main