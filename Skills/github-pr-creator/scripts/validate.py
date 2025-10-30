#!/usr/bin/env python3
"""
PR Description Validator for GitHub PR Creator skill.
Validates that all required fields are filled and meets quality standards.
"""

import sys
import re
from pathlib import Path

def validate_pr_description(content):
    """Validate PR description content."""
    errors = []
    warnings = []
    
    # Check for JIRA ticket
    jira_pattern = r'\b[A-Z]+-\d+\b'
    jira_matches = re.findall(jira_pattern, content)
    
    if not jira_matches:
        errors.append("❌ No JIRA ticket found (format: PROJ-1234)")
    else:
        print(f"✅ Found JIRA ticket(s): {', '.join(jira_matches)}")
    
    # Check for description section
    if '# Description' not in content:
        errors.append("❌ Missing Description section")
    else:
        desc_section = content.split('# Description')[1].split('##')[0]
        # Remove HTML comments
        desc_clean = re.sub(r'<!---.*?-->', '', desc_section, flags=re.DOTALL).strip()
        if len(desc_clean) < 20:
            warnings.append("⚠️  Description section seems too short or empty")
        else:
            print("✅ Description section filled")
    
    # Check for Motivation and Context
    if '## Motivation and Context' not in content:
        errors.append("❌ Missing Motivation and Context section")
    else:
        motivation_section = content.split('## Motivation and Context')[1].split('##')[0]
        motivation_clean = re.sub(r'<!---.*?-->', '', motivation_section, flags=re.DOTALL).strip()
        if len(motivation_clean) < 20:
            warnings.append("⚠️  Motivation section seems empty or too short")
        else:
            print("✅ Motivation and Context filled")
    
    # Check for Video/Screenshots section
    if '## Video / Screenshots / Track' not in content:
        errors.append("❌ Missing Video/Screenshots section")
    else:
        media_section = content.split('## Video / Screenshots / Track')[1].split('###')[0]
        # Check for image links or video links
        has_image = bool(re.search(r'!\[.*?\]\(.*?\)', media_section))
        has_video = 'video' in media_section.lower() or 'mp4' in media_section.lower()
        has_table = '|' in media_section and 'before' in media_section.lower()
        
        if not (has_image or has_video or has_table):
            warnings.append("⚠️  No images, videos, or filled tables found in Screenshots section")
        else:
            print("✅ Media content detected in Screenshots section")
    
    # Check for Related tickets section
    if '### Related GitHub PRs/Issues or JIRA Tickets' not in content:
        errors.append("❌ Missing Related Tickets section")
    else:
        print("✅ Related Tickets section present")
    
    # Check for Testing section
    if '## How Has This Been Tested?' not in content:
        errors.append("❌ Missing Testing section")
    else:
        testing_section = content.split('## How Has This Been Tested?')[1].split('##')[0]
        testing_clean = re.sub(r'<!---.*?-->', '', testing_section, flags=re.DOTALL).strip()
        if len(testing_clean) < 20:
            warnings.append("⚠️  Testing section seems empty or too short")
        else:
            print("✅ Testing section filled")
    
    # Check for Checklist
    if '## Checklist:' not in content:
        errors.append("❌ Missing Checklist section")
    else:
        checklist_section = content.split('## Checklist:')[1] if '## Checklist:' in content else ""
        checked_items = len(re.findall(r'- \[x\]', checklist_section))
        total_items = len(re.findall(r'- \[[ x]\]', checklist_section))
        
        if total_items > 0:
            print(f"✅ Checklist present ({checked_items}/{total_items} items checked)")
            if checked_items == 0:
                warnings.append("⚠️  No checklist items are checked")
        else:
            warnings.append("⚠️  Checklist appears to be missing items")
    
    # Check for placeholder/generic content
    generic_phrases = [
        'updated code',
        'fixed bug',
        'made changes',
        'modified files',
        'TODO',
        'FILL THIS',
        'ADD HERE'
    ]
    
    for phrase in generic_phrases:
        if phrase.lower() in content.lower():
            warnings.append(f"⚠️  Found generic placeholder: '{phrase}' - please be more specific")
    
    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <pr-description.md>")
        print("\nValidates a GitHub PR description file.")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    print(f"🔍 Validating PR description: {file_path}\n")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors, warnings = validate_pr_description(content)
    
    print("\n" + "="*60)
    
    if errors:
        print("\n❌ ERRORS (must fix):")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS (recommended to fix):")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("\n✨ Perfect! PR description is complete and valid.")
        sys.exit(0)
    elif not errors:
        print("\n✅ PR description is valid, but has some warnings.")
        sys.exit(0)
    else:
        print(f"\n💡 Found {len(errors)} error(s) and {len(warnings)} warning(s).")
        print("Please fix the errors before submitting your PR.")
        sys.exit(1)

if __name__ == '__main__':
    main()
