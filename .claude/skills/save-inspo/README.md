# Design Inspo Saver

A Claude Code skill for quickly saving design inspiration to your GitHub repository with automatic categorization, tagging, and indexing.

## Overview

This skill helps you build a searchable, well-organized collection of design inspiration by:
- Accepting various input types (URLs, images, videos, screenshots)
- Auto-suggesting categories based on content analysis
- Generating relevant tags for easy filtering
- Creating structured metadata for each item
- Maintaining a central index for future querying (perfect for building a FE app later!)
- Auto-committing to your GitHub repo

## Installation

This skill is project-scoped and lives in `.claude/skills/design-inspo-saver/`.

**To use it:**
1. Ensure it's in your repo's `.claude/skills/` directory
2. Restart Claude Code to load the skill
3. Start saving inspiration!

## Usage

### Quick Save (Minimal Input)

Just provide a URL and let the skill handle the rest:

```
Save to inspo: https://dribbble.com/shots/12345
```

The skill will:
- Download or screenshot the content
- Suggest a category
- Ask for tags
- Save everything with metadata
- Commit and push

### Detailed Save (Full Control)

Provide all details upfront:

```
Add to inspo: https://linear.app
Category: Product Design
Tags: saas, minimalist, project-management
Notes: Love the command palette interaction
```

### Supported Input Types

- **Direct image URLs**: `.png`, `.jpg`, `.gif`, `.webp`, etc.
- **Video URLs**: `.mp4`, `.mov`, etc.
- **Web page URLs**: Any website (will screenshot or save URL)
- **Local files**: Paths to existing files on your machine
- **Screenshots**: From clipboard or temp locations

## File Structure

```
Inspo/
├── Product Design/
│   ├── 2024-10-30-dashboard-analytics.png
│   ├── 2024-10-30-dashboard-analytics.meta.json
│   ├── 2024-10-30-linear-homepage.png
│   └── 2024-10-30-linear-homepage.meta.json
├── Motion Design/
│   ├── 2024-10-30-loading-animation.gif
│   └── 2024-10-30-loading-animation.meta.json
└── index.json
```

### Metadata File Structure

Each saved item gets a `.meta.json` file:

```json
{
  "filename": "2024-10-30-dashboard-analytics.png",
  "category": "Product Design",
  "source_url": "https://dribbble.com/shots/12345",
  "saved_date": "2024-10-30T14:23:45Z",
  "media_type": "image",
  "tags": ["dashboard", "analytics", "dark-mode", "charts"],
  "notes": "Great use of data visualization"
}
```

### Central Index

The `Inspo/index.json` file maintains a queryable index of all saved items:

```json
{
  "last_updated": "2024-10-30T14:23:45Z",
  "total_items": 42,
  "items": [
    {
      "id": "1698675825000",
      "filename": "2024-10-30-dashboard-analytics.png",
      "path": "Inspo/Product Design/2024-10-30-dashboard-analytics.png",
      "category": "Product Design",
      "source_url": "https://dribbble.com/shots/12345",
      "saved_date": "2024-10-30T14:23:45Z",
      "media_type": "image",
      "tags": ["dashboard", "analytics", "dark-mode", "charts"],
      "thumbnail": null
    }
  ]
}
```

This structure makes it easy to:
- Query by category, tags, or date
- Build a searchable frontend app
- Generate galleries or collections
- Export to other formats

## Categories

The skill auto-suggests categories based on content analysis. Common categories include:

- Product Design
- Marketing Sites
- Mobile Apps
- Web Apps
- UI Patterns
- Illustrations
- Branding
- Typography
- Photography
- Motion Design
- 3D Design

You can always specify your own custom category.

## Tags

Tags are generated in these groups:

### 1. Media Type (auto-detected)
- image, video, gif, screenshot, webpage

### 2. App/Website Type (auto-suggested)
- saas-dashboard, e-commerce, portfolio, landing-page, mobile-app, marketing-site, admin-panel

