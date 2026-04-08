# Secret Network

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[concepts/cryptographic-primitives]], [[chains/penumbra]], [[coins/zcash]]
**Type:** Layer 1 blockchain (Cosmos SDK)
**Mainnet:** Operational since September 2020
**Native coin:** SCRT

---

## Overview

Secret Network is the **first blockchain to offer private smart contracts on mainnet**. It achieves privacy through **Trusted Execution Environments (TEEs)** — hardware-level secure computation zones — rather than ZK proofs. This allows arbitrary smart contract computation to occur privately, without exposing inputs, outputs, or contract state.

---

## Technical Architecture

### Trusted Execution Environments (TEE / Intel SGX)

Secret Network's privacy is based on **Intel SGX (Software Guard Extension)**:
- Smart contracts run inside encrypted hardware enclaves.
- The host OS, cloud provider, and even node operators cannot see contract state.
- Encryption is enforced at the hardware level, not just software.
- A network-level key management system distributes secret keys to authenticated SGX nodes.

**Limitation:** TEE-based privacy depends on hardware manufacturer integrity (Intel). SGX has had documented side-channel vulnerabilities (Spectre, Meltdown variants). ZK-based systems like Penumbra and Zcash are not subject to hardware trust assumptions.

### Secret Contracts

Secret contracts are written in **Rust-based CosmWasm** and extend the standard CosmWasm interface with private metadata capabilities:
- Contract state is encrypted by default.
- Inputs to contract calls are private.
- Outputs can be selectively disclosed.

### Cosmos SDK Foundation

Secret Network is built on the **Cosmos SDK**, enabling:
- IBC (Inter-Blockchain Communication) connectivity to the Cosmos ecosystem.
- SCRT staking for Proof-of-Stake consensus and governance.
- Native compatibility with Cosmos tooling (Keplr wallet, IBC bridges, etc.).

---

## Ecosystem

| Metric | Value |
|---|---|
| dApps on mainnet | 30+ |
| Full-time builders | 100+ |
| Mainnet launch | September 2020 |

Notable Secret applications:
- **SecretSwap** — Private DEX
- **Shade Protocol** — Private stablecoin and DeFi ecosystem
- **Secret NFTs** — NFTs with private metadata (ownership or content can be hidden)
- **Private lending protocols**

---

## Privacy Model vs. ZK Systems

| Approach | Secret Network (TEE) | Zcash/Penumbra (ZK) |
|---|---|---|
| Privacy mechanism | Hardware enclave | Mathematical proof |
| Trust assumption | Hardware manufacturer (Intel) | Cryptographic hardness |
| Smart contract support | ✅ Full arbitrary computation | Limited (Penumbra: no; Zcash: no) |
| Performance | Fast (no proof generation) | Slower (proof generation needed) |
| Side-channel risks | ✅ Real (Spectre, etc.) | Minimal |
| Auditability | Encrypted state; SGX audit | Mathematical guarantees |

---

## Use Cases

Secret Network's private smart contracts enable novel applications impossible on transparent chains:

- **Private voting** — Governance without vote visibility until reveal.
- **Private bidding / auctions** — Sealed bid auctions.
- **Secret NFTs** — NFTs with hidden artwork or metadata unlockable only by owner.
- **Cross-chain privacy** — Shield assets from Ethereum, Cosmos chains, and others.
- **Compliance use cases** — Privacy-preserving KYC/AML where users prove compliance without revealing data.

---

## Key Links

- Documentation: https://docs.scrt.network
- GitHub: https://github.com/scrtlabs/SecretNetwork
- Community: Weekly developer calls, Mondays 5pm UTC on Discord

---

## Backlinks

Sources:
- `raw/articles/Secret Network Introduction _ Secret Network.md`
- `raw/articles/Comparing on-chain Privacy Technologies.md`
