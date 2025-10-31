# GitHub PR Creator

Automatically generate comprehensive, well-structured GitHub pull request descriptions from your branch name and git history.

## 🎯 Purpose

Stop spending time manually filling out PR templates! This skill:
- ✅ Extracts JIRA tickets from branch names
- ✅ Analyzes your git commits and changes
- ✅ Fills out your PR template automatically
- ✅ Validates all required fields
- ✅ Ensures quality standards (screenshots, testing, etc.)

## 📦 What's Included

```
github-pr-creator/
├── skill.md                    # Main skill definition
├── README.md                   # This file
├── templates/
│   └── pr-template.md         # Your team's PR template
├── scripts/
│   └── validate.py            # Validation script
└── tests/
    └── sample_input.md        # Test cases and examples
```

## 🚀 Quick Start

### 1. Upload to Claude Code

- Open Claude Code
- Add this skill (Skills → Add Skill → Select `github-pr-creator` folder)

### 2. Create a PR

Simply provide your branch name:

```
Create a PR for feature/PM-1234-add-dark-mode
```

Or:

```
Generate PR description for bugfix/PM-5678-fix-login
```

### 3. Review and Use

Claude will:
1. Analyze your git history
2. Extract the JIRA ticket (PM-1234)
3. Fill out the entire PR template
4. Validate all required fields
5. Give you a ready-to-paste PR description

## 💡 Usage Examples

### Example 1: Feature Branch

**You say:**
```
Create a PR for feature/PM-1234-add-user-authentication
```

**Claude does:**
1. Runs `git log origin/main..HEAD` to see commits
2. Finds commits like "PM-1234: Add login form", "PM-1234: Add JWT auth"
3. Extracts PM-1234 from branch name
4. Generates description: "Added user authentication system with JWT tokens, login form, and session management"
5. Links to JIRA ticket
6. Reminds you to add screenshots of login flow
7. Pre-checks "Tests added" (found test files)

**You get:**
A complete PR description ready to copy-paste into GitHub!

### Example 2: Bug Fix

**You say:**
```
Generate PR for bugfix/PM-5678-fix-dashboard-crash
```

**Claude does:**
1. Analyzes bug fix commits
2. Focuses description on the bug and root cause
3. Links PM-5678
4. Suggests regression testing
5. Pre-checks relevant checklist items

### Example 3: UI Changes

**You say:**
```
Make a PR for feature/PM-9012-redesign-settings
```

**Claude detects:**
- UI files changed (`.tsx`, `.css`)
- Creates before/after table structure
- **Strongly** reminds you to add screenshots
- Pre-checks "E2E testing required"

## 🔧 How It Works

### Information Gathering

The skill runs git commands to gather:
- Branch name and commits
- Changed files
- Commit messages
- Diff statistics

### Smart Analysis

It intelligently:
- Extracts JIRA tickets (format: `PROJ-1234`)
- Identifies change type (feature, bugfix, refactor)
- Detects UI changes (CSS, component files)
- Finds test files
- Spots documentation updates

### Template Filling

Uses your exact template from `templates/pr-template.md` and fills:
- **Description**: Based on commit messages
- **Motivation**: Links to JIRA, explains the "why"
- **Screenshots**: Prompts for required media
- **Testing**: Suggests relevant test scenarios
- **Checklist**: Pre-checks items based on file changes

### Validation

Ensures:
- ✅ JIRA ticket is present
- ✅ All sections filled
- ✅ Screenshots/video reminded
- ✅ Quality standards met

## 📋 Required Input

**Minimum:**
- Branch name

**Optional:**
- Base branch (defaults to `main`)
- Additional context

## 🎨 Customization

### Update PR Template

Edit `templates/pr-template.md` to match your team's format.

### Adjust JIRA Pattern

If your JIRA uses different format, edit `skill.md`:
```markdown
JIRA ticket format is typically `[A-Z]+-[0-9]+`
```

Change to your pattern (e.g., `[0-9]+` for numeric-only).

### Modify Validation Rules

Edit `scripts/validate.py` to add/remove validation checks.

## ✅ Validation

After generating a PR description, validate it:

```bash
# Save the generated description
pbpaste > my-pr.md

# Validate
python ~/github-pr-creator/scripts/validate.py my-pr.md
```

The script checks:
- ✅ JIRA ticket present
- ✅ All sections filled
- ✅ Media content mentioned
- ✅ No generic placeholders
- ⚠️  Warnings for improvements

## 🎯 Best Practices

### 1. Good Branch Names

✅ **Good:**
- `feature/PM-1234-add-dark-mode`
- `bugfix/PM-5678-fix-login-error`
- `refactor/PM-9012-optimize-queries`

❌ **Avoid:**
- `feature/new-stuff`
- `fix`
- `updates`

### 2. Meaningful Commits

✅ **Good:**
```
PM-1234: Add dark mode toggle component
PM-1234: Implement theme persistence
PM-1234: Update color palette for dark theme
```

❌ **Avoid:**
```
wip
fixes
updates
```

### 3. Always Review

- Review generated description
- Add your manual testing details
- Upload screenshots/video
- Check all checklist items

## 📊 What Gets Auto-Filled vs Manual

### ✅ Auto-Filled:
- Description summary (from commits)
- JIRA ticket links
- Motivation/context (from commits)
- File change analysis
- Smart checklist pre-checking

### ⚠️ Needs Your Input:
- Screenshots/videos (you must upload)
- Detailed manual testing steps
- Performance testing results
- Any special considerations

## 🔍 Troubleshooting

### "No JIRA ticket found"

- Ensure branch name includes ticket: `feature/PROJ-123-description`
- Or include in first commit: `PROJ-123: Add feature`
- You can manually add it to the generated PR

### "Description seems empty"

- Make sure you have commits on your branch
- Write more detailed commit messages
- Provide additional context when invoking

### "Can't find base branch"

Specify explicitly:
```
Create PR for my-branch against develop
```

## 🧪 Testing

See `tests/sample_input.md` for comprehensive test cases including:
- Feature branches
- Bug fixes
- UI changes
- Documentation updates
- Edge cases

## 🤝 Contributing

Found a bug or have improvements?
1. Update the skill files
2. Test thoroughly
3. Share with your team

## 📝 Template Format

Your PR template is stored in `templates/pr-template.md`. The skill preserves:
- All markdown formatting
- HTML comments
- Table structures
- Checklist format

## 🔗 Integration

Works with:
- ✅ Git repositories
- ✅ GitHub
- ✅ JIRA ticket systems
- ✅ Claude Code
- ✅ Any markdown-based PR template

## 📄 License

Free to use and modify for your team's needs.

---

**Made with ❤️ for efficient PR creation**

Save time, maintain quality, ship faster! 🚀
