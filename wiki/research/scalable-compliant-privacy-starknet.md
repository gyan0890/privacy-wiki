# Scalable Compliant Privacy on Starknet

**Category:** Research Papers
**Related:** [[chains/strk20]], [[chains/starknet]], [[concepts/zero-knowledge-proofs]], [[concepts/zk-snarks]]
**Authors:** Lior Goldberg, Maya Dotan, Ittay Dror, Gideon Kaempfer, Nir Levi, Noa Oved, Arad Reder, Anat Veredgorn, Noa Wolfgor
**Organization:** StarkWare
**Published:** March 2026
**Paper:** `raw/papers/2026-474.pdf`

---

## Summary

This paper introduces the STRK20 privacy protocol — a shielded payment layer for Starknet that achieves privacy, scalability, and regulatory compliance simultaneously. The design is grounded in four protocol properties (Privacy, Scalability, Compliance, and Integrity) and implemented using Starknet's native Cairo language and the Stwo STARK prover.

The central claim is that previous privacy systems have treated compliance as an afterthought or adversary. STRK20 treats it as a first-class design constraint, arguing that **compliant privacy** is the only viable path to mainstream adoption.

---

## Core Protocol Properties

The paper specifies four properties the protocol must satisfy:

**Privacy** — Users' token balances, transaction amounts, counterparty addresses, and activity timing are hidden from all parties except those with explicit viewing authorization.

**Scalability** — The system must remain performant as the privacy pool grows. Note discovery cost scales with the user's own activity (`O(user activity)`), not total pool size — achieved through the channel architecture.

**Compliance** — Authorized parties (auditing entities) can reconstruct a user's complete transaction history on legal request. Forward-tracing (deposit → current state) and backward-tracing (withdrawal → original deposits) are both supported. Threshold encryption enables multi-party auditing.

**Integrity** — The protocol guarantees that no note can be double-spent, and that all state transitions are valid. Enforced by STARK proofs verified on-chain.

---

## Architecture Overview

The system has three components:

### Privacy Pool Contract

A single Starknet smart contract that holds:
- Encrypted notes (the UTXO-style value units)
- A nullifier set (spent note registry)
- Channel registry (note discovery metadata)

The contract validates STARK proofs before accepting any state transition. It never has access to plaintext note contents.

### Client-Side Proving (Stwo)

All proofs are generated on the user's device using the **Stwo prover** — StarkWare's optimized STARK prover implementation. The proving is done in **Cairo**, Starknet's native programming language.

This matters for two reasons:
1. The proving server never sees private inputs (balances, keys, transaction details).
2. The same language and prover used for STRK20 are used throughout the rest of Starknet — no separate trusted component to audit.

### Compliance Framework

Users escrow their viewing keys to an auditing entity's public key `K_audit` during account setup (`SetViewingKey` action). The auditing entity can decrypt these on legal request to reconstruct transaction history.

---

## The Note Model

Value in STRK20 is represented as **notes**: immutable records containing `(owner: Starknet address, token: ERC-20 address, amount: u128)`.

Notes are created by `Deposit` or `CreateNote` actions and destroyed by `UseNote`. A spent note cannot be reused — its nullifier is published on-chain and permanently recorded in the nullifier set.

**Nullifier derivation:**
```
nullifier = H1(channel, token, index, note_key)
```

