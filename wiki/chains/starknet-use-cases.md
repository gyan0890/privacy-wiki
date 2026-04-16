# STRK20 Use Cases

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[chains/strk20]], [[chains/starknet]], [[concepts/privacy-vs-compliance]]

---

## Overview

STRK20 is not a general-purpose privacy tool. Its design — native compliance, atomic DeFi composability, client-side proving, low cost per transaction — makes it specifically suited to a set of use cases where existing solutions fail. This page examines each in depth: the problem it solves, how STRK20 addresses it, and why alternative chains cannot replicate it.

---

## 1. Private On-Chain Payroll & Invoicing

### The Problem

Every on-chain salary payment is permanently public. A single address lookup on any block explorer reveals:

- Exact salary of every employee paid in crypto
- Full compensation history across the organization
- Business relationships with contractors and their rates
- Payroll cadence and cash flow patterns

This is not a theoretical concern. Companies that have attempted on-chain payroll have faced exactly these leaks. The result: on-chain payroll has remained a niche product confined to crypto-native organizations comfortable with radical transparency. Traditional companies — which represent the majority of potential enterprise blockchain adoption — have a hard structural blocker.

### The STRK20 Solution

With STRK20, a payroll processor operates from a shielded pool:

1. The company's treasury holds tokens in its STRK20 privacy pool.
2. Each pay cycle, the processor executes `UseNote` (company funds) → `CreateNote` (employee's shielded address).
3. No public link exists between the company wallet and individual employee wallets.
4. Employees receive shielded balances. They can hold, spend within the privacy pool, or `Withdraw` to a public address at their discretion.

For contractors and invoices, the same flow applies. A contractor submits a shielded address; the company pays to that address. The invoice amount, counterparty identity, and payment date are all private to the two parties (and the auditing entity if required).

### Why This Matters at Scale

Payroll is structurally different from other use cases:

- **Recurring**: every two weeks, every month — high frequency
- **High-value**: large token volumes per transaction
- **Volume**: hundreds or thousands of employees per company

Every pay cycle is a cluster of high-value transactions. At enterprise scale, payroll could represent one of the highest sustained fee-density use cases on the network — not a one-time event but a structural revenue engine.

### Compliance Integration

Payroll is one of the most compliance-heavy financial activities: employment records, tax withholding, wage reporting, AML requirements for larger payments. STRK20's viewing key architecture handles this natively:

- Employers escrow viewing keys with their accounting system or auditor.
- All payment history is reconstructible for tax filings and audits.
- Travel rule data (sender/receiver identity and amount) is available to authorized parties without being permanently public.

### Opportunity: Enterprise Payroll Platforms

Global payroll platforms processing billions annually in contractor payments are a natural integration target. The combination of STRK20's compliance framework with a payroll product's existing KYC/AML infrastructure could create the first enterprise-grade private on-chain payroll product at scale.

---

## 2. Political & Charitable Donations

### The Problem

The right to donate to political causes and charities without public disclosure is a cornerstone of freedom of association in most democratic jurisdictions. Traditional finance protects this — your bank does not post your political donations publicly.

On-chain donations destroy this protection entirely. Any contribution to a political campaign, activist organization, or cause in a jurisdiction with political risk is permanently traceable to the donor's on-chain address — and from there, often to their identity.

The **chilling effect** is real and documented: donors in adversarial political environments, whistleblowers supporting oversight organizations, individuals in jurisdictions where certain causes are persecuted. Public-chain crypto donations create a permanent, searchable record that can be used against donors.

At the same time, donation-receiving organizations — political campaigns, NGOs, charities — face their own compliance requirements: FEC reporting in the US, AML obligations, donor KYC for large gifts. They cannot simply accept anonymous funds.

### The STRK20 Solution

STRK20 separates **public anonymity** from **regulatory compliance** — exactly what this use case requires.

- A donor shields their assets and donates to the campaign's shielded address.
- On the public blockchain: the paymaster address sends a transaction to the privacy pool contract. No donor identity. No donation amount.
- For regulatory compliance: the donating organization registers its viewing key with its compliance officer or the relevant electoral authority (e.g., FEC). All donations are auditable to them — donor identity (if KYC was performed off-chain), amount, date.
- The donor's privacy is protected from the general public; the organization's compliance obligations are met.

This is **compliant-privacy** in its purest form: hiding information from everyone except those with a legal need to know.

### Why This Is Distinctive

The critical insight is that donation-receiving organizations are not opposed to auditing — they actively need it. What they (and donors) need is the ability to comply with reporting requirements **without** making that information permanently public. STRK20 creates exactly this distinction.

Other "anonymous" crypto solutions (mixing services, Monero) fail organizations with compliance needs because they cannot selectively disclose to regulators. STRK20's viewing key architecture makes selective disclosure the default, not an afterthought.

### Opportunity: Election Cycle Impact

Political donation infrastructure is rebuilt around each major election cycle. A platform that enables compliant private donations — positioned explicitly as the crypto equivalent of a sealed ballot — could capture significant volume around US and international elections. The demand is high-frequency and concentrated in campaign seasons, making it an excellent product launch window.

---

## 3. Private OTC & Institutional Block Trades

### The Problem

Large on-chain trades face a fundamental adversarial environment:

- **Front-running**: a pending large order is visible in the mempool before execution. Bots buy ahead of the order and sell immediately after — extracting value directly from the trader.
- **Price impact signaling**: broadcasting a large buy of token X immediately depresses the price, even before the trade executes.
- **Counterparty intelligence**: competitors learn exactly what a fund is buying, when, and how much.

This is why institutional OTC trading exists off-chain. Large funds use OTC desks specifically to avoid these on-chain visibility problems. The consequence is that substantial institutional volume never touches on-chain venues.

### The STRK20 Solution

Both counterparties operate from shielded balances. A block trade on STRK20 looks like this:

1. Counterparties negotiate the trade off-chain (amount, price, settlement time).
2. Both hold their respective tokens in STRK20 shielded balances.
3. An atomic settlement transaction simultaneously `UseNote` for both sides and `CreateNote` for both recipients.
4. On-chain: a single transaction from the paymaster to the privacy pool. No visible amounts, no counterparty identities.
5. Each counterparty can verify their note receipt client-side.

This creates a **genuinely new market**: private on-chain OTC settlement with atomic finality, at the cost and speed of Starknet. No off-chain custodian required. No counterparty default risk (atomic settlement). No information leakage.

### Why Only on Starknet

Private atomic settlement requires:

- Privacy at the execution layer (not just a wrapper)
- Low enough cost that OTC-sized trades are economically efficient
- Proving overhead small enough that settlement is fast

Starknet's Stwo prover achieves the cost/performance profile required. On EVM chains, ZK proof generation costs are high enough that large OTC trades become economically unattractive. Starknet's proof economics — optimized for the STARK prover — are a structural moat.

### Opportunity: Institutional DeFi

OTC desks and prime brokerage services serving institutional crypto clients are a direct integration target. A private settlement layer with compliance viewing keys (for fund auditors) and atomic finality is a product that has no equivalent on any other chain today.

---

## 4. Private AI Agent Payments

### The Problem

AI agents executing financial tasks on-chain create a new category of information leakage. An agent that pays for APIs, services, compute resources, and inter-agent transactions using a public wallet exposes:

- Which AI strategies are active and at what scale
- Which external services (oracles, data providers, LLM APIs) the agent uses
- Agent-to-agent payment relationships (revealing multi-agent architectures)
- Activity timing (allowing inference about when strategies are running)

This is not theoretical — as AI agent deployment on-chain scales, the payment graph becomes a rich intelligence source for competitors and MEV extractors.

### The STRK20 Solution

An AI agent holds its operational budget in a STRK20 shielded balance. All agent payments execute from the privacy pool:

- API payments: `UseNote` → paymaster → API provider's shielded address
- Inter-agent transfers: channel-based private payments between agent wallets
- Compute resource payments: same flow, private amounts

The agent's **on-chain footprint becomes opaque**. Competitors cannot identify which strategies are running, which data sources are being queried, or how much is being spent. MEV bots cannot front-run agent transactions because they cannot identify agent activity.

### Unique Starknet Advantage

AI agents need **programmable + private**. This combination does not exist on EVM chains:

- Privacy protocols on EVM (Tornado Cash, Railgun) are not natively composable with arbitrary smart contract logic.
- Agents need to make conditional payments, interact with DeFi, respond to oracle data — all from a private context.

STRK20 is the only primitive that combines Cairo's full programmability (arbitrary smart contract logic) with native privacy in a single composable layer. An agent can deposit into the privacy pool, execute a swap, and make a conditional payment — all in a single Cairo transaction, all private.

### Emerging Ecosystem

Starknet's ELIZA multi-agent framework integration (2025) positions the network as a leading platform for on-chain AI agent activity. STRK20 is a natural complement: as agent deployment scales, agents handling real financial value will have strong incentives to operate privately. The privacy pool becomes a standard component of agent architecture.

---

## 5. Private Gaming & Virtual Economies

### The Problem

Fully on-chain games require all state to be on the blockchain — including player inventories, balances, and strategies. This is not just a privacy inconvenience; it fundamentally breaks competitive game design:

- **Opponent intelligence**: in any strategy game, seeing your opponent's full resource state removes the strategic dimension.
- **Targeted extraction**: players with large on-chain inventories become targets for coordinated attacks.
- **Balance sniping**: bots monitor player balances and act on that information (e.g., purchasing items just before a player needs them).
- **Meta-game distortion**: professional players avoid on-chain games entirely because public state eliminates strategic depth.

This is a known limitation of Starknet's existing gaming ecosystem. Games like Loot Survivor are built on Starknet precisely for compute capabilities, but the public state limitation has kept serious competitive gaming off-chain.

### The STRK20 Solution

In-game assets are represented as STRK20 tokens (shielded ERC-20s). Player balances and inventories are held in the privacy pool:

- **Shielded inventory**: a player's item holdings are not visible to opponents.
- **Private trades**: player-to-player trades execute as note exchanges — neither side reveals their full holdings.
- **Hidden strategies**: in-game resource accumulation, crafting, and preparation are private until the player chooses to reveal (e.g., at the point of action).
- **Fair competitive play**: information asymmetry is based on gameplay, not blockchain lookups.

Game logic itself can remain public (ensuring fair rules) while player state becomes private. The combination of provable execution (Starknet's STARK proofs ensure game rules are followed) and private state (STRK20 hides player inventories) is architecturally unique.

### Why This Is a Starknet-Native Opportunity

Starknet already has the on-chain gaming community. Dojo Engine projects, Loot Survivor, and a growing ecosystem of provable games are native to the network. STRK20 is not a new audience — it is a privacy upgrade for an existing community that has been waiting for exactly this capability.

No other chain has both the compute for complex game logic (via Cairo's provable execution) and native privacy (STRK20) in a single composable environment.

---

## 6. Confidential Prediction Markets

### The Problem

Prediction market positions are currently visible on-chain. This creates two specific failure modes:

**Signaling manipulation**: a large position taken on a prediction market is itself a signal that sophisticated actors exploit. If a well-known trader buys a large stake on one outcome, other participants update their beliefs based on that visible action — even if the original trader has no special information. Visibility corrupts price discovery.

**Adversarial inference**: in markets for sensitive events (political elections, corporate outcomes, geopolitical events), public positions create risk for participants. Taking a position on a politically sensitive outcome in an adversarial jurisdiction can have real-world consequences.

### The STRK20 Solution

Prediction market positions held as shielded notes. The market mechanism itself runs on-chain (transparent, auditable), but individual positions are private until resolution.

At resolution, the winning positions can be verified against the shielded pool — the protocol can prove that the winning side collectively held a certain total stake (for liquidity pool calculations) without revealing individual positions. This requires some additional ZK circuit design for the aggregation step, but is feasible within STRK20's architecture.

The result: a prediction market with **genuine price discovery** — prices reflect information, not social signaling — and **participant safety** in sensitive political or reputational contexts.

---

## 7. Private Identity & Credential Payments

### The Problem

Two developments are on a collision course:

1. **ZK-based identity systems** (Worldcoin, Starknet ID, Proof of Humanity) can prove things about a user — "this is a human", "this person is over 18", "this address has passed KYC" — without revealing which specific human.
2. **On-chain payments** are fully public and link every payment to an address.

The combination today is broken: you can prove you're a human without revealing your identity, but when you pay, you reveal your address — and from your address, your entire payment history.

### The STRK20 Solution

Combining ZK identity with STRK20 payments creates a new primitive: **private verified commerce**.

The flow:
1. A user attaches a ZK identity proof to their STRK20 account: "this account is controlled by a verified human with KYC status X".
2. When making a payment, the transaction includes a proof of identity attribute without revealing the specific identity.
3. The merchant or service receives: proof that a verified human paid, the payment amount (in a shielded note), and the compliance-relevant identity attributes — without learning which specific person paid.

Use cases:
- **Age-gated purchases**: prove you are over 18 without revealing your identity or payment history.
- **KYC-gated services**: access services requiring identity verification while keeping transactions private.
- **Human-verified micropayments**: content platforms, APIs, and services that want to exclude bot payments while preserving user privacy.
- **Reputation-portable commerce**: users carry verifiable credentials between services without creating a permanent public link between their identity and their purchasing behavior.

This is a genuinely new class of transaction that does not exist in traditional finance (which links identity to payment by default) or current crypto (which either exposes everything or verifies nothing).

---

## Summary: Where STRK20 Wins

| Use Case | Why Not Public Chain | Why Not Existing Privacy Solutions | STRK20 Advantage |
|---|---|---|---|
| Payroll | Salary exposure blocks adoption | Monero has no compliance; Zcash has no smart contracts | Compliance + smart contract composability |
| Donations | Chilling effect on free association | Mixers have no selective disclosure | Viewing key = selective disclosure to regulators |
| OTC Trades | Front-running, price signaling | No atomic settlement with privacy | Atomic private settlement on low-cost chain |
| AI Agents | Payment graph exposure | EVM privacy tools lack programmability | Cairo programmability + native privacy |
| Gaming | Public state breaks competitive design | No existing chain has compute + privacy | Starknet's compute capability + STRK20 |
| Prediction Markets | Position signaling corrupts discovery | No compliant private position-taking exists | Private positions with auditable aggregation |
| Identity Payments | Identity always linked to payment | No identity+privacy primitive exists | ZK identity + shielded payments = verified private commerce |

---

## See Also

- [[chains/strk20|STRK20 Protocol]] — Technical architecture of the STRK20 standard
- [[chains/starknet|Starknet Overview]] — Network architecture and ecosystem
- [[concepts/privacy-vs-compliance|Privacy vs. Compliance]] — The design tradeoffs STRK20 navigates
- [[research/scalable-compliant-privacy-starknet|Whitepaper Summary]] — The StarkWare specification this builds on
