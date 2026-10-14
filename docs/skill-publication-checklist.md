# Skill publication checklist

Copy this list into the pull request that adds or changes a skill, and tick every item. A skill is published only when all items are ticked.

The skill contains none of the following (instructions, scripts, examples, fixtures, screenshots):

- [ ] customer names, domains, URLs, data samples or screenshots of customer data;
- [ ] internal hostnames, IP addresses, file paths, environment names, or tool names that exist only inside NobleSEO;
- [ ] prompts, thresholds, weights, scoring formulas or decision rules copied from private NobleSEO code or documents;
- [ ] names of people, internal teams or partners;
- [ ] secrets, keys or tokens;
- [ ] text in a language other than English.

And:

- [ ] fixtures are synthetic;
- [ ] requirements are listed in `SKILL.md`;
- [ ] an eval prompt exists in `evals/` and was run in Claude Code and in Codex.
