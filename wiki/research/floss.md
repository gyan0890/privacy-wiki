# FLOSS: Fast Linear Online Secret-Shared Shuffling

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/FLOSS.pdf`
**Authors:** Ian Chang, Sela Navot (University of Washington), Alex Ozdemir (Max Planck Institute), Nirvan Tyagi (University of Washington)
**Related:** [[concepts/cryptographic-primitives]], [[research/privada]]

---

## Abstract

FLOSS achieves the **fastest known online permutations in the malicious-secure 2-party computation (2PC) setting**. It can shuffle **2^20 elements (≈1 million) in under 500ms** — approximately 800x faster than alternatives.

The key innovation is the **arithmetic permutation circuit abstraction** and an efficient preprocessing algorithm for **authenticated shuffle tuples**.

---

## Background: Secret-Shared Shuffling

Shuffling data is a fundamental privacy operation: it breaks linkability between inputs and outputs. If Alice has a list of entries and wants to shuffle them with the help of an untrusted server (without the server learning the mapping), she needs a **secret-shared shuffle protocol**.

Applications:
- Anonymous credential issuance
- Private database query answering
- Privacy-preserving audits
- E-voting systems
- Oblivious RAM (ORAM) constructions

The challenge: doing this securely against a *malicious* adversary (one who deviates from the protocol) while being fast enough for practical use.

---

## Key Contributions

### 1. Arithmetic Permutation Circuit Abstraction
FLOSS introduces a clean abstraction for permutation circuits in the arithmetic domain. This allows using standard MPC tools (secret sharing, multiplication triples) rather than specialized garbled circuits.

### 2. Authenticated Shuffle Tuples
A preprocessing technique: before the online protocol, the parties generate "authenticated shuffle tuples" — pre-computed values that enable the online shuffle phase to be extremely fast.

This is the key insight: most of the expensive computation moves to a preprocessing phase (which can be done offline), making the online phase very cheap.

### 3. Performance
- **500ms for 2^20 elements** in the online phase
- **800x faster** than prior best alternatives
- Malicious-secure under Universal Composability (UC) framework

---

## Relevance to Privacy Ecosystem

Fast shuffling is a building block for many privacy systems:

- **Mixnets** — Anonymous communication networks rely on efficient shuffling.
- **Private set intersection** — Shuffling prevents the other party from learning query patterns.
- **Anonymous credential systems** — Shuffles break the link between issuance and use.
- **Private voting** — Shuffle-based vote mixing (like Helios) benefits directly.
- **Privacy Pools** (see [[protocols/privacy-pools]]) — The association set construction is related to shuffling approaches.

FLOSS makes these applications practical at scale by removing the performance bottleneck in the shuffle step.

---

## Technical Notes

- **2PC setting:** Two parties (not more) — appropriate for client-server architectures.
- **UC security:** Proofs under Universal Composability framework, the strongest standard for composable cryptographic protocols.
- **Preprocessing model:** Most efficient when the expensive preprocessing can be done before the actual data is known.

---

## Backlinks

Source: `raw/papers/FLOSS.pdf`
