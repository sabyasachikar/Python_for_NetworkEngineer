# Solution: make a second commit

With the virtual environment active and inside the project folder:

```bash
# 2 and 3: install rich and record it
pip install rich

# edit requirements.txt so it now contains:
#   ipython
#   rich
# (open it in VS Code, add the line, save)

# 4: stage and commit only the requirements change
git add requirements.txt
git commit -m "Add rich to project requirements"

# 5: push and check GitHub
git push
```

A cleaner way to record what is installed, instead of editing the file by hand, is:

```bash
pip freeze > requirements.txt
```

That writes the exact versions of everything installed. Early in the course either
approach is fine. Later, when versions matter, `pip freeze` is the reliable one.

Confirm on your GitHub repository page that `requirements.txt` now lists rich and
that your second commit message appears in the history.
