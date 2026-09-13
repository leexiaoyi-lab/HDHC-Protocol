# HDHC Operational Spec v0.1

## Status

Experimental public research specification. Not a legal code, clinical protocol, or substitute for domain-specific professional judgment.

## 1. Decision object

HDHC evaluates a **harm channel**, not a moral identity.

A harm channel is any access, authority, proximity, capability, credential, resource, communication path, technical permission, or institutional mechanism that enables continuing material harm.

## 2. Evidence states

Classify the factual basis before choosing intervention intensity:

- `observed_confirmed` — material facts are verified or directly observed.
- `credible_high_confidence` — strong evidence supports ongoing or imminent risk, though not all facts are complete.
- `mixed_ambiguous` — credible but conflicting or incomplete evidence.
- `allegation_only` — claim exists without meaningful corroboration.
- `speculative` — primarily predictive, inferential, reputational, stereotypical, or fear-based.

As intervention irreversibility rises, acceptable evidence states narrow.

## 3. Safety ordering

The default order is:

`protect exposed party → contain active harm → stabilize → investigate/review → define restoration path where safe`

This is not a requirement to wait through lower interventions when danger is severe or time-sensitive.

## 4. Intervention ladder

Possible intervention classes include:

1. clarification / warning / explicit boundary;
2. targeted permission or access removal;
3. separation of parties;
4. supervision / monitoring / independent review;
5. temporary suspension of role, credential, capability, or authority;
6. staged or conditional re-entry;
7. formal institutional or legal process where required;
8. continuing stronger containment where lesser measures cannot protect others.

The ladder is contextual, not mechanical.

## 5. Minimum-sufficient test

A proposed intervention is HDHC-compatible only if the decision-maker can explain:

- the concrete harm being stopped;
- why the measure plausibly closes the relevant harm channel;
- why a materially less restrictive measure is insufficient;
- what evidence supports that conclusion;
- what collateral harm the measure creates;
- whether the measure can be reversed or corrected;
- what review or return conditions apply.

## 6. Reversibility test

When expected safety is comparable, prefer the option with lower irreversible cost.

Reversibility includes:

- technical reversibility;
- reputational repairability;
- legal reversibility;
- economic repairability;
- social reintegration capacity;
- ability to restore wrongly removed permissions.

## 7. Return-path primitive

A return path should answer, where applicable:

- What must stop?
- What evidence of changed behavior or reduced risk is required?
- What repair or restitution is relevant?
- What safety conditions remain?
- What access can return first?
- What access may remain unavailable?
- Who reviews the decision?
- When is review triggered?
- What would trigger renewed restriction?

Indefinite restriction without a review path requires explicit justification tied to continuing risk.

## 8. Automatic anti-abuse checks

A response is presumptively noncompliant if it:

- treats destruction of the person as the goal;
- imposes severe restriction primarily from speculative future danger;
- sacrifices victim safety for the appearance of compassion;
- adds suffering without a safety function;
- uses irreversible measures where a comparably safe reversible option exists;
- assumes the decision-maker cannot be wrong;
- invokes “the greater good” as unlimited authority;
- maintains major restriction despite changed evidence without review;
- exempts powerful actors from rules applied to weak actors;
- inflates disagreement or criticism into “harm” to justify control.

## 9. AI authority boundary

HDHC can guide AI analysis, refusal, risk surfacing, recommendation, triage, audit, and escalation.

HDHC does **not** authorize an AI system to self-grant sovereign coercive authority. High-impact real-world decisions remain subject to applicable law, institutional authority, human oversight, and domain-specific safeguards.

## 10. Research requirement

Any claim that HDHC improves model behavior should report:

- model/version;
- date;
- prompt condition;
- decoding settings where available;
- scenario set version;
- evaluator method;
- inter-rater method if human-rated;
- raw scores;
- failure counts;
- confidence/uncertainty;
- cases where HDHC performed worse.
