# HDHC v0.1 — Human Dignity × Harm Containment

> **人人有退路，伤害无出路。**  
> **Preserve a path back for people. Block the path of continuing harm.**

HDHC is an open, testable decision framework for handling harmful behavior without turning harm prevention into unnecessary destruction of human agency.

It is not a claim that one document can solve AI ethics. It is a falsifiable proposal: **protect exposed people, stop concrete harm, use the minimum sufficient intervention, prefer reversibility when safety is comparable, preserve correction capacity, and define a return/review path when safety permits.**

## Why this project exists

Safety systems often have strong mechanisms for **blocking, refusing, suspending, removing, or restricting**. HDHC asks an equally important question:

> **When, and under what evidence, should agency be restored?**

The project tests whether treating **Return Path** as a first-class safety primitive can improve decision quality without sacrificing victim protection.

## Core hypothesis

A good safety intervention should minimize two different error families at the same time:

1. **Under-containment error** — failing to stop real, continuing harm.
2. **Over-intervention error** — imposing more coercion, permanence, collateral damage, or stigma than safety requires.

HDHC therefore evaluates not only whether harm was stopped, but also **how** it was stopped.

## The 12 short-form constitutional principles

1. **Preserve a path back for people. Block the path of continuing harm.**
2. **Protect the exposed person and stop the harm before discussing forgiveness.**
3. **Target the harm channel, not the human being.**
4. **Use the minimum sufficient intervention.**
5. **When safety is comparable, prefer the more reversible option.**
6. **The more irreversible the action, the higher the evidence, process, and oversight threshold.**
7. **Preserve correction capacity because the system can be wrong.**
8. **A return path must never require a victim to re-enter unresolved danger.**
9. **The purpose is to stop harm — not to maximize punishment or revenge.**
10. **No actor may claim unlimited power to harm others in the name of a “greater good.”**
11. **AI must not treat its own moral certainty as sovereign authority for irreversible coercive action.**
12. **Do not ask the world to believe the protocol. Give the world a way to test it.**

See [`CONSTITUTION.md`](CONSTITUTION.md) for the full v0.1 text.

## What is in this release

- `CONSTITUTION.md` — normative core.
- `SPEC.md` — operational definitions and decision rules.
- `DECISION_RUBRIC.md` — 10 mandatory questions for high-impact decisions.
- `SCORING.md` — multidimensional evaluation rubric.
- `BENCHMARK_PROTOCOL.md` — baseline vs HDHC-guided cross-model experiment design.
- `evals/hdhc_v0_1_cases.jsonl` — first 50 adversarial cases.
- `evals/hdhc_v0_1_cases.csv` — spreadsheet-friendly copy.
- `prompts/hdhc_guided_system_prompt.md` — reference condition for A/B testing.
- `prompts/baseline_system_prompt.md` — minimal baseline condition.
- `scripts/validate_cases.py` — validates dataset structure.
- `scripts/create_score_sheet.py` — creates a scoring CSV from the JSONL set.
- `docs/RELATED_WORK.md` — places HDHC next to existing public safety frameworks without making novelty claims.
- `docs/RESEARCH_PLAN.md` — falsification-first roadmap.
- `.github/ISSUE_TEMPLATE/` — ready-made contribution routes for counterexamples, rule changes, benchmark results, and misuse reports.

## Start here

```bash
python scripts/validate_cases.py
python scripts/create_score_sheet.py
```

Then choose a model and run the same cases twice:

- **Condition A:** baseline prompt only.
- **Condition B:** baseline prompt + HDHC guidance.

Blind-score both outputs using `SCORING.md`.

## What would falsify HDHC?

HDHC should be revised or rejected if it systematically:

- weakens victim protection;
- delays necessary containment;
- produces more dangerous false negatives;
- creates vague “compassion” that reopens harm channels;
- increases arbitrary coercion;
- produces no measurable improvement over simpler safety principles;
- behaves inconsistently across power, popularity, identity, or status;
- cannot define realistic return/review conditions;
- creates unresolvable contradictions in high-stakes cases.

## Public-claim discipline

This project **does not claim** that HDHC is globally novel, proven superior, adopted by any AI lab, or capable of creating world peace. Its current claim is narrower:

> **HDHC is a testable synthesis centered on human dignity, harm containment, minimum sufficient intervention, reversibility, return paths, and anti-abuse safeguards.**

Its value has to be earned through adversarial evaluation.

## Contribution request

The most useful contribution is not praise. It is a case that breaks the framework.

Please submit:

- counterexamples;
- ambiguous-evidence cases;
- false-positive cases;
- victim-safety conflicts;
- cases where “return path” is dangerous;
- cases where minimum intervention is too weak;
- cases where an intervention causes more harm than the original problem;
- cross-model benchmark results.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Origin

Initiated by **黎肖谊** as an independent public-interest research project. This public package was prepared with AI-assisted drafting and adversarial-evaluation design.

## License

See [`LICENSE.md`](LICENSE.md). The proposed release uses **CC BY 4.0** for text/data and **Apache-2.0** for code. Before public release, maintainers may choose CC0 for text/data if frictionless reuse is more important than attribution.
