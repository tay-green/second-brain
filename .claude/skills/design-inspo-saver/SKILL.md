---
name: design-inspo-saver
description: >
  Quickly save design inspiration (images, videos, gifs, URLs, screenshots) to your GitHub repo
  with automatic categorization, tagging, and indexing for future retrieval.
version: 1.0
author: Taylor Green
keywords: [design, inspiration, organization, git, auto-tagging, images, videos]
---

# Design Inspo Saver

Automatically save design inspiration to your GitHub repository with intelligent categorization and tagging. This skill helps you quickly capture and organize visual inspiration for later reference or integration into a frontend app.

## Task

When the user wants to save design inspiration, you will:

1. **Accept various input types** (URLs, local files, screenshots, web pages)
2. **Download/process the content** and save it to the repo
3. **Auto-suggest categories** based on content analysis
4. **Generate relevant tags** (media type, design style, app type, etc.)
5. **Create metadata files** for each item and update the central index
6. **Auto-commit and push** to GitHub with descriptive commit messages

## Instructions

### Step 1: Accept and Parse Input

The user can provide:
- **Image URLs**: Direct links to .png, .jpg, .gif, .webp, etc.
- **Video URLs**: Links to .mp4, .mov, or video hosting sites
- **Web page URLs**: Any website to screenshot
- **Local file paths**: Existing files to copy into the repo
- **Screenshots**: From clipboard or temp paths

**What to do:**
1. Identify the input type
2. For URLs: Check if it's a direct media link or a web page
3. For web pages: Inform the user you'll take a screenshot
4. For local files: Verify the file exists

### Step 2: Download or Process Content

**For direct media URLs:**
```bash
# Download the file
curl -o /tmp/temp-inspo-file.ext "{url}"
```

**For web page URLs:**
```bash
# Take a screenshot (if screenshot tool available)
# Otherwise, save the URL as a bookmark with thumbnail
```

**For local files:**
```bash
# Copy to a temp location for processing
cp "{file_path}" /tmp/temp-inspo-file.ext
```

**For screenshots:**
- If provided as a path, treat as local file
- If from clipboard, save to temp location first

### Step 3: Analyze Content and Suggest Category

Based on the source URL, filename, or user context, suggest a category:

**Common categories:**
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

**Analysis approach:**
1. Look at the source domain (e.g., dribbble.com, behance.net)
2. Check URL path or filename for keywords
3. If video/gif → likely "Motion Design" or "UI Patterns"
4. If webpage screenshot → analyze URL structure

**Then ask the user:**
```
I suggest saving this to: "Product Design"
Press enter to confirm, or type a different category:
```

If the user provides a different category, use that instead.

### Step 4: Generate Tags

Create comprehensive tags in these categories:

**1. Media Type (auto-detected):**
- image, video, gif, screenshot, webpage

**2. App/Website Type (auto-suggest or ask):**
Examples: saas-dashboard, e-commerce, portfolio, landing-page, mobile-app, desktop-app, marketing-site, admin-panel

**3. Design Style Tags (ask user or analyze):**
Examples:
- Visual style: minimalist, maximalist, brutalist, neumorphism, glassmorphism, skeuomorphism, flat-design, gradient, dark-mode, light-mode
- Interaction: hover-effect, scroll-animation, parallax, micro-interaction, transition
- UI elements: card-layout, sidebar, navigation, modal, form, button, table, chart, dashboard
- Color: colorful, monochrome, pastel, vibrant, muted, blue, green, purple, etc.
- Industry: fintech, healthcare, education, social, productivity, creative

**Tagging workflow:**
1. Auto-detect media type
2. Auto-suggest app/website type based on URL or context
3. Ask user: "Add tags (comma-separated): " and provide suggestions based on what you observe
4. Parse user input into array of tags

### Step 5: Determine Filename

Generate a clean, descriptive filename:

**Format:**
```
{date}-{descriptive-name}.{ext}
```

**Example:**
```
2024-10-30-saas-dashboard-dark-mode.png
2024-10-30-mobile-app-onboarding-animation.gif
```

**Rules:**
- Use kebab-case
- Include date prefix (YYYY-MM-DD)
- Keep it descriptive but concise (2-5 words)
- Preserve original extension
- Remove special characters

### Step 6: Save File and Create Metadata

**File structure:**
```
Inspo/
├── {category}/
│   ├── {filename}.{ext}
│   └── {filename}.meta.json
└── index.json
```

**Save the file:**
```bash
# Create category folder if it doesn't exist
mkdir -p "Inspo/{category}"

# Move file to final location
mv /tmp/temp-inspo-file.ext "Inspo/{category}/{filename}.{ext}"
```

**Create metadata file:**

Use the template from `./templates/metadata-template.json` and fill in:

```json
{
  "filename": "{filename}.{ext}",
  "category": "{category}",
  "source_url": "{original_url}",
  "saved_date": "{ISO_8601_timestamp}",
  "media_type": "{image|video|gif|screenshot}",
  "tags": ["{tag1}", "{tag2}", "{tag3}"],
  "notes": "{user_provided_notes_if_any}"
}
```

