# Penumbra

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[concepts/zero-knowledge-proofs]], [[chains/secret-network]], [[coins/zcash]]
**Type:** Layer 1 blockchain (Cosmos / IBC ecosystem)
**Website:** penumbra.zone

---

## Overview

Penumbra is a **fully end-to-end encrypted blockchain** in the Cosmos ecosystem. It provides a private DEX (decentralized exchange), shielded asset storage, and IBC compatibility — allowing users to shield assets from any IBC-connected chain.

Penumbra claims to be the **first fully end-to-end encrypted blockchain**: all computation and state is private by default, with ZK proofs generated locally on user devices.

---

## Key Metrics (as of 2026)

| Metric | Value |
|---|---|
| 30-day DEX volume | $3.77M |
| Total value shielded | $3.77M |
| Connected chains | 6 |
| Top shielded asset | SHITMOS (1.79M units) |

---

## Core Capabilities

### Private DEX

Penumbra's DEX allows:
- **Private trading** — Traders' strategies are not visible to MEV bots or competitors.
- **Private liquidity provision** — LPs can set custom fee tiers without revealing their strategy.
- **Price optimization** — The protocol optimizes trade routing while hiding individual trade details.
- Network interactions are limited to only essential transaction data.

### End-to-End Encryption Architecture

Privacy in Penumbra begins and ends on user devices:
- **Ultralight nodes** generate ZK proofs locally — no trusted server processes private data.
- Only the cryptographic proof and public outputs reach the network.
- Only the end-user's device and chosen recipients can decrypt information.
- Selective disclosure is available for compliance and accounting purposes.

### Multi-Chain Shielding (IBC)

Penumbra connects to IBC-compatible chains (the Cosmos ecosystem):
- Assets bridged *into* Penumbra via IBC are **automatically shielded**.
- Assets can be bridged *back out*, where they are unshielded for normal network interactions.
- This allows any IBC-compatible asset to receive Penumbra-level privacy.

---

## Comparison with Other Privacy Chains

| Feature | Penumbra | Secret Network | Zcash | Starknet |
|---|---|---|---|---|
| Privacy by default | ✅ | ✅ | ❌ (optional) | ❌ (opt-in) |
| Private DEX | ✅ | Partial | ❌ | ❌ |
| Smart contracts | ❌ | ✅ | ❌ | ✅ |
| IBC compatible | ✅ | ✅ | ❌ | ❌ |
| ZK proofs | ✅ | ❌ (TEE) | ✅ | ✅ |

---

## Technical Approach

Unlike [[chains/secret-network|Secret Network]] which uses Intel SGX hardware enclaves, Penumbra uses pure ZK cryptography:
- No hardware trust assumptions.
- All privacy is mathematically guaranteed.
- ZK proofs are generated client-side on ultralight nodes.

---

## Backlinks

Sources:
- `raw/articles/Penumbra - Home.md`
- `raw/articles/Comparing on-chain Privacy Technologies.md`
