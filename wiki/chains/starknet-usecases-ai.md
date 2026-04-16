# STRK20 Use Cases: AI, Machine Learning & Autonomous Agents

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[chains/strk20]], [[chains/starknet-use-cases]], [[chains/starknet]]

---

## Overview

AI and privacy are on a collision course. Modern AI systems are trained on sensitive data, generate inferences from private inputs, and increasingly act as autonomous financial agents holding real assets. Every step in this pipeline leaks information: training data reveals what the model knows, inference inputs reveal what users ask, and agent behavior reveals the strategies they execute.

STRK20 and Starknet's ZK architecture address several layers of this problem — particularly the settlement, incentive, and verification layers — while pairing with off-chain privacy compute (FHE, MPC, federated learning) for the heavy computational work. This page covers nine use cases at the intersection of AI and privacy.

---

## 1. Encrypted RAG (Retrieval-Augmented Generation)

### The Concept

A Retrieval-Augmented Generation (RAG) system that answers queries over a private knowledge base without the inference server learning the query, the retrieved documents, or the answer. The data owner monetizes access to their knowledge base without exposing its contents.

### Market Landscape

Enterprise RAG (non-private) is growing rapidly: 72% of enterprises are prioritizing private/hybrid LLM deployments in 2025, and the largest blocker for SMB AI adoption is "inability to use internal data securely."

**Private AI** (private-ai.com) offers privacy filters for RAG pipelines. **Amazon Bedrock** provides confidential computing infrastructure for protected RAG deployments. Differential Privacy-based RAG (MURAG algorithm) is published research, with individual privacy filtering built into the retrieval step.

**The gap**: No production blockchain-native encrypted RAG system exists. Current solutions are centralized server-side privacy (you trust the server not to look). A cryptographically verifiable private RAG — where the data owner can prove their knowledge base was queried privately — doesn't exist at production scale.

### Why STRK20 / Starknet

STRK20's role is in the **economic layer** of encrypted RAG, not the compute layer:

