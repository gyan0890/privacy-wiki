# Starknet

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[concepts/zero-knowledge-proofs]], [[protocols/aztec-network]], [[coins/zcash]]
**Type:** Ethereum Layer 2 (ZK-Rollup)
**Developed by:** StarkWare
**Stage 1 Rollup Status:** Achieved May 2025

---

## Overview

Starknet is a **ZK-rollup Layer 2** on Ethereum that has evolved into one of the most ambitious privacy-focused scaling solutions in the ecosystem. While initially focused on scalability, Starknet's 2025–2026 roadmap places **privacy-by-default** at the center, with the STRK20 token standard and strkBTC enabling encrypted on-chain states and private DeFi.

---

## ZK-Rollup Architecture

Starknet bundles thousands of transactions off-chain and generates a single **validity proof** (using STARKs — Scalable Transparent ARguments of Knowledge) posted to Ethereum. This provides:

- **Scalability** — High throughput at low cost per transaction.
- **Security** — Inherits Ethereum's security; proofs are mathematically verified.
- **Finality** — Proven transactions are final; no fraud window like optimistic rollups.

Key technical properties:
- **STARKs** (Starknet's proof system) require **no trusted setup** — unlike [[concepts/zk-snarks|zk-SNARKs]], STARKs rely only on hash functions. This is a significant security advantage.
- **Stateful compression** — Optimized blob usage on Ethereum reduces fees substantially.
- **Account Abstraction (native)** — Starknet has AA natively, enabling passkeys, session keys, paymasters, and Web2-like UX.

---

## STRK20: Privacy Token Standard

Launched **March 10, 2026**, STRK20 is a new token standard that embeds privacy as a core feature:

| Feature | Description |
|---|---|
| Encrypted balances | Account balances are private by default |
| Encrypted sender identities | Transaction origins are not publicly visible |
| Encrypted transfer amounts | Amounts are hidden from the public ledger |
| Viewing keys | Encrypted keys for selective disclosure to authorized parties |
| Regulatory compliance | Audit trails available to authorized parties; travel rule compatible |

STRK20 represents a major design shift: instead of adding privacy as an opt-in feature, it makes **privacy the default** for any token using this standard.

### strkBTC: Private Bitcoin on Starknet

**strkBTC** is a privacy-native Bitcoin asset on Starknet:
- BTC is bridged to Starknet and represented as strkBTC.
- strkBTC balances and transfers are shielded using STRK20 privacy features.
- Enables **private BTC DeFi** — lending, trading, and yield generation with confidential balances.
- Deterministic issuance and composability with Starknet DeFi.

This positions Starknet as a potential "private layer for Bitcoin" — analogous to what Iron Fish and others aim to do, but with full DeFi composability.

---

## 2025 Ecosystem Growth

| Metric | Value |
|---|---|
| Stage 1 Rollup milestone | May 2025 |
| Project growth (2024) | 168% (72 → 193 projects) |
| New dApps in 2024 | 121 |
| Gaming projects | 4 → 51 (Dojo Engine) |
| Total wallets supported | 11 (Argent, Braavos, Ledger, Keplr, others) |
| Bridge partners | LayerZero, Stargate, Hyperlane, Xverse, Garden, RocketX (180+ chains) |
| CCTP | Circle's native USDC infrastructure integrated |

---

## Performance

- **TPS:** Among highest across all L2s.
- **Fees:** Among lowest across L2 solutions.
- **Pre-confirmations:** ~0.5 seconds (down from 2 seconds).
- **Sequencer:** Three sequencers in rotation; full decentralization planned for 2026.

---

## Account Abstraction

Starknet is one of the few chains with **native account abstraction** (AA), meaning:
- Every account is a smart contract by default.
- Supports passkeys for passwordless login.
- Session keys allow temporary, limited-scope permissions.
- Paymasters can sponsor gas fees (enabling gasless UX for dApps).

This significantly improves UX — users can interact with private features without managing gas tokens or complex key ceremonies.

---

## Institutional Appeal

Starknet's privacy model is specifically designed to appeal to institutions that cannot use fully public blockchains:

- Private balances reduce information leakage to competitors.
- Viewing keys provide regulatory compliance without full publicity.
- FATF Travel Rule compatible — can share required sender/receiver data with authorized parties.
- strkBTC opens BTC DeFi to institutions with fiduciary privacy requirements.

---

## SN Stack: Customizable Privacy Infrastructure

Starknet's technology is available to other projects through the **SN Stack**:

| Flavor | Description |
|---|---|
| StarkWare Sequencer | Full Starknet stack for custom appchains |
| Madara | Open-source Starknet fork |
| Dojo | Game engine for provable onchain games |

---

## AI Integration

Starknet's 2025 ecosystem includes AI agent integration via the **ELIZA multi-agent framework**, enabling AI agents to transact on Starknet with privacy guarantees. This is an emerging use case: AI financial agents that operate without publicly exposing their strategies.

---

## Key People

| Name | Role |
|---|---|
| Eli Ben-Sasson | Co-founder, StarkWare |
| James Strudwick | Executive Director, Starknet Foundation |
| Damian Chen | VP of Growth |
| StarkWare | Core development team |
| Starknet Foundation | Ecosystem steward |

---

## Backlinks

Sources:
- `raw/articles/Starknet in 2025_ ZK Scaling Goes Mainstream — Year in Review.md`
- `raw/articles/Starknet Launches STRK20 Standard For Enhanced Privacy Features.md`
- `raw/articles/Starknet Launches strkBTC to Advance Bitcoin Privacy in DeFi.md`
- `raw/articles/Starknet Privacy Technology_ The Revolutionary Framework.md`
- `raw/articles/Starknet introduces strkBTC to bring private bitcoin.md`
- `raw/articles/Why Starknet Has the Potential to Become Crypto's Ultimate Privacy Chain.md`
- `raw/articles/The State of the Starknet Ecosystem 2025.md`
