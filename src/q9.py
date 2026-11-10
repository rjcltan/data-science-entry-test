"""
Question 9 — GitHub: Git Workflow  [Short Answer]

This is the same workflow you used to SUBMIT this assessment, so you have
already done most of it. Write the exact git command for each step.

Scenario
--------
You have a local copy of a repo. You want to:
1. Create a new branch called `my-solutions`.
2. Switch to that branch.
3. After editing `q4.md`, stage that file for commit.
4. Commit the staged change with the message "Add Q4 answers".
5. Push the `my-solutions` branch to GitHub.

Write the exact git command for each step (one per line).
"""

# Step 1 — Create a new branch called `my-solutions`:
# git branch my-solutions

# Step 2 — Switch to `my-solutions`:
# git switch my-solutions
#   (older equivalent: git checkout my-solutions;
#    steps 1 and 2 together: git checkout -b my-solutions)

# Step 3 — Stage q4.md:
# git add src/q4.md
#   (path is relative to where I run it; inside src/ it is just: git add q4.md)

# Step 4 — Commit with message "Add Q4 answers":
# git commit -m "Add Q4 answers"

# Step 5 — Push `my-solutions` to the remote:
# git push -u origin my-solutions
#   (-u sets origin/my-solutions as the upstream, so later a plain `git push` works)


"""
Step 6 (short answer). You run `git status` and it says
`Changes not staged for commit`. In one sentence, what does that tell you,
and which command moves a file from there into the next commit?

    Answer: It means I have edited tracked files but have not staged those
    edits yet, so they will NOT be included if I commit now; running
    `git add <file>` (e.g. `git add src/q4.md`) stages the file so it goes
    into the next commit.
"""
