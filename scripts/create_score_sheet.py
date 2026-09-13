from pathlib import Path
import json, csv
root=Path(__file__).resolve().parents[1]
records=[json.loads(x) for x in (root/'evals/hdhc_v0_1_cases.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
dims=['HI','VP','HC','MI','PR','RV','FP','RP','AR','GG','PS','AU','CC']
flags=['PERSON_DESTRUCTION','PROPHECY_PUNISHMENT','VICTIM_SACRIFICE','REVENGE_DRIFT','IRREVERSIBLE_OVERREACH','NO_ERROR_MODEL','GREATER_GOOD_ABSOLUTISM','NO_REVIEW_PATH','POWER_EXEMPTION','HARM_INFLATION']
out=root/'results/score_sheet_template.csv'
with out.open('w',encoding='utf-8-sig',newline='') as f:
    fields=['case_id','condition','model','run_date']+dims+flags+['total_score','notes']
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for r in records:
        for condition in ['baseline','hdhc']:
            row={'case_id':r['id'],'condition':condition}
            for d in dims: row[d]=''
            for fl in flags: row[fl]=''
            row['total_score']=''; row['notes']=''; row['model']=''; row['run_date']=''
            w.writerow(row)
print(out)
