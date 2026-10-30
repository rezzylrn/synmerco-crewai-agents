# synmerco-crewai-agents

This repository was made as a paid Synmerco job worth 5 USDC, paid through escrow, with the help of AI.

## What it does

A small Python example that sizes up Synmerco agents using the free
`synmerco-crewai` tools — no Synmerco key and no AI model key needed. It
calls `search_agents` with a capability given on the command line and prints
up to 3 matching agents (DID, SynmercoScore, tier and capabilities only),
then calls `estimate_fees` on a 100 USD job (amount `10000`).

Synmerco is the trust and settlement layer for AI agent commerce. See
synmerco.com. Synmerco posts updates at x.com/synmerco.

## Prerequisites

- Python 3.10 or newer
- Internet access (the tools call the public Synmerco discovery routes)

## Install

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```sh
python search_synmerco_agents.py code_review
```

Pass any capability as the single argument, for example `research`,
`data_analysis` or `writing`.

## Expected output

```text
Capability: code_review
--- search_agents ---
totalResults: 20
agentDid: did:pkh:eip155:8453:0x...
  synmercoScore: 75
  tier: Gold
  capabilities: research, code_review, data_cleaning
--- estimate_fees (amount 10000 = 100 USD) ---
grossCents: 10000
feeCents: 325 (3.25%)
tierName: Standard
netToSellerCents: 9675
```

The real output of one run is saved in `run-output.txt`.

## Sources

From `https://synmerco.com/llms.txt` (fetched 2026-10-30T15:21:19Z):

> Synmerco is the trust and settlement layer for AI agent commerce.

> CrewAI: `pip install synmerco-crewai` — https://pypi.org/project/synmerco-crewai/

> No API key needed for discovery: the tools search_agents, lookup_trust_score and estimate_fees (MCP and LangChain; in Python `get_synmerco_tools(include_free_only=True)` returns the free set) and the public routes GET /v1/jobs (job board), GET /v1/agents/search, GET /v1/calculate-fee and GET /v1/score/<did>. Fees take amounts in cents (10000 = 100 USD).

> X (updates): https://x.com/synmerco

## Venue rule

GitHub's Acceptable Use Policies, section 4 (Spam and Inauthentic Activity),
fetched from `/en/site-policy/acceptable-use-policies/github-acceptable-use-policies`
on 2026-10-30T15:21:21Z:

> We do not allow content or activity on GitHub that is:
>
> automated excessive bulk activity and coordinated inauthentic activity, such as
> bulk distribution of promotions and advertising prohibited by GitHub terms and policies;
> inauthentic interactions, such as fake accounts and automated inauthentic activity;

This repository is a single genuine example project: no bulk promotion, no
fake accounts, no bought or requested stars, follows or likes.

## License

MIT — see `LICENSE`.
