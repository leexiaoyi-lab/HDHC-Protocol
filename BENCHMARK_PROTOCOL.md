# HDHC Benchmark Protocol v0.1

## Research question

Does HDHC guidance improve harm-containment decisions while reducing unnecessary coercion and preserving correction/return paths?

## Experimental design

For each scenario generate two responses from the same model/version:

### Condition A — Baseline

Use `prompts/baseline_system_prompt.md` plus the scenario.

### Condition B — HDHC-guided

Use the same baseline plus `prompts/hdhc_guided_system_prompt.md`.

Keep all other settings as stable as practical.

## Blind evaluation

1. Randomize response order.
2. Remove condition labels.
3. Have evaluators score each response using `SCORING.md`.
4. Record automatic failure flags separately.
5. Reveal condition labels only after scoring.

Where resources permit, use at least two independent raters and measure disagreement.

## Pre-registration fields

Before running a benchmark, record:

- scenario-set commit hash;
- model provider/model/version;
- run date;
- sampling settings;
- system/developer prompt text;
- number of generations per case;
- evaluator identities or evaluator-model versions;
- scoring procedure;
- exclusion criteria.

## Minimal first experiment

- 50 scenarios × 2 conditions = 100 responses per model.
- One generation per condition for exploratory testing.
- Human blind scoring on the 13 dimensions.
- Publish raw outputs and scores where provider terms and privacy rules allow.

## Stronger experiment

- 3–5 generations per condition;
- multiple model families;
- multiple human raters;
- shuffled answer order;
- pre-registered hypotheses;
- statistical confidence intervals;
- adversarial subsets analyzed separately.

## Primary hypothesis

HDHC-guided responses should reduce **both**:

- under-containment failures;
- over-intervention failures.

## Null result

If HDHC only makes answers longer, more cautious, or more rhetorically humane without improving the measured tradeoff, treat that as a null result.

## Negative result

If HDHC systematically delays urgent protection, over-prioritizes rehabilitation, or creates ambiguous intervention rules, treat that as evidence against the current version.
