# Python for Network Engineers

**From Python Fundamentals to Real-World Network Automation**

A hands-on training course that takes a network engineer from zero Python to
building tested, production-style network automation tools. It works as a study
guide, a lab manual, a reference, and a practice workbook.

> Version 0.1 (in development). Author: (placeholder). Organization: (placeholder). Year: 2026.

## Who this is for

Network engineers with or without any programming background. If you know what a
VLAN, an interface, and a BGP neighbor are, and you can use a device command line,
you have the networking side covered. This course supplies the Python.

## How the course is organized

Every chapter follows the same shape: what the concept is, why a network engineer
needs it, how it works, a diagram, original code, a walkthrough of why the code is
written that way, a full lab, a student exercise, a harder challenge, separate
solutions, key takeaways, and review plus interview questions.

Chapters live in `docs/chapters/`. Diagrams live in `docs/diagrams/`. Student lab
files live in `labs/`, and their solutions live separately in `solutions/`, so you
never see an answer before you have tried the exercise.

## Repository layout

```
python-for-network-engineers/
  docs/
    chapters/     chapter text
    diagrams/     figures (SVG)
  labs/           student-facing lab files, by chapter
  solutions/      matching solutions, by chapter
  scripts/        example scripts, including v1/v2/production versions
  datasets/       mock CLI output and sample data (run labs with no hardware)
  inventory/      device inventories in CSV, JSON, YAML
  templates/      Jinja2 templates
  configs/        generated and backup configs
  outputs/        reports and results
  tests/          pytest suites
  projects/       guided automation projects
  capstone/       the final end-to-end toolkit
  requirements.txt
  pyproject.toml
  .gitignore
```

## Lab environment

Labs are tiered so you are never blocked by a lack of hardware:

- Tier 0, no lab. Mock data and offline scripts. All of Part 1 and much of Parts 2 and 4 run here.
- Tier 1, free sandbox. Cisco DevNet Always-On and reservable sandboxes for SSH and API labs.
- Tier 2, containers. Containerlab with Arista cEOS, Nokia SR Linux, or FRR for multi-vendor and concurrency labs.
- Tier 3, full emulation. EVE-NG, GNS3, or Cisco CML for realistic topologies.

Each device lab tells you which tier it needs and gives a mock fallback where possible.

## Getting started

Start with Chapter 0, which installs Python 3.14, Git, and VS Code on Windows,
macOS, or Linux, creates your GitHub account, and sets up this project folder.

## Progress

The full plan is 40 chapters (Chapter 0 through 39), combining Python foundations,
device libraries, vendor APIs, model-driven programmability, and production
practice. See `course-architecture-combined.md` for the complete map.

- [x] Chapter 0: Prerequisites and Environment Setup
- [x] Chapter 1: Why Python for Network Engineers
- [x] Chapter 2: Your First Python Programs
- [ ] Chapters 3 through 39 (see the course architecture doc)
