# PlasmaBlind: A Private Layer 2 With Instant Client-Side Proving

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/PlasmaBlind.pdf`
**Authors:** Pierre Daix-Moreux (Ethereum Foundation), Chengru Zhang (University of Hong Kong)
**Related:** [[concepts/zero-knowledge-proofs]], [[protocols/aztec-network]], [[chains/starknet]], [[research/shielded-csv]]

---

## Abstract

PlasmaBlind is a **private Layer 2 protocol** that achieves **sub-100ms proving times on consumer hardware**. It combines Plasma's off-chain architecture with ZK proofs and folding schemes to provide transaction privacy with instant, client-side proof generation.

---

## Background

Plasma is an older Ethereum L2 architecture (pre-dating rollups) where users maintain their own state and can exit to mainnet. Plasma was largely superseded by rollups due to complexity. PlasmaBlind revisits the Plasma architecture with modern ZK techniques to unlock a key property: **client-side proving without trusted operators**.

---

## Key Contributions

### 1. Sub-100ms Client-Side Proving
The paper's headline achievement: generating a ZK proof of transaction validity in under **100ms on consumer hardware** (laptop/phone). This is practical for real-time UX.

Achieved through:
- **Folding schemes** — An efficient proof composition technique (related to Nova/SuperNova) that allows incremental proof generation without the overhead of recursive SNARKs.
- Minimal proof complexity per transaction.

### 2. Proof-Carrying Data (PCD) + IVC
Uses **Incrementally Verifiable Computation (IVC)** where each transaction proof includes proof of all prior history. This allows:
- Instant verification of the entire chain state.
- No need to replay transaction history.
- Efficient synchronization after being offline.

### 3. Privacy via BlindFold Technique
The "BlindFold" technique:
- Hides transaction amounts, senders, and receivers.
- Uses Merkle trees for state management.
- Enables private exits: leaving the L2 doesn't reveal transaction history.

### 4. Instant Exits
Unlike traditional Plasma (which required long challenge periods), PlasmaBlind allows users to exit instantly to Ethereum while maintaining privacy, using ZK proofs to demonstrate valid ownership without revealing history.

---

## Comparison with Other Private L2s

| Feature | PlasmaBlind | Aztec (Ignition) | Starknet |
|---|---|---|---|
| Proving location | Client-side | Client-side (PXE) | Server-side |
| Proving time | <100ms | Seconds | Seconds-minutes |
| Privacy model | Full transaction privacy | Full transaction privacy | Optional (STRK20) |
| Architecture | Plasma-based | Custom L2 | ZK-Rollup |
| Smart contracts | ❌ | ✅ | ✅ |

---

## Significance

PlasmaBlind is significant because it demonstrates that **instant, mobile-compatible ZK proving is achievable**. This removes a major UX barrier: if generating privacy proofs requires minutes on a server, privacy tools will remain niche. If they take 100ms on a phone, they can become mainstream.

The folding-scheme approach used here is a frontier technique also explored in projects like Lurk (Protocol Labs) and ESP (Ethereum).

---

## Backlinks

Source: `raw/papers/PlasmaBlind.pdf`
