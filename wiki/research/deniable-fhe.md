# Deniable FHE: Tighter Deniability Analysis and TFHE-based Construction

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/2026-597.pdf`
**Authors:** Towa Toyooka, Yohei Watanabe (University of Electro-Communications), Mitsugu Iwamoto (AIST)
**Related:** [[concepts/cryptographic-primitives]], [[chains/starknet]]

---

## Abstract

This paper improves **Deniable Fully Homomorphic Encryption (DFHE)** — a cryptographic scheme that combines the properties of FHE (computation on encrypted data) and deniable encryption (the ability to produce fake keys that decrypt to different but plausible plaintexts).

Key results:
- **84% reduction in randomness size** through tighter deniability bounds.
- A new **TFHE-based construction** that is faster than the prior BGV-based approach.

---

## Background Concepts

### Fully Homomorphic Encryption (FHE)
FHE allows **computing on encrypted data without decrypting it**. A server holding encrypted data can perform operations (addition, multiplication) and return an encrypted result — the server never sees the plaintext.

Applications:
- Privacy-preserving cloud computing
- Machine learning on private data
- Private smart contract execution (referenced in [[chains/starknet]]'s roadmap)

### Deniable Encryption
Deniable encryption allows a user to produce **two valid decryption keys**: one for the real message, and a "fake" key for a different, plausible message. If coerced into revealing a key, the user can reveal the fake key without the coercer being able to detect the deception.

This is relevant for:
- Whistleblowers who may be compelled to reveal keys
- Journalists handling sensitive sources
- Activists in authoritarian regimes

### Deniable FHE (DFHE)
Combines both properties: a scheme where you can compute on encrypted data *and* the encryption is deniable. This is significantly harder to construct than either property alone.

---

## Key Contributions

### Tighter Deniability Analysis
Prior constructions overestimated the randomness needed for security. This paper provides tighter analysis, reducing randomness requirements by **84%** without compromising security. This dramatically improves practical efficiency.

### TFHE-based Construction
TFHE (Torus Fully Homomorphic Encryption) has very fast **bootstrapping** — the operation that "refreshes" encrypted values to prevent noise accumulation. The paper's TFHE-based DFHE construction:
- Outperforms the prior BGV-based construction in speed.
- Provides formal security proofs and deniability guarantees.
- Is more practically deployable.

---

## Relevance to Privacy Blockchain Ecosystem

Deniable FHE represents an advanced direction for privacy infrastructure:

- **Coercion resistance** — Systems using DFHE could resist legal or physical coercion to reveal private keys.
- **FHE for private smart contracts** — As chains like [[chains/starknet]] explore FHE for private computation, deniability adds an extra protection layer.
- **Private state channels** — Lightning Network-style channels with coercion-resistant encryption.

This is relatively nascent but points toward a future where cryptographic coercion resistance is practical.

---

## Backlinks

Source: `raw/papers/2026-597.pdf`
