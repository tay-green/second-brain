# Sample Skill Creation Requests

These are example inputs you can use to test the Skill Maker.

## Example 1: Product Demo Follow-up Email

**User Request:**
> "Create a skill that turns product demo notes into follow-up emails."

**Expected Behavior:**
- Ask clarifying questions about email tone, format, required sections
- Generate `demo-to-follow-up/` folder with skill.md, email template, sample notes
- Include validation for required email fields

---

## Example 2: API Documentation Generator

**User Request:**
> "I need a skill that generates API documentation from OpenAPI/Swagger files."

**Expected Behavior:**
- Ask about documentation format (Markdown, HTML, etc.)
- Ask about sections to include (examples, authentication, error codes)
- Generate skill with template for different endpoint types
- Include script to validate OpenAPI schema

---

## Example 3: Code Review Checklist

**User Request:**
> "Create a skill that generates code review checklists based on the programming language and project type."

**Expected Behavior:**
- Ask about programming languages to support
- Ask about project types (web app, library, CLI tool, etc.)
- Generate templates for different language-specific concerns
- Include examples for common scenarios

---

## Example 4: Meeting Notes to Action Items

**User Request:**
> "I want to extract action items from meeting notes and format them as Jira tickets."

**Expected Behavior:**
- Ask about meeting note structure
- Ask about required Jira fields (priority, assignee, labels, etc.)
- Generate Jira ticket template
- Include validation for required fields
- Add examples of different meeting note formats

---

## Testing Instructions

1. Copy one of the example requests above
2. Paste it into Claude Code with the Skill Maker skill active
3. Answer the clarifying questions
4. Verify the generated skill structure matches expectations
5. Run validation: `python scripts/validate.py <generated-skill-path>`
6. Test the generated skill with sample input
