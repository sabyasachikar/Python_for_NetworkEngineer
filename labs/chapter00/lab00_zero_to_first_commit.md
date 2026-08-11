# Lab 0.1: From Zero to First Commit

This lab sets up your whole working environment and proves it end to end. You do it
once. Everything else in the course runs inside what you build here.

## Objective

Go from a fresh machine to code pushed on GitHub: Python installed, a virtual
environment active, Git configured, and your first commit visible online.

## Network scenario

You are joining a team that keeps all of its automation in GitHub. Before you can
contribute a single script, your machine has to be set up and your first commit has
to land in a repository.

## Prerequisites

A computer running Windows, macOS, or Linux, administrator rights to install
software, and internet access.

## Files required

None to start. During the lab you create `requirements.txt` and `.gitignore`, and
you run `scripts/chapter00/check_setup.py`.

## Steps

1. Install Python 3.14 for your operating system. Confirm with `python --version`
   (Windows) or `python3 --version` (macOS and Linux).
2. Upgrade pip: `python -m pip install --upgrade pip`.
3. Create the project folder and virtual environment, then activate it:
   - Windows: `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
   - macOS and Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
   Confirm your prompt shows `(.venv)`.
4. Install IPython (`pip install ipython`), start it, and run the short session from
   Chapter 0 Part D. Type `exit` to leave.
5. Install VS Code and the Microsoft Python extension.
6. Create a GitHub account and turn on two-factor authentication.
7. Install Git, then set `user.name`, `user.email`, and `init.defaultBranch main`.
8. Create `requirements.txt` (one line: `ipython`) and `.gitignore` (`.venv/`,
   `__pycache__/`, `.env`). Then `git init`, `git add .`, `git commit -m "Initial
   commit: course project setup"`.
9. Create the empty GitHub repository named `python-for-network-engineers`, add it as
   `origin`, and `git push -u origin main`. Authenticate with a personal access
   token, not your password.
10. Put `check_setup.py` in `scripts/chapter00/` and run it.

## Expected output

`check_setup.py` prints your version, OS, interpreter path, and a line saying your
Python is new enough. Your GitHub page shows `requirements.txt`, `.gitignore`, and
your first commit message.

## Verification

You are done when your prompt shows `(.venv)` while active, `check_setup.py` reports
your Python is new enough, and your files appear on GitHub.

## Common errors

See the Common Errors section in Chapter 0. The frequent ones are the missing "Add
to PATH" checkbox on Windows, the PowerShell execution policy blocking activation,
using `python` instead of `python3` on macOS and Linux, and trying to push with your
password instead of a token.

## Student exercise

See `exercise_second_commit.md` in this folder.

## Challenge lab

See `challenge_branch_and_readme.md` in this folder.

## Solutions

In `solutions/chapter00/`. Try the exercise and challenge yourself before opening them.
