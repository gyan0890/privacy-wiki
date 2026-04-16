# STRK20: Scalable Compliant Privacy on Starknet

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[chains/starknet]], [[concepts/zero-knowledge-proofs]], [[concepts/zk-snarks]], [[research/scalable-compliant-privacy-starknet]]
**Developed by:** StarkWare
**Launched:** March 2026
**Specification:** ["Scalable Compliant Privacy on Starknet" (2026)](../research/scalable-compliant-privacy-starknet.md)

---

## What is STRK20?

STRK20 is a **privacy token standard** for Starknet that makes shielded balances, encrypted transfers, and compliance-grade audit trails first-class features of any ERC-20-style token on the network.

Where most "privacy" solutions are bolt-on layers — mixers, wrappers, separate rollups — STRK20 is a **native protocol primitive** built directly on Starknet's proving infrastructure. Any token can adopt the standard; privacy is opt-in at the token level, always on at the transaction level once you enter the privacy pool.

The design solves a problem that has blocked institutional and enterprise blockchain adoption for years: **you cannot have privacy and compliance at the same time on-chain**. STRK20's answer is that you can — by separating who can see what, and cryptographically enforcing those boundaries.

---

## Three Core Pillars

### 1. Privacy Pool Contract

The on-chain anchor. A single smart contract on Starknet that stores:

- **Encrypted notes** — the fundamental unit of value (see [Note Model](#the-note-model) below).
- **Nullifier set** — a registry of spent notes, preventing double-spending without revealing which note was spent.
- **Channel registry** — metadata for note discovery (see [Note Discovery](#note-discovery-channels)).

All balance information is encrypted. The contract enforces validity without ever learning what it holds.

### 2. Client-Side Proving

All STARK proofs are generated **on the user's own device** using the [Stwo prover](https://github.com/starkware-libs/stwo). The key implication: the proving server never sees the private inputs. No third party learns your balances, transaction graph, or keys.

This is only practical because:
- Stwo is a highly optimized STARK prover capable of running client-side.
- Cairo is the programming language of both the STRK20 circuits and Starknet itself — no separate circuit DSL, single unified codebase.

### 3. Compliance Framework

An optional but protocol-native auditing mechanism. Users escrow their **viewing keys** to a designated auditing entity during account setup. The auditor can, on legal request:

- **Forward-trace** from a deposit: follow the chain of notes forward to find current holdings.
- **Backward-trace** from a withdrawal: reconstruct all historical deposits that contributed to a given withdrawal.

Critically, this is **selective disclosure** — the auditor sees only what they are given keys to see, and cannot access the entire pool. Threshold encryption allows multi-party auditing (e.g., requiring 3-of-5 regulators to cooperate before a trace can be executed).

---

## The Note Model

STRK20 uses a **UTXO-inspired note model** rather than an account balance model. A note is an immutable record with three fields:

| Field | Type | Description |
|---|---|---|
| `owner` | Starknet address | Who can spend this note |
| `token` | ERC-20 contract address | Which token this note represents |
| `amount` | u128 (128-bit unsigned integer) | How much of the token |

Notes are **created once and spent entirely**. To send a partial amount, a transaction spends an existing note and creates two new ones — one for the recipient, one as change back to the sender. This mirrors Bitcoin's UTXO model but with encrypted amounts.

### Nullifiers

When a note is spent, a **nullifier** is derived and published:

```
nullifier = H1(c, token, i, k)
```

Where:
- `c` = channel identifier
- `token` = token contract address
- `i` = note index within the channel
- `k` = the note's spending key (secret)

The nullifier is deterministic and unique per note, but reveals nothing about the note's contents. The smart contract checks that a nullifier has not been published before accepting the spend.

---

## Note Discovery: Channels

A fundamental challenge with shielded pools: how does a recipient know they received a payment, without the pool broadcasting every note to everyone?

STRK20 solves this with **channels** — unidirectional, persistent links between a sender and a recipient.

### Channel Structure

```
Channel: sender → recipient (identified by Starknet address)
  └─ Subchannel: per token type
       └─ Notes: sequential index 0, 1, 2, …
```

A channel is established once between two parties. After that, the recipient only needs to scan **their own channels** — not the entire pool. Discovery cost scales with `O(user's own activity)`, not `O(pool size)`. This is critical for practical performance.

### Sequential Indexing

Notes within a subchannel are assigned sequential indices. This has a compliance benefit: the auditing entity can verify there are no gaps in the sequence, confirming that no notes were hidden from an audit trail.

### Key Derivation (ECDH)

Channel establishment uses **Elliptic Curve Diffie-Hellman (ECDH) on the STARK curve**. When a sender opens a channel:

1. Both parties derive a shared secret from their keys.
2. The shared secret encrypts all future note information sent over that channel.
3. The recipient recovers the note details using their own private key.

This means even the channel metadata (token type, index hints) is encrypted end-to-end.

---

## Encryption Schemes

STRK20 uses two encryption primitives, both operating on the STARK curve (native to Starknet):

| What is encrypted | Method |
|---|---|
| Note amounts | Symmetric hash-and-add encryption (homomorphism on felt252 values) |
| Channel/subchannel info | ECDH key agreement → symmetric encryption |
| Viewing key | Asymmetric encryption to auditing entity's public key `K_audit` |

The use of the STARK curve throughout means all cryptographic operations are **natively efficient inside Cairo circuits** — no curve switching, no expensive field conversions.

---

## Transaction Actions

Every STRK20 transaction is composed of a sequence of **typed actions**, executed in a strict enforced order:

| # | Action | What it does |
|---|---|---|
| 1 | `SetViewingKey` | Establishes or rotates the user's viewing key, escrowed to the auditor |
| 2 | `OpenChannel` | Creates a new sender→recipient channel |
| 3 | `OpenSubchannel` | Opens a token-specific subchannel within an existing channel |
| 4 | `Deposit` | Moves publicly held tokens into the privacy pool (creates notes) |
| 5 | `UseNote` | Spends one or more existing notes (publishes nullifiers) |
| 6 | `CreateNote` | Creates new notes for recipients |
| 7 | `Withdraw` | Moves tokens out of the privacy pool to a public Starknet address |

The enforced ordering is critical for compliance: every transaction can be fully reconstructed by an auditor with the appropriate viewing keys, in deterministic sequence.

---

## The Paymaster: Breaking the Identity Link

Even with encrypted balances, broadcasting a transaction from your own wallet leaks your Starknet address as the transaction originator. STRK20 breaks this link via the **paymaster service** — a native Starknet feature.

The flow:

1. User constructs and signs the transaction **off-chain**.
2. User sends the signed transaction to the **paymaster** via an off-chain channel.
3. Paymaster **broadcasts** the transaction to the network under its own address.
4. Network sees only: paymaster address → privacy pool contract. The actual user's address never appears on-chain.

Gas fees are covered by the paymaster (and reimbursed via the privacy pool). This is the **identity layer** of privacy — STRK20 hides not just balances but who is transacting.

---

## Anonymous DeFi

One of the most significant capabilities of STRK20: **interacting with DeFi protocols directly from the privacy pool**, in a single atomic transaction.

The canonical example is an AMM swap:

1. `UseNote` — spend a shielded USDC note.
2. Atomic swap via an AMM (e.g., swap USDC → ETH at the current pool price).
3. `CreateNote` — the ETH proceeds are deposited as a new shielded note.

All three steps execute atomically. The transaction is **anonymous** (identity hidden via paymaster), though not fully private — AMM mechanics require amount disclosure at the swap boundary. Full amount privacy in DeFi remains an open research area.

This composability is unique: STRK20 is not a sidechain or separate environment. It operates within the Starknet execution environment, meaning any Starknet protocol can be used.

---

## Virtual StarknetOS Execution Model

The proving system uses a clever architecture called the **Virtual StarknetOS**:

- The client-side STARK proof simulates the execution of a Starknet OS step on the user's device.
- This produces a proof that the user's private actions were valid, without revealing those actions.
- The on-chain verifier checks the STARK proof and updates the pool state accordingly.

Because Cairo is the language of both the privacy circuits and Starknet itself, the prover and verifier share the same underlying infrastructure as the rest of Starknet. There is no separate proving pipeline to maintain or audit.

---

## Compliance Framework: How Auditing Works

### Viewing Keys

Each user generates a **viewing key pair** (`vk_priv`, `vk_pub`). The public key is registered on-chain via `SetViewingKey`. The private key is encrypted to the auditing entity's key `K_audit` and stored encrypted in the pool.

An auditor who possesses the regulatory authority to trace a user:
1. Decrypts the escrowed viewing key using `K_audit`.
2. Uses `vk_priv` to decrypt all of that user's notes across their channels.
3. Can reconstruct the full transaction history.

### Forward and Backward Tracing

| Trace Direction | Start | End | Use Case |
|---|---|---|---|
| Forward | Deposit transaction | Current note locations | Where did these funds go? |
| Backward | Withdrawal transaction | All contributing deposits | Where did this money come from? |

Together these enable full AML/CFT compliance investigations without requiring the privacy pool to be permanently open.

### Threshold Encryption (Optional)

The viewing key can be encrypted under a **threshold scheme** (e.g., 3-of-5). Multiple auditing entities must cooperate to decrypt a viewing key. This prevents unilateral surveillance while satisfying multi-jurisdictional regulatory requirements.

---

## Why Starknet for This?

STRK20 could theoretically be built on other ZK chains, but several properties make Starknet uniquely suited:

| Property | Why It Matters |
|---|---|
| Cairo language | No separate circuit DSL — same language for app and proof code |
| Stwo STARK prover | Efficient enough for client-side proof generation on consumer hardware |
| No trusted setup | STARKs require only hash functions; no ceremony, no toxic waste risk |
| Native account abstraction | Paymaster functionality built into the protocol layer |
| EVM composability | Starknet bridges to Ethereum; shielded assets can interact with ETH DeFi |
| Fee efficiency | Low per-transaction cost makes high-frequency use cases (payroll, agent payments) economically viable |

---

## Comparison to Other Privacy Approaches

| System | Privacy Model | Compliance | Composable DeFi | Trusted Setup |
|---|---|---|---|---|
| **STRK20** | Shielded notes (UTXO) | Native viewing keys | Yes (atomic) | No |
| [[protocols/aztec-network\|Aztec]] | UTXO notes (PLONK) | Limited | Partial | Universal only |
| [[protocols/railgun\|Railgun]] | Shielded balances | Basic | Yes | No (STARKs) |
| [[coins/zcash\|Zcash]] | Shielded pools | Viewing keys | No | Partial (Groth16) |
| [[chains/secret-network\|Secret Network]] | TEE enclaves | Limited | Yes | No (SGX) |

STRK20's combination of **native compliance**, **atomic DeFi composability**, and **no trusted setup** is currently unique in the ecosystem.

---

## See Also

- [[chains/starknet-use-cases|STRK20 Use Cases]] — Real-world applications from payroll to AI agents
- [[research/scalable-compliant-privacy-starknet|Research Paper Summary]] — Technical summary of the StarkWare whitepaper
- [[chains/starknet|Starknet Overview]] — Architecture, ecosystem, and broader roadmap
- [[concepts/zero-knowledge-proofs|Zero-Knowledge Proofs]] — Foundational concepts
- [[protocols/privacy-pools|Privacy Pools]] — Comparable compliant privacy protocol on Ethereum

---

## Backlinks

Sources:
- `raw/papers/2026-474.pdf` — "Scalable Compliant Privacy on Starknet" (StarkWare, March 2026)
- `raw/articles/Starknet Launches STRK20 Standard For Enhanced Privacy Features.md`
- `raw/articles/Starknet Privacy Technology_ The Revolutionary Framework.md`
