# Skill Maker (create-skill)

A meta-skill for Claude Code that generates new Claude Skills from natural-language descriptions.

## 🎯 Purpose

Instead of manually writing `skill.md` files, folder structures, and templates, just describe what you want your skill to do in plain language. The Skill Maker will:

1. Ask clarifying questions to understand your needs
2. Generate a complete skill folder with proper structure
3. Create templates, validation scripts, and documentation
4. Package everything for easy upload to Claude

## 📦 What You Get

When you use this skill, it generates a complete skill package:

```
your-new-skill/
├── skill.md              # Claude Skill definition with YAML metadata
├── templates/            # Example templates and boilerplate
│   └── example.md
├── scripts/              # Python validation and helper scripts
│   └── validate.py
├── tests/                # Sample inputs and test cases
│   └── sample_input.md
└── README.md             # Usage guide and documentation
```

## 🚀 Quick Start

### 1. Upload to Claude Code

Upload the entire `create-skill/` folder to Claude Code as a skill:

- Open Claude Code
- Click "Skills" → "Add Skill"
- Select the `create-skill` folder
- Confirm upload

### 2. Activate the Skill

In Claude Code, type:
```
Use the create-skill skill to build me a new skill that [describe what you want]
```

### 3. Answer Questions

The Skill Maker will ask 5-7 clarifying questions like:
- What's the skill's name and purpose?
- What input does it expect?
- What output should it produce?
- Does it need templates or validation?

### 4. Get Your Skill

You'll receive:
- Complete folder structure
- All necessary files populated
- Validation script to check correctness
- Ready-to-upload .zip file (optional)

## 💡 Examples

### Example 1: Email Generator

**You say:**
> "Create a skill that turns product demo notes into follow-up emails."

**Skill Maker does:**
1. Asks about email tone, required sections, note format
2. Generates `demo-to-follow-up/` folder
3. Creates email template with placeholders
4. Adds sample demo notes for testing
5. Includes README with examples

### Example 2: Code Documentation

**You say:**
> "I need a skill that generates API docs from OpenAPI specs."

**Skill Maker does:**
1. Asks about output format (Markdown, HTML)
2. Asks what sections to include
3. Generates `openapi-to-docs/` folder
4. Creates templates for endpoints, auth, errors
5. Adds OpenAPI validation script

### Example 3: Custom Workflow

**You say:**
> "Build a skill that converts Figma design feedback into GitHub issues."

**Skill Maker does:**
1. Asks about feedback format and GitHub fields
2. Generates `figma-to-github/` folder
3. Creates GitHub issue template
4. Adds validation for required fields
5. Includes examples of different feedback types

## 🔧 Advanced Usage

### Validating Generated Skills

After generating a skill, validate it:

```bash
python scripts/validate.py path/to/your-new-skill
```

This checks:
- ✅ skill.md exists with valid YAML frontmatter
- ✅ Required metadata fields (name, description, version)
- ⚠️  Recommended files (README.md, templates/)

### Customizing Generated Skills

All generated skills are fully editable:

1. Open the generated `skill.md` file
2. Modify instructions, add examples, refine prompts
3. Update templates in `templates/` folder
4. Add or modify validation scripts
5. Re-run validation to ensure structure is still valid

### Packaging for Distribution

Create a .zip for easy sharing:

```bash
cd your-new-skill
zip -r ../my-skill.zip .
```

Then share `my-skill.zip` with others or upload to Claude.

## 📋 Skill Structure Reference

### skill.md Format

```markdown
---
name: skill-slug
description: >
  Clear description of what the skill does.
version: 1.0
author: Your Name
keywords: [relevant, keywords]
---

# Skill Name

Instructions in natural language...
```

### Best Practices

1. **Use natural language**: Claude Skills don't need rigid syntax
2. **Include examples**: Show input/output pairs
3. **Add templates**: Provide boilerplate for common outputs
4. **Validate inputs**: Use scripts to catch common mistakes
5. **Document thoroughly**: Good READMEs help users understand usage

## 🛠️ Customization

### Modify Default Questions

Edit `skill.md` (Step 1) to change the clarifying questions asked.

### Add New Template Types

Add files to `templates/` for different skill patterns:
- `skill-template-api.md` - For API integration skills
- `skill-template-doc.md` - For documentation skills
- `skill-template-transform.md` - For data transformation skills

### Extend Validation

Edit `scripts/validate.py` to add:
- Custom YAML field checks
- Template validation
- Output format verification
- Integration tests

## 📚 Resources

- [Claude Skills Documentation](https://docs.anthropic.com/claude/docs/skills) (Anthropic)
- [YAML Specification](https://yaml.org/spec/) (for metadata)
- [Markdown Guide](https://www.markdownguide.org/) (for skill.md formatting)

## 🤝 Contributing

Found a bug or have a suggestion? You can:
1. Modify the skill to fit your needs
2. Share improved versions with the community
3. Create variants for specialized use cases

## 📄 License

This skill is provided as-is for use with Claude Code. Modify and distribute freely.

---

**Made with ❤️ for the Claude Skills community**
