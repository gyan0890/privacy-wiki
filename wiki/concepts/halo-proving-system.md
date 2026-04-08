# Halo Proving System

**Category:** [[_index#foundational-concepts|Foundational Concepts]]
**Related:** [[concepts/zk-snarks]], [[concepts/zero-knowledge-proofs]], [[coins/zcash]]
**Introduced by:** Electric Coin Co. (Sean Bowe, Jack Grigg, Daira Hopwood), 2019

---

## Overview

**Halo** (and its successor **Halo 2**) is a zero-knowledge proving system that eliminates the need for a [[concepts/zk-snarks#the-trusted-setup-problem|trusted setup ceremony]] while maintaining practical performance. It was first described in a paper by Sean Bowe, Jack Grigg, and Daira-Emma Hopwood at Electric Coin Co. in 2019 and deployed in [[coins/zcash]]'s Orchard shielded pool in May 2022 (Network Upgrade 5).

This was a landmark: the first production blockchain deployment of a setup-free, recursively composable ZK proving system.

---

## The Problem Halo Solves

Traditional [[concepts/zk-snarks|zk-SNARKs]] require a one-time trusted setup that generates "toxic waste" — secret randomness that, if retained, could allow an attacker to silently counterfeit coins. Multi-party ceremonies reduce this risk but never eliminate it entirely.

Halo removes this requirement. The system's security relies only on standard cryptographic hardness assumptions (discrete logarithm), with no special randomness that must be destroyed.

---

## Key Innovation: Recursive Proof Composition

Halo's core technical breakthrough is **nested amortization** (also called **recursive proof composition**): the ability for a single proof to attest to the correctness of an unbounded number of other proofs.

This has two important consequences:

1. **Scalability** — Proofs of large computations can be compressed into a single small proof, without the cost growing with computation size.
2. **Incremental Verifiability** — A prover can continuously extend a proof as new blocks are added, allowing a "proof of the entire chain history" that remains constant in size.

---

## Halo vs. Halo 2

| Feature | Halo (2019) | Halo 2 (deployed 2022) |
|---|---|---|
| Trusted Setup | None | None |
| Recursive Composition | Yes | Yes (improved) |
| Proof Size | ~1 KB | ~1 KB |
| Proving Time | Practical | Improved |
| Deployment | Research paper | Zcash Orchard (NU5) |

Halo 2 is the production version. It uses the **Pasta curves** (Pallas and Vesta), a pair of elliptic curves designed specifically for efficient recursive proof composition.

---

## Deployment in Zcash Orchard

The **Orchard** shielded pool (Zcash's third-generation shielded protocol) uses Halo 2 as its proving system. It was activated in **Network Upgrade 5 (NU5)** on May 31, 2022.

Key improvements over the Sapling pool (which uses Groth16):
- No trusted setup — users don't need to trust any ceremony
- Recursive composability enables future cross-chain proofs
- Foundation for the Zcash "unified address" system (see [[coins/zcash#unified-addresses]])

---

## Broader Impact

Halo's approach has influenced other ZK systems:

- The **Ethereum Foundation** funded research into Halo-based approaches
- **Protocol Labs** (Filecoin) and the **Filecoin Foundation** collaborated on the recursion research
- The technique is referenced in discussions of ZK-EVM scaling

---

## Collaborators

| Person | Affiliation | Role |
|---|---|---|
| Sean Bowe | Electric Coin Co. | Co-inventor |
| Jack Grigg | Electric Coin Co. | Co-inventor |
| Daira-Emma Hopwood | Electric Coin Co. | Co-inventor, protocol author |
| Protocol Labs | External | Recursion research collaboration |
| Ethereum Foundation | External | Research support |

---

## Backlinks

Sources covering this concept:
- `raw/articles/What is Halo for Zcash_.md`
- `raw/articles/What are zk-SNARKs_.md`
- `raw/papers/protocol.pdf` (Zcash Protocol Specification)
