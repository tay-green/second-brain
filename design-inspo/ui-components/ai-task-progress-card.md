---
title: AI Task Progress Card with Timeline
category: ui-components
tags: [progress-card, timeline, ai, task-tracker, loading-state, checklist, vertical-timeline, glassmorphism, card-ui]
source: Unknown
date_saved: 2025-11-05
colors: [#FFFFFF, #F8F9FA, #3B82F6, #E5E7EB, #6B7280]
design_patterns: [card-component, progress-indicator, timeline-view, loading-states, vertical-stepper]
components: [progress-card, circular-progress, timeline-stepper, status-icons, text-input]
---

# AI Task Progress Card with Timeline

![AI Task Progress Card](ai-task-progress-card.png)

## Overview
Sophisticated progress card showing AI task execution with a vertical timeline, progress indicator, and status updates. Features glassmorphic styling and clear visual hierarchy.

## Key Design Elements
- **Header section**:
  - 3D book stack icon with circular progress (2%)
  - "Top 3 books" title
  - "Estimated time 4min 52s" subtitle
- **Vertical timeline** with four stages:
  - "Creating plan" (active with spinner)
  - "Developing logic" (inactive)
  - "Designing screens" (inactive)
  - "Final touches" (inactive)
- **Status indicators**:
  - Active state: spinner animation
  - Inactive states: empty circles
  - Connected by vertical line
- **Bottom action** - "What should we make?" input with mic icon
- **Card styling** - Soft rounded corners, subtle shadow, white background

## Notable Features
- Real-time progress visualization
- Clear task breakdown
- Active state highlighting
- Time estimation for user expectations
- Vertical connection lines between steps
- Glassmorphic icon treatment
- Clean typography hierarchy
- Microphone input for voice commands

## Interaction Patterns
- Loading/processing states clearly shown
- Sequential task flow visualization
- Progress percentage and time estimate
- Voice input option
- Visual feedback on current step

## Technical Details
- Percentage-based progress (2%)
- Time-based estimates (4min 52s)
- Multi-step process visualization
- Active/inactive state management

## Use Cases
- AI task processing interfaces
- Multi-step form progress
- Workflow visualization
- Loading states for complex operations
- Project management dashboards
- Onboarding flows
- Tutorial progress
- Build/compile progress
- Long-running task indicators
