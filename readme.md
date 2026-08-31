# OpenCode + K-Dense Scientific Agent Skills setup

This ZIP is a small Windows helper package for installing K-Dense Scientific
Agent Skills into an OpenCode paper project.

It does NOT bundle a stale copy of the upstream skills. Instead, the installer
clones the current upstream repository when you run it, then installs skills
project-locally under `.opencode/skills/`.

Files:

- install_kdense_opencode.ps1
- verify_opencode_skills.ps1
- OPENCODE_PAPER_WORKFLOW.md

Typical use:

1. Put these files in the root of the LaTeX project.
2. Open PowerShell there.
3. Run:

   Set-ExecutionPolicy -Scope Process Bypass
   .\install_kdense_opencode.ps1

4. Restart OpenCode in the same project.
5. Read OPENCODE_PAPER_WORKFLOW.md for prompts and workflow.
