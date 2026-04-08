# Privacy vs. Compliance

**Category:** [[_index#foundational-concepts|Foundational Concepts]]
**Related:** [[concepts/fungibility]], [[protocols/privacy-pools]], [[protocols/railgun]], [[chains/starknet]]

---

## The Core Tension

Financial privacy and regulatory compliance sit in fundamental tension. Privacy protects individuals from surveillance, discrimination, and harm. Compliance frameworks — AML (Anti-Money Laundering), KYC (Know Your Customer), FATF Travel Rules — are designed to prevent crime and preserve state visibility into financial flows.

Blockchain technology throws this tension into sharp relief: public chains expose every transaction forever, while privacy chains can make transactions invisible even to governments.

The question that defines the 2025–2026 privacy landscape is: **can you have both?**

---

## Why Privacy Matters

Privacy is not primarily about hiding crime. It is a prerequisite for fundamental freedoms:

- **Freedom of expression** — People share more openly when not surveilled.
- **Protection from discrimination** — Financial data reveals religion, politics, medical conditions, relationships.
- **Safety** — Wealthy individuals face kidnapping risks when balances are public.
- **Dignity and autonomy** — The ability to transact without asking permission is a form of self-determination.
- **Fungibility** — Without privacy, coins can be "tainted" based on their history, destroying the property of equal value. See [[concepts/fungibility]].

Bitcoin's transparency is a design flaw for many use cases, not a feature.

---

## Regulatory Pressure Timeline

| Year | Event |
|---|---|
| 2018 | Europol warns of criminal shift to privacy coins |
| 2020 | IRS awards $625K bounty for Monero tracing tools to Chainalysis + Integra FEC |
| 2021 | Tornado Cash sees peak usage; darknet markets shift to Monero |
| 2022 | US Treasury sanctions Tornado Cash smart contracts |
| 2024 | Binance, Kraken delist Monero; South Korea, Australia restrict privacy coins |
| 2025 | EU MiCA regulations tighten; US GENIUS Act proposed to restrict privacy coin exchanges |
| 2026 | Dubai imposes regional restrictions on privacy assets |

---

## Compliance Approaches in Modern Privacy Protocols

The frontier of privacy technology in 2025–2026 is "compliance-aware privacy" — systems that give users genuine privacy while providing mechanisms for authorized disclosure. Key approaches:

### 1. Viewing Keys / Selective Disclosure
Users hold cryptographic viewing keys that allow them to selectively reveal transaction history to auditors, tax authorities, or regulators — without making it public.

Implemented in: [[coins/zcash]] (viewing keys), [[chains/starknet]] (STRK20 framework), [[protocols/aztec-network]] (audit access).

### 2. Association Set Providers (ASPs)
[[protocols/privacy-pools]] introduces a novel model: deposits are grouped into "association sets" by third-party ASPs who vet addresses against sanctions lists. Users can prove they belong to a clean set without revealing which deposit they made.

Bad actors are effectively excluded from the privacy pool — their funds can be recovered via "ragequit" but they can't benefit from anonymity.

### 3. Proof of Innocence
[[protocols/railgun]] uses a "private proof of innocence" system: users prove they are *not* in a sanctions or criminal set, without revealing their identity. This is the inverse of traditional compliance: rather than proving who you are, you prove you're not someone harmful.

### 4. On-Chain Blacklists
Some protocols integrate OFAC/sanctions screening directly into smart contracts. Addresses flagged by authorities cannot transact in the protocol.

---

## The Tornado Cash Precedent

The 2022 US Treasury sanctions of Tornado Cash — a smart contract mixing protocol on Ethereum — established a dangerous precedent: immutable code can be sanctioned, and its developers prosecuted. Roman Storm was prosecuted in 2023.

Despite this, Tornado Cash had ~3,900 monthly active users by December 2025, demonstrating that usage persisted even under sanctions.

This case accelerated development of compliance-native alternatives like [[protocols/privacy-pools]] and [[protocols/railgun]], which explicitly address the "no bad actors" requirement.

---

## The Exchange Delisting Problem

Privacy coin exchange delistings (Binance, Kraken, others) reduce fiat liquidity and retail accessibility. The response has been to develop alternative infrastructure:

- **Atomic swaps** — Direct wallet-to-wallet BTC/ETH → XMR exchanges (Baltex.io and others).
- **DEX integration** — Privacy coins on decentralized exchanges.
- **Self-hosted infrastructure** — Running full nodes and peer-to-peer trading.

[[coins/monero]] has been most affected by delistings; [[coins/zcash]] somewhat less so due to its transparent address option.

---

## Key Entities in the Compliance Debate

| Entity | Position |
|---|---|
| FATF (Financial Action Task Force) | Pushes Travel Rule requiring sender/receiver data sharing |
| US Treasury / OFAC | Sanctions on mixers; supports KYC for exchanges |
| Chainalysis | Builds tracing tools; IRS contract holder |
| 0xbow / Privacy Pools | Building compliance-native privacy |
| Aztec Labs | "Privacy Abstraction" with selective disclosure |
| StarkWare | STRK20 with viewing keys for regulators |
| EFF / Cypherpunks | Privacy as a fundamental right; oppose all surveillance |

---

## Backlinks

Sources covering this concept:
- `raw/articles/Why is privacy so important_.md`
- `raw/articles/Privacy Pools_ How to Protect Users Privacy While Meeting the Compliance Requirements.md`
- `raw/articles/Privacy Pools — Striking The Balance In Privacy And Regulations.md`
- `raw/articles/Addressing the Privacy and Compliance Challenge in Public Blockchain Token Transactions.md`
- `raw/articles/From Aztec to Zcash_ The year pragmatic privacy took root.md`
- `raw/articles/Privacy Coins Jumped 288% in 2025 While Everything Else Fell.md`
