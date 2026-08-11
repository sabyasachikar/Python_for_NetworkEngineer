# Solution: work on a branch

```bash
# 1: create and switch to the branch
git checkout -b add-readme

# 2: create README.md (in VS Code or from the terminal), for example:
#   # Python for Network Engineers
#   My working repository for the Python for Network Engineers course.

# 3: stage and commit on the branch
git add README.md
git commit -m "Add project README"

# 4: push the branch to GitHub
git push -u origin add-readme
```

On GitHub you will see a prompt to open a pull request for the `add-readme` branch.
Open it, review the change, and click Merge. Then bring the merged result back to
your machine:

```bash
# 6: return to main and pull the merged change
git checkout main
git pull
```

What the branch gave you: you built and pushed the README without ever touching the
working `main` branch. If the change had been wrong, `main` would have stayed clean
and you could have deleted the branch. On a team, this is how people work on the same
repository at the same time without stepping on each other, and the pull request is
where a change gets reviewed before it becomes part of main.
