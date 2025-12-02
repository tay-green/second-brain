# Second Brain 🧠

A comprehensive personal knowledge repository—literally a digital extension of my brain. This is where I capture, organize, and retrieve everything: design inspiration, acquired knowledge, articles, GTD tasks, and custom automation workflows.

**Think of it as:** A searchable, organized dump of everything in my head that I want to reference, build upon, or never forget.

## 📁 Structure

### `/.claude/skills/`
Custom Claude Skills for automation and workflows:

- **save-inspo** - Automatically save design inspiration (images, videos, URLs, screenshots) to the repo with intelligent categorization, tagging, and GitHub sync
- **create-skill** - Meta-skill that generates new Claude Skills from plain-language descriptions
- **github-pr-creator** - Auto-generate GitHub PR descriptions by analyzing git history and changes

Each skill includes comprehensive instructions, templates, validation scripts, and examples.

### `/gtd/`
Getting Things Done (GTD) workflow management system:

- **INBOX.md** - Capture everything here, process daily
- **NEXT.md** - Actionable tasks organized by context (@computer-work, @email-work, @phone-calls, etc.)
- **SOMEDAY.md** - Future ideas and projects not actionable right now
- **WAITING.md** - Tasks blocked on others
- **WEEKLY.md** - Weekly review checklist and planning
- **MONTHLY.md** - Monthly accomplishments and goals
- **QUARTERLY.md** - Quarterly strategic review
- **projects/** - Individual project folders with dedicated NEXT.md and PROJECT-PLAN.md files

### `/design-inspo/`
Curated design inspiration and reference library:

- **layouts/** - Layout patterns and structures (e.g., Replit agent interfaces)
- **ui-components/** - Component designs and variants (e.g., AI task progress cards, pill buttons)
- **ux-writing/** - Writing examples and patterns
- **animations/** - Animation references
- **color-palettes/** - Color scheme inspiration
- **patterns/** - Design patterns and interactions
- **typography/** - Typography examples

### `/app/`
Next.js 14 application (App Router) for potential web interface.

## 🧑‍💻 What Goes Here?

Anything and everything:
- 🎨 **Design inspiration** I find on the web (layouts, UI components, interactions)
- 📝 **Notes and knowledge** I acquire (articles, learnings, documentation)
- ✅ **Tasks and projects** (GTD workflow for managing my life)
- 🤖 **Automation workflows** (Claude Skills to streamline repetitive tasks)
- 📊 **Ideas and concepts** I want to remember and build upon

If it's worth keeping, it goes here.

## 🚀 Getting Started

### For GTD Workflow

1. Start by capturing tasks in `gtd/INBOX.md`
2. Process inbox daily - move items to appropriate lists
3. Check `gtd/NEXT.md` for actionable tasks by context
4. Use `gtd/WEEKLY.md` for weekly reviews
5. Track project-specific work in `gtd/projects/`

### For Design Inspiration

Browse `/design-inspo/` folders to find reference materials organized by category. Each item includes screenshots and markdown notes.

### For Claude Skills

Run skills directly through Claude by referencing them:
```
Save this to my inspo: https://dribbble.com/shots/example
```

Or create new skills:
```
Create a skill that [description]
```

### For Web Interface (Optional)

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the app.

## 🛠️ Tech Stack

- **Next.js 14** (App Router)
- **React 18**
- **TypeScript**

## 📝 Task Format

Tasks in GTD files follow this format:
```markdown
- [ ] Task description [P1-P4] [duration] @context
```

- **P1-P4**: Priority level
- **duration**: Estimated time (e.g., 15m, 1h, 2h)
- **@context**: Where/how the task can be done

## 🔄 Workflow

1. **Capture** → Everything goes into INBOX.md or gets saved via skills
2. **Clarify** → Process inbox items daily
3. **Organize** → Move to NEXT, SOMEDAY, WAITING, or project files
4. **Reflect** → Weekly/monthly/quarterly reviews
5. **Engage** → Work from NEXT.md based on context and priority
6. **Reference** → Search design-inspo, notes, and knowledge as needed

## 🧠 Philosophy

Your brain is for having ideas, not storing them. This repository offloads the burden of remembering everything so I can focus on creating, connecting ideas, and taking action.

**It's a living system** that grows with me—new skills, new knowledge, new projects, all interconnected and retrievable.

## 📄 License

Private repository for personal use.
