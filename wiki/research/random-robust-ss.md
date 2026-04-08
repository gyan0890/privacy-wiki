# Random Robust Secret Sharing with Perfect Privacy and its Applications

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/Random_Robust_SS.pdf`
**Authors:** Mohammad Hassan Ameri, Jeremiah Blocki (Purdue University)
**Related:** [[concepts/cryptographic-primitives]], [[research/privada]]

---

## Abstract

This paper introduces **Random Robust Secret Sharing (RRSS)** — a secret sharing scheme that achieves **(t−1)-perfect privacy** with robustness against **random corruption** of shares. Applications include **fuzzy password-authenticated key exchange (fPAKE)** and conditional encryption.

---

## Background: Secret Sharing

**Shamir Secret Sharing** (the classical scheme) splits a secret into `n` shares such that:
- Any `t` shares can reconstruct the secret.
- Fewer than `t` shares reveal nothing.

**Robust** secret sharing adds: even if some shares are corrupted (tampered with), the secret can still be reconstructed correctly (or the corruption detected).

**Perfect privacy** means: corrupted shares provide *zero* information about the secret — not just negligible, but exactly zero.

---

## Key Contribution: RRSS

**Random Robust Secret Sharing (RRSS)** introduces a new regime:

| Property | Requirement |
|---|---|
| Privacy | (t−1)-perfect: fewer than t shares reveal nothing |
| Robustness | Against **random** corruption (not adversarial) |
| Efficiency | First efficient construction for arbitrary Hamming distances |

The key distinction: prior robust secret sharing schemes protect against *adversarial* corruption (an attacker who strategically corrupts shares). RRSS focuses on *random* corruption — shares damaged by noise, transmission errors, or memoryless corruption.

This makes RRSS more efficient for applications where the threat model involves noisy channels rather than active attackers.

---

## Applications

### 1. Fuzzy Password-Authenticated Key Exchange (fPAKE)
Traditional password authentication requires exact matches. **fPAKE** allows authentication with a "fuzzy" password — one that's close to but not exactly the stored version. Applications:

- **Biometric authentication** — Fingerprints and iris scans vary slightly each reading; fuzzy matching is essential.
- **Voice authentication** — Voice prints are noisy.
- **Passphrase disambiguation** — Tolerate minor typing errors or variations.

RRSS enables secure fPAKE by allowing the secret (cryptographic key) to be split into shares that can tolerate noisy reconstruction.

### 2. Conditional Encryption
A form of encryption where the message can be decrypted only if the decryptor possesses a value within a certain distance (Hamming distance) of a threshold. Applications:

- Encrypting data to a biometric — only the person whose scan matches within tolerance can decrypt.
- Privacy-preserving access control in IoT (allow decryption if device ID is close to expected value).

---

## Technical Details

- Uses **Hamming distance** as the error metric.
- Achieves tight bounds: the construction is efficient precisely because it focuses on random (not adversarial) corruption.
- Security proofs are information-theoretic, providing strong guarantees.

---

## Relevance to Privacy Ecosystem

RRSS sits at the intersection of secret sharing and practical authentication:
- **Hardware wallet recovery** — Sharing recovery seeds with fuzzy tolerance for input errors.
- **Private key backup** — Secret sharing for private keys where shares may be partially corrupted over time.
- **Biometric-tied private keys** — Using biometric data as a key derivation source with fuzzy matching.

While not directly about blockchain, these applications have direct relevance to key management in privacy-preserving systems.

---

## Backlinks

Source: `raw/papers/Random_Robust_SS.pdf`
