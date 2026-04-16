# STRK20 Use Cases: Identity, Social & Communication

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[chains/strk20]], [[chains/starknet-use-cases]], [[concepts/privacy-vs-compliance]]

---

## Overview

Identity and social use cases share a structural problem: the most useful things about a social network (finding people, building trust, transacting) require disclosing information — but disclosure is irreversible. Every piece of identity information shared online permanently expands your attack surface. STRK20's architecture — selective disclosure via ZK proofs, payment privacy, compliance-grade audit trails — maps directly onto the design requirements for privacy-preserving social infrastructure.

This page covers six use cases: selective disclosure credentials, private social graphs, private subscriptions, private messaging, private matchmaking, and private contact discovery.

---

## 1. Selective Disclosure

### The Concept

ZK credentials that prove specific attributes (age ≥ 18, nationality = EU, KYC status = verified) without revealing the underlying identity. A user can prove they are eligible for a service without sharing their name, address, or any other personal data. The credential itself is a ZK proof, not a document.

### Market Landscape

**Polygon ID** (rebranded as Billions in Feb 2025 after acquisition by Holonym, $30M Series A) is the leading enterprise ZK identity platform. POCs with Deutsche Bank and HSBC. Uses W3C Verifiable Credentials with ZK proofs for attribute-level disclosure.

**Holonym** acquired Gitcoin Passport (35M credentials) and is integrating ZK proofs for privacy-preserving verification. $5.5M seed funded.

**Worldcoin** registered 12–16M iris scans by 2025 and uses the Semaphore protocol for proof-of-personhood without identity disclosure. ZK proofs assert "this person has not already participated" without revealing who.

**zkMe** and similar providers offer ZK-KYC: regulated services can verify a user has passed KYC without receiving any personal data — just a ZK proof signed by an accredited KYC provider.

**The market signal**: 8.03% of all on-chain activity in the identity category uses Polygon ID / related ZK identity frameworks. Financial institutions see this as the path to compliant DeFi access without building their own identity infrastructure.

### Why STRK20 / Starknet

- STRK20's compliance framework (viewing keys for auditors) pairs with selective disclosure credentials: a user proves they have a valid credential → unlocks access to shielded pool → viewing key escrowed to the compliance auditor (not the credential issuer).
- This separates "can this user transact?" (credential check) from "who is transacting?" (compliance question) — allowing KYC-gated access to DeFi without the DeFi protocol ever seeing the user's identity.
- Cairo circuits: credential verification logic is Cairo-native; Starknet can verify any W3C Verifiable Credential's ZK proof as part of a transaction.

### Product: StarkPass

A ZK credential passport for Starknet that enables attribute-gated DeFi access.

**How it works:**

1. User completes KYC with an accredited issuer (e.g., Holonym, Worldcoin Orb). Issuer provides a ZK credential: "this wallet corresponds to a verified adult in jurisdiction X."
2. User stores credential in StarkPass wallet. The credential is a ZK proof — no personal data stored on-chain.
3. DeFi protocol sets access rules: "users must hold a valid age-18+ credential and non-US-person credential to access."
4. User submits StarkPass credential proof as part of transaction. Cairo contract verifies the proof.
5. User's identity is never shared with the DeFi protocol. Compliance auditor's viewing key only reveals that the user transacted — not who they are unless legally required.

**Target Users:** DeFi protocols that need KYC gating without handling personal data (regulatory compliance without GDPR liability); individual users wanting access to institutional DeFi without identity exposure; enterprises running KYC as a service.

**Business Model:** B2B credential infrastructure.

**Revenue Model:**
- Protocol licensing: DeFi protocols pay $10,000–$100,000/year to integrate StarkPass credential verification
- Credential issuance fee: $1–$10 per credential issued (to the KYC issuer; StarkPass takes 20% as infrastructure)
- Enterprise KYC-as-a-service: $50,000–$500,000/year for banks and financial institutions running compliant DeFi access
- Consumer premium: users pay $5–$20/year for multi-credential passport (cross-protocol credential portability)

