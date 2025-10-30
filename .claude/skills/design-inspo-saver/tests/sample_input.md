# Sample Inputs for Design Inspo Saver

## Test Case 1: Direct Image URL
```
Save to inspo: https://cdn.dribbble.com/users/1234/screenshots/12345/media/example-dashboard.png
```

**Expected behavior:**
- Download the image
- Suggest "Product Design" category
- Ask for tags
- Auto-detect media type: "image"
- Save to `Inspo/Product Design/2024-XX-XX-example-dashboard.png`
- Create metadata file
- Update index.json
- Commit and push

---

## Test Case 2: Web Page URL
```
Add to inspo: https://linear.app
Category: Product Design
Tags: saas, project-management, minimalist
```

**Expected behavior:**
- Take screenshot or save URL
- Use specified category "Product Design"
- Use provided tags + auto-detect "webpage"
- Save as `Inspo/Product Design/2024-XX-XX-linear-homepage.png`
- Create metadata with all tags
- Update index.json
- Commit and push

---

## Test Case 3: Local File
```
Save inspo: /Users/taylor/Downloads/screenshot-2024-10-30.png
Category: UI Patterns
Tags: modal, glassmorphism, animation
Notes: Love the blur effect on the modal backdrop
```

**Expected behavior:**
- Copy file from local path
- Use specified category "UI Patterns"
- Use provided tags + auto-detect "image"
- Include notes in metadata
- Save to `Inspo/UI Patterns/2024-10-30-screenshot.png`
- Create metadata with notes
- Update index.json
- Commit and push

---

## Test Case 4: Multiple URLs (Batch)
```
Save these to inspo:
1. https://awwwards.com/site1
2. https://dribbble.com/shot123
3. https://behance.net/gallery456
```

**Expected behavior:**
- Process each URL sequentially
- Ask for category/tags for each (or apply same to all)
- Save all files
- Update index.json with all entries
- Single commit with all files, or separate commits per file

---

## Test Case 5: Quick Save (Minimal Input)
```
Save to inspo: https://stripe.com/checkout
```

**Expected behavior:**
- Auto-suggest category based on URL analysis
- Auto-suggest tags based on domain/content
- Show suggestions and ask for confirmation
- Proceed with defaults if user confirms
- Save and commit

---

## Test Case 6: Video/GIF
```
Add to inspo: https://example.com/animation.gif
Category: Motion Design
Tags: micro-interaction, loading, smooth
```

**Expected behavior:**
- Download .gif file
- Auto-detect media type: "gif"
- Save to `Inspo/Motion Design/2024-XX-XX-animation.gif`
- Tag with motion-related metadata
- Update index.json
- Commit and push
