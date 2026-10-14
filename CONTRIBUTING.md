# Contributing

Issues are welcome. Pull requests from outside the NobleSEO team are accepted for documentation and skills only, with signed-off commits (`git commit -s`). Until a license is published (see README), contributions cannot be merged without a separate written agreement with the NobleSEO rights holder.

## Adding or changing a skill

1. One folder per skill: `plugins/nobleseo/skills/<name>/SKILL.md` with `name` (equal to the folder name) and `description` in the frontmatter, plus any `scripts/`.
2. List runtime requirements in a "Requirements" section of `SKILL.md`.
3. Add one manual eval prompt in `skills/<name>/evals/` and, for scripts, a case in `scripts/smoke_charts.py` or a similar smoke test with **synthetic** data only.
4. Complete the [skill publication checklist](docs/skill-publication-checklist.md) in the pull request description.

## Releasing

1. Update `CHANGELOG.md` under a new version heading.
2. Set the same `version` in `plugins/nobleseo/.claude-plugin/plugin.json`, `plugins/nobleseo/.codex-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
3. Run `python scripts/check_repo.py` and `python scripts/smoke_charts.py`.
4. Install from a fresh clone in Claude Code and in Codex and run each skill's eval prompt.
5. Tag `vX.Y.Z` and publish a GitHub release with the changelog section.

## License changes

Do not add a `LICENSE` file or a `license` field to any manifest. That happens only after written approval from the NobleSEO rights holder, recorded in `CHANGELOG.md` under a "License" heading in the same commit. CI enforces this.
