# Zcash (ZEC)

**Category:** [[_index#privacy-coins|Privacy Coins]]
**Related:** [[coins/monero]], [[coins/bitcoin-privacy]], [[concepts/zk-snarks]], [[concepts/halo-proving-system]]
**Ticker:** ZEC
**Launched:** October 28, 2016

---

## Overview

Zcash is a cryptocurrency that was the first to integrate [[concepts/zero-knowledge-proofs|zero-knowledge proofs]] for transaction privacy at scale. It was forked from Bitcoin's codebase but added optional strong privacy: users can choose between **transparent** (Bitcoin-like, fully public) and **shielded** (fully private) transactions.

Zcash's core innovation — proving transaction validity without revealing any details — has influenced virtually every blockchain privacy project that followed.

---

## History and Origins

| Event | Date |
|---|---|
| Zerocoin paper (Bitcoin privacy extension proposal) | 2013 |
| Electric Coin Co. (ECC) founded | 2015 |
| Zcash genesis block | October 28, 2016 |
| Sapling upgrade (faster shielded transactions) | October 2018 |
| Canopy upgrade (new development fund structure) | November 2020 |
| Network Upgrade 5 / Orchard pool (Halo 2) | May 31, 2022 |
| Grayscale files for first ZEC ETF | 2025 |
| Shielded pool reaches ~25% of circulating supply | 2025 |

Zcash was founded by **Zooko Wilcox**, a longtime cypherpunk, alongside a team of cryptographers from MIT, Johns Hopkins, and other institutions. The core company is **Electric Coin Co. (ECC)**, with the **Zcash Foundation** as an independent steward.

---

## Transparent vs. Shielded Addresses

Zcash offers two address types:

### Transparent Addresses (t-addresses)
- Identical to Bitcoin: sender, receiver, and amount are fully public on the blockchain.
- All transactions can be traced by anyone.
- Still used by many exchanges for compliance simplicity.

### Shielded Addresses
Three generations of shielded pool technology:

| Pool | Protocol | Proving System | Trusted Setup? | Addresses |
|---|---|---|---|---|
| Sprout (2016) | BCTV14 | zk-SNARK | Yes | z-addr (legacy) |
| Sapling (2018) | Groth16 | zk-SNARK | Yes | zs-addr |
| Orchard (2022) | Halo 2 | **No setup** | No | Unified Address |

In a shielded transaction, the blockchain records only proof of validity — no sender, receiver, or amount is revealed. Even the memo field (unique to Zcash) is encrypted.

---

## How Shielded Transactions Work

1. The sender creates a **note** (a ZEC UTXO commitment) containing the amount, receiver's public key, and a random secret.
2. A [[concepts/zero-knowledge-proofs|zero-knowledge proof]] is generated showing: (a) the sender knows the spending key for the input note, (b) input amounts equal output amounts, (c) no coins are created.
3. The nullifier for the spent note is published, preventing double-spend.
4. The receiver's note is encrypted and added to the note commitment tree.
5. The receiver uses their private key to find and decrypt their incoming note.

No external observer can link sender to receiver, or learn any amounts.

---

## Unified Addresses

Introduced with the Orchard upgrade, **Unified Addresses (UAs)** combine transparent and shielded receiving addresses into a single string. Wallets supporting UAs automatically route transactions to the best available shielded pool, reducing user friction and improving the default privacy experience.

---

## Economics

Zcash has a fixed supply of **21 million ZEC** (identical to Bitcoin).

| Parameter | Value |
|---|---|
| Max supply | 21,000,000 ZEC |
| Block time | ~75 seconds |
| Block reward (current) | 1.5625 ZEC |
| Halving interval | ~4 years |
| Inflation curve | Nearly identical to Bitcoin |

**Block reward distribution (post-Canopy, as of November 2024):**
- **80%** to miners
- **8%** to Zcash Community Grants Committee (ZCG) for ecosystem funding
- **12%** to "lockbox" for future community-determined disbursements

---

## Mining

Zcash uses **Equihash**, a memory-hard proof-of-work algorithm designed to be ASIC-resistant at launch. Unlike [[coins/monero]]'s RandomX, Zcash ASICs do exist (Antminer Z series) and dominate mining.

- Can also be GPU-mined (with lower efficiency vs. ASICs)
- Solo mining possible but pool mining more consistent
- See `raw/articles/Can I make money mining Zcash_.md`

---

## Viewing Keys and Selective Disclosure

Zcash supports **viewing keys**: private keys that allow the holder to see all incoming and outgoing transactions for an address. Users can share viewing keys with:
- Tax authorities
- Auditors
- Employers or business counterparties

This provides a compliance path without requiring full public transparency or custom regulatory infrastructure.

---

## Wallets and Exchanges

**Recommended wallets:**
- Zashi (official ECC wallet, mobile) — defaults to shielded
- YWallet — fast, lightweight
- ZecWallet — desktop

**Zcash unified addresses (Orchard-capable):** Supported in Zashi, ZecWallet Lite, Nighthawk

**Notable exchange considerations:** Many exchanges only support transparent ZEC; shielded deposits/withdrawals require wallets with shielded support.

---

## 2025–2026 Developments

- **Shielded supply growth** — Reached ~25% of circulating supply in shielded pools in 2025.
- **Zebra 3.1** — New Rust-based full node implementation, improving performance and decentralization.
- **Grayscale ZEC ETF filing** — First institutional investment vehicle filing for Zcash.
- **Governance challenges** — Ongoing community discussions about funding structure and development priorities.

---

## Comparison with Monero

| Feature | Zcash | Monero |
|---|---|---|
| Privacy | Optional (shielded) | Mandatory (all txs) |
| Anonymity set | Users in shielded pool (~25% supply) | Entire network |
| Proving system | Halo 2 (no setup) | Ring signatures + RingCT |
| Supply cap | 21M ZEC | ~18.1M XMR + tail emission |
| Trusted setup | Eliminated (Orchard+) | Never required |
| Regulatory exposure | Moderate (transparent txs exist) | High (mandatory privacy) |
| Exchange listings | More accessible | Increasingly restricted |

See also: [[coins/monero]], [[coins/privacy-coins-overview]]

---

## Key People and Organizations

| Name | Role |
|---|---|
| Zooko Wilcox | CEO, Electric Coin Co.; founder |
| Sean Bowe | Lead cryptographer; Halo inventor |
| Jack Grigg | Cryptography engineer; Halo co-inventor |
| Daira-Emma Hopwood | Protocol specification author |
| Zcash Foundation | Independent steward of Zcash ecosystem |
| Zcash Community Grants (ZCG) | Community funding body |

---

## Backlinks

Sources:
- `raw/articles/What is Zcash_.md`
- `raw/articles/Who created Zcash_.md`
- `raw/articles/How is Zcash different than Bitcoin_.md`
- `raw/articles/What is the difference between shielded and transparent Zcash_.md`
- `raw/articles/What are the economics of Zcash_.md`
- `raw/articles/What is Halo for Zcash_.md`
- `raw/articles/Is Zcash traceable_.md`
- `raw/articles/Does Zcash contain a backdoor_.md`
- `raw/articles/What are Zcash unified addresses_.md`
- `raw/articles/What is the difference between Zcash and ZEC_.md`
- `raw/articles/Does Zcash have a max supply_.md`
- `raw/articles/How to buy and use Zcash Orchard.md`
- `raw/articles/How to run a Zcash Full Node.md`
- `raw/articles/How to spend your Zcash on everyday items.md`
- `raw/articles/What's the best Zcash wallet_.md`
- `raw/articles/What's the best Zcash exchange_.md`
- `raw/papers/protocol.pdf` (Official Zcash Protocol Specification)