---

## 2. Private Social Graph

### The Concept

A social network where the relationship graph — who you follow, who follows you, who you interact with — is encrypted. Your social connections are not publicly queryable by anyone with a block explorer. Only you (and people with whom you share explicit access) can see your full connection graph.

### Market Landscape

**Lens Protocol** ($46M+ raised, latest $15M Feb 2026) built on Polygon stores all social interactions — follows, posts, comments, mirrors — on-chain. ~40,000–60,000 DAU as of late 2025. Profile NFTs are user-owned. However, the social graph is fully public — every follow and interaction is visible to anyone.

**Farcaster** ($180M raised, $150M Series A) reached ~80,000 DAU in peak 2024, declining to ~40,000–60,000 by late 2025. Hybrid architecture: identity on Optimism (permanent), content on off-chain hubs. More gas-efficient than Lens but still not private — follows are public.

**The structural gap**: Both Lens and Farcaster have identified the privacy problem but haven't solved it. The social graph is inherently valuable data — it reveals your professional network, political affiliations, community memberships, and behavioral patterns. On public blockchains, this is permanently exposed.

**DeSoc (Decentralized Society)** research by Vitalik et al. proposes "soul-bound tokens" and on-chain identity, but hasn't solved the privacy dimension of social graphs.

### Why STRK20 / Starknet

- Follow relationships as STRK20 notes: a "follow" is a private note linking follower to followee. Neither party's address appears in the transaction observable by others.
- Mutual connection proof: two users can prove they are mutually connected (for access control purposes) via a ZK predicate without revealing their full follow lists.
- Engagement payments (tips, subscriptions) via STRK20: all financial interactions within the social graph are private.

**Important caveat**: STRK20 solves the payment and follower-count privacy problem, but the content layer (posts, comments) requires separate encryption (off-chain or via a dedicated encrypted content protocol like Lit Protocol or XMTP). The full solution is STRK20 + content encryption layer.

### Product: ShadowGraph

An encrypted social graph layer for Starknet, positioning as a privacy infrastructure component that any Starknet social dApp can integrate.

**How it works:**

1. User publishes a public key + shielded Starknet address. Their social graph is anchored to this address.
2. Follow: sender creates a STRK20 note encoding the follower relationship. Only the followee (with their viewing key) can see they have a new follower. The follower's identity is hidden from the public.
3. Mutual follow proof: if Bob also follows Alice, both can generate a ZK proof of mutual connection — usable for group access control or trust verification — without publishing the mutual follow publicly.
4. Application layer: social dApps query the user's local decrypted graph (using their viewing key) to build their feed.

**Target Users:** Privacy-conscious social media users, journalists and activists in adversarial jurisdictions, professional networking applications where connections are competitive intelligence, DAO communities with sensitive governance discussions.

**Business Model:** Infrastructure B2B.

**Revenue Model:**
- Developer API subscription: $500–$5,000/month per application built on ShadowGraph
- Encryption infrastructure per-user fee: $0.01–$0.10/month per active user on the platform (paid by the application, not the user)
- Enterprise private community hosting: $10,000–$100,000/year for organizations running private internal social graphs

---

## 3. Private Subscriptions

### The Concept

Creator subscriptions where the payment is anonymous — the creator doesn't learn who pays them, and the subscriber's payment history is not publicly visible. This protects subscribers who might be adversely affected by disclosure (e.g., subscribing to political or investigative journalism, adult content, legal advice, or sensitive community memberships).

### Market Landscape

There is no dominant blockchain-native private subscription platform. Traditional privacy-focused tools (Substack with anonymous email aliases, Proton Mail billing) provide partial privacy but the payment rail is always traceable (credit card → subscriber identity).

