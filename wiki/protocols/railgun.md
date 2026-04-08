# Railgun

**Category:** [[_index#privacy-protocols|Privacy Protocols]]
**Related:** [[concepts/zero-knowledge-proofs]], [[protocols/privacy-pools]], [[concepts/privacy-vs-compliance]]

---

## Overview

Railgun is a **decentralized, on-chain ZK privacy protocol** for EVM-compatible blockchains. It allows users to shield tokens and NFTs, conduct private transactions, and interact with DeFi protocols without exposing their on-chain activity.

Unlike [[protocols/privacy-pools]] (which uses ASPs) or [[protocols/aztec-network]] (which is a full L2), Railgun operates as a smart contract system on existing chains — Ethereum, Polygon, Arbitrum, BSC, and others.

---

## Core Features

### Shielding Assets
Users can "shield" any ERC-20 token or NFT into a private Railgun balance:
- Tokens are deposited into Railgun's smart contracts.
- The user receives a private "0zk address" balance.
- No external observer can see the user's shielded balance.

### Private Transactions
Within the shielded pool, users can transfer tokens to other 0zk addresses:
- Transactions are private — amounts and parties not visible on-chain.
- ZK proofs verify correctness without revealing details.

### Private DeFi Interaction
Railgun's most distinctive feature: users can interact with public DeFi protocols (Uniswap, Aave, etc.) from their private balance, receiving results back into their private balance. This is called the **Relayer Network** pattern.

### Unshielding
To move funds back to a public address, users "unshield" — the private balance is reduced and the public address receives tokens.

---

## Proof of Innocence

Railgun implements a **Private Proof of Innocence** system:

- Users can generate a ZK proof demonstrating their shielded funds did *not* originate from a sanctioned or blacklisted address.
- This proof can be shared with compliance-sensitive counterparties.
- Crucially, the proof reveals *only* non-membership in a bad-actor list — not the user's identity or transaction history.

This is analogous to [[protocols/privacy-pools|Privacy Pools']] association set approach, but implemented differently (user-driven proofs rather than ASP-maintained lists).

---

## Compliance Tools

Railgun provides several mechanisms for compliance:

| Tool | Description |
|---|---|
| Viewing keys | Shareable read-only keys revealing transaction history to authorized parties |
| Proof of innocence | ZK proof of non-association with sanctioned addresses |
| Tax integrations | Tools for generating tax-compliant reports from shielded activity |
| Non-custodial 0zk addresses | User controls all keys; no custodian risk |

---

## Governance

Railgun is **fully decentralized** — there is no "Railgun company." The protocol is governed by RAIL token holders through an on-chain governance system:

- Governors stake RAIL to participate.
- Active governors receive rewards.
- Protocol upgrades require community votes.

---

## 0zk Addresses

A **0zk address** (zero-knowledge address) is a Railgun shielded address. It:
- Functions like a stealth address — each sender generates a unique one-time address for the recipient.
- Is not linkable to the recipient's public address.
- Can receive funds from any EVM address (shielded or not).

---

## Ecosystem Position

Railgun is positioned as a privacy layer *for existing dApps*, not a replacement:
- Works on chains where users are already active (Ethereum, Polygon, etc.)
- DeFi protocols don't need to integrate Railgun — users bring privacy to protocols through the Relayer Network
- Complements compliance-first approaches like Privacy Pools

---

## Backlinks

Sources:
- `raw/articles/On-chain ZK Privacy Ecosystem.md`
- `raw/articles/From Aztec to Zcash_ The year pragmatic privacy took root.md`