- Data owners tokenize their knowledge base as STRK20-gated access rights. Each query requires a STRK20 micro-payment; the payment is private (data owners don't learn which organizations are querying their data).
- Stwo proofs verify that the RAG system returned results from the committed knowledge base (anti-hallucination guarantee for regulated industries).
- Compliance: viewing keys allow audit of total query volume and revenue without exposing which specific queries were run.

The actual encrypted RAG computation runs off-chain using confidential computing (AWS Nitro Enclaves, Azure Confidential Computing) or FHE (Zama). Starknet settles access rights and payments.

### Product: VaultQuery

A private knowledge base marketplace where organizations monetize proprietary data via encrypted RAG with STRK20-settled access payments.

**How it works:**

1. Data owner indexes their knowledge base, encrypts it, and commits the encrypted index root hash on-chain.
2. Queries: users submit STRK20 micro-payments + encrypted query. The off-chain inference engine (confidential computing) executes RAG against the encrypted index.
3. Results returned to user. Stwo proof verifies that results came from the committed index (not fabricated).
4. Data owner receives STRK20 payment. The querying organization is hidden.
5. Audit: data owner's viewing key reveals total query volume + revenue — not individual query contents.

**Target Users:** Financial research firms (monetizing proprietary databases), legal knowledge bases (case law, contract templates), medical protocol databases (clinical decision support), corporate knowledge management.

**Business Model:** Marketplace with per-query fees.

**Revenue Model:**
- Marketplace commission: 10–20% of each query payment
- Data owner listing fee: $500–$5,000/month per knowledge base indexed
- Compliance tier (HIPAA/GDPR-certified query infrastructure): $50,000–$200,000/year per enterprise deployment

---

## 2. Encrypted Model Training

### The Concept

Training a machine learning model on encrypted data — using Fully Homomorphic Encryption (FHE) — so that the model developer never sees the raw training data. Sensitive datasets (medical records, financial transactions, behavioral data) can train production models without privacy exposure.

### Market Landscape

**Zama** ($1B+ valuation, 2023) is the category leader. Their Concrete ML library is open-source and scikit-learn compatible. It supports encrypted Logistic Regression training as of Concrete ML v1.4+. PyTorch conversion APIs allow standard ML code to be compiled to FHE circuits.

**GPU-accelerated FHE** frameworks (HEngine, CAT) are emerging and reducing training overhead.

**The honest limitation**: FHE encrypted training is 1,000–100,000× slower than plaintext training. For simple models (logistic regression, small neural networks), this is manageable. For deep learning, it is currently impractical — even with GPU acceleration. The technology is advancing rapidly; Zama expects practical deep learning FHE within 3–5 years.

**Starknet's specific role**: STARK proofs verify computation correctness; they don't execute computations on encrypted data. Starknet cannot run FHE training natively. Its role is the **settlement and audit layer** for encrypted training programs.

### Product: EncryptTrain

An encrypted model training marketplace where data contributors are paid in STRK20 and Stwo proofs verify training integrity.

**How it works:**

1. Model developer posts training request: desired model architecture, dataset requirements, maximum training budget (STRK20).
2. Data contributors encrypt their datasets and submit FHE-encrypted training batches off-chain.
3. Training coordinator (off-chain, confidential computing) aggregates encrypted gradients and returns updated model.
4. Stwo proof generated: verifies that the model checkpoint is derived from the claimed dataset (integrity guarantee, not privacy guarantee).
5. Data contributors receive STRK20 payments proportional to their contribution, verified by the on-chain proof.

**Target Users:** Healthcare providers contributing patient data to disease models, financial institutions training fraud detection models on combined transaction data, retail companies training recommendation models without sharing customer data.

**Business Model:** Marketplace with training coordination fees.

**Revenue Model:**
- Coordination fee: 5–10% of total training budget
- Data quality certification (audited datasets that meet minimum quality thresholds): $5,000–$50,000 per certification
- Enterprise deployment: managed FHE training infrastructure with SLA: $50,000–$500,000/year

---

## 3. Collaborative Encrypted Model Training

### The Concept

Multiple organizations contribute data to train a shared model via federated learning, with privacy guarantees: no participant's data leaves their environment, Stwo proofs verify each gradient update is valid, and STRK20 incentives distribute revenue from the trained model back to contributors.

### Market Landscape

**Flower** (flwr.dev) is the leading federated learning framework — open source, production-deployed by dozens of enterprises. It supports horizontal federated learning (same model architecture, different organizations' data).

**Ocean Protocol** (Compute-to-Data) lets data owners offer compute access to their data without giving the data itself to model trainers. $5M raised (older data); 1.4M Ocean Nodes deployed in 70+ countries.

**Gensyn** (decentralized ML compute) raised significant VC backing for distributed training coordination.

**Healthcare federated learning**: 2024–2025 research shows federated learning on medical imaging achieving 96.1% accuracy with differential privacy (ε=1.9). Multi-center healthcare studies are the primary production use case today.

**Blockchain's specific role**: Most federated learning runs without blockchain (Flower coordinates over HTTP). Blockchain adds: (1) verifiable contribution accounting (who contributed what gradient), (2) censorship-resistant incentive distribution, (3) immutable audit trail for regulated industries.

### Product: FederatedStark

A federated learning coordination protocol on Starknet with Stwo-verified gradient contributions and STRK20 incentive distribution.

**How it works:**

1. Model organizer deploys training contract: architecture, contribution requirements, training rounds, budget (STRK20).
2. Participants (hospitals, banks, enterprises) run local training on their private data. Each round, they compute gradient updates.
3. Each participant submits their gradient update + Stwo proof of "this gradient was computed on a dataset meeting the quality requirements." The gradient itself is submitted off-chain (encrypted); only the proof goes on-chain.
4. Training coordinator aggregates encrypted gradients (off-chain) → produces new model checkpoint.
5. At training completion: each verified contributor receives STRK20 payment proportional to their Stwo-proved contributions.
6. Model access rights are tokenized: downstream users pay STRK20 to run inference; revenue flows back to contributors.

**Target Users:** Hospital networks (disease model training across institutions), insurance consortia (risk model improvement), retail analytics (customer behavior models without data sharing), autonomous vehicle networks (safety model training).

**Business Model:** Protocol with per-training-round fees and model licensing.

**Revenue Model:**
- Training round fee: 2–5% of total training budget per round
- Model licensing: 10–30% of downstream inference revenue flowing to contributor pool
- Enterprise setup: $50,000–$500,000 for custom federated learning consortium setup

---

## 4. Encrypted ML Predictions

### The Concept

Running ML inference on encrypted inputs — the user's input never leaves their device in plaintext, and the model never learns what it was asked. Outputs are encrypted and returned to the user. This is "blind inference" or "private prediction."

### Market Landscape

**Nillion** ($45M Series A, $400M valuation) launched mainnet in March 2025. Its nilAI framework provides private inference: linear computations on the server, non-linear activations handled client-side (hybrid MPC approach). 60+ projects building on the platform.

**Zama Concrete ML** supports encrypted inference for models up to moderate complexity (logistic regression, shallow neural networks).

**EncryptedLLM** (research paper, 2025) achieves 200× faster CPU FHE inference via GPU acceleration.

**The honest tradeoff**: Private inference today is practical for simple models and batch predictions. Real-time LLM inference with full input privacy is still 100–1,000× too slow for consumer applications. The technology is improving; niche production deployments are viable today.

### Why STRK20 / Starknet

- Starknet's role: verify that the inference provider ran the computation correctly (Stwo proof of inference), not encrypt the computation itself.
- STRK20 payment: users pay for encrypted inference via shielded notes. The prediction service doesn't know who is querying (user identity hidden) or what they queried (input encrypted).
- Marketplace: prediction services are listed on-chain; payments settle via STRK20; Stwo proofs of inference correctness are the trust mechanism.

### Product: BlindOracle

A private ML prediction marketplace where users query encrypted models with hidden inputs.

**How it works:**

1. Model owner registers a prediction service on BlindOracle: model architecture commitment (hash), per-query STRK20 price.
2. User encrypts their input locally (using model owner's public key) → submits encrypted query + STRK20 payment note.
3. Model owner runs inference on encrypted input (off-chain, via Nillion or Zama) → returns encrypted result + Stwo proof of correct inference.
4. User decrypts result locally.
5. Model owner receives STRK20 payment. User's query content remains unknown to the model owner.

**Target Users:** Healthcare (private symptom checker where clinic doesn't learn your symptoms), financial risk scoring (bank runs credit model without seeing applicant's full financial data), fraud detection (merchant verifies card without learning spending history).

**Business Model:** Marketplace with per-inference fees.

**Revenue Model:**
- Marketplace commission: 10–15% of per-inference fees
- Model listing fee: $100–$1,000/month per model hosted
- Enterprise tier (custom SLA, dedicated inference infrastructure): $50,000–$200,000/year

---

## 5. Encrypted ML Marketplaces

### The Concept

A marketplace for AI models and training datasets where buyers and sellers transact with privacy: buyers don't reveal what they're training; sellers don't expose model weights or training data; and payments are private.

### Market Landscape

**Ocean Protocol** is the most mature decentralized data marketplace. As of 2025: 1.4M Ocean Nodes in 70+ countries, Ocean Predictoor generating $2B+ in volume on Oasis Sapphire. Enterprise v1 launching Q3 2025. Ocean's Compute-to-Data architecture lets buyers run models on sellers' data without the data ever leaving the seller's custody.

**Ritual Network** is building an L1 blockchain for AI with an Infernet oracle for on-chain model execution. It positions Starknet-style logic but specialized for AI workloads.

**SingularityNET + Fetch.ai + Ocean** merged into the **Artificial Superintelligence Alliance (ASI)** in 2024 — the largest decentralized AI ecosystem by token market cap.

**The gap STRK20 fills**: Ocean and ASI use transparent token transactions. Buyers reveal what they're buying; sellers see who bought. For sensitive AI use cases (a bank buying a competitor's risk model, a pharma company buying genomics data), this transparency is a dealbreaker.

### Product: PrivateAI Market

A privacy-first AI model and dataset marketplace built on STRK20.

**How it works:**

1. Seller lists asset: dataset or model. Encrypted metadata (description readable to all; underlying asset encrypted). Commitment hash of asset posted on-chain.
2. Buyer browses listings. Interest is expressed via anonymous STRK20 note payment.
3. On payment confirmation: seller generates a Stwo proof that the delivered asset matches the committed hash. Buyer receives decryption key via STRK20 channel (ECDH-encrypted).
4. Neither buyer's nor seller's full identity is revealed in the transaction — only their Starknet shielded addresses.
5. Dispute resolution: the committed hash and the delivered asset can be compared by an arbitrator with viewing key access.

**Target Users:** Financial institutions buying proprietary risk models, pharmaceutical companies licensing genomics datasets, enterprises buying competitor-class models without revealing their AI strategy.

**Business Model:** Marketplace with commission.

**Revenue Model:**
- Marketplace fee: 3–5% of each transaction
- Premium listing (featured, verified quality certification): $1,000–$10,000/month
- Compliance wrapper (audited data provenance, GDPR-compliant dataset certification): $10,000–$100,000 per dataset

---

## 6. Private Analytics

### The Concept

Analytics systems that compute aggregate statistics (DAU, revenue, cohort metrics) over user behavior data without any individual data points being exposed. Differential privacy adds calibrated noise; ZK proofs verify the noise was correctly added. Data is useful for business decisions; no individual can be identified.

### Market Landscape

**Plausible Analytics** and **Fathom Analytics** are the consumer-facing privacy analytics leaders — both GDPR-compliant, cookie-free, no individual tracking. Revenue model: SaaS $9–$99/month.

**PrivChain-AI** (2025 research) achieved 94.7% fraud detection accuracy with strong differential privacy (ε=1.0) on blockchain-coordinated analytics. 40% faster communication than baseline.

**Apple** has invested billions in differential privacy infrastructure, using it across iOS to collect aggregate device usage statistics without individual exposure.

**The on-chain opportunity**: DeFi protocols, NFT marketplaces, and Starknet dApps have valuable behavioral data (swap patterns, liquidity provision strategies, NFT collection behaviors) that they can monetize to researchers and competitors — but only if they can publish the insights without exposing individual users.

### Product: StealthMetrics

On-chain differential privacy analytics for Starknet protocols, with Stwo-verified noise addition.

**How it works:**

1. Protocol integrates StealthMetrics SDK: behavioral events (swaps, LP actions, governance votes) are locally differentially privatized before leaving the user's client.
2. Events aggregated on-chain: Starknet contract accumulates noisy event counts by cohort.
3. At query time (weekly/monthly): Cairo contract generates Stwo proof that the published aggregate was computed with the declared privacy budget (ε, δ). Any researcher querying the aggregate can verify the proof.
4. Researchers pay in STRK20 to access aggregate cohort analytics. Data owner receives payments; individual users are protected.

**Target Users:** DeFi protocols (Ekubo, JediSwap on Starknet) wanting to monetize anonymous usage data, NFT marketplaces tracking collector behavior, Starknet Foundation tracking ecosystem metrics without surveillance.

**Business Model:** Analytics-as-a-service with data buyer fees.

**Revenue Model:**
- Data buyer access fee: $500–$5,000/month per protocol's analytics feed
- Protocol integration fee: $5,000–$50,000/year per protocol using StealthMetrics
- Compliance certification (GDPR/CCPA-approved DP implementation): $20,000–$100,000/year

---

## 7. Private Recommendation Engines

### The Concept

Recommendation systems that improve suggestions without the platform ever seeing individual user behavior. Users contribute interaction data via federated learning; models improve over time; the platform earns revenue from better recommendations — without building a surveillance data store.

### Market Landscape

**Federated recommendation systems** are in production at major tech companies. Google's Gboard uses federated learning for next-word prediction. Academic frameworks (2025) show group-verifiable secure aggregation with secret sharing, dynamic privacy budget allocation, and hybrid neuro-fuzzy models for interpretability.

**The privacy imperative**: GDPR's data minimization principle is increasingly enforced. Fines for behavioral profiling without consent have reached hundreds of millions of dollars. Federated recommendation sidesteps most GDPR liability because no personal data leaves the user's device.

**Starknet's opportunity**: Most federated recommendation is centralized (Google, Apple). A decentralized federated recommendation protocol — where contributors are paid and no central party holds the model — doesn't yet exist at production scale.

### Product: RecoStark

A decentralized federated recommendation protocol on Starknet with STRK20 user incentives.

**How it works:**

1. Application deploys RecoStark: specifies model architecture, minimum contributors, STRK20 reward pool.
2. Users install lightweight local model (stored on device). As they interact with the app, the local model fine-tunes on their behavior (never leaves device).
3. Periodically: user's device submits encrypted gradient update + Stwo proof of valid contribution (gradient was computed on real interactions, meets minimum data quality).
4. Platform aggregates updates (federated averaging, off-chain), publishes new model checkpoint.
5. STRK20 rewards distributed to contributors proportional to verified gradient contributions.
6. Recommendations improve; user behavior data never leaves their device.

**Target Users:** DeFi protocols wanting personalized token recommendations without tracking users, NFT marketplaces optimizing collection discovery, social dApps on Starknet improving content feed quality.

**Business Model:** B2B protocol licensing.

**Revenue Model:**
- Protocol fee: 5–10% of STRK20 reward pool per training round
- Premium model hosting (real-time inference, custom model architecture support): $10,000–$100,000/year
- Analytics reporting (aggregate recommendation performance metrics, privacy-preserved): $5,000–$50,000/year

---

## 8. Encrypted Behavioral Analytics

### The Concept

User behavior data (clicks, dwell time, scroll depth, purchase patterns) analyzed in aggregate without any individual behavior record being stored or transmitted in plaintext. Privacy is cryptographic — not policy-based.

### Market Landscape

**Apple** is the benchmark: its Differential Privacy implementation (iOS, macOS) collects aggregate usage statistics with formally bounded privacy loss. The PPML (Privacy-Preserving Machine Learning) workshop (2025) showcased Apple's research in private behavioral analytics. Apple reports aggregate emoji usage, popular words, browsing patterns — with no individual records.

**iCloud Private Relay** (Apple) uses a multi-hop architecture where no single server knows both who the user is and what they're browsing.

**The on-chain opportunity**: Blockchain behavioral analytics today are completely public. Every wallet's behavior — which protocols they use, when, how much — is permanently exposed. STRK20 plus differential privacy enables the first provably private on-chain behavioral analytics layer.

### Product: PrivBehavior

An on-chain behavioral analytics layer for Starknet that applies differential privacy to protocol usage metrics.

**How it works:**

1. User's STRK20 transactions are locally perturbed with calibrated DP noise before being recorded on a behavior analytics ledger.
2. Protocol analytics engine aggregates noisy signals → produces behavior cohorts (e.g., "high-frequency traders," "passive LPs," "governance participants").
3. Cairo contract generates Stwo proof that cohort statistics were derived from STRK20-compliant private inputs.
4. Behavior insights sold to:
   - Protocol growth teams (optimize user journeys): STRK20 access fee
   - Ecosystem researchers (Starknet Foundation, VCs): STRK20 access fee
   - Competitors (benchmarking): STRK20 access fee with differential privacy (no individual behavior learnable)

**Target Users:** Starknet protocols, ecosystem researchers, VC firms doing quantitative diligence on Starknet projects.

**Business Model:** Analytics marketplace.

**Revenue Model:**
- Cohort data subscription: $1,000–$10,000/month per data buyer
- Custom cohort construction: $5,000–$50,000 per bespoke research request
- Protocol integration (embed PrivBehavior analytics tracking): $5,000–$50,000/year

---

## 9. Autonomous Crypto Agents

### The Concept

AI agents that hold STRK20 shielded balances, execute trades and transactions autonomously, and hide their on-chain footprint from competitors and MEV extractors. The agent's holdings, strategies, and activity patterns are private by default.

### Market Landscape

**Virtuals Protocol** (Base L2) is the leading AI agent launchpad. Reached $1.9B market cap in November 2024. Agents are tokenized — users hold "agent tokens" and earn from agent performance. Revenue model: 5–10% on token creation + 2–5% ongoing trading.

**ElizaOS** (formerly ai16z, Solana-based) is the dominant open-source AI agent framework. Rapidly growing builder ecosystem in 2025.

**AI crypto tokens market cap**: $7.02B as of February 2025. Hundreds of autonomous agents are deployed managing liquidity, arbitrage, governance participation, and social media engagement.

**The privacy problem**: Every agent's on-chain transactions are public. A successful agent's trading strategy can be reverse-engineered from its on-chain history. MEV bots front-run agents' large swaps. Competitors copy strategies visible in the mempool.

**Starknet + STRK20 as the privacy layer for AI agents** is a direct fit: Starknet already has ElizaOS integration (announced 2025 Starknet ecosystem), and STRK20 provides the shielded treasury.

### Product: GhostAgent

A framework for deploying autonomous AI agents on Starknet with STRK20-shielded treasuries.

**How it works:**

1. Agent developer deploys an ElizaOS-compatible agent configured to use a Starknet wallet with STRK20 treasury.
2. Agent holds operational capital as STRK20 shielded notes. On-chain observers see only: paymaster → privacy pool. No agent address visible.
3. Agent executes trades via Ekubo (Starknet's DEX): `UseNote` → swap → `CreateNote`. Trade amounts hidden; strategy inferred only from aggregate pool movements (not individual agent positions).
4. Agent-to-agent payments (multi-agent systems): STRK20 channel transfers between agent addresses — private from external observers.
5. Performance metrics: agent operator can prove performance (via viewing key access to own notes) without revealing the strategy to competitors.

**Target Users:** Quantitative crypto funds deploying on-chain strategies, MEV mitigation tooling for institutional traders, DAO treasury management bots, autonomous DeFi yield optimization agents.

**Business Model:** Framework licensing + performance fee protocol.

**Revenue Model:**
- Framework license: $5,000–$50,000/year for commercial agent deployments
- Protocol performance fee: 1–2% of assets under agent management (settled in STRK20)
- Insurance/security audit: $10,000–$100,000 per agent security certification (MEV resistance + private treasury audit)
- Institutional custody tier (multi-sig + viewing key compliance dashboard for fund administrators): $50,000–$500,000/year

---

## Summary Table

| Use Case | Starknet's Role | Off-Chain Partner | Technical Readiness | Viability |
|---|---|---|---|---|
| Encrypted RAG | Settlement, access payments | AWS Nitro / Zama | **Production** (off-chain compute ready) | **High** |
| Encrypted Model Training | Settlement, audit trail | Zama FHE | **Research** (simple models viable) | **Medium** |
| Collaborative Training | Gradient verification, incentives | Flower / Gensyn | **Research** (healthcare deployments) | **Medium** |
| Encrypted ML Predictions | Marketplace, proof verification | Nillion / Zama | **Early Production** (Nillion mainnet 2025) | **High** |
| Encrypted ML Marketplaces | Settlement, provenance | Ocean Protocol model | **Production** (Ocean deployed) | **High** |
| Private Analytics | DP proof verification, access | Differential Privacy algorithms | **Production** (DP mature) | **High** |
| Private Recommendation | Contribution verification, incentives | Flower federated learning | **Research/Early** | **Medium** |
| Behavioral Analytics | DP proof, access marketplace | Apple DP methodology | **Production** (methods mature) | **High** |
| Autonomous Agents | Private treasury, MEV resistance | ElizaOS / Virtuals | **Production** (agents deployed) | **High** |

---

## See Also

- [[chains/strk20|STRK20 Protocol]] — Technical architecture
- [[chains/starknet-use-cases|Core Use Cases]] — Payroll, donations, OTC, AI agents
- [[chains/starknet-usecases-defi|DeFi Use Cases]] — Dark pools, perpetuals, lending
- [[chains/starknet-usecases-sensitive|Healthcare & Biometrics]] — DNA matching, patient analytics
