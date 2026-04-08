# Monero (XMR)

**Category:** [[_index#privacy-coins|Privacy Coins]]
**Related:** [[coins/zcash]], [[coins/bitcoin-privacy]], [[concepts/cryptographic-primitives]], [[concepts/fungibility]]
**Ticker:** XMR
**Launched:** April 18, 2014

---

## Overview

Monero is the dominant **mandatory-privacy cryptocurrency**. Unlike [[coins/zcash|Zcash]] which makes privacy optional, every Monero transaction is private by default — no user can accidentally make a public transaction. This design choice gives Monero the strongest [[concepts/fungibility|fungibility]] of any major cryptocurrency.

The word "Monero" means "coin" in Esperanto, chosen to reflect its decentralized, international character.

---

## History and Origins

| Event | Date |
|---|---|
| CryptoNote v2 whitepaper published (by "Nicolas van Saberhagen") | October 2013 |
| BitMonero launched (fork of Bytecoin) by user "thankful_for_today" | April 2014 |
| Community fork creates Monero | May 2014 |
| RingCT (Ring Confidential Transactions) activated | January 2017 |
| Bulletproofs integrated (smaller proofs) | October 2018 |
| RandomX mining algorithm deployed (ASIC-resistant) | November 2019 |
| Hard cap of 18.132M XMR reached; tail emission begins | May 2022 |
| Exchange delistings (Binance, Kraken) | 2024–2025 |
| FCMP++ upgrade scheduled | Q1 2026 |

---

## The Privacy Triad

Monero's privacy is achieved through three interlocking mechanisms:

### 1. Ring Signatures

Ring signatures allow a sender to sign a transaction as *one of a group* (the "ring"), making it computationally infeasible to determine which member actually signed.

In practice:
- The real sender's output is mixed with **decoy outputs** (called "ring members") selected from the blockchain.
- Current mandatory minimum ring size: **11** (as of 2024; effectively expanded to whole-chain with FCMP++).
- Observers can confirm *someone* in the ring signed; they cannot identify *who*.
- Limitation: Temporal analysis and "churning" patterns have been studied as potential attack vectors.

### 2. Stealth Addresses (One-Time Addresses)

Every Monero transaction automatically generates a **unique, one-time receiving address**. The mechanism:

1. Sender uses recipient's public view key + a random value to compute a unique address.
2. Recipient scans blockchain using private view key to identify incoming payments.
3. No two transactions share a receiving address; the receiver's published address is never on-chain.

This prevents receiver-side linkability entirely.

### 3. Ring Confidential Transactions (RingCT)

Activated in January 2017, RingCT hides transaction **amounts** using [[concepts/cryptographic-primitives#pedersen-commitments|Pedersen commitments]]:

- Amounts are encrypted with commitments; the network can verify that inputs equal outputs (no new coins created) without knowing the values.
- **Bulletproofs** (integrated 2018) reduced proof sizes by ~80%, significantly lowering transaction fees.
- **Bulletproofs++** (expected 2026) target a further ~30% size reduction.

---

## Upcoming Major Upgrade: FCMP++

**Full-Chain Membership Proofs (FCMP++)** is the most significant Monero upgrade since RingCT, scheduled for Q1 2026.

Instead of using a small ring of decoy outputs (~11), FCMP++ proves membership in the **entire UTXO set** — essentially the whole blockchain. This:

- Expands the anonymity set from 11 to millions of outputs.
- Makes chain-analysis correlation attacks computationally impractical.
- Provides mathematically provable untraceability.
- Replaces ring signatures entirely.

---

## Economics

| Parameter | Value |
|---|---|
| Hard supply cap | 18,132,000 XMR |
| Cap reached | May 2022 |
| Tail emission | 0.6 XMR per block, indefinitely |
| Block time | ~2 minutes |
| Mining algorithm | RandomX (CPU-optimized) |

### Tail Emission

Unlike Bitcoin and Zcash, Monero has a **permanent tail emission** of 0.6 XMR/block (~432 XMR/day). This is a deliberate design choice:

- Ensures miners are always incentivized to secure the network.
- Avoids Bitcoin's long-term security budget problem (where miners eventually rely solely on fees).
- Results in ~0.87% annual inflation at current supply, declining over time.

---

## Mining

Monero uses **RandomX**, a CPU-optimized proof-of-work algorithm introduced November 2019. It was specifically designed to be ASIC-resistant:

- Efficiently runs on consumer x86/x86-64 CPUs.
- GPUs provide ~20% of CPU performance (inefficient for mining).
- ASICs cannot be efficiently designed due to the algorithm's use of random code execution.
- Favored CPUs (as of 2026): AMD Ryzen, Intel i9 series.

**RandomX v2** (January 2026) made further optimizations favoring consumer CPUs.

**Mining economics:** Pools dominate due to variance; fees typically 0–2%; PPLNS reward schemes most common. See `raw/articles/Can I make money mining Zcash_.md` equivalent context.

---

## Wallets

| Wallet | Type | Notes |
|---|---|---|
| Official GUI Wallet | Desktop | Full node; most private |
| Official CLI Wallet | Command-line | Maximum control |
| Cake Wallet | Mobile (iOS/Android) | User-friendly; remote node |
| Monerujo | Android | Open source; lightweight |

---

## Network Privacy Beyond Transactions

Monero protects more than just transaction content:

- **Dandelion++** — Transaction propagation protocol that obscures the originating IP address. A transaction "stems" through a random relay chain before broadcasting to the full network.
- **Transaction fees** — Dynamically sized based on tx size and network congestion; typically under $0.01.
- **Dynamic block size** — Block size adjusts to network demand, preventing both spam and capacity crises.

---

## 2026 Roadmap

| Upgrade | Status | Impact |
|---|---|---|
| FCMP++ | Scheduled Q1 2026 | Whole-chain anonymity sets |
| Cuprate Node (Rust) | In development | 7x faster initial sync; lower hardware requirements |
| Seraphis + Jamtis | Final testing | Modern tx structure + human-readable addresses |
| RandomX v2 | Deployed Jan 2026 | Better consumer CPU optimization |
| Bulletproofs++ | Expected 2026 | ~30% smaller transaction proofs |

---

## Market Data (Early 2026)

| Metric | Value |
|---|---|
| All-time high | $797 (January 2026) |
| Market cap | ~$8.3 billion |
| Circulating supply | ~18.45 million XMR |
| 24h trading volume | ~$195 million |

Note: Despite exchange delistings, Monero trading volume has remained resilient through atomic swaps and DEX liquidity.

---

## Regulatory Status and Traceability

Monero faces significant regulatory pressure due to its strong privacy:

- **Exchange delistings:** Binance (Feb 2024), Kraken (multiple regions).
- **IRS bounty:** $625,000 contract (2020) awarded to Chainalysis and Integra FEC for Monero tracing research.
- **Academic analysis:** Several studies have identified theoretical vulnerabilities (ring size zero attacks, temporal analysis, output merging). All practical attacks require adversarial conditions; FCMP++ eliminates most ring-signature-specific risks.
- **Current consensus:** As of 2025, Monero remains practically untraceable with current public tooling.

---

## Illicit Use

Due to its strong privacy, Monero has become the preferred coin for:
- **Darknet markets** — AlphaBay relaunched 2021 as Monero-only; three of the five largest DNMs accepted XMR by 2019.
- **Ransomware** — DarkSide, REvil (switched to Monero-only in 2021), and WannaCry-related groups.
- **Cryptojacking** — Monero mining malware found on Showtime, Starbucks Wi-Fi (Argentina), and others.

This illicit use profile is the primary justification for exchange delistings and regulatory pressure.

---

## Key People and Organizations

| Name | Role |
|---|---|
| Nicolas van Saberhagen | Pseudonymous CryptoNote author |
| thankful_for_today | Anonymous BitMonero creator |
| Riccardo Spagni (fluffypony) | Former lead maintainer; South Africa |
| Monero Research Lab (MRL) | Semi-anonymous research group |
| Core Team | Mostly anonymous contributors |

---

## Backlinks

Sources:
- `raw/articles/How Does Monero (XMR) Work_ Privacy Features Explained 2026.md`
- `raw/articles/How Monero Privacy Works.md`
- `raw/articles/Monero - Wikipedia.md`
- `raw/articles/Monero (XMR) in 2026_ Privacy, Technology, Use Cases, and Price Outlook.md`
- `raw/articles/Privacy Coins Jumped 288% in 2025 While Everything Else Fell.md`