**Push Protocol v2** introduced incentivized messaging: influencers charge PUSH tokens for inbox access. This is subscription-adjacent but focused on direct messaging, not content gating.

**Privacy coin subscriptions**: Some Monero and Zcash-based services accept anonymous payments, but these require users to acquire and manage privacy coins — a significant friction barrier.

**The gap**: There is no mainstream subscription platform where a credit-card user can subscribe to a creator and have that relationship remain private from both the creator and the platform. STRK20 enables this if paired with a consumer-friendly on-ramp.

### Why STRK20 / Starknet

- Subscription as recurring private note: each billing cycle creates a STRK20 note transfer from subscriber to creator's shielded address. The creator receives payment; the subscriber's identity is hidden.
- Starknet account abstraction: a "subscription session key" can be configured to automatically renew the payment each period without requiring manual signing — matching the UX of traditional subscriptions.
- Compliance: creator's viewing key allows their accountant or the platform to verify subscription revenue for tax purposes without seeing subscriber identities.

### Product: Inkognito

A private subscription platform for creators and newsletters.

**How it works:**

1. Creator sets up an Inkognito channel: content, price, billing period.
2. Subscriber deposits stablecoin (USDC) into STRK20 pool via familiar fiat-to-crypto onramp (MoonPay, Transak, etc.).
3. Subscription session key configured: each billing period, the session key automatically creates a STRK20 note transfer to the creator's channel address.
4. Creator publishes content behind an access gate: Starknet contract verifies that a valid subscription note exists for the requester before serving decryption key.
5. Creator sees: total subscriber count and revenue — but not individual subscriber identities unless they explicitly reveal themselves.

**Target Users:** Investigative journalists (subscriber privacy from political pressure), adult content creators (subscriber privacy from social consequences), legal/medical advisors (subscriber privacy for professional sensitivity), political commentators in adversarial jurisdictions.

**Business Model:** Platform fee on subscription revenue.

**Revenue Model:**
- Platform fee: 5–10% of creator subscription revenue
- Onramp revenue share: 0.5–1% of fiat-to-STRK20 conversions (via MoonPay/Transak partner arrangement)
- Premium creator tier (custom domain, analytics dashboard, email distribution): $50–$500/month

---

## 4. Private Messaging & Email

### The Concept

End-to-end encrypted messaging where messages are sent between Starknet addresses, payment channels for premium messaging (anti-spam bonds), and private group communications for DAO/community coordination.

### Market Landscape

**XMTP** ($49.9M raised, $750M protocol valuation) is the leading decentralized messaging standard. It is integrated into Coinbase's Base wallet as native messaging. Wallet-to-wallet DMs + group chats + notifications. Mainnet transition expected March 2026.

**Push Protocol** is the notification layer for Web3. Integrated with Unstoppable Domains and numerous DeFi protocols. Monetizes via premium features and creator incentives.

**Skiff** (E2EE email + Web3) offers anonymous email aliases and ETH domain support. Privacy-first but limited institutional adoption.

**zkEmail** is an emerging protocol enabling ZK proofs for email authentication without exposing email content or address. Used for on-chain account recovery via email credentials.

**The gap**: Existing platforms (XMTP, Push) don't handle payment-gated messaging natively. There's no "pay to reach my inbox" system with hidden payment amounts. Spam resistance in decentralized messaging requires economic barriers, but those barriers need to be paid privately.

### Why STRK20 / Starknet

- Payment-gated inbox: a user can require a minimum STRK20 note payment to send them a message. The payment amount is hidden from public view (preventing competitive intelligence: "X paid $500 to reach this founder = this deal is big").
- Group channel funding: DAO group chats can be funded via anonymous STRK20 pool contributions — group members pay for relayer infrastructure without individual payment records.
- Anti-spam bonds: messaging relayers can require STRK20 bond deposits (refunded if message is not marked spam). This creates economic spam resistance without the relayer knowing sender identity.

### Product: NullPost

