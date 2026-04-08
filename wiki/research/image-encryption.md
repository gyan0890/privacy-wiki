# Format-Preserving Compression-Tolerating Authenticated Encryption for Images

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/2026-585.pdf`
**Authors:** Alexandra Boldyreva, Kaishuo Cheng, Jehad Hussen (Georgia Tech)
**Related:** [[concepts/cryptographic-primitives]]

---

## Abstract

This paper introduces the **first provably-secure format-preserving authenticated encryption (aIE) scheme specifically for images**. A key innovation: decryption tolerates JPEG compression — the encrypted image can be compressed and then correctly decrypted even though compression is a lossy operation.

---

## Problem Statement

Encrypting images for storage or transmission is straightforward. The hard problem is: what if the encrypted image gets **JPEG-compressed** (as happens routinely in cloud storage, social media, and CDNs)?

Standard encryption is brittle to compression: even one bit of difference in the ciphertext causes decryption to fail catastrophically. JPEG compression intentionally discards information, making decrypted images corrupt.

This is a practical problem for:
- Encrypted image storage in cloud platforms that automatically re-compress
- Privacy-preserving image sharing where the distribution channel applies compression
- Browser-based image privacy tools

---

## Key Contributions

### 1. Format-Preserving Authenticated Encryption (aIE)
The scheme produces a ciphertext that:
- **Looks like a valid JPEG image** — format-preserving, not distinguishable from a normal photo.
- **Authenticates** the content (AEAD properties — cannot be tampered without detection).
- **Survives compression** — decryption succeeds even after JPEG compression.

### 2. Provable Security
First formal security analysis of this type of scheme, with proofs against chosen-plaintext and chosen-ciphertext attacks.

### 3. Browser Plugin Implementation
Implemented as a practical browser plugin, enabling in-browser image encryption/decryption for web use cases.

### 4. Image Similarity Preservation
The encrypted images preserve some visual similarity properties (via feature vectors), allowing image-to-image search over encrypted datasets.

---

## Technical Mechanisms

### JPEG Compression and Encryption Interaction
JPEG compression operates in the frequency domain (DCT coefficients). The scheme:
- Encrypts image data in a way that JPEG compression changes predictably.
- The decryption algorithm accounts for the compression artifacts.
- Uses block permutation techniques to spread the encryption across the spatial domain.

---

## Relevance to Privacy Ecosystem

While not directly blockchain-focused, this paper addresses a fundamental gap in practical privacy tooling: most privacy schemes assume data integrity, but real-world systems introduce lossy transformations. The techniques here could apply to:
- Privacy-preserving media storage on decentralized storage networks (IPFS, Filecoin, Arweave)
- NFT metadata encryption where images may be reprocessed by display platforms
- Private image sharing with selective disclosure

---

## Backlinks

Source: `raw/papers/2026-585.pdf`
