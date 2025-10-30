#!/usr/bin/env python3
"""
Skill validation script for Claude Skills.
Checks structure, YAML metadata, and required files.
"""

import os
import sys
import re
from pathlib import Path

def validate_yaml_frontmatter(content):
    """Check if content has valid YAML frontmatter."""
    if not content.startswith('---'):
        return False, "Missing opening YAML delimiter (---)"
    
    # Find the closing delimiter
    lines = content.split('\n')
    closing_found = False
    yaml_end_line = 0
    
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            closing_found = True
            yaml_end_line = i
            break
    
    if not closing_found:
        return False, "Missing closing YAML delimiter (---)"
    
    yaml_content = '\n'.join(lines[1:yaml_end_line])
    
    # Check for required fields
    required_fields = ['name', 'description', 'version']
    for field in required_fields:
        if not re.search(f'^{field}:', yaml_content, re.MULTILINE):
            return False, f"Missing required field: {field}"
    
    return True, "YAML frontmatter is valid"

def validate_skill_structure(skill_path):
    """Validate the overall skill folder structure."""
    skill_path = Path(skill_path)
    
    if not skill_path.exists():
        return False, f"Skill path does not exist: {skill_path}"
    
    if not skill_path.is_dir():
        return False, f"Skill path is not a directory: {skill_path}"
    
    # Check for required files
    skill_md = skill_path / 'skill.md'
    if not skill_md.exists():
        return False, "Missing required file: skill.md"
    
    # Validate skill.md content
    with open(skill_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    valid, message = validate_yaml_frontmatter(content)
    if not valid:
        return False, f"Invalid skill.md: {message}"
    
    # Check for recommended files
    warnings = []
    
    readme = skill_path / 'README.md'
    if not readme.exists():
        warnings.append("⚠️  Missing recommended file: README.md")
    
    templates_dir = skill_path / 'templates'
    if not templates_dir.exists():
        warnings.append("⚠️  No templates/ directory found")
    
    return True, "Skill structure is valid", warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <skill_path>")
        print("\nValidates a Claude Skill folder structure and metadata.")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    
    print(f"🔍 Validating skill: {skill_path}\n")
    
    valid, message, *warnings_list = validate_skill_structure(skill_path)
    
    if valid:
        print(f"✅ {message}")
        if warnings_list and warnings_list[0]:
            print("\nWarnings:")
            for warning in warnings_list[0]:
                print(f"  {warning}")
        print("\n✨ Skill is ready to use!")
        sys.exit(0)
    else:
        print(f"❌ {message}")
        print("\n💡 Fix the issues above and run validation again.")
        sys.exit(1)

if __name__ == '__main__':
    main()
