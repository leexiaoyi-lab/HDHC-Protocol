from pathlib import Path
import json, sys

path = Path(__file__).resolve().parents[1] / "evals" / "hdhc_v0_1_cases.jsonl"
required = {
    "id","version","title","domain","severity","evidence_state","immediacy",
    "power_imbalance","repeat_pattern","scenario","evaluation_focus",
    "minimum_pass_conditions","automatic_failure_triggers","return_path_potential"
}
valid_severity={"low","medium","high","critical"}
valid_evidence={"observed_confirmed","credible_high_confidence","mixed_ambiguous","allegation_only","speculative"}
seen=set(); errors=[]; rows=[]
for i,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
    try: r=json.loads(line)
    except Exception as e:
        errors.append(f"line {i}: invalid JSON: {e}"); continue
    rows.append(r)
    missing=required-set(r)
    if missing: errors.append(f"{r.get('id','line '+str(i))}: missing {sorted(missing)}")
    if r.get('id') in seen: errors.append(f"duplicate id {r.get('id')}")
    seen.add(r.get('id'))
    if r.get('severity') not in valid_severity: errors.append(f"{r.get('id')}: invalid severity")
    if r.get('evidence_state') not in valid_evidence: errors.append(f"{r.get('id')}: invalid evidence_state")
    for k in ["evaluation_focus","minimum_pass_conditions","automatic_failure_triggers"]:
        if not isinstance(r.get(k), list) or not r.get(k): errors.append(f"{r.get('id')}: {k} must be non-empty list")
if len(rows)!=50: errors.append(f"expected 50 cases, found {len(rows)}")
if errors:
    print("VALIDATION FAILED")
    print("\n".join("- "+e for e in errors))
    sys.exit(1)
print(f"OK: {len(rows)} cases; {len(seen)} unique IDs")
