# Privacy Coins: Overview

**Category:** [[_index#privacy-coins|Privacy Coins]]
**Related:** [[coins/zcash]], [[coins/monero]], [[coins/bitcoin-privacy]], [[concepts/privacy-vs-compliance]]

---

## What Are Privacy Coins?

Privacy coins are cryptocurrencies that use cryptographic techniques to conceal transaction details — sender, receiver, amount, or some combination. They exist to solve a fundamental problem with transparent blockchains like Bitcoin: that every financial transaction is permanently public.

---

## The Major Privacy Coins

### Monero (XMR)
- **Privacy model:** Mandatory — all transactions are private by default.
- **Mechanisms:** Ring signatures (sender), stealth addresses (receiver), RingCT (amounts).
- **Anonymity set:** Entire network (all outputs); expanding further with FCMP++ in 2026.
- **Fungibility:** Strongest of any major coin.
- **Regulatory status:** Most restricted — delistings from Binance, Kraken, others.
- Full article: [[coins/monero]]

### Zcash (ZEC)
- **Privacy model:** Optional — users choose transparent or shielded transactions.
- **Mechanisms:** zk-SNARKs (Groth16 / Halo 2).
- **Anonymity set:** Users using shielded pool (~25% of supply in 2025).
- **Fungibility:** Partial — only shielded ZEC is fungible.
- **Regulatory status:** Moderate — transparent address option reduces pressure.
- Full article: [[coins/zcash]]

### Dash (DASH)
- **Privacy model:** Optional (PrivateSend feature).
- **Mechanisms:** CoinJoin-based mixing (not cryptographic privacy).
- **Privacy strength:** Weakest of the three — CoinJoin can be partially deanonymized.
- **Status:** Declining privacy focus; primary use as fast payments.

---

## Comparison Table

| Feature | Monero | Zcash | Dash | Bitcoin |
|---|---|---|---|---|
| Privacy by default | ✅ | ❌ (optional) | ❌ (optional) | ❌ (none) |
| Cryptographic privacy | ✅ (ring sigs + RingCT) | ✅ (zk-SNARKs) | ❌ (mixing) | ❌ |
| Transaction amounts hidden | ✅ | ✅ (shielded) | ❌ | ❌ |
| Sender hidden | ✅ | ✅ (shielded) | Partial | ❌ |
| Receiver hidden | ✅ | ✅ (shielded) | ❌ | ❌ |
| Fixed supply | ❌ (tail emission) | ✅ (21M) | ✅ (18.9M) | ✅ (21M) |
| Trusted setup required | ❌ | Eliminated (Orchard+) | N/A | N/A |
| Exchange delistings | Many | Some | Few | N/A |

---

## Other Privacy-Oriented Coins and Protocols

Beyond the "big three," a broader ecosystem has emerged:

| Project | Type | Privacy Approach |
|---|---|---|
| [[chains/penumbra]] | L1 chain (Cosmos) | End-to-end encrypted DEX and IBC shielding |
| [[chains/secret-network]] | L1 smart contracts | Intel SGX TEE for private execution |
| [[protocols/iron-fish]] | L1 chain | ZK proofs; multi-asset bridged privacy |
| [[protocols/railgun]] | Smart contract protocol | ZK privacy layer for EVM chains |
| [[protocols/privacy-pools]] | Smart contract | Compliance-aware ZK mixing |
| [[protocols/aztec-network]] | Ethereum L2 | Confidential smart contract execution |

---

## Market Performance

Privacy coins as a category surged **288%** in 2025 while the broader crypto market declined:

| Coin | 2025 Performance |
|---|---|
| Monero (XMR) | ~119% gain; reached $797 ATH in January 2026 |
| Zcash (ZEC) | ~1,000% from 2025 lows to $744 (November 2025) |

Drivers:
- Growing demand for financial privacy in a surveillance-heavy world
- Institutional interest preceding potential ETF products
- Privacy technology maturation (Aztec mainnet, Privacy Pools launch, Starknet STRK20)

---

## Regulatory Headwinds (2024–2026)

| Event | Impact |
|---|---|
| Binance Monero delisting (Feb 2024) | Major liquidity reduction; shifted to P2P/atomic swaps |
| EU MiCA regulations | Complexity for European exchanges |
| US GENIUS Act (proposed) | Would restrict privacy coin exchanges |
| Dubai regional restrictions | Limits trading in MENA region |
| South Korea, Australia restrictions | Reduced accessibility in Asia-Pacific |

Despite these headwinds, privacy coin market caps have grown, suggesting existing users are accumulating and new infrastructure (atomic swaps, DEX listings) replaces exchange liquidity.

---

## Use Cases

**Legitimate:**
- Private peer-to-peer commerce
- Protection from financial surveillance in authoritarian regimes
- Merchant privacy (competitors cannot see revenue)
- Protection against targeted theft (wealth not visible)
- Fungibility preservation (untainted coins)
- Privacy-preserving payroll and payments

**Illicit (documented):**
- Darknet markets (Monero dominant after 2021)
- Ransomware payments (Monero preferred by major groups since 2021)
- Cryptojacking (Monero mining malware)
- Money laundering

The illicit use cases drive regulatory pressure, while legitimate use cases drive market demand. The tension defines the regulatory debate around privacy coins. See [[concepts/privacy-vs-compliance]].

---

## The "Pragmatic Privacy" Shift (2025)

2025 saw a shift toward **compliance-aware privacy** — systems that preserve meaningful user privacy while enabling authorized disclosure. Key developments:

- **Privacy Pools** (0xbow) — Compliance-native ZK mixing with ASP-based allowlists.
- **Railgun** — Proof of innocence system.
- **Aztec Ignition Chain** — Private smart contracts with selective disclosure.
- **Starknet STRK20** — Encrypted token balances with viewing keys.
- **Circle USDCx** — Privacy-preserving USDC (in testing).
- **EY Nightfall** — Ethereum L2 for enterprise privacy.
- **Canton Network** — Goldman Sachs, BNY Mellon private financial infrastructure.

This represents a maturing of the space beyond "full anonymity vs. full transparency" toward nuanced, programmable privacy.

---

## Backlinks

Sources:
- `raw/articles/What are Privacy Coins, and How Do They Work_.md`
- `raw/articles/Comparing on-chain Privacy Technologies.md`
- `raw/articles/Privacy Coins Jumped 288% in 2025 While Everything Else Fell.md`
- `raw/articles/From Aztec to Zcash_ The year pragmatic privacy took root.md`
- `raw/articles/On-chain ZK Privacy Ecosystem.md`
