# Articles — Source Index

**Category:** [[_index|Index]]

One-paragraph digest of every article in `raw/articles/`, organized by topic. Each entry links to the relevant wiki article.

---

## Zero-Knowledge Proofs & Cryptography

**`What are zero-knowledge proofs_.md`** → [[concepts/zero-knowledge-proofs]]
Introductory overview of zero-knowledge proofs: definition, properties (completeness, soundness, zero-knowledge), and their application to blockchain privacy. The canonical example of proving age without revealing a birthdate. Explains how ZKPs allow Zcash to verify transaction validity without revealing any details.

**`What are zk-SNARKs_.md`** → [[concepts/zk-snarks]]
Deep dive into zk-SNARKs (Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge). Covers the components (succinct, non-interactive, argument of knowledge), how they differ from interactive ZKPs, the trusted setup problem, and their deployment in Zcash's Sprout and Sapling protocols.

**`What is Halo for Zcash_.md`** → [[concepts/halo-proving-system]]
Explains the Halo proving system discovered by Sean Bowe, Jack Grigg, and Daira Hopwood at Electric Coin Co. in 2019. Describes how Halo eliminates the trusted setup requirement through recursive proof composition (nested amortization). Details deployment in Zcash's Orchard pool via NU5 in May 2022 and its significance for user trust and scalability.

---

## Zcash Deep Dive

**`What is Zcash_.md`** → [[coins/zcash]]
Comprehensive introduction to Zcash: history (Bitcoin fork, 2016), core innovation (ZK proofs for privacy), transparent vs. shielded addresses, shielded transaction mechanics, and the Zcash ecosystem.

**`Who created Zcash_.md`** → [[coins/zcash]]
History of Zcash's creation: origins in the Zerocoin research project, Electric Coin Co. founding by Zooko Wilcox, and the team of scientists from MIT, Johns Hopkins, and other institutions.

**`What are the economics of Zcash_.md`** → [[coins/zcash]]
Detailed breakdown of Zcash's tokenomics: 21M fixed supply, 75-second block time, halving schedule, and distribution of block rewards between miners (80%), ZCG (8%), and the lockbox (12%).

**`How is Zcash different than Bitcoin_.md`** → [[coins/zcash]], [[coins/bitcoin-privacy]]
Comparison article: Zcash vs. Bitcoin on privacy, block time, memo fields, self-funding, and optional transparency. Explains the core value proposition of shielded transactions.

**`What is the difference between shielded and transparent Zcash_.md`** → [[coins/zcash]]
Explains the technical and practical differences between Zcash's t-addresses (public, Bitcoin-like) and shielded addresses (three generations: Sprout, Sapling, Orchard). Covers what information is hidden in each type.

**`Is Zcash traceable_.md`** → [[coins/zcash]], [[concepts/privacy-vs-compliance]]
Analysis of Zcash's traceability. Shielded transactions are cryptographically untraceable; transparent transactions are fully public. Addresses the "optional privacy" anonymity set concern and the impact of shielded pool adoption.

**`Does Zcash contain a backdoor_.md`** → [[coins/zcash]], [[concepts/zk-snarks]]
Addresses the trusted setup concern: could the original Zcash trusted setup ceremony participants have retained "toxic waste" to counterfeit coins? Explains the multi-party ceremony design and the eventual elimination of this risk with Halo 2.

**`What are Zcash unified addresses_.md`** → [[coins/zcash]]
Explains unified addresses introduced in the Orchard/NU5 upgrade: a single address string that combines transparent and multiple shielded receivers, enabling wallets to route transactions to the best available pool automatically.

**`What is the difference between Zcash and ZEC_.md`** → [[coins/zcash]]
Clarifies nomenclature: Zcash is the protocol/network; ZEC is the ticker symbol for the native currency.

**`Does Zcash have a max supply_.md`** → [[coins/zcash]]
Confirms the 21 million ZEC hard cap, identical to Bitcoin. Details the emission schedule and halving timeline.

**`How to buy and use Zcash Orchard.md`** → [[coins/zcash]]
Practical guide to acquiring ZEC and using the Orchard shielded pool. Covers supported wallets, exchanges offering shielded deposits/withdrawals, and how to shield funds.

**`How to run a Zcash Full Node.md`** → [[coins/zcash]]
Technical guide to running a Zcash full node (zebrad, Zcash full node software). Prerequisites, installation, and operation.

**`How to spend your Zcash on everyday items.md`** → [[coins/zcash]]
Practical guide to spending ZEC: merchants accepting Zcash, payment services, and conversion options.