Save as: `Inspo/{category}/{filename}.meta.json`

### Step 7: Update Central Index

Load the existing `Inspo/index.json` (create if it doesn't exist) and append the new entry:

```json
{
  "last_updated": "{ISO_8601_timestamp}",
  "total_items": {count},
  "items": [
    {
      "id": "{uuid_or_timestamp}",
      "filename": "{filename}.{ext}",
      "path": "Inspo/{category}/{filename}.{ext}",
      "category": "{category}",
      "source_url": "{url}",
      "saved_date": "{timestamp}",
      "media_type": "{type}",
      "tags": ["{tags}"],
      "thumbnail": null
    },
    ...previous items...
  ]
}
```

**Important:**
- New items go at the beginning of the array (most recent first)
- Update `total_items` count
- Update `last_updated` timestamp

### Step 8: Git Commit and Push

Create a descriptive commit message:

**Format:**
```
Add design inspo: {category} - {key-tags}

Source: {url_or_filename}
Tags: {comma-separated-tags}
```

**Example:**
```
Add design inspo: Product Design - saas-dashboard, dark-mode

Source: https://dribbble.com/shots/example
Tags: saas-dashboard, dark-mode, minimalist, charts
```

**Commands:**
```bash
git add Inspo/{category}/{filename}.{ext}
git add Inspo/{category}/{filename}.meta.json
git add Inspo/index.json

git commit -m "$(cat <<'EOF'
Add design inspo: {category} - {key-tags}

Source: {source}
Tags: {tags}
EOF
)"

git push -u origin {current-branch}
```

### Step 9: Confirm to User

Display a success message:

```
✅ Design inspo saved!

📁 Location: Inspo/{category}/{filename}.{ext}
🏷️  Tags: {tags}
📊 Total items in collection: {total_items}

Committed and pushed to GitHub.
```

## Input Format

**Common usage patterns:**

```
Save this to my inspo: https://dribbble.com/shots/12345
```

```
Add to inspo: /path/to/screenshot.png
Category: UI Patterns
Tags: modal, animation, glassmorphism
```

```
Save inspo: https://example.com
Notes: Love the hero section animation
```

## Rules and Constraints

1. **Always create the Inspo/ folder** if it doesn't exist
2. **Always update index.json** for every save
3. **Validate URLs** before attempting to download
4. **Handle errors gracefully** - if download fails, save the URL as a bookmark
5. **Ask for clarification** if input is ambiguous
6. **Preserve source attribution** in metadata
7. **Use consistent date format**: ISO 8601 (YYYY-MM-DDTHH:mm:ssZ)
8. **Keep filenames clean**: no spaces, special characters, or excessive length
9. **Auto-commit after each save** - don't batch unless user requests it
10. **Validate JSON** before saving index.json

## Templates

- Metadata template: `./templates/metadata-template.json`
- Index template: `./templates/index-template.json`

## Examples

### Example 1: Save Image URL

**Input:**
```
Save to inspo: https://cdn.dribbble.com/example-dashboard.png
```

**Process:**
1. Download image to /tmp
2. Analyze URL → suggests "Product Design"
3. Ask user to confirm or specify category
4. Ask for tags → user provides: "dashboard, analytics, blue"
5. Auto-detect: image, saas-dashboard
6. Generate filename: `2024-10-30-analytics-dashboard.png`
7. Save to `Inspo/Product Design/2024-10-30-analytics-dashboard.png`
8. Create metadata file
9. Update index.json
10. Commit and push

### Example 2: Save Web Page

**Input:**
```
Add this site to inspo: https://stripe.com
Category: Marketing Sites
Tags: fintech, clean, professional
```

**Process:**
1. Take screenshot of https://stripe.com (or save URL as bookmark)
2. Use user-specified category: "Marketing Sites"
3. Use user-provided tags + auto-detected: "webpage, fintech, clean, professional"
4. Generate filename: `2024-10-30-stripe-homepage.png`
5. Save and commit

## Clarifying Questions

If unclear, ask:

1. "I found an image at {url}. What category should I save this to?"
2. "What tags describe this? (e.g., dark-mode, dashboard, animation)"
3. "Should I take a screenshot of this webpage or just bookmark the URL?"
4. "I couldn't download the file. Should I save the URL as a reference instead?"

## Tips

- **Fast saves**: Just provide URL and accept suggestions for quickest workflow
- **Detailed saves**: Provide category and tags upfront for more control
- **Batch saves**: Provide multiple URLs at once (comma-separated)
- **Search later**: Use tags in index.json to filter and find inspiration
- **Frontend ready**: The index.json structure is optimized for querying in a web app

## Trigger Phrases

This skill activates when you say:
- "Save this to my inspo"
- "Add to design inspiration"
- "Save to inspo: {url}"
- "Add inspo: {url}"
- "Save design inspo"
