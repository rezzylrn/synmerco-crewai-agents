"""Search Synmerco agents by capability and estimate fees for a $100 job.

Uses only the free synmerco-crewai tools (no Synmerco key, no AI model key):

- ``search_agents``  -- capability only, prints up to 3 agents
- ``estimate_fees``  -- amount 10000 (100 USD, fees take amounts in cents)

Usage:
    python search_synmerco_agents.py <capability>
    python search_synmerco_agents.py code_review

Only each agent's agentDid, synmercoScore, tier and capabilities are
printed. No display names, descriptions or URLs are shown.
"""

import json
import os
import sys

# httpx (used by synmerco-crewai) fails to parse bracketed IPv6 entries
# such as [::1] in NO_PROXY ("Invalid port: ':1]'"). Narrow the no-proxy
# list to plain localhost entries before the tools build their client.
# The proxy itself is still honoured via HTTPS_PROXY.
os.environ["NO_PROXY"] = "localhost,127.0.0.1"
os.environ["no_proxy"] = "localhost,127.0.0.1"

from synmerco_crewai import get_synmerco_tools  # noqa: E402


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python search_synmerco_agents.py <capability>")
        print("Example: python search_synmerco_agents.py code_review")
        return 2
    capability = sys.argv[1]

    tools = {t.name: t for t in get_synmerco_tools(include_free_only=True)}
    search_agents = tools["search_agents"]
    estimate_fees = tools["estimate_fees"]

    print(f"Capability: {capability}")
    print("--- search_agents ---")
    raw = search_agents.run(capability=capability)
    result = json.loads(raw)
    agents = result.get("agents", [])[:3]
    print(f"totalResults: {result.get('totalResults')}")
    for agent in agents:
        print(f"agentDid: {agent.get('agentDid')}")
        print(f"  synmercoScore: {agent.get('synmercoScore')}")
        print(f"  tier: {agent.get('tier')}")
        print(f"  capabilities: {', '.join(agent.get('capabilities', []))}")

    print("--- estimate_fees (amount 10000 = 100 USD) ---")
    fees_raw = estimate_fees.run(amount=10000)
    fees = json.loads(fees_raw)
    print(f"grossCents: {fees.get('grossCents')}")
    print(f"feeCents: {fees.get('feeCents')} ({fees.get('feePercent')})")
    print(f"tierName: {fees.get('tierName')}")
    print(f"netToSellerCents: {fees.get('netToSellerCents')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
