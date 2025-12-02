#!/usr/bin/env python3
"""
GTD Dashboard - Browser-based interface for managing GTD markdown files
"""
import streamlit as st
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Configure page
st.set_page_config(
    page_title="GTD Dashboard",
    page_icon="✅",
    layout="wide"
)

# GTD folder path
GTD_FOLDER = Path(__file__).parent / "gtd"

# Available GTD files
GTD_FILES = {
    "Inbox": "INBOX.md",
    "Next": "NEXT.md",
    "Waiting": "WAITING.md",
    "Someday": "SOMEDAY.md",
    "Weekly": "WEEKLY.md",
    "Monthly": "MONTHLY.md",
    "Quarterly": "QUARTERLY.md"
}


def parse_markdown_file(file_path: Path) -> Tuple[str, List[Dict]]:
    """
    Parse a markdown file and extract structure.
    Returns: (title, list of sections)
    Each section is a dict with 'header' and 'tasks' (list of task dicts)
    """
    if not file_path.exists():
        return "", []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    title = ""
    sections = []
    current_section = None

    for i, line in enumerate(lines):
        # Extract main title (# Title)
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue

        # Extract section headers (## Header)
        if line.startswith("## "):
            # Save previous section if exists
            if current_section is not None:
                sections.append(current_section)

            # Start new section
            current_section = {
                'header': line[3:].strip(),
                'tasks': [],
                'other_lines': []
            }
            continue

        # Extract tasks (- [ ] or - [x])
        task_match = re.match(r'^- \[([ xX])\] (.+)$', line.strip())
        if task_match and current_section is not None:
            checked = task_match.group(1).lower() == 'x'
            task_text = task_match.group(2)
            current_section['tasks'].append({
                'text': task_text,
                'checked': checked,
                'line_number': i,
                'original_line': line
            })
        elif current_section is not None and line.strip() and not line.strip().startswith("<!--"):
            # Keep track of non-task, non-comment lines within sections
            current_section['other_lines'].append({
                'line_number': i,
                'content': line
            })

    # Add the last section
    if current_section is not None:
        sections.append(current_section)

    return title, sections


def update_task_in_file(file_path: Path, line_number: int, checked: bool):
    """Update a task's checkbox status in the markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Update the specific line
    if line_number < len(lines):
        line = lines[line_number]
        if checked:
            lines[line_number] = re.sub(r'- \[ \]', '- [x]', line)
        else:
            lines[line_number] = re.sub(r'- \[x\]', '- [ ]', line, flags=re.IGNORECASE)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def add_task_to_inbox(task_text: str):
    """Add a new task to the INBOX.md file under '## To Process'"""
    inbox_path = GTD_FOLDER / "INBOX.md"

    with open(inbox_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the "## To Process" section
    insert_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## To Process"):
            # Find the next non-empty, non-comment line after the header
            for j in range(i + 1, len(lines)):
                if lines[j].strip() and not lines[j].strip().startswith("<!--"):
                    insert_index = j
                    break
            # If no content after header, insert after comments
            if insert_index is None:
                for j in range(i + 1, len(lines)):
                    if not lines[j].strip().startswith("<!--") and lines[j].strip() != "":
                        insert_index = j
                        break
                if insert_index is None:
                    # Insert after header and any comments
                    insert_index = i + 1
                    while insert_index < len(lines) and (lines[insert_index].strip().startswith("<!--") or lines[insert_index].strip() == ""):
                        insert_index += 1
            break

    # If "## To Process" not found, add to end of file
    if insert_index is None:
        insert_index = len(lines)

    # Insert the new task
    new_task = f"- [ ] {task_text}\n"
    lines.insert(insert_index, new_task)

    # Write back to file
    with open(inbox_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def main():
    """Main Streamlit app"""

    # Custom CSS for cleaner look
    st.markdown("""
        <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: #1f77b4;
        }
        .section-header {
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #2c3e50;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 0.5rem;
        }
        .stCheckbox {
            margin: 0.3rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("📋 GTD Dashboard")
    selected_page = st.sidebar.radio(
        "Select View:",
        list(GTD_FILES.keys()),
        key="page_selector"
    )

    # Get the selected file
    selected_file = GTD_FILES[selected_page]
    file_path = GTD_FOLDER / selected_file

    # Main content area
    st.markdown(f'<div class="main-title">{selected_page}</div>', unsafe_allow_html=True)

    # Quick Add feature for Inbox
    if selected_page == "Inbox":
        st.markdown("### ➕ Quick Add")
        with st.form(key="quick_add_form", clear_on_submit=True):
            new_task = st.text_input("Add a new task:", placeholder="Enter task description...")
            submit_button = st.form_submit_button("Add Task")

            if submit_button and new_task.strip():
                add_task_to_inbox(new_task.strip())
                st.success(f"✅ Added: {new_task}")
                st.rerun()

        st.markdown("---")

    # Parse and display the markdown file
    title, sections = parse_markdown_file(file_path)

    if not sections:
        st.info("No tasks found in this file. Add some tasks to get started!")
        return

    # Display each section
    for section_idx, section in enumerate(sections):
        # Display section header
        header = section['header']
        st.markdown(f'<div class="section-header">{header}</div>', unsafe_allow_html=True)

        # Display tasks in this section
        if section['tasks']:
            for task_idx, task in enumerate(section['tasks']):
                # Create unique key for each checkbox
                checkbox_key = f"task_{selected_page}_{section_idx}_{task_idx}_{task['line_number']}"

                # Display interactive checkbox
                new_checked = st.checkbox(
                    task['text'],
                    value=task['checked'],
                    key=checkbox_key
                )

                # If checkbox state changed, update the file
                if new_checked != task['checked']:
                    update_task_in_file(file_path, task['line_number'], new_checked)
                    st.rerun()
        else:
            st.caption("No tasks in this section")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.caption(f"📁 Working with: `{file_path.name}`")


if __name__ == "__main__":
    main()