### 3. Design Style Tags
- **Visual style**: minimalist, brutalist, glassmorphism, neumorphism, dark-mode, gradient
- **Interaction**: hover-effect, scroll-animation, micro-interaction, parallax
- **UI elements**: card-layout, sidebar, navigation, modal, form, button, dashboard
- **Color**: colorful, monochrome, pastel, vibrant, blue, purple
- **Industry**: fintech, healthcare, education, social, productivity

## Examples

### Example 1: Save a Dribbble Shot

**Input:**
```
Save to inspo: https://dribbble.com/shots/12345-analytics-dashboard
```

**What happens:**
1. Skill downloads the image
2. Suggests category: "Product Design"
3. Asks: "Add tags (e.g., dashboard, analytics, charts):"
4. You provide: "dashboard, dark-mode, charts"
5. Saves to: `Inspo/Product Design/2024-10-30-analytics-dashboard.png`
6. Creates metadata file
7. Updates index.json
8. Commits with message: `Add design inspo: Product Design - dashboard, dark-mode`
9. Pushes to GitHub

### Example 2: Screenshot a Marketing Site

**Input:**
```
Add to inspo: https://stripe.com
Category: Marketing Sites
Tags: fintech, clean, professional, gradient
```

**What happens:**
1. Takes screenshot of Stripe homepage
2. Uses your specified category
3. Uses your tags + auto-detected "webpage"
4. Saves to: `Inspo/Marketing Sites/2024-10-30-stripe-homepage.png`
5. Creates metadata
6. Updates index
7. Commits and pushes

### Example 3: Save a Local Screenshot

**Input:**
```
Save inspo: ~/Downloads/figma-export-modal.png
Category: UI Patterns
Tags: modal, glassmorphism, overlay
Notes: Perfect example of depth and hierarchy
```

**What happens:**
1. Copies file from your Downloads
2. Uses specified category and tags
3. Includes your notes in metadata
4. Saves to: `Inspo/UI Patterns/2024-10-30-figma-export-modal.png`
5. Commits and pushes

## Future Frontend App

The `index.json` structure is designed to be easily consumed by a frontend application. You could build:

- **Gallery view**: Display all inspo with filtering by category/tags
- **Search**: Full-text search across tags and notes
- **Collections**: Group related inspiration
- **Moodboards**: Combine multiple items into boards
- **API**: Serve the index.json as a simple API endpoint

Example frontend query:
```javascript
// Fetch all dark-mode dashboard inspiration
const darkModeDashboards = index.items.filter(item =>
  item.tags.includes('dashboard') && item.tags.includes('dark-mode')
);
```

## Tips

1. **Quick saves**: Just paste a URL and accept suggestions for the fastest workflow
2. **Descriptive tags**: Add specific tags like "micro-interaction" or "glassmorphism" for better searchability
3. **Use notes**: Add context for why you saved something
4. **Consistent categories**: Stick to a core set of categories for easier organization
5. **Source attribution**: The skill automatically saves the source URL for proper attribution

## Workflow Integration

This skill works great with:
- **Browsing design sites**: Save shots from Dribbble, Behance, Awwwards as you browse
- **Design research**: Build themed collections for specific projects
- **Team sharing**: Others can clone your repo and access the same inspo collection
- **Portfolio building**: Reference your saved inspo when creating case studies

## Trigger Phrases

The skill activates when you say:
- "Save this to my inspo"
- "Add to design inspiration"
- "Save to inspo: {url}"
- "Add inspo: {url}"
- "Save design inspo"

## Troubleshooting

**Download fails:**
- The skill will save the URL as a reference if direct download isn't possible
- Check if the URL requires authentication or is region-locked

**Category not suggested:**
- You can always specify your own custom category
- If the URL doesn't provide enough context, the skill will ask

**Index.json gets large:**
- Consider archiving old entries or splitting into multiple files
- The structure supports pagination for frontend apps

## Contributing

Want to improve this skill? Ideas for enhancements:
- Add thumbnail generation
- Implement duplicate detection
- Support for video hosting platforms (YouTube, Vimeo)
- Batch processing of multiple URLs
- Search command to query saved inspo

## Version History

- **v1.0** (2024-10-30): Initial release
  - Multi-format input support
  - Auto-categorization
  - Tag generation
  - Central indexing
  - Git auto-commit
