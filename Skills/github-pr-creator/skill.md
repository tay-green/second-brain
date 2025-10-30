---
name: github-pr-creator
description: >
  Automatically generates GitHub pull request descriptions based on a standard template.
  Takes a branch name as input and fills in PR details by analyzing git history and changes.
version: 1.0
author: Taylor Green
keywords: [github, pull-request, pr, git, automation, template]
---

# GitHub PR Creator

Automatically generate well-structured GitHub pull request descriptions using a standard template. This skill analyzes your git branch, commit history, and changes to intelligently fill out all required PR fields.

## Task

When the user provides a branch name, you will:

1. **Gather information** from the git repository
2. **Analyze the changes** to understand what was modified
3. **Fill out the PR template** with relevant details
4. **Validate** that all required fields are completed
5. **Output** a complete PR description ready to paste into GitHub

## Instructions

### Step 1: Gather Git Information

Given the branch name, collect the following:
- Branch name and base branch (usually `main` or `develop`)
- All commits on this branch (commit messages and descriptions)
- Files changed in this branch
- Diff summary (additions/deletions)

Use git commands:
```bash
# Get current branch info
git branch --show-current
git log origin/main..HEAD --oneline

# Get commit messages
git log origin/main..HEAD --format="%s%n%b"

# Get changed files
git diff origin/main..HEAD --name-only

# Get diff stats
git diff origin/main..HEAD --stat
```

### Step 2: Extract Context

From the gathered information, identify:
- **JIRA ticket(s)**: Look for patterns like `PROJ-1234` in branch name or commit messages
- **Type of change**: Bug fix, feature, refactor, documentation, etc.
- **Affected components**: Which parts of the codebase were modified
- **Related PRs/issues**: Any references in commit messages

### Step 3: Fill Out the Template

Use the PR template from `./templates/pr-template.md` and populate:

**Description Section:**
- Summarize what was changed in 2-3 sentences
- If commits have detailed messages, extract key points
- Be specific about functionality added/modified

**Motivation and Context:**
- Explain WHY this change was needed
- Reference the JIRA ticket or GitHub issue if found
- Describe the problem being solved

**Video / Screenshots / Track:**
- List the files/components that should be demonstrated
- Suggest what screenshots or videos would be helpful
- If UI changes detected, create a before/after table structure
- **IMPORTANT**: Remind the user to add at least one image or video

**Related GitHub PRs/Issues or JIRA Tickets:**
- Auto-link any JIRA tickets found (format: `[PROJ-1234](https://your-jira.atlassian.net/browse/PROJ-1234)`)
- Link any referenced GitHub issues or PRs
- **IMPORTANT**: If no ticket found, alert the user that this is required

**How Has This Been Tested:**
- Suggest test scenarios based on the type of change
- Mention relevant test files if they were modified
- Prompt user to describe their manual testing

**Checklist:**
- Pre-check items that likely apply based on the changes
- Flag if documentation files were modified (check documentation box)
- Flag if test files were added/modified (check tests box)

### Step 4: Validate Required Fields

Before outputting, ensure:
- ✅ At least one JIRA ticket is linked (if not found, warn the user)
- ✅ Description is filled with specific details (not just "updated code")
- ✅ Motivation section explains the "why"
- ✅ User is reminded to add screenshots/video
- ✅ Testing section has guidance
- ✅ All checklist items are addressed

If any validations fail, include a warning at the top of the output.

### Step 5: Output Format

Present the completed PR description in a markdown code block with:
1. Any validation warnings at the top
2. The complete filled-out template
3. A summary of what was auto-filled vs. what needs manual input

## Input Format

**Minimal input:**
```
Branch name: feature/PROJ-123-add-user-auth
```

**Alternative inputs:**
```
Branch: bugfix/PROJ-456-fix-login
Base branch: develop
```

```
Create PR for feature/PROJ-789-update-dashboard
```

## Output Format

The output should be:

```markdown
## ⚠️ Validation Warnings (if any)
- [ ] No JIRA ticket found - please add one
- [ ] Remember to add screenshots or video

---

# Pull Request Description

[Complete filled template here]

---

## 📝 Auto-filled vs Manual
✅ Auto-filled:
- Description (based on commits)
- JIRA ticket (PROJ-123)
- Changed files list

⚠️ Needs your input:
- Screenshots/video
- Manual testing details
- Performance testing requirements
```

## Rules and Constraints

1. **Always use the template** from `./templates/pr-template.md` - do not deviate from the structure
2. **Be specific**: Avoid generic descriptions like "updated code" or "fixed bug"
3. **Extract from commits**: Use actual commit messages to inform the description
4. **Validate tickets**: JIRA ticket format is typically `[A-Z]+-[0-9]+`
5. **Flag missing media**: Always remind user to add screenshots/video if not present
6. **Check all fields**: Ensure every section has meaningful content or a prompt for the user
7. **Preserve formatting**: Keep the exact markdown structure from the template
8. **Smart defaults**: Pre-check checklist items based on file changes (tests, docs, etc.)

## Templates

The PR template structure is defined in: `./templates/pr-template.md`

## Examples

### Example 1: Feature Branch

**Input:**
```
Branch: feature/PM-1234-add-dark-mode
```

**Process:**
1. Run `git log origin/main..HEAD` → finds 5 commits about dark mode
2. Run `git diff --name-only` → finds CSS files, theme files, settings page
3. Extract JIRA ticket: PM-1234
4. Generate description from commits
5. Check UI files changed → prompt for screenshots
6. Validate JIRA ticket found ✅

**Output:**
Complete PR description with:
- Description: "Added dark mode support including theme switcher, persistent user preference, and updated all UI components"
- Motivation: Links to PM-1234
- Screenshots prompt with before/after table
- Checklist with "Tests added" pre-checked (test files found)

### Example 2: Bug Fix Branch

**Input:**
```
Branch: bugfix/PM-5678-fix-login-error
```

**Process:**
1. Analyze commits → "Fixed authentication timeout issue"
2. Check changed files → auth.ts, login.tsx
3. Extract JIRA: PM-5678
4. Generate bug fix description
5. Suggest test scenarios

**Output:**
PR description focused on the bug, root cause, and fix with appropriate testing guidance.

## Clarifying Questions

If information is unclear, ask:
1. "I couldn't find a JIRA ticket in the branch name or commits. What ticket should this PR link to?"
2. "Should I compare against `main` or a different base branch?"
3. "I see UI changes - do you have screenshots or a video ready to add?"

## Validation Script

Run `python ./scripts/validate.py <pr-description.md>` to validate the generated PR description before submitting.

## Tips

- **Branch naming helps**: Use format like `feature/TICKET-123-short-description` for best results
- **Commit messages matter**: Detailed commit messages = better PR descriptions
- **Review before posting**: Always review the generated description and add your manual testing details
- **Screenshots are required**: Don't skip the visual documentation
- **Link everything**: Connect your PR to tickets, related PRs, and documentation

## Trigger Phrases

This skill activates when you say:
- "Create a PR for [branch-name]"
- "Generate PR description for [branch]"
- "Make a pull request for [branch-name]"
- "Fill out PR template for [branch]"