A private messaging layer for Starknet with payment-gated inboxes and anti-spam STRK20 bonds.

**How it works:**

1. User sets up a NullPost address (linked to their Starknet address via stealth address scheme).
2. User optionally sets inbox price: "minimum 0.10 USDC STRK20 note to message me." This is visible; the amount paid by each sender is not.
3. Sender composes message, encrypted to recipient's public key (ECDH on STARK curve), attaches STRK20 note payment.
4. Message delivered. Recipient decrypts with private key.
5. If recipient marks message as spam, sender's STRK20 bond is slashed. Legitimate senders get bonds refunded after 7 days.

**Target Users:** Crypto founders (signal-vs-noise inbox management), journalists (anonymous source communication), DAO contributors (coordination without exposing communication graph), high-profile individuals in adversarial jurisdictions.

**Business Model:** Infrastructure protocol with relayer staking.

**Revenue Model:**
- Relayer fee: 10% of all message bond payments go to relayer operators
- Premium inbox features: vanity addresses, bulk messaging APIs, analytics dashboard: $50–$500/month
- Enterprise messaging (corporate internal encrypted communication, compliance-grade): $10,000–$100,000/year

---

## 5. Private Matchmaking

### The Concept

A matching application (dating, professional networking, co-founder discovery) where preferences are submitted as ZK proofs, matches are computed on encrypted inputs, and the match result is revealed only if both parties confirm mutual interest. No one — including the platform — learns what a user's preferences are, only whether a match has been confirmed.

### Market Landscape

**Decentralized dating** is nascent. RUMORS (blockchain-verified profiles + encrypted data) targets crypto enthusiasts. Viola.AI and Ponder are early-stage.

The most significant market signal: **Worldcoin/World signed a partnership with Match Group** (Tinder, Hinge, OkCupid owner) to deploy World ID for human verification — specifically to address AI-generated fake profiles, which Tinder estimates account for 20–30% of all accounts.

**The Worldcoin-Match Group pilot** (launched in Japan) proves that major platforms are willing to adopt ZK identity infrastructure when it solves a real product problem (bot elimination). Privacy-preserving matchmaking is the next logical step.

### Why STRK20 / Starknet

- Preference as ZK predicate: a user's preferences (age range, location, interests) are encoded as a ZK circuit. The matchmaking engine tests for compatibility without learning individual preferences.
- Mutual match confirmation: only when two users both confirm interest does the match surface — preventing asymmetric data leakage (platform learning "user X finds user Y attractive" before a reciprocal signal).
- STRK20 premium features: premium matchmaking tiers, "super like" equivalents, and profile boosts can be purchased via STRK20 notes — anonymous from the perspective of the public.
- Sybil resistance: Starknet ID + Worldcoin proof-of-humanity gates account creation to real individuals.

### Product: ZeroDate

A privacy-preserving matching platform where preferences are never disclosed to the platform or the public.

**How it works:**

1. User registers with Starknet ID + optional Worldcoin proof-of-humanity.
2. User submits preference profile as ZK circuit inputs. Preferences are committed locally; only the commitment hash goes on-chain.
3. Matching: Cairo contract runs compatibility check as a ZK predicate — outputs "compatible / not compatible" without revealing either party's preferences.
4. If compatible: both parties receive an anonymized match signal. Neither learns the other's identity until they both confirm interest via signed transaction.
5. On double-confirm: match surfaces. Both users can now message via NullPost or another E2EE layer.

**Target Users:** Privacy-conscious dating app users, professional co-founder and business partner matching, LGBTQ+ users in jurisdictions with social risk, crypto community social discovery.

**Business Model:** Freemium with premium features.

**Revenue Model:**
- Premium subscription: $15–$30/month in STRK20 for unlimited matches, profile boost, preference broadening
- Super match: $5–$20 per premium match signal (STRK20 note — anonymous)
- B2B: License ZK matchmaking engine to other platforms (professional networking, team formation): $50,000–$500,000/year

