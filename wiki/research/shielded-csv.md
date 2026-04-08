# Shielded CSV: Private and Efficient Client-Side Validation

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/2025-068.pdf`
**Authors:** Jonas Nick (Blockstream), Liam Eagen (Alpen Labs), Robin Linus (ZeroSync)
**Related:** [[coins/bitcoin-privacy]], [[concepts/zero-knowledge-proofs]], [[concepts/cryptographic-primitives]]

---

## Abstract

This paper introduces **Shielded CSV** — the first **client-side validation (CSV)** protocol that is also private. A key achievement: only **64 bytes** of data per transaction need to be written to the blockchain, dramatically reducing on-chain footprint while preserving full transaction privacy.

---

## Background: Client-Side Validation (CSV)

In traditional blockchains, all nodes validate all transactions. Client-side validation shifts this: instead of every node checking every transaction, only the relevant parties (sender and receiver) validate transactions involving their assets.

This improves scalability but existing CSV protocols are not private — transaction history is still visible to validators.

---

## Key Contributions

1. **Privacy in CSV** — First demonstration that client-side validation can be combined with transaction privacy.

2. **64 bytes on-chain per transaction** — Extremely compact on-chain footprint. Bitcoin transactions are typically 200–250 bytes; Zcash shielded transactions are ~2KB.

3. **Proof Carrying Data (PCD)** — The paper uses PCD as an abstraction for efficient, composable proofs. Each transaction carries a proof of its entire history without the verifier needing to check the full chain.

4. **Signature Half-Aggregation with Commitments** — A novel technique combining signature aggregation with commitment schemes for efficient batch verification.

5. **IoS-Accumulator** — An "Incremental on-chain State Accumulator" enabling efficient proof composition across transactions.

6. **Advanced Spending Policies** — Supports shared accounts (multisig) and atomic swaps natively within the protocol.

---

## Technical Mechanisms

### Proof Carrying Data
Each transaction output carries a compact proof that it was correctly generated from valid inputs. Receivers can verify the entire provenance of funds by checking only the proof, not replaying the transaction history.

### 64-Byte On-Chain Commitment
Rather than publishing full transaction details, Shielded CSV publishes a tiny commitment on-chain. This is sufficient to anchor the proof chain while hiding all transaction details.

---

## Significance for Bitcoin Privacy

Current Bitcoin privacy techniques (CoinJoin, Lightning) are far from ideal. Shielded CSV represents a potential path to:
- Strong transaction privacy on Bitcoin
- Without changing Bitcoin's base-layer protocol significantly
- With minimal on-chain footprint

This paper is particularly relevant as Bitcoin's privacy limitations (see [[coins/bitcoin-privacy]]) become more widely understood.

---

## Limitations and Open Questions

- Full implementation not yet deployed.
- PCD proofs require significant computation.
- Interaction model with Bitcoin mainnet still to be specified in deployment context.

---

## Backlinks

Source: `raw/papers/2025-068.pdf`
