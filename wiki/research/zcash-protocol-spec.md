# Zcash Protocol Specification

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/protocol.pdf`
**Version:** 2025.6.3-143-g4aecfb
**Authors:** Daira-Emma Hopwood, Sean Bowe, Taylor Hornby, Nathan Wilcox (Electric Coin Company)
**Related:** [[coins/zcash]], [[concepts/zk-snarks]], [[concepts/halo-proving-system]], [[concepts/cryptographic-primitives]]

---

## Overview

The Zcash Protocol Specification is the authoritative technical reference for the Zcash protocol. This document specifies all protocol behavior after the following network upgrades: Overwinter, Sapling, Blossom, Heartwood, Canopy, NU5 (Network Upgrade 5), NU6, and NU6.1.

This is the primary source document for implementation of the Zcash protocol.

---

## Protocol Components Specified

### Shielded Payment Protocols

The specification covers three generations of Zcash's shielded payment system:

| Protocol | Pool | Status |
|---|---|---|
| Sprout | Legacy shielded pool | Deprecated (no new deposits) |
| Sapling | Second-generation shielded pool | Active |
| Orchard | Third-generation shielded pool (Halo 2) | Active (recommended) |

### Consensus Rules
- Block validation
- Transaction validation (transparent and shielded)
- Equihash proof-of-work validation
- Chain selection

### Cryptographic Primitives Specified
- **zk-SNARKs** — Complete specification of proof generation and verification circuits for each pool.
- **Commitment schemes** — Note commitment construction for Sprout, Sapling, and Orchard.
- **Nullifier derivation** — How spending a note produces an unlinkable nullifier.
- **Key derivation** — Hierarchical deterministic key derivation from spending keys, viewing keys, and incoming viewing keys.
- **Note encryption** — How transaction outputs are encrypted for the recipient.
- **Unified addresses** — Specification of the multi-pool address format.

### Equihash PoW
The Zcash proof-of-work algorithm:
- Memory-hard to resist ASIC dominance (though Zcash ASICs now exist)
- Parameterized (Equihash-200,9 for mainnet)
- Designed for CPU/GPU mining accessibility

---

## Key Protocol Properties

### Balance Security
The specification proves that the total value in the transparent and shielded pools is bounded by the total emission schedule. No coins can be created except through the block reward. ZK proofs ensure shielded transaction validity without revealing amounts.

### Privacy Guarantees

For Sapling/Orchard shielded transactions:
- **Sender privacy** — Nullifiers reveal spending without revealing which note was spent.
- **Receiver privacy** — Note commitments reveal nothing about the recipient.
- **Amount privacy** — Values are hidden behind commitments and verified by ZK proofs.
- **Memo privacy** — The 512-byte encrypted memo field is private.

### Transparent Addresses
Standard Bitcoin-compatible UTXO model; fully public. The specification explicitly distinguishes transparent transactions (no privacy guarantees) from shielded transactions.

---

## Notable Technical Details

### Sapling Circuit
The Sapling shielded transfer circuit proves:
1. The prover knows the spending key for an existing note commitment.
2. The output commitments correspond to valid notes.
3. The value balance is consistent (no new coins created).
4. Randomness was used correctly (preventing re-use attacks).

### Orchard / Halo 2
The Orchard pool replaces Sapling's Groth16 proving system with Halo 2:
- No trusted setup required.
- Uses the Pallas and Vesta elliptic curves (Pasta curves).
- Enables recursive proof composition.
- Implements the "Action" transaction model (unifying spend and output into single actions).

---

## Document Use

This specification is used by:
- Zcash core developers implementing protocol changes
- Third-party wallet and exchange developers
- Academic researchers studying ZK blockchain protocols
- Auditors verifying protocol correctness

---

## Backlinks

Source: `raw/papers/protocol.pdf`
Related: [[coins/zcash]], [[concepts/zk-snarks]], [[concepts/halo-proving-system]]