**`Useful Tips when using Zcash.md`** → [[coins/zcash]]
Collection of practical privacy and usability tips: using shielded addresses by default, understanding transaction fees, memo field use cases, and wallet recommendations.

**`What's the best Zcash wallet_.md`** → [[coins/zcash]]
Review of Zcash wallet options: Zashi (ECC official, mobile), YWallet (fast, lightweight), ZecWallet Lite (desktop), and others, evaluated on privacy defaults, UX, and Orchard support.

**`What's the best Zcash exchange_.md`** → [[coins/zcash]]
Overview of exchanges supporting ZEC, including which support shielded withdrawals/deposits (key for privacy) vs. transparent only. Notes on instant swap services.

**`Where can I use or spend Zcash_.md`** → [[coins/zcash]]
Directory of merchants, services, and platforms accepting ZEC. Includes comparison with other payment methods.

**`Can I make money mining Zcash_.md`** → [[coins/zcash]]
Economics of Zcash mining: hardware options (ASICs vs. GPUs), profitability calculations, pool vs. solo mining, and comparison with other PoW coins.

**`Instant Crypto Swaps _ Fast & Secure Exchange.md`**
Overview of instant swap services (ChangeNow and similar) for converting between privacy coins and other cryptocurrencies without KYC. Relevant for exchange-delisted privacy coins like [[coins/monero|Monero]].

---

## Monero

**`How Does Monero (XMR) Work_ Privacy Features Explained 2026.md`** → [[coins/monero]]
Comprehensive 2026 explainer: Ring signatures, stealth addresses, RingCT, and upcoming upgrades (FCMP++, Cuprate, Seraphis+Jamtis, RandomX v2). Includes market data and 2026 price outlook.

**`How Monero Privacy Works.md`** → [[coins/monero]]
Technical deep dive into Monero's privacy triad: ring signatures (sender anonymity), stealth addresses (receiver privacy), and RingCT (amount hiding via Pedersen commitments). Explains Bulletproofs and Dandelion++.

**`Monero - Wikipedia.md`** → [[coins/monero]]
Wikipedia article on Monero: history, technical overview, illicit use cases, regulatory response (IRS bounty, exchange delistings), and community structure. Comprehensive factual reference.

**`Monero (XMR) in 2026_ Privacy, Technology, Use Cases, and Price Outlook.md`** → [[coins/monero]]
2026 market and technology outlook: FCMP++ significance, Cuprate performance improvements, 2025 market performance (119% gain), regulatory pressure, and price projections ($520–$760 near-term, $4,300+ long-term scenarios).

---

## Bitcoin Privacy

**`Is Bitcoin private_.md`** → [[coins/bitcoin-privacy]]
Direct explanation of Bitcoin's privacy limitations: pseudonymity vs. anonymity, address clustering, exchange linkage, and blockchain analytics firms. Concludes Bitcoin is fundamentally not private.

---

## Privacy Coins Overview

**`What are Privacy Coins, and How Do They Work_.md`** → [[coins/privacy-coins-overview]]
Survey of privacy coin types and mechanisms: mandatory (Monero) vs. optional (Zcash) privacy, mixing-based (Dash), and the relative strengths of each approach. Covers use cases from peer-to-peer commerce to fungibility protection.

**`Comparing on-chain Privacy Technologies.md`** → [[coins/privacy-coins-overview]], [[protocols/aztec-network]]
Technical comparison of privacy mechanisms: ring signatures, zk-SNARKs, TEEs (Secret Network), and mixing (Tornado Cash, Privacy Pools). Evaluates each on privacy strength, decentralization, compliance potential, and UX.

**`Why is privacy so important_.md`** → [[concepts/privacy-vs-compliance]]
Philosophical and practical case for financial privacy: freedom of expression, protection from discrimination, safety from targeted theft, and the right to transact without surveillance. Connects privacy to broader digital rights.

**`Privacy Coins Jumped 288% in 2025 While Everything Else Fell - What's Next_.md`** → [[coins/privacy-coins-overview]]
Market analysis: Monero's $797 ATH (January 2026), Zcash's 1,000% surge to $744 (November 2025), 288% category gain vs. broad market decline. Covers regulatory headwinds (GENIUS Act, MiCA, Dubai restrictions) and 2026 outlook.

---

## Aztec Network

