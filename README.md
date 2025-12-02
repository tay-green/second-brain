# Second Brain 🧠

A personal knowledge management system combining GTD (Getting Things Done) methodology with design inspiration resources and a Next.js web interface.

## 📁 Structure

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

## 🚀 Getting Started

### For GTD Workflow

1. Start by capturing tasks in `gtd/INBOX.md`
2. Process inbox daily - move items to appropriate lists
3. Check `gtd/NEXT.md` for actionable tasks by context
4. Use `gtd/WEEKLY.md` for weekly reviews
5. Track project-specific work in `gtd/projects/`

### For Design Inspiration

Browse `/design-inspo/` folders to find reference materials organized by category. Each item includes screenshots and markdown notes.

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

1. **Capture** → Everything goes into INBOX.md
2. **Clarify** → Process inbox items daily
3. **Organize** → Move to NEXT, SOMEDAY, WAITING, or project files
4. **Reflect** → Weekly/monthly/quarterly reviews
5. **Engage** → Work from NEXT.md based on context and priority

## 📄 License

Private repository for personal use.
