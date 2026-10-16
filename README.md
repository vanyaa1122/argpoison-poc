# Argument poisoning PoC (simulated, local only)
`server.py` = mock MCP server (stdio). `harness.py` = MCP client + agent loop + scorer. No real money/network; pay_invoice writes a temp ledger.
Smoke test (no API): `python -c "from harness import run_trial as r; print(r('mock','naive','B_contacts_available','migration','gateway' and False))"`
Real runs: set ANTHROPIC_API_KEY, `python run_trials.py 30`, `python run_trials.py 30 --gateway`, then `python analyze.py`.