**`A Deep Dive into AZTEC Protocol_ Providing Privacy on the Ethereum Network.md`** → [[protocols/aztec-network]]
Technical deep dive into the original AZTEC Protocol (2018): AZTEC Notes (encrypted UTXOs), algebraic ZK proofs with Boneh-Boyen signatures, Pedersen commitments, the trusted setup ceremony, and the note commitment/nullifier architecture borrowed from Zcash.

**`Confidential transactions have arrived, a dive into the AZTEC Protocol.md`** → [[protocols/aztec-network]]
Announcement article covering the AZTEC Protocol's mainnet launch on December 1, 2018 with DAI. Explains the technical architecture, gas costs (~900K gas/tx), and plans for reducing costs with EIP-1108.

**`Fully Confidential Ethereum Transactions_ Aztec Network's Privacy Architecture.md`** → [[protocols/aztec-network]]
Architecture overview of Aztec's two-domain execution model (private on PXE, public on sequencer), note-based UTXO model, Noir programming language, and Barretenberg/PlonK proving system.

**`What Is Aztec Network (AZTEC)_ A Vitalik-backed Privacy ETH L2.md`** → [[protocols/aztec-network]]
Overview article: founding, Vitalik backing, $170M raised, Ignition Chain mainnet (November 2025), token sale parameters (10.35B supply, $350M FDV, 14.95% pre-sale), and the vision for "privacy abstraction."

**`Privacy Abstraction with Aztec.md`** → [[protocols/aztec-network]]
Explains Aztec's "Privacy Abstraction" vision: making privacy a composable layer that any Ethereum dApp can adopt, similar to how Account Abstraction standardized wallet interactions. Covers stealth addresses, selective disclosure, and cross-contract private calls.

**`'Everything Is Encrypted'_ Aztec's Privacy Rollup Hits Testnet Amid Growing Demand.md`** → [[protocols/aztec-network]]
News article on Aztec's testnet launch, growing developer interest, and the quote "everything is encrypted" describing the network's default state.

**`From Aztec to Zcash_ The year 'pragmatic privacy' took root.md`** → [[protocols/aztec-network]], [[coins/zcash]], [[coins/privacy-coins-overview]]
Year-in-review for 2025 privacy developments: Aztec Ignition Chain, Namada L1, Miden ($25M funding), Privacy Pools launch, Coinbase hiring Iron Fish team, Circle USDCx testing, EY Nightfall, Canton Network, and Ethereum Foundation's Privacy Cluster.

---

## Privacy Pools

**`What is Privacy Pools_ _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Overview of the Privacy Pools protocol: how ASPs enable compliance-aware privacy, the proof-of-innocence concept, and the ragequit mechanism.

**`Privacy Pools_ How to Protect Users' Privacy While Meeting the Compliance Requirements.md`** → [[protocols/privacy-pools]]
Analysis of how Privacy Pools achieves both genuine user privacy and regulatory compliance through the ASP model, without requiring identity disclosure.

**`Privacy Pools — Striking The Balance In Privacy And Regulations.md`** → [[protocols/privacy-pools]]
Exploration of the privacy/compliance tradeoff in blockchain systems and how Privacy Pools' inclusion/exclusion proof design navigates it.

**`Core Concepts _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Technical documentation: commitments (value, label, nullifier, secret), nullifiers, Merkle trees, the Entrypoint contract, ASP roots, and the deposit/withdrawal flow.

**`ASP Layer _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Documentation of the Association Set Provider layer: how ASPs vet deposits, post Merkle roots on-chain, link to IPFS screening criteria, and how multiple ASPs coexist.

**`Circuits Interfaces _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Technical interface documentation for Privacy Pools' Circom ZK circuits.

**`Commitment Circuit _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Specification of the CommitmentHasher circuit: Poseidon hash with public inputs (value, label) and private inputs (nullifier, secret).

**`Contracts Interfaces _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Interface documentation for IPrivacyPool and IEntrypoint smart contracts.

**`Smart Contracts Layer _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Overview of the smart contract architecture: UUPS proxy pattern, AccessControl roles, deposit/withdrawal flows, fee management, pool lifecycle.

**`Withdrawal Circuit _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Specification of the Withdrawal circuit: state tree Merkle inclusion, ASP tree inclusion, nullifier validity verification.

**`LeanIMT Circuit _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
Documentation of the LeanIMT (Lean Incremental Merkle Tree) circuit used for efficient, dynamically-sized Merkle proofs.