---

## 6. Private Contact Discovery

### The Concept

Finding people you know in a new network without disclosing your contact list to the network's servers. Signal's Private Set Intersection (PSI) protocol is the gold standard — your contacts never leave your device; the server only sees hashed identifiers and cannot reconstruct your contact list.

### Market Landscape

**Signal** implemented PSI-based contact discovery in 2017 and has 100M+ users. Their protocol uses multi-party computation to find mutual contacts without either party learning what the other's full contact list is. Academic work (Kales et al., USENIX 2019) has optimized PSI to handle 1,000 contacts against a billion-entry database in ~2.92 seconds.

**WhatsApp's approach** is significantly weaker: it sends full contact hashes to servers. Researchers in 2025 disclosed a vulnerability: WhatsApp's low-entropy phone number hashes (10 digits) allow enumeration attacks that could crawl 3.5B users' contact graphs.

**The gap**: No Web3 application has implemented serious PSI-based contact discovery. Most "find your friends" features in Web3 social apps require submitting contact information to servers.

### Why STRK20 / Starknet

- Wallet-address contact discovery uses higher-entropy identifiers than phone numbers, making hash enumeration attacks harder.
- STRK20 payment can gate contact discovery (prevent mass enumeration by making each discovery query cost a small STRK20 note fee — refunded if the contact is found, consumed if not).
- ZK mutual connection proof: once mutual contact is established, a ZK proof of "I know this person" can be used for reputation-weighted introductions without revealing the full contact graph.

### Product: ZeroContacts

A PSI-based contact discovery protocol for Starknet applications.

**How it works:**

1. User registers their Starknet address hash in ZeroContacts (one-time, local computation).
2. When using a new Starknet application, user wants to find friends. They submit a ZK commitment of their contact list (wallet addresses of people they know).
3. ZeroContacts server runs PSI computation: returns only the intersection (contacts who are also registered) — without learning which contacts were queried.
4. Each PSI query costs a small STRK20 micro-payment (anti-enumeration fee, refunded on contact match).
5. The full contact list never leaves the user's device.

**Target Users:** Web3 social applications (Lens, Farcaster equivalents on Starknet) wanting Friend Discovery without privacy compromise; any on-chain application that needs "find your contacts" functionality.

**Business Model:** B2B protocol infrastructure.

**Revenue Model:**
- API licensing: applications pay per PSI query batch ($0.001–$0.01 per user onboarded)
- Enterprise contact discovery with compliance (KYC-linked contact mapping for regulated platforms): $50,000–$200,000/year
- Protocol fee on STRK20 anti-enumeration payments: 10% of all micro-payment fees collected

---

## Summary Table

| Use Case | Closest Competitor | STRK20 Advantage | Technical Complexity | Viability |
|---|---|---|---|---|
| Selective Disclosure | Polygon ID / Holonym | Native STARK proving, Starknet composability | Medium | **High** |
| Private Social Graph | Lens (transparent) | Hidden follow graph, payment privacy | High | **Medium** |
| Private Subscriptions | None (gap in market) | Recurring private payment, session keys | Low | **High** |
| Private Messaging | XMTP ($750M valuation) | Payment-gated inbox, STRK20 anti-spam | Medium | **Medium** |
| Private Matchmaking | Traditional dating apps | ZK preference matching, sybil resistance | High | **Medium** |
| Private Contact Discovery | Signal (100M users, centralized) | On-chain PSI, wallet-address entropy | High | **Medium** |

---

## See Also

- [[chains/strk20|STRK20 Protocol]] — Technical architecture
- [[chains/starknet-use-cases|Core Use Cases]] — Payroll, donations, OTC, AI agents
- [[chains/starknet-usecases-defi|DeFi Use Cases]] — Dark pools, perpetuals
- [[chains/starknet-usecases-ai|AI & Machine Learning]] — Encrypted inference, autonomous agents
