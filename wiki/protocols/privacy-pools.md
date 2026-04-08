# Privacy Pools

**Category:** [[_index#privacy-protocols|Privacy Protocols]]
**Related:** [[concepts/zk-snarks]], [[concepts/cryptographic-primitives]], [[concepts/privacy-vs-compliance]], [[protocols/railgun]]
**Developed by:** 0xbow
**Research basis:** Vitalik Buterin et al.
**Seed funding:** $3.5 million (Ethereum Foundation backed)

---

## Overview

Privacy Pools is a **compliance-aware privacy protocol** that allows users to make private cryptocurrency withdrawals while demonstrating they are not connected to illicit activity. It was born from research by Vitalik Buterin into how to have privacy *without* giving bad actors the same privacy.

The key insight: privacy doesn't require hiding *everyone equally*. A well-designed system can exclude sanctioned addresses from the privacy pool while preserving genuine privacy for legitimate users.

---

## The Core Problem

Previous privacy protocols (most notably Tornado Cash) provided equal privacy to everyone — including criminals and sanctioned entities. This made them easy targets for regulatory action, and resulted in the 2022 US Treasury sanctions of Tornado Cash.

Privacy Pools solves this with **Association Set Providers (ASPs)**: trusted third parties that maintain lists of "clean" deposits. Users prove they belong to a clean set without revealing *which* deposit they made.

---

## How It Works

### Deposit
1. User deposits ETH or ERC-20 tokens into a Privacy Pool via the Entrypoint contract.
2. A **commitment** is created: `C = Poseidon(value, label, nullifier, secret)` where value and label are public; nullifier and secret are private.
3. The commitment is added to a **Merkle tree** (LeanIMT — Lean Incremental Merkle Tree).
4. A small vetting fee is charged; the deposit is recorded.

### ASP Vetting
Association Set Providers continuously scan deposits and:
- Maintain a list of "approved" deposits (not linked to OFAC sanctions, known criminal activity, etc.)
- Post the Merkle root of their approved set on-chain.
- Multiple ASPs can operate simultaneously with different criteria.

### Withdrawal
1. User wants to withdraw (possibly a different amount than deposited, or from a different address).
2. User generates a [[concepts/zk-snarks|Groth16 zk-SNARK]] proof demonstrating:
   - They control a valid deposit in the state tree (Merkle inclusion proof).
   - Their deposit is included in the ASP's approved set.
   - They have not already spent this deposit (nullifier check).
3. Proof is verified on-chain; funds are released to recipient address.
4. The nullifier is published, preventing double-withdrawal.

No external observer can link the withdrawal to the original deposit.

---

## "Proof of Innocence"

Privacy Pools introduces the concept of **proof of innocence**: rather than proving *who you are*, you prove you are *not* someone harmful.

Users can generate an inclusion proof showing their deposit is in an ASP's approved set (a set that excludes sanctioned addresses). This provides a cryptographic statement: "My deposit was vouched for by [ASP] as not being from a known bad actor."

This is fundamentally different from KYC: no identity is revealed, only non-membership in a bad-actor set.

---

## Architecture: Three Layers

### 1. Smart Contract Layer

**IEntrypoint** — Central registry and router:
- Manages asset-specific pool addresses
- Handles deposits (ETH and ERC-20)
- Routes withdrawal proofs to the correct pool
- Manages ASP root registry
- Collects and distributes fees
- Follows UUPS upgradeable proxy pattern (OpenZeppelin AccessControl)

**IPrivacyPool** — Per-asset pool contract:
- Maintains commitment Merkle tree
- Tracks nullifier registry
- Handles ragequit functionality

### 2. Zero-Knowledge Layer

**Circuits (written in Circom):**

| Circuit | Function |
|---|---|
| CommitmentHasher | Creates commitment from value, label, nullifier, secret using Poseidon |
| WithdrawalCircuit | Verifies state tree membership + ASP tree inclusion + nullifier validity |
| LeanIMT Circuit | Efficient Merkle inclusion proofs with dynamic depth |

**Proving system:** Groth16 with BLS12-381 curve. A single verification takes ~40M Soroban instructions (40% of testnet max on Stellar).

### 3. ASP Layer

ASPs operate as off-chain services that:
- Monitor deposits
- Screen against sanctions lists and known criminal addresses
- Publish Merkle roots of approved deposits on-chain
- Link roots to IPFS documents explaining their screening criteria

Multiple ASPs with different standards can coexist, giving users choice of which compliance standard they want to prove against.

---

## Ragequit Mechanism

If a user's deposit is rejected by all ASPs (or they simply want out), they can **ragequit**: publicly reveal the connection between their deposit and withdrawal to recover funds. This sacrifices privacy but ensures no one's funds are permanently trapped.

The ragequit mechanism is critical for the protocol's legitimacy: users have an exit, so there is no "privacy ransom" where funds become inaccessible.

---

## Partial Withdrawals

Users can withdraw less than their full deposit, maintaining the remainder as a private commitment. This enables:
- Breaking up large deposits into smaller withdrawals
- Privacy-preserving recurring payments
- Partial spending while keeping the balance private

---

## LeanIMT (Lean Incremental Merkle Tree)

A custom Merkle tree implementation optimized for on-chain use:
- Dynamic depth — tree grows as deposits are added, without pre-allocating all leaves
- Single-child node optimization — reduces proof size for sparse trees
- Compatible with Circom circuit generation

---

## Stellar Prototype

A prototype implementation was built on Stellar's Soroban smart contract platform, demonstrating that Privacy Pools' architecture is chain-agnostic. This used Soroban's native contract system with Groth16 verification.

---

## Development Stack

| Component | Technology |
|---|---|
| Smart contracts | Solidity (Ethereum), Soroban (Stellar) |
| ZK circuits | Circom |
| SDK | TypeScript |
| Relayer | Node.js service |
| Hash function | Poseidon |
| Proving system | Groth16 / BLS12-381 |

---

## Key Entities

| Entity | Role |
|---|---|
| 0xbow | Implementation team |
| Vitalik Buterin | Original research; investor |
| Ethereum Foundation | Seed funder |
| Stellar Foundation | Prototype partner |
| Sky (formerly Maker DAO) | Ecosystem partner |
| ASPs | Third-party screening providers |

---

## Backlinks

Sources:
- `raw/articles/What is Privacy Pools_.md`
- `raw/articles/Privacy Pools_ How to Protect Users Privacy While Meeting the Compliance Requirements.md`
- `raw/articles/Privacy Pools — Striking The Balance In Privacy And Regulations.md`
- `raw/articles/Core Concepts _ Privacy Pools Documentation.md`
- `raw/articles/ASP Layer _ Privacy Pools Documentation.md`
- `raw/articles/Circuits Interfaces _ Privacy Pools Documentation.md`
- `raw/articles/Commitment Circuit _ Privacy Pools Documentation.md`
- `raw/articles/Contracts Interfaces _ Privacy Pools Documentation.md`
- `raw/articles/Smart Contracts Layer _ Privacy Pools Documentation.md`
- `raw/articles/Withdrawal Circuit _ Privacy Pools Documentation.md`
- `raw/articles/LeanIMT Circuit _ Privacy Pools Documentation.md`
- `raw/articles/SDK Utilities _ Privacy Pools Documentation.md`
- `raw/articles/Developer Guide _ Privacy Pools Documentation.md`
- `raw/articles/Prototyping Privacy Pools on Stellar.md`
- `raw/articles/Privacy Pools Documentation.md` (and versions 1–4)
