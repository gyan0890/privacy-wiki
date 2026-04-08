# Fungibility

**Category:** [[_index#foundational-concepts|Foundational Concepts]]
**Related:** [[concepts/privacy-vs-compliance]], [[coins/monero]], [[coins/zcash]], [[coins/bitcoin-privacy]]

---

## Definition

**Fungibility** is the property of a good where each individual unit is interchangeable with any other unit of the same good. A dollar bill is fungible: it doesn't matter which specific bill you hold — each is worth the same as any other.

In the context of cryptocurrencies, fungibility means that each coin is equal in value and treatment to every other coin of the same denomination, regardless of its transaction history.

---

## Why Fungibility Matters for Cryptocurrency

Unlike physical cash, cryptocurrency transaction histories are typically recorded permanently on a public blockchain. This creates a problem: a coin that was previously used in a criminal transaction can be identified and "tainted." Exchanges, merchants, or other parties may refuse to accept or may discount such coins.

If some coins are worth less than others due to their history, the currency is **not truly fungible**. This undermines a core property of sound money.

### The Bitcoin Fungibility Problem

[[coins/bitcoin-privacy|Bitcoin]] has no inherent privacy. Every BTC's entire transaction history is publicly visible. Blockchain analytics firms (Chainalysis, Elliptic, etc.) assign "risk scores" to coins based on their provenance. Exchanges may freeze or seize coins flagged as "tainted."

A BTC that touched a sanctioned address is technically worth the same as any other BTC in protocol terms — but practically, it may be worthless if no exchange will accept it.

---

## Privacy Coins and Fungibility

| Coin | Privacy Model | Fungibility |
|---|---|---|
| Bitcoin | Fully transparent | Poor — coins can be tainted |
| [[coins/zcash\|Zcash]] | Optional shielded | Partial — only shielded ZEC is fungible |
| [[coins/monero\|Monero]] | Mandatory privacy | **High** — all XMR is indistinguishable |

### Zcash's Fungibility Challenge

Zcash supports both transparent and shielded addresses. Only coins in the shielded pool are genuinely fungible — coins that have passed through transparent addresses carry a visible history.

This creates a "two-tier" fungibility problem: the shielded pool provides strong fungibility for its participants, but only ~25% of ZEC circulating supply was in the shielded pool as of 2025. Coins moving between transparent and shielded pools create linkage risks.

### Monero's Fungibility Strength

[[coins/monero|Monero]] achieves the strongest practical fungibility of any major cryptocurrency. Because all transactions are private by default (ring signatures obscure senders, RingCT hides amounts, stealth addresses protect receivers), there is no mechanism for analyzing transaction history to selectively taint coins.

The upcoming **FCMP++ upgrade** (Full-Chain Membership Proofs) will further strengthen this by expanding the anonymity set from a small ring to nearly the entire blockchain, making chain-analysis correlation attacks computationally impractical.

---

## Fungibility and the Legal System

The law implicitly treats physical cash as fungible — a dollar is a dollar regardless of what crimes it may have "witnessed." Privacy advocates argue that digital currencies should enjoy the same treatment.

However, regulators and courts have increasingly accepted that cryptocurrency fungibility can be selectively undermined — frozen wallets, sanctioned addresses, and exchange delistings all reflect this. The Tornado Cash sanctions case is the extreme example: an entire class of transactions (mixing) was deemed inherently suspect.

---

## Fungibility as a Design Goal

Projects explicitly designing for fungibility:
- [[coins/monero]] — Mandatory privacy ensures no coin differs from another
- [[protocols/railgun]] — Proof of innocence removes the "taint" concern without requiring identity disclosure
- [[protocols/privacy-pools]] — Compliance-aware pools that admit only "clean" coins, making all pool participants equivalent from a compliance perspective

---

## Backlinks

Sources covering this concept:
- `raw/articles/Is Bitcoin private_.md`
- `raw/articles/What are Privacy Coins, and How Do They Work_.md`
- `raw/articles/Comparing on-chain Privacy Technologies.md`
- `raw/articles/How Monero Privacy Works.md`
