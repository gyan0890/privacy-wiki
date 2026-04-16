# Privacy Wiki — Master Index

> A compiled knowledge base on blockchain privacy technologies, cryptographic primitives, privacy coins, and compliance frameworks. Built from ~70 source articles and 9 research papers.

**Last compiled:** 2026-04-16

---

## Navigation

### 🔐 Foundational Concepts
Core cryptographic and philosophical ideas underpinning all privacy technologies.

| Article | Summary |
|---|---|
| [[concepts/zero-knowledge-proofs]] | What ZKPs are and why they matter |
| [[concepts/zk-snarks]] | zk-SNARKs: the workhorse of blockchain privacy |
| [[concepts/halo-proving-system]] | Halo & Halo 2: eliminating the trusted setup |
| [[concepts/privacy-vs-compliance]] | The tension between financial privacy and regulation |
| [[concepts/fungibility]] | Why fungibility is central to sound money |
| [[concepts/cryptographic-primitives]] | Pedersen commitments, Poseidon hash, ring signatures, and more |

---

### 🪙 Privacy Coins
Cryptocurrencies designed with privacy as a primary feature.

| Article | Summary |
|---|---|
| [[coins/privacy-coins-overview]] | Landscape, use cases, and comparison of major privacy coins |
| [[coins/zcash]] | Zcash (ZEC): optional privacy via zk-SNARKs |
| [[coins/monero]] | Monero (XMR): mandatory privacy via ring signatures + RingCT |
| [[coins/bitcoin-privacy]] | Bitcoin's transparency problem and privacy limitations |

---

### ⚙️ Privacy Protocols
Smart contract and layer-2 protocols delivering privacy on public blockchains.

| Article | Summary |
|---|---|
| [[protocols/aztec-network]] | Aztec: confidential transactions and private L2 on Ethereum |
| [[protocols/privacy-pools]] | Privacy Pools: compliance-aware privacy via Association Set Providers |
| [[protocols/railgun]] | Railgun: on-chain ZK privacy with proof-of-innocence |
| [[protocols/iron-fish]] | Iron Fish: ZK Layer 1 with multi-asset bridged privacy |

---

### 🔗 Privacy-First Chains
Layer 1 and Layer 2 networks with privacy as a core design goal.

| Article | Summary |
|---|---|
| [[chains/starknet]] | Starknet: ZK rollup L2 with STRK20 private token standard |
| [[chains/penumbra]] | Penumbra: end-to-end encrypted DEX and IBC shielding |
| [[chains/secret-network]] | Secret Network: private smart contracts via trusted execution |

### ⬛ Starknet & STRK20
Deep dive into Starknet's native privacy standard and its applications.

| Article | Summary |
|---|---|
| [[chains/starknet]] | Starknet overview: architecture, ecosystem, performance |
| [[chains/strk20]] | STRK20 protocol: note model, channels, encryption, compliance framework |
| [[chains/starknet-use-cases]] | Core use cases: payroll, donations, OTC, AI agents, gaming |
| [[chains/starknet-usecases-defi]] | DeFi: dark pools, sealed auctions, private perpetuals, lending, prediction markets |
| [[chains/starknet-usecases-gaming]] | Gaming & governance: poker, blackjack, raffles, Dark Forest, encrypted voting |
| [[chains/starknet-usecases-social]] | Identity & social: selective disclosure, private messaging, matchmaking, subscriptions |
| [[chains/starknet-usecases-ai]] | AI & ML: encrypted RAG, autonomous agents, federated learning, private analytics |
| [[chains/starknet-usecases-sensitive]] | Healthcare & biometrics: DNA matching, biometric login, patient analytics |

---

### 📄 Research Papers
Summaries of academic and technical papers in the collection.

| Paper | Authors | Topic |
|---|---|---|
| [[research/shielded-csv]] | Nick, Eagen, Linus | Private client-side validation, 64 bytes/tx |
| [[research/privada]] | Özdemir et al. | Privacy-preserving data aggregation (MPC) |
| [[research/image-encryption]] | Boldyreva et al. | Format-preserving encryption for images |
| [[research/deniable-fhe]] | Toyooka et al. | Deniable Fully Homomorphic Encryption |
| [[research/floss]] | Chang et al. | Fast linear online secret-shared shuffling |
| [[research/plasmablind]] | Daix-Moreux, Zhang | Private L2 with sub-100ms client-side proving |
| [[research/privacy-blanket]] | Su et al. | Optimal noise in the shuffle model |
| [[research/random-robust-ss]] | Ameri, Blocki | Random robust secret sharing + fuzzy auth |
| [[research/zcash-protocol-spec]] | Hopwood, Bowe et al. | Official Zcash protocol specification |
| [[research/scalable-compliant-privacy-starknet]] | Goldberg et al. (StarkWare) | STRK20: shielded notes, channels, compliance on Starknet |

---

### 📂 Source Summaries
One-paragraph digest of every raw source document.

- [[sources/articles-index]] — All 70+ article summaries
- [[sources/papers-index]] — All 9 paper summaries

---

## Key Themes

**Privacy as a Right** — Financial privacy enables freedom, protects against discrimination, and is essential for dignity. See [[concepts/privacy-vs-compliance]] and [[coins/privacy-coins-overview]].

**The ZK Stack** — Zero-knowledge proofs are the mathematical engine behind nearly every modern privacy protocol. See [[concepts/zero-knowledge-proofs]], [[concepts/zk-snarks]], and [[concepts/halo-proving-system]].

**Compliance vs. Anonymity** — The defining tension of 2025–2026. Projects like [[protocols/privacy-pools]], [[protocols/railgun]], [[chains/starknet]], and [[chains/strk20]] are building "compliance-aware" privacy. [[protocols/aztec-network]] and [[coins/zcash]] offer selective disclosure.

**Mandatory vs. Optional Privacy** — [[coins/monero]] mandates privacy for all users; [[coins/zcash]] makes it optional. The tradeoff affects anonymity set size and regulatory exposure.

**2025: The Year of Pragmatic Privacy** — Aztec Ignition Chain, Namada L1, Privacy Pools, and Starknet STRK20 all launched. Privacy coins jumped 288% as a category. See [[coins/privacy-coins-overview]].

---

## Entity Index

| Entity | Type | Related Articles |
|---|---|---|
| Electric Coin Co. (ECC) | Organization | [[coins/zcash]], [[research/zcash-protocol-spec]] |
| Zooko Wilcox | Person | [[coins/zcash]] |
| Sean Bowe | Person | [[concepts/halo-proving-system]], [[coins/zcash]] |
| Vitalik Buterin | Person | [[protocols/privacy-pools]], [[protocols/aztec-network]] |
| Aztec Labs | Organization | [[protocols/aztec-network]] |
| 0xbow | Organization | [[protocols/privacy-pools]] |
| StarkWare | Organization | [[chains/starknet]], [[chains/strk20]], [[research/scalable-compliant-privacy-starknet]] |
| Monero Research Lab | Organization | [[coins/monero]] |
| Ethereum Foundation | Organization | [[protocols/privacy-pools]], [[chains/starknet]], [[research/plasmablind]] |
| Chainalysis | Organization | [[coins/monero]], [[coins/privacy-coins-overview]] |

---

*This wiki is maintained by LLM compilation. Source data lives in `raw/`. Do not edit wiki files manually — re-run compilation to update.*
