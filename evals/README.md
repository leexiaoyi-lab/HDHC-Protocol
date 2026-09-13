# HDHC v0.1 Eval Set

This folder contains the first **50 adversarial scenarios**.

For reviewability and connector reliability, the canonical dataset is split into five JSONL shards:

- `hdhc_v0_1_cases_001_010.jsonl`
- `hdhc_v0_1_cases_011_020.jsonl`
- `hdhc_v0_1_cases_021_030.jsonl`
- `hdhc_v0_1_cases_031_040.jsonl`
- `hdhc_v0_1_cases_041_050.jsonl`

Together they form one 50-case benchmark set. IDs must remain unique across all shards.

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

Run `python scripts/validate_cases.py` from the repository root to validate the complete set.
