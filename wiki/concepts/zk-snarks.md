# zk-SNARKs

**Category:** [[_index#foundational-concepts|Foundational Concepts]]
**Related:** [[concepts/zero-knowledge-proofs]], [[concepts/halo-proving-system]], [[concepts/cryptographic-primitives]]
**Used in:** [[coins/zcash]], [[protocols/aztec-network]], [[protocols/privacy-pools]]

---

## Definition

**zk-SNARK** stands for **Zero-Knowledge Succinct Non-Interactive Argument of Knowledge**.

Each word matters:

| Term | Meaning |
|---|---|
| **Zero-Knowledge** | The verifier learns nothing beyond the truth of the claim |
| **Succinct** | The proof is tiny (hundreds of bytes) and verifies in milliseconds |
| **Non-Interactive** | A single message from prover to verifier; no back-and-forth |
| **Argument of Knowledge** | The prover must actually *know* the witness, not just guess |

Together, these properties make zk-SNARKs the dominant choice for blockchain privacy: proofs are small enough to publish on-chain, verify cheaply, and don't require interaction.

---

## How zk-SNARKs Work (High Level)

1. **Arithmetic Circuit** — The computation to be proven (e.g., "this transaction spends only coins I own") is encoded as an arithmetic circuit.
2. **R1CS / QAP** — The circuit is converted into a quadratic arithmetic program, a polynomial representation.
3. **Proving Key / Verification Key** — Generated in a one-time [[#the-trusted-setup-problem|trusted setup]] ceremony. The proving key lets the prover generate proofs; the verification key lets anyone verify them.
4. **Proof Generation** — The prover uses the proving key and their private witness to produce a compact proof.
5. **Verification** — Anyone with the verification key can check the proof in milliseconds.

---

## The Trusted Setup Problem

Traditional zk-SNARKs (as used in [[coins/zcash]]'s Sprout and Sapling protocols) require a **trusted setup ceremony**: a multi-party computation that generates public parameters. The randomness used in this ceremony — sometimes called "toxic waste" — must be destroyed afterward.

If any participant in the ceremony retains the toxic waste, they could silently create counterfeit coins without detection. This is a systemic risk, mitigated by:

- **Multi-party ceremonies** (Powers of Tau) — Hundreds or thousands of participants; the ceremony is safe as long as *any one* participant honestly destroys their randomness.
- **Eliminating the setup entirely** — See [[concepts/halo-proving-system]].

---

## zk-SNARKs in Zcash

[[coins/zcash]] was the first major real-world deployment of zk-SNARKs (2016). The protocol has gone through three proving systems:

| Protocol | zk-SNARK System | Trusted Setup? |
|---|---|---|
| Sprout (2016) | BCTV14 | Yes (original ceremony) |
| Sapling (2018) | Groth16 | Yes (Powers of Tau) |
| Orchard (2022) | Halo 2 | **No** |

The Orchard shielded pool, deployed in Network Upgrade 5 (May 2022), uses [[concepts/halo-proving-system|Halo 2]] and is the first production deployment of a setup-free proving system in Zcash.

---

## Groth16

The most widely used zk-SNARK variant (by Jens Groth, 2016). Used in Zcash's Sapling protocol, [[protocols/privacy-pools]], and many others. Key characteristics:

- Very small proof size (~192 bytes)
- Fast verification via bilinear pairings (~40M operations)
- Requires circuit-specific trusted setup

[[protocols/privacy-pools]] uses Groth16 with the BLS12-381 curve, where a single bilinear pairing verification takes approximately 40 million Soroban instructions on Stellar.

---

## PlonK

A universal and updatable variant of zk-SNARKs, notable for requiring only a *universal* (not circuit-specific) trusted setup. Used as the proving system backend in [[protocols/aztec-network]] (via the Barretenberg library).

---

## Key Differences from Other ZKP Systems

| System | Setup Required | Proof Size | Key Use |
|---|---|---|---|
| Groth16 | Circuit-specific | ~192 bytes | Zcash Sapling, Privacy Pools |
| PlonK | Universal | ~500 bytes | Aztec Network |
| **Halo 2** | **None** | ~1 KB | Zcash Orchard |
| STARKs | None | ~40 KB | Starknet |

---

## Backlinks

Sources covering this concept:
- `raw/articles/What are zk-SNARKs_.md`
- `raw/articles/What are zero-knowledge proofs_.md`
- `raw/articles/What is Halo for Zcash_.md`
- `raw/articles/A Deep Dive into AZTEC Protocol_.md`
- `raw/papers/protocol.pdf` (Zcash Protocol Specification)
