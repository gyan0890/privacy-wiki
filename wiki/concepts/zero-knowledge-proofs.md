# Zero-Knowledge Proofs

**Category:** [[_index#foundational-concepts|Foundational Concepts]]
**Related:** [[concepts/zk-snarks]], [[concepts/halo-proving-system]], [[concepts/cryptographic-primitives]]
**Used in:** [[coins/zcash]], [[protocols/aztec-network]], [[protocols/privacy-pools]], [[chains/starknet]]

---

## What Is a Zero-Knowledge Proof?

A zero-knowledge proof (ZKP) is a cryptographic protocol that allows one party — the **prover** — to convince another party — the **verifier** — that a statement is true, without revealing *any* information beyond the validity of the statement itself.

The classic intuition: imagine proving you are over 21 years old without showing your driver's license or date of birth. The verifier learns only that the claim is true; nothing else is disclosed.

Formally, a ZKP satisfies three properties:

1. **Completeness** — If the statement is true and both parties follow the protocol, the verifier will be convinced.
2. **Soundness** — If the statement is false, no cheating prover can convince the verifier (except with negligible probability).
3. **Zero-knowledge** — If the statement is true, the verifier learns nothing beyond that fact.

---

## Why ZKPs Matter for Blockchain Privacy

Public blockchains like Bitcoin record every transaction in full on a globally visible ledger. Anyone can observe sender, receiver, and amount. Zero-knowledge proofs break this link: they allow the network to verify that a transaction is valid (no counterfeiting, no double-spending) without revealing *who* transacted or *how much* was sent.

This is the core innovation behind [[coins/zcash]]'s shielded transactions: the blockchain carries a proof that a valid transaction occurred, not the transaction details themselves.

---

## Interactive vs. Non-Interactive ZKPs

Early ZKP constructions required back-and-forth communication (interactive proofs). For blockchains, this is impractical — proofs must be published and verifiable by anyone at any time.

**Non-interactive ZKPs** solve this: the prover generates a single message (the proof) and posts it to the chain. Anyone can verify it without further communication. The dominant non-interactive variant used in blockchain applications is [[concepts/zk-snarks|zk-SNARKs]].

---

## Applications in the Privacy Stack

| Application | How ZKPs Are Used |
|---|---|
| [[coins/zcash]] Shielded Transactions | Prove a transaction is valid without revealing sender, receiver, or amount |
| [[protocols/aztec-network]] | Confidential smart contract execution on Ethereum |
| [[protocols/privacy-pools]] | Prove membership in an "approved" set without revealing which deposit you made |
| [[chains/starknet]] | Bundle thousands of transactions into one proof for Ethereum |
| [[research/plasmablind]] | Private L2 with sub-100ms client-side proving |
| [[research/shielded-csv]] | Client-side validation with only 64 bytes on-chain |

---

## Key Terminology

- **Prover** — The party making a claim and generating the proof.
- **Verifier** — The party checking the proof.
- **Witness** — The secret information the prover knows (e.g., a private key or transaction details).
- **Statement** — The public claim being proved (e.g., "this transaction is valid").
- **Trusted Setup** — A one-time ceremony to generate public parameters for some ZKP systems. A potential vulnerability if the ceremony is compromised. Eliminated by [[concepts/halo-proving-system|Halo]].

---

## Backlinks

Sources covering this concept:
- `raw/articles/What are zero-knowledge proofs_.md`
- `raw/articles/What are zk-SNARKs_.md`
- `raw/articles/A Deep Dive into AZTEC Protocol_.md`
- `raw/articles/Privacy Pools Documentation.md`
- `raw/papers/protocol.pdf` (Zcash Protocol Specification)
