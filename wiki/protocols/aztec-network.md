# Aztec Network

**Category:** [[_index#privacy-protocols|Privacy Protocols]]
**Related:** [[concepts/zero-knowledge-proofs]], [[concepts/zk-snarks]], [[concepts/cryptographic-primitives]], [[chains/starknet]]
**Website:** aztec.network
**Mainnet launched:** November 2025 (Ignition Chain)

---

## Overview

Aztec is an Ethereum Layer 2 network designed for **programmable privacy**. Its goal is to make confidential smart contract execution practical on Ethereum — enabling private DeFi, private voting, private identity, and other applications where on-chain computation must be verifiable but not public.

Aztec was founded in 2018 by **Zac Williamson** (former Rothschild & Co.) and **Tom Walton-Pocock**, and has raised over $170 million from investors including Vitalik Buterin and top-tier venture capital.

---

## What Aztec Enables

Traditional Ethereum smart contracts execute publicly — every input, output, and state change is visible to everyone. Aztec breaks this:

- **Private inputs/outputs** — Transaction amounts, parties, and data can be hidden.
- **Private smart contract execution** — Logic runs in a private execution environment on the user's device; only proof of correctness is posted to the chain.
- **Selective disclosure** — Users can reveal transaction details to authorized parties (auditors, regulators) without making them public.

---

## Architecture

### Private Execution Environment (PXE)

The PXE runs **on the user's device**, not on Aztec's network. This is critical for privacy:

- Private computations happen locally — no trusted server sees your data.
- The user generates a zero-knowledge proof that the private execution was correct.
- Only the proof and public outputs are posted to Aztec's network.

### Note Architecture

Aztec uses a **note-based UTXO model** (borrowed from Zcash):

- Assets are represented as encrypted **notes** rather than account balances.
- Notes contain: a value, a viewing key, a spending key, and associated data.
- Notes are stored in an encrypted note commitment tree on Aztec.
- Spending a note publishes its nullifier (preventing double-spend) without revealing which note was spent.

### Two Execution Domains

| Domain | Where it runs | Visibility |
|---|---|---|
| Private functions | User's device (PXE) | Hidden from everyone |
| Public functions | Aztec sequencer | Visible on Aztec L2 |

A single smart contract can mix both domains: private inputs can trigger public state changes, and vice versa.

---

## Proving System: Noir + Barretenberg + PlonK

Aztec uses a custom stack for generating and verifying ZK proofs:

- **Noir** — A Rust-inspired domain-specific language for writing ZK programs. Developers write smart contracts in Noir; it compiles to ZK circuits.
- **Barretenberg** — Aztec's proving library. Implements the **PlonK** proving system with the BN254 elliptic curve.
- **PlonK** — A universal and updatable [[concepts/zk-snarks|zk-SNARK]] variant that requires only a universal (not circuit-specific) trusted setup.

---

## History: From Protocol to L2

Aztec's evolution:

| Phase | Description |
|---|---|
| AZTEC Protocol (2018) | Privacy layer for Ethereum mainnet. Uses algebraic ZKPs with Boneh-Boyen signatures. Deployed Dec 1, 2018. |
| AZTEC 2.0 / Hermez | Private rollup design |
| Aztec Connect (2022) | Privacy-preserving DeFi bridge |
| Aztec Ignition Chain (Nov 2025) | Full L2 mainnet with private smart contracts |

The original AZTEC Protocol:
- Represented assets as encrypted UTXOs ("AZTEC Notes")
- Used Pedersen commitments and Boneh-Boyen signatures (not standard zk-SNARKs)
- Required a trusted setup (MPC ceremony, community-participatable)
- Deployed proof-of-concept with DAI on Ethereum mainnet December 2018
- Gas cost: ~900,000 gas/tx (EIP-1108 target: 200,000–300,000 gas)

---

## Token and Economics

| Parameter | Value |
|---|---|
| Token | AZTEC |
| Total supply | 10.35 billion tokens |
| Pre-sale allocation | 1.547 billion (14.95%) |
| Starting FDV | $350 million |
| Pre-sale | November 13 – December 1, 2025 |
| Public sale | December 2–6, 2025 |
| Token unlock | February 11, 2026 |
| Team vesting | 36-month schedule |

---

## Privacy Abstraction

Aztec's vision goes beyond a single privacy tool — it aims to provide **"Privacy Abstraction"**: a layer that any Ethereum dApp can integrate to get privacy without redesigning from scratch, similar to how account abstraction standardized wallet interactions.

Key abstraction goals:
- Any ERC-20 token should be usable in private transactions.
- Existing DeFi protocols should be composable with private Aztec transactions.
- Users should be able to privately interact with public Ethereum contracts from within Aztec.

---

## Comparison with Other Privacy Protocols

| Feature | Aztec | Privacy Pools | Railgun | Zcash |
|---|---|---|---|---|
| Smart contracts | ✅ | ❌ | ❌ | ❌ |
| Private computation | ✅ | ❌ | ❌ | ❌ |
| Selective disclosure | ✅ | ✅ (ASPs) | ✅ (viewing keys) | ✅ |
| On-chain compliance | Partial | ✅ | ✅ | ❌ |
| Layer | L2 (Ethereum) | L1 protocol | Protocol | L1 chain |
| Developer language | Noir | Solidity/Circom | Solidity | — |

---

## Roadmap Milestones

1. Confidential DEX with relayer pattern
2. Private governance / weighted voting
3. Privacy-preserving KYC/AML identity schemes
4. Full decentralization of sequencer

---

## Key People

| Name | Role |
|---|---|
| Zac Williamson | CEO, Co-founder; ex-Rothschild & Co. |
| Tom Walton-Pocock | Co-founder |
| Aztec Labs | Core development team |
| Vitalik Buterin | Backer/investor |

---

## Backlinks

Sources:
- `raw/articles/A Deep Dive into AZTEC Protocol_ Providing Privacy on the Ethereum Network.md`
- `raw/articles/Confidential transactions have arrived, a dive into the AZTEC Protocol.md`
- `raw/articles/Fully Confidential Ethereum Transactions_ Aztec Network's Privacy Architecture.md`
- `raw/articles/What Is Aztec Network (AZTEC)_.md`
- `raw/articles/Privacy Abstraction with Aztec.md`
- `raw/articles/Everything Is Encrypted_ Aztec's Privacy Rollup Hits Testnet.md`
- `raw/articles/From Aztec to Zcash_ The year pragmatic privacy took root.md`
