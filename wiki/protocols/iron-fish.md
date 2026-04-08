# Iron Fish

**Category:** [[_index#privacy-protocols|Privacy Protocols]]
**Related:** [[concepts/zero-knowledge-proofs]], [[coins/zcash]], [[chains/starknet]]
**Website:** ironfish.network
**Mainnet launched:** April 2023
**Acquired by:** Coinbase (team acquisition, 2025)

---

## Overview

Iron Fish is a Layer 1 proof-of-work blockchain that provides **optional privacy for any asset**. Its key differentiation is **multi-asset support** — users can import crypto assets from other chains and conduct private transactions for those assets on Iron Fish.

The project was backed by a16z and raised $27–28 million before its mainnet launch. In 2025, Coinbase acquired the Iron Fish team to scale privacy infrastructure to millions of users.

---

## Core Features

### Zero-Knowledge Privacy
Iron Fish uses ZK proofs (similar to [[coins/zcash|Zcash]]'s approach) for private transactions:
- Sender, receiver, and amounts are hidden in shielded transactions.
- Every account has a shielded address by default.
- Transactions are encrypted end-to-end.

### Multi-Asset Support
Iron Fish was the **first protocol to support multi-asset private transactions**:
- Any crypto asset can be imported via bridge providers.
- Once imported, assets can be transacted privately.
- Native bridging to Ethereum, Base, and Polygon via Bridge.IronFish.
- Third-party bridge access to 20+ EVM-compatible chains via ChainPort Bridge.

### Wallet Options
| Wallet | Type | Description |
|---|---|---|
| Node App | Desktop | Runs a full Iron Fish node |
| OreoWallet | Browser extension | Lightweight; accessible |

### Compliance
Iron Fish takes a proactive compliance stance:
- Integrates ChainPort's predictive screening for sanctions detection.
- Claims a "strong stance that Iron Fish is to be used for good."
- Real-time threat detection can freeze malicious addresses.

---

## 2025 Developments

- **SuiFish** — Expansion to Sui network bringing Iron Fish privacy to the Sui ecosystem.
- **Mobile wallet** — Launched 2025 for iOS and Android.
- **Coinbase acquisition** — Coinbase acquired the Iron Fish team to integrate privacy primitives into Base and Coinbase's broader infrastructure.

This acquisition is significant: it suggests that major centralized exchanges and L2 networks see user-level privacy as a coming requirement, and are building teams for it.

---

## Relationship to Zcash

Iron Fish is philosophically similar to [[coins/zcash|Zcash]] (ZK-based, shielded transactions) but differs in:
- **Multi-asset** support (Zcash is ZEC-only on its native chain)
- **Bridge-first** design — Iron Fish is explicitly positioned as a privacy layer for other chains' assets
- **L1 architecture** — Not an L2 rollup or smart contract protocol

---

## Backlinks

Sources:
- `raw/articles/Private, anonymous, and easy to use cryptocurrency.md`
- `raw/articles/From Aztec to Zcash_ The year pragmatic privacy took root.md`
