# Sample Test Cases for GitHub PR Creator

## Test Case 1: Feature Branch with JIRA Ticket

**Input:**
```
Branch: feature/PM-1234-add-user-authentication
```

**Expected Behavior:**
- Extract JIRA ticket: PM-1234
- Analyze commits related to authentication
- Detect security/auth related files
- Fill template with authentication-specific content
- Suggest security testing in checklist
- Remind user to add screenshots of login flow

**Sample Git Setup:**
```bash
# To test this locally
git checkout -b feature/PM-1234-add-user-authentication
# Make some commits
git commit -m "PM-1234: Add login form component"
git commit -m "PM-1234: Implement JWT authentication"
git commit -m "PM-1234: Add password validation"
```

---

## Test Case 2: Bug Fix Branch

**Input:**
```
Branch: bugfix/PM-5678-fix-dashboard-crash
```

**Expected Behavior:**
- Extract JIRA ticket: PM-5678
- Focus on bug description and root cause
- Emphasize testing to prevent regression
- Suggest specific test scenarios
- Pre-check "Tests added/updated" if test files modified

**Sample Git Setup:**
```bash
git checkout -b bugfix/PM-5678-fix-dashboard-crash
git commit -m "PM-5678: Fix null pointer error in dashboard"
git commit -m "Add test case for dashboard error handling"
```

---

## Test Case 3: UI Changes (Screenshots Required)

**Input:**
```
Branch: feature/PM-9012-redesign-settings-page
```

**Expected Files Changed:**
- `settings.tsx`
- `settings.css`
- `components/SettingsForm.tsx`

**Expected Behavior:**
- Detect UI/styling files
- Create before/after table structure
- **Strongly** remind user to add screenshots
- Suggest which views to screenshot
- Pre-check "This change requires end-to-end testing"

---

## Test Case 4: Documentation Update

**Input:**
```
Branch: docs/PM-3456-update-api-documentation
```

**Expected Files Changed:**
- `README.md`
- `docs/api-guide.md`

**Expected Behavior:**
- Focus on documentation improvements
- Pre-check "Documentation added/updated"
- No screenshot reminder (unless examples shown)
- Simpler testing description

---

## Test Case 5: Branch Without JIRA Ticket

**Input:**
```
Branch: hotfix/fix-production-error
```

**Expected Behavior:**
- Warning: No JIRA ticket found
- Ask user to provide JIRA ticket
- Still fill out rest of template based on commits
- Include validation warning at top of output

---

## Test Case 6: Multiple Related Changes

**Input:**
```
Branch: feature/PM-7890-integrate-payment-gateway
```

**Expected Files Changed:**
- `payment/PaymentService.ts`
- `payment/StripeAdapter.ts`
- `checkout/CheckoutPage.tsx`
- `tests/payment.test.ts`

**Expected Behavior:**
- Comprehensive description covering multiple components
- Link to PM-7890
- Suggest payment flow testing scenarios
- Pre-check tests (test files found) and e2e testing
- Remind about screenshots of checkout flow

---

## Test Case 7: Refactoring (No User-Facing Changes)

**Input:**
```
Branch: refactor/PM-4567-optimize-data-fetching
```

**Expected Behavior:**
- Focus on technical improvements
- Explain performance benefits
- Mention metrics if available (from commits)
- May not need screenshots
- Pre-check "This change requires performance testing"

---

## Test Case 8: Base Branch Not Main

**Input:**
```
Branch: feature/PM-1111-new-dashboard
Base: develop
```

**Expected Behavior:**
- Compare against `develop` instead of `main`
- Use `git log origin/develop..HEAD`
- Note in description which branch this targets

---

## Testing the Skill

### Manual Test Process:

1. **Create a test branch:**
   ```bash
   cd ~/your-test-repo
   git checkout -b feature/TEST-123-sample-feature
   ```

2. **Make some commits:**
   ```bash
   echo "test" > test.txt
   git add test.txt
   git commit -m "TEST-123: Add test functionality"
   ```

3. **Activate the skill:**
   ```
   Create a PR for feature/TEST-123-sample-feature
   ```

4. **Verify output:**
   - Check that TEST-123 is extracted
   - Verify all template sections present
   - Confirm validation warnings if applicable
   - Test validation script on output

### Validation Test:

```bash
# Save generated PR description
echo "[generated content]" > test-pr.md

# Run validation
python ~/github-pr-creator/scripts/validate.py test-pr.md
```

---

## Edge Cases to Test

1. **Very long branch names**
2. **Special characters in branch name**
3. **No commits on branch** (just branched)
4. **Hundreds of files changed** (large refactor)
5. **Binary files changed** (images, etc.)
6. **Merge conflicts mentioned in commits**
7. **Multiple JIRA tickets** in commits
8. **WIP/draft commits** that need cleanup

---

## Expected Output Structure

Every generated PR should have:

```markdown
## ⚠️ Validation Warnings
[if any issues found]

---

# Description
[2-3 sentence summary based on commits]

## Motivation and Context
[Why this change, link to JIRA ticket]

## Video / Screenshots / Track
[Table structure or prompt to add media]

### Related GitHub PRs/Issues or JIRA Tickets
- [PM-1234](link)

## How Has This Been Tested?
[Suggested test scenarios]

## Checklist:
- [x] Tests added/updated
- [ ] Documentation added/updated
- [x] This change requires end-to-end testing
- [ ] This change requires performance testing.

---

## 📝 Auto-filled vs Manual
[Summary of what was automated vs needs user input]
```