The nullifier is deterministic (same note always produces same nullifier) and unlinkable (reveals nothing about the note's contents).

---

## Note Discovery: The Channel Architecture

The paper identifies note discovery as a core scalability challenge: how does a recipient find notes addressed to them, without scanning the entire pool?

The solution is **channels**: persistent, unidirectional, sender→recipient communication structures.

```
Channel: Alice → Bob
  Subchannel (USDC): notes [0, 1, 2, 3, ...]
  Subchannel (ETH):  notes [0, 1, ...]
```

A channel is established once per sender-recipient pair. After that:
- Sender assigns notes sequential indices within the relevant subchannel.
- Recipient scans only their own channels, not the full pool.
- Discovery cost: `O(number of channels × notes per channel)` for a given user.

Channel metadata (token types, index hints) is encrypted end-to-end using **ECDH on the STARK curve**. Sequential indices also provide auditability: an auditor can verify no notes were omitted from a disclosed channel.

---

## Encryption

The paper uses two cryptographic primitives, both native to the STARK curve:

**Hash-and-add symmetric encryption** for note amounts:
- Amounts are encrypted by adding a pseudorandom pad derived from a shared secret.
- Homomorphic property: encrypted amounts can be summed without decryption.

**ECDH key agreement** for channel and subchannel establishment:
- Shared secret derived from sender's private key + recipient's public key (or vice versa).
- Shared secret encrypts all channel metadata.

**Asymmetric encryption to `K_audit`** for viewing key escrow:
- User's `vk_priv` is encrypted to the auditing entity's public key.
- Only the entity with `K_audit_priv` can decrypt.

---

## Transaction Structure

Every STRK20 transaction is an ordered sequence of typed actions:

| Action | Description |
|---|---|
| `SetViewingKey` | Register/rotate viewing key; escrow to auditing entity |
| `OpenChannel` | Establish sender→recipient channel on STARK curve |
| `OpenSubchannel` | Create token-specific subchannel |
| `Deposit` | Move public ERC-20 tokens into the privacy pool |
| `UseNote` | Spend one or more notes (publishes nullifiers) |
| `CreateNote` | Create new notes for recipients |
| `Withdraw` | Move tokens from privacy pool to public address |

The strict enforced ordering is both a correctness requirement and a compliance feature: the full transaction sequence can be reconstructed by an auditor with the appropriate viewing keys.

---

## Anonymous DeFi

The paper extends the basic payment model to support **atomic DeFi interactions** directly from the privacy pool.

The key insight: because STRK20 operates within Starknet's execution environment (not a separate rollup or sidechain), a single Cairo transaction can:

1. Spend a shielded note (`UseNote`)
2. Execute an AMM swap in an external Starknet contract
3. Deposit the proceeds as a new shielded note (`CreateNote`)

The user's identity is hidden via the paymaster. However, the paper is explicit that this achieves **anonymity** (identity privacy) but not full **amount privacy** — AMM mechanics require visible amounts at the swap interface. Full amount privacy in DeFi composability is identified as future work.

---

## Compliance: Tracing Mechanisms

The auditing framework supports two complementary trace operations:

**Forward trace**: Given a deposit transaction, an auditor with the appropriate viewing key can follow the chain of `UseNote` → `CreateNote` transitions to determine where the deposited funds currently reside. This answers: "What happened to these funds after they entered the pool?"

**Backward trace**: Given a withdrawal transaction, an auditor can reconstruct all deposits that contributed to it by traversing the note graph in reverse. This answers: "Where did this money come from?"

Together these satisfy standard AML/CFT investigation workflows: both origin and destination can be determined for any transaction involving the privacy pool.

**Threshold encryption** is discussed as an extension: the viewing key can be encrypted under a `t-of-n` threshold scheme, requiring cooperation among `t` auditing entities before decryption is possible. This supports multi-jurisdictional regulatory frameworks without unilateral surveillance capability.

---

## Virtual StarknetOS Execution Model

The proof architecture uses a **Virtual StarknetOS** model:

- The STRK20 transaction is represented as a simulated Starknet OS execution step.
- The Stwo prover generates a STARK proof that this simulated execution is valid.
- The on-chain verifier checks the proof and updates the pool state.

Because both the simulation and the real Starknet OS use Cairo and the Stwo prover, the trust boundary is minimal. There is no separate ZK circuit to audit — the privacy layer uses exactly the same proving infrastructure as the rest of the network.

---

## Key Contributions

The paper makes three novel contributions:

1. **Channel-based note discovery** that scales independently of pool size — solving a practical bottleneck that makes shielded pools impractical at scale.

2. **Native compliance architecture** where viewing keys and auditing are first-class protocol features, not retrofit additions — enabling the protocol to satisfy regulatory requirements without sacrificing cryptographic privacy guarantees.

3. **Anonymous DeFi composability** via atomic transactions that span the privacy pool and external Starknet protocols — extending shielded asset utility beyond simple transfers.

---

## Limitations and Future Work

The paper acknowledges several open areas:

- **Amount privacy in DeFi**: AMM interactions require visible amounts at swap boundaries. Full amount privacy requires DeFi protocols to natively support shielded inputs, which is not yet standard.
- **Client-side proving performance**: proof generation on consumer devices is feasible but adds latency. Prover optimization is ongoing work.
- **Multi-hop note tracing**: tracing through many intermediate parties in the note graph is computationally expensive for auditors; optimization is identified as future work.

---

## Significance

STRK20 is the first production-deployed privacy protocol that achieves all of: no trusted setup (STARKs), native compliance (viewing keys), atomic DeFi composability, and client-side proving. Each of these properties has been achieved individually by other systems; combining them in a single coherent protocol on a scalable L2 is the paper's primary contribution.

For practical purposes, it resolves the central tension that has blocked institutional adoption of private on-chain transactions: the belief that privacy and compliance are mutually exclusive. STRK20 demonstrates architecturally that they are not.

---

## See Also

- [[chains/strk20|STRK20 Protocol]] — Full technical reference
- [[chains/starknet-use-cases|STRK20 Use Cases]] — Applied use cases from payroll to AI agents
- [[chains/starknet|Starknet Overview]] — Network context
- [[concepts/zero-knowledge-proofs|Zero-Knowledge Proofs]] — Foundational concepts
