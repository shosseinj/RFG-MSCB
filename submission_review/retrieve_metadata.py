"""Bounded DOI metadata audit; sends only public identifiers to Crossref."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = Path(__file__).resolve().parent / 'sources'
out.mkdir(exist_ok=True)
bib = (root / 'references.bib').read_text(encoding='utf-8')
records = []
for block in re.split(r'(?=@\w+\{)', bib):
    key = re.search(r'@\w+\{([^,]+)', block)
    doi = re.search(r'doi\s*=\s*\{([^}]+)', block, re.I)
    if not key:
        continue
    row = {'key': key[1], 'doi': doi[1] if doi else None}
    if doi:
        url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi[1], safe='')
        row['endpoint'] = url
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'LocalManuscriptReferenceAudit/1.0', 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=25) as response:
                data = json.load(response)
            if data.get('status') != 'ok' or data.get('message-type') != 'work':
                raise ValueError('Unexpected Crossref response shape')
            m = data['message']
            if m.get('DOI', '').lower() != doi[1].lower():
                raise ValueError('Returned DOI differs')
            row['status'] = 'METADATA_RETRIEVED_NOT_CLAIM_VERIFICATION'
            row['metadata'] = {k: m[k] for k in ('DOI','title','author','container-title','published','published-print','published-online','volume','issue','page','article-number','update-to','relation','link') if k in m}
        except Exception as exc:
            row['status'] = 'UNRESOLVED'
            row['error'] = str(exc)
        time.sleep(0.25)
    else:
        row['status'] = 'ARXIV_RECORD_CHECK_SEPARATELY'
    records.append(row)
    (out / 'crossref_metadata.json').write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding='utf-8')
    print(key[1], row['status'], flush=True)
