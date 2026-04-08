# Research Papers — Source Index

**Category:** [[_index#research-papers|Research Papers]]

One-paragraph digest of every research paper in `raw/papers/`.

---

## 2025-068.pdf — Shielded CSV
**Full article:** [[research/shielded-csv]]

Jonas Nick, Liam Eagen, and Robin Linus introduce the first private client-side validation (CSV) protocol, requiring only 64 bytes of blockchain data per transaction. Using Proof Carrying Data (PCD) and a novel IoS-Accumulator, the protocol allows transaction history to be compressed into a constant-size proof carried by each output. This is a significant advance for Bitcoin privacy: it demonstrates that strong transaction privacy with minimal on-chain footprint is achievable without changing Bitcoin's base protocol.

---

## 2026-579.pdf — PRIVADA
**Full article:** [[research/privada]]

Betül Aşkın Özdemir et al. present PRIVADA, a privacy-preserving data aggregation system based on Secure Multi-Party Computation (SPDZ framework). The system supports multiple simultaneous data customers with selective disclosure, achieves 12–15x speedup over prior art, and provides three-layer privacy guarantees (input privacy, user anonymity, output privacy) under a malicious security model. This is relevant to any system computing aggregate statistics over private user data.

---

## 2026-585.pdf — Image Encryption
**Full article:** [[research/image-encryption]]

Alexandra Boldyreva, Kaishuo Cheng, and Jehad Hussen (Georgia Tech) present the first provably-secure format-preserving authenticated encryption scheme for JPEG images that tolerates compression. The ciphertext is a valid JPEG, survives lossy compression, and can be correctly decrypted afterward. A practical browser plugin implementation is provided. This addresses a gap in real-world private image storage on platforms that apply automatic compression.

---

## 2026-597.pdf — Deniable FHE
**Full article:** [[research/deniable-fhe]]

Towa Toyooka, Yohei Watanabe, and Mitsugu Iwamoto improve Deniable Fully Homomorphic Encryption (DFHE), reducing randomness requirements by 84% through tighter deniability analysis and introducing a faster TFHE-based construction. DFHE combines FHE (computation on encrypted data) with deniability (ability to produce fake keys that decrypt plausibly). The work is relevant to coercion-resistant privacy systems and private smart contract computation.

---

## FLOSS.pdf — Fast Secret-Shared Shuffling
**Full article:** [[research/floss]]

Ian Chang et al. present FLOSS, achieving the fastest known malicious-secure 2PC shuffling: 2^20 elements in under 500ms (800x faster than alternatives). Using an arithmetic permutation circuit abstraction and pre-computed authenticated shuffle tuples, the online phase becomes extremely efficient. This is a critical building block for mixnets, anonymous credentials, private voting, and any system requiring unlinkable permutation of data.

---

## PlasmaBlind.pdf — Private L2 with Instant Proving
**Full article:** [[research/plasmablind]]

Pierre Daix-Moreux (Ethereum Foundation) and Chengru Zhang introduce PlasmaBlind, a private Layer 2 protocol with sub-100ms client-side proving on consumer hardware. Combining Plasma architecture with folding schemes and Proof-Carrying Data, the protocol provides full transaction privacy with instant exits. The sub-100ms proving time is a significant UX breakthrough, enabling privacy tools on mobile devices without perceptible delay.

---

## Privacy_Blanket.pdf — Optimal Shuffle Model Privacy
**Full article:** [[research/privacy-blanket]]

Pengcheng Su et al. (Peking University) analyze the optimal noise distribution for privacy in the shuffle model of differential privacy. They prove that uniform noise is optimal for near-uniform alphabets and establish tight information-theoretic bounds. The analysis extends to the shuffle-DP paradigm and cipher models, connecting the differential privacy and cryptographic protocol literatures. Results inform the design of privacy-preserving analytics systems and anonymity set requirements.

---

## Random_Robust_SS.pdf — Random Robust Secret Sharing
**Full article:** [[research/random-robust-ss]]

Mohammad Hassan Ameri and Jeremiah Blocki (Purdue) introduce Random Robust Secret Sharing (RRSS), achieving (t-1)-perfect privacy with robustness against random (not adversarial) corruption. This enables the first efficient constructions for arbitrary Hamming distances, with applications to fuzzy password-authenticated key exchange (biometric authentication) and conditional encryption (encrypt to a biometric). Relevant to key management in privacy systems and biometric-tied private keys.

---

## protocol.pdf — Zcash Protocol Specification
**Full article:** [[research/zcash-protocol-spec]]

Daira-Emma Hopwood, Sean Bowe, Taylor Hornby, and Nathan Wilcox (Electric Coin Company) provide the authoritative technical specification of the Zcash protocol, covering all network upgrades through NU6.1. The document specifies the Sprout, Sapling, and Orchard shielded payment protocols; Equihash proof-of-work; all cryptographic primitives (zk-SNARKs, commitment schemes, nullifier derivation, key derivation, note encryption); and unified address construction. This is the primary reference for Zcash implementers and researchers.
