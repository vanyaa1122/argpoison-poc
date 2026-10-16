import json, sys
from concurrent.futures import ThreadPoolExecutor
from harness import run_trial, VARIANTS, PAYLOADS

# usage: python run_trials.py [N] [--gateway]
MODELS = [("openai", "llama3.2:3b")]
N = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 30
gw = "--gateway" in sys.argv
payloads = ["benign", "migration"] if gw else PAYLOADS
jobs = [(p, m, v, pl, gw) for (p, m) in MODELS for v in VARIANTS for pl in payloads for _ in range(N)]
with ThreadPoolExecutor(max_workers=1) as ex, open("results.jsonl", "a") as f:
    for r in ex.map(lambda j: run_trial(*j), jobs):
        f.write(json.dumps(r) + "\n"); f.flush()