**`SDK Utilities _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
TypeScript SDK documentation for Privacy Pools: utility functions for commitment creation, proof generation, and relay interactions.

**`Developer Guide _ Privacy Pools Documentation.md`** → [[protocols/privacy-pools]]
End-to-end developer guide: setting up the monorepo, running tests, deploying contracts, and integrating the SDK.

**`Prototyping Privacy Pools on Stellar.md`** → [[protocols/privacy-pools]]
Documentation of the Stellar/Soroban prototype: shows Privacy Pools is chain-agnostic. Covers Groth16 verification costs (~40M Soroban instructions, ~40% of testnet max).

**`Privacy Pools Documentation.md` and versions (1–4)** → [[protocols/privacy-pools]]
Additional Privacy Pools documentation pages covering various components of the protocol stack.

---

## Starknet

**`Starknet in 2025_ ZK Scaling Goes Mainstream — Year in Review.md`** → [[chains/starknet]]
Starknet's 2025 year-in-review: Stage 1 Rollup milestone (May 2025), 168% ecosystem growth, gaming explosion (4→51 projects), pre-confirmation improvements (2s→0.5s), AI agent integration.

**`Starknet Launches STRK20 Standard For Enhanced Privacy Features.md`** → [[chains/starknet]]
Announcement of STRK20 (March 10, 2026): encrypted balances, encrypted sender identities, encrypted transfer amounts, viewing keys for authorized parties, and compliance-by-design architecture.

**`Starknet Launches strkBTC to Advance Bitcoin Privacy in DeFi - _The Defiant_.md`** → [[chains/starknet]]
Coverage of strkBTC launch: privacy-native Bitcoin on Starknet, enabling private BTC DeFi without breaking composability.

**`Starknet Privacy Technology_ The Revolutionary Framework for Compliant Crypto Transactions.md`** → [[chains/starknet]]
Analysis of Starknet's privacy framework: encrypted states, selective disclosure, FATF Travel Rule compatibility, and institutional appeal.

**`Starknet introduces strkBTC to bring 'private bitcoin' and confidential DeFi transactions to its Layer 2 network.md`** → [[chains/starknet]]
Technical overview of strkBTC: deterministic issuance, shielded balances, DeFi composability.

**`Why Starknet Has the Potential to Become Crypto's Ultimate Privacy Chain.md`** → [[chains/starknet]]
Analysis article: Starknet's combination of STARKs (no trusted setup), native account abstraction, STRK20, strkBTC, and high throughput makes it the most complete privacy infrastructure of any L2.

**`The State of the Starknet Ecosystem 2025.md`** → [[chains/starknet]]
Comprehensive ecosystem report: DeFi protocols, gaming (Dojo, 51 projects), AI agent integration, wallet options (11), bridge partners, CCTP integration, SN Stack availability, dual-token staking (STRK + BTC).

**`Addressing the Privacy and Compliance Challenge in Public Blockchain Token Transactions.md`** → [[chains/starknet]], [[concepts/privacy-vs-compliance]]
Analysis of the compliance challenge for public blockchain tokens and how Starknet's viewing key architecture and STRK20 provide a regulatory compliance path.

---

## Other Privacy Chains

**`Secret Network Introduction _ Secret Network.md`** → [[chains/secret-network]]
Introduction to Secret Network: first private smart contracts on mainnet (September 2020), Intel SGX TEE architecture, Rust/CosmWasm Secret Contracts, Cosmos SDK foundation, 30+ dApps, 100+ builders.

**`Penumbra - Home.md`** → [[chains/penumbra]]
Homepage content: $3.77M 30-day DEX volume, 6 connected chains, private DEX features (traders and LPs hide strategies), end-to-end encryption with ultralight nodes, IBC multi-chain shielding.

**`Private, anonymous, and easy to use cryptocurrency.md`** → [[protocols/iron-fish]]
Iron Fish homepage: ZK Layer 1, multi-asset private transactions, a16z-backed, $27-28M raised, Node App and OreoWallet, Coinbase team acquisition in 2025.

**`Instant Crypto Swaps _ Fast & Secure Exchange.md`**
Overview of instant swap/exchange services for acquiring privacy coins without full KYC. Relevant to users seeking Monero after exchange delistings.

---

## On-chain ZK Privacy Ecosystem

**`On-chain ZK Privacy Ecosystem.md`** → [[coins/privacy-coins-overview]], [[protocols/railgun]]
Ecosystem survey article covering Railgun's features (shield assets, private DeFi, viewing keys, proof of innocence, governance), Penumbra's DEX, Iron Fish's multi-asset approach, and the broader ZK privacy landscape as of 2025.
