# Git Workflow Notes

## Goal

Document the Git concepts and workflows learned while developing the Weather Dashboard project.

---

## Git Basics

### Repository Status

Check the current state of the repository:

```bash
git status
```

Git reports whether files are:

| State | Meaning |
|---------|---------|
| Untracked | File has not been added to Git |
| Modified | File changed since last commit |
| Staged | Ready to be committed |

### Saving Changes

Stage and commit changes:

```bash
git add .
git commit -m "message"
```

Push commits to GitHub:

```bash
git push
```

### Updating Local Repository

Download the latest changes from GitHub:

```bash
git pull
```

---

## Branching Strategy

Feature development was performed on dedicated branches instead of directly on `main`.

Create a feature branch:

```bash
git checkout -b improve-ui
```

Benefits:

- Keeps the main branch stable
- Isolates experimental changes
- Simplifies code review and testing

---

## Merge Workflow

After completing UI improvements, the feature branch was merged into `main`.

### Merge Process

```bash
git checkout main
git pull origin main
git merge improve-ui
git push origin main
```

### Verification

Check repository status after merging:

```bash
git status
```

Expected output:

```text
On branch main
nothing to commit, working tree clean
```

---

## Commit Discipline

During this project, commits were grouped by logical changes.

Examples:

```text
feat: improve weather dashboard UI
docs: add setup guide
fix: resolve merge issue
```

Lessons learned:

- Keep commits focused on a single change
- Use descriptive commit messages
- Commit regularly rather than saving large batches of work

---

## Troubleshooting

### Vim Merge Editor

During a merge operation Git opened the Vim editor to confirm the merge commit message.

To complete the merge:

```text
Esc
:wq
Enter
```

This saves the default merge message and exits Vim.

### Lesson Learned

Git operations may invoke external tools such as Vim. Understanding basic editor commands helps avoid confusion during merges.

---

## Reflection

Key Git concepts practiced during this project:

- Git status and file tracking
- Staging and committing changes
- Pulling updates from GitHub
- Creating feature branches
- Merging branches into main
- Resolving merge confirmation prompts
- Writing meaningful commit messages

The project demonstrated how Git supports an organized and traceable development workflow, especially when working with AI-assisted code generation tools.
