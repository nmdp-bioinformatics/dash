## FORK METHOD
Note: master might be main

1. Log into Github web interface with your username-nmdp account

2. Browse to the repo at https://github.com/nmdp-bioinformatics/project, hit the Fork button

3. Copy the clone URL from the Github web page for the fork (something like https://github.com/username-nmdp/project.git)

4. Clone the fork

```
$ git clone https://github.com/username-nmdp/graph-imputation-match.git
$ cd graph-imputation-match
```

5. Add upstream as remote

`$ git remote add upstream https://github.com/nmdp-bioinformatics/graph-imputation-match`

6. Pull and merge latest changes from upstream master to your local master branch

`$ git checkout master`

make sure my fork (origin) master is up-to-date with upstream master

`$ git pull upstream master`

(if you forget you will have merge conflicts)

`$ git push`
(or more explicit)

`$ git push origin master`

7. Create a new local feature branch

`$ git checkout -b reorg-match`

8. Edit files locally

Commit changes to local feature branch
(get any updates that have occurred to upstream in the meantime)

```
$ git pull upstream master
$ git commit -m "made changes”
```

9. Push changes from local feature branch to remote feature branch on your fork

`$ git push origin reorg-match`

11. Browse to the Github web page for your fork repo (something like https://github.com/username-nmdp/graph-imputation-match) and hit the new pull request button

12. Edit the pull request description and hit save (or create or new, I can't remember) button

13. Other contributors will review the changes in the pull request

14. When the pull request looks good, it is merged into the upstream repo

15. Hit the delete branch button to delete your remote feature branch (the commits have been merge upstream, so it is no longer necessary)

16. Delete your local feature branch

`$ git branch -d new-feature-branch`
