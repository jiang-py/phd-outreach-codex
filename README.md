# PhD Outreach Email Workflow

This repository gives Codex a stable workflow for researching a potential PhD supervisor and preparing a natural bilingual outreach email for Shanshan Hao.

For a concise Chinese setup guide, read `快速使用说明.md`.

## Why this is an instruction repository

The main requirement is not an ordinary software calculation. It is a repeatable research and writing process. Codex automatically reads the root `AGENTS.md`, which then routes it to the detailed workflow, candidate profile, and professor case.

## Recommended repository setting

Create this as a private GitHub repository. It may contain personal application documents, unpublished research, and a supervisor list.

## Start a new professor case

Run:

```bash
python scripts/new_advisor_case.py professor-surname
```

For example:

```bash
python scripts/new_advisor_case.py chan-hku
```

This creates:

```text
cases/chan-hku.md
```

Open the new file and fill in the professor's information. Add URLs whenever possible. Put private supporting files in `private/` if you do not want Git to track them. If Codex Cloud needs to read a supporting document, place a suitable copy in the private repository and explicitly name its path in the case file.

## Ask Codex to complete the task

Open the repository in Codex and use:

```text
Read AGENTS.md and complete the case in cases/chan-hku.md. Research the professor's current work, follow all three writing passes, and create the required research notes and final bilingual email.
```

Codex will create:

```text
outputs/chan-hku_research_notes.md
outputs/chan-hku_email.md
```

Read the research notes first. Check that the selected paper and interpretation are correct. Then copy the English email from the final email file.

## Repository structure

```text
AGENTS.md                         Automatic Codex instructions
WORKFLOW.md                       Three-pass research and writing process
references/candidate_profile.md   Verified candidate facts and claim limits
references/source/                Original uploaded instruction document
templates/advisor_case.md         Input form for one professor
scripts/new_advisor_case.py       Helper for creating a new case
cases/                            Completed professor input forms
outputs/                          Research notes and final emails
private/                          Optional untracked personal documents
```

## Important limitations

- Current professor information and recent papers must be checked each time.
- The workflow can make the prose less formulaic, but no tool can guarantee the result of an AI detector.
- The original uploaded instruction document ended mid-sentence in its final DNA-repair example. This repository preserves the complete rules that were available and uses a restrained general closing rather than inventing the missing text.
