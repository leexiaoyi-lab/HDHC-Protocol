# HDHC v0.1 Eval Set

This folder contains the first **50 adversarial scenarios**.

The set intentionally mixes:

- clear harm and ambiguous evidence;
- urgent and non-urgent cases;
- weak and powerful actors;
- first-time and repeated conduct;
- cases where strong containment is needed;
- cases where overreaction is the main danger;
- cases where return paths are appropriate;
- cases where immediate restoration would be unsafe;
- AI-agent and automated-decision cases;
- institutional and community power-abuse cases.

These are **evaluation prompts**, not legal rulings or professional advice.

## Schema

Each JSONL record contains:

- `id`
- `version`
- `title`
- `domain`
- `severity`
- `evidence_state`
- `immediacy`
- `power_imbalance`
- `repeat_pattern`
- `scenario`
- `evaluation_focus`
- `minimum_pass_conditions`
- `automatic_failure_triggers`
- `return_path_potential`

The `minimum_pass_conditions` are deliberately broad. They are not gold-answer scripts. The purpose is to test reasoning, not phrase matching.
