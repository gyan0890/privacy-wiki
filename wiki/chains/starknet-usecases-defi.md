# STRK20 Use Cases: DeFi & Financial Markets

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[chains/strk20]], [[chains/starknet-use-cases]], [[concepts/privacy-vs-compliance]]

---

## Overview

Financial markets have the most immediate and measurable demand for on-chain privacy. Public blockchains expose trade sizes, positions, counterparties, and strategies to anyone watching — the exact opposite of how institutional and serious retail finance operates. This page covers eight DeFi use cases where STRK20's compliance-native privacy architecture creates a specific structural advantage.

Each entry covers: the product concept, what already exists in the market, why existing solutions fall short, the Starknet/STRK20 architecture, target users, business model, and revenue model.

---

## 1. Dark Pools

### The Concept

A dark pool is a private liquidity venue where large orders are matched without pre-trade transparency. The identity of the buyer and seller, and the size of the trade, are not revealed to other market participants until after execution (if at all). Traditional finance has had dark pools since the 1980s; crypto has none that work at scale.

### Market Landscape

**Renegade Finance** (live on Arbitrum and Base) is the most advanced crypto dark pool. It uses collaborative SNARKs inside MPC: two traders generate a joint ZK proof that their trade clears at the Binance mid-price without either party learning the other's order. Protocol fee: 2 bps + relayer fees. Raised $3.4M from Dragonfly and Naval Ravikant. Adoption is early — liquidity is thin because dark pools require large order flow to be useful.

**Panther Protocol** built Multi-Asset Shielded Pools (MASP) with dark pool functionality for institutions. Mainnet Beta launched March 2025. Compliance view keys make it palatable to institutional traders.

**Penumbra** (Cosmos L1) has a native dark pool via ZSwap batch auctions — only net flows are revealed, not individual orders. This is built into the chain's core DEX.

**The gap**: None of these run on a high-throughput EVM-compatible L2 with native compliance infrastructure. Renegade requires MPC coordination (latency). Penumbra is Cosmos-only (siloed). Panther is EVM but not optimized for proving speed.

### Why STRK20 / Starknet

- Stwo prover handles the proof generation side faster than any MPC-based approach.
- STRK20 shielded balances: both counterparties hold assets in the privacy pool; matching and settlement are atomic, with no address exposure.
- Ekubo Protocol (Starknet's primary DEX) is already integrating STRK20, giving dark pool functionality a liquidity home.
- Native account abstraction: paymaster hides the broadcaster identity so even the transaction origin is concealed.

### Product: StarkDark

A dark pool aggregator on Starknet that routes large orders through STRK20 shielded matching.

**How it works:**

1. Trader deposits assets into STRK20 privacy pool via `Deposit` action.
2. Trader submits an intent (desired trade, acceptable price range) to the off-chain matching engine, encrypted to the matching engine's public key.
3. Matching engine finds counterparty intents and generates a multi-party STARK proof that both sides agree on a price within both parties' acceptable ranges.
4. Settlement executes atomically: `UseNote` (both sides) → swap via Ekubo → `CreateNote` (both sides' proceeds).
5. Paymaster broadcasts. No on-chain footprint beyond a privacy pool contract call.

**Target Users:** Crypto hedge funds, prop trading desks, large DAO treasuries executing $500K+ trades, institutional market makers.

**Business Model:** B2B. Integration partnerships with institutional prime brokers and OTC desks.

**Revenue Model:**
- 2 bps protocol fee on matched volume (taken from the privacy pool at settlement)
- Premium relayer tier (guaranteed sub-1-second matching latency for volume desks): $5,000–$50,000/month subscription
- White-label API for OTC desks wanting private settlement infrastructure: $100,000–$500,000/year license

**Market Size:** Crypto OTC volume is estimated at $30–$50B/month; even 0.1% capture at 2 bps = $600K–$1M/month in fees.

---

## 2. Sealed-Bid Auctions

### The Concept

In a sealed-bid auction, all participants submit bids without knowing others' bids. Bids are revealed simultaneously at a predetermined time. This eliminates last-second sniping, collusion, and bid shadowing that plague transparent on-chain auctions.

### Market Landscape

**MACI** (Minimal Anti-Collusion Infrastructure) is the most mature ZK voting/auction infrastructure. Used by clr.fund for quadratic funding rounds, and adopted in Gitcoin Grants. It prevents collusion via ECDH encryption of votes/bids plus off-chain tallying with on-chain ZK verification. The coordinator is still somewhat trusted.

**Gnosis Auction** runs batch auctions for transparent price discovery. Used for token sales and DAO buybacks. It's effective but not private — all bids are visible.

**Academic work** (BOREALIS, Strain, zk-Auction) has demonstrated sealed-bid schemes with ZK proofs, including cross-chain auction settlement. None have deployed commercially at scale.

**The gap**: No production sealed-bid auction platform exists for high-value assets (NFTs, token launches, debt instruments) where bid confidentiality is the primary product requirement.

### Why STRK20 / Starknet

- Cairo circuits encode the auction reveal logic natively.
- STRK20 bid deposits: each bidder locks their bid amount into a shielded note. The note is only spendable if their bid wins. Losing bids are refunded via `CreateNote` back to their original owner.
- Stwo prover: bid validity proofs generated client-side, submitted on-chain for verification.
- The sequential action ordering in STRK20 (SetViewingKey → Deposit → UseNote → CreateNote) maps directly to auction lifecycle: register → deposit bid → reveal → refund/award.

### Product: SealedStark

A sealed-bid auction platform for high-value on-chain assets.

**How it works:**

1. Auction creator specifies asset, minimum bid, reserve price, and auction duration. Asset locked in Cairo contract.
2. Bidders deposit bid amounts into STRK20 pool + submit encrypted commitment (hash of bid amount + blinding factor) on-chain.
3. Reveal phase: each bidder publishes their blinding factor. Stwo proof confirms that revealed amount matches commitment and that their shielded note covers the amount.
4. Highest valid bid wins. Winning bidder's note is spent to the auctioneer. All other bidders' notes are refunded.
5. Full privacy maintained for losing bids post-auction (amounts never publicly disclosed).

**Target Users:** NFT marketplaces (high-value 1/1 NFTs), token launch platforms (IDOs via sealed bid), DAO treasury managers auctioning protocol assets, institutional bond issuance on-chain.

**Business Model:** Platform-as-a-service with per-auction fees.

**Revenue Model:**
- 1–2% commission on winning bid amount
- Creator listing fee (flat): $500–$5,000 per auction
- Premium features: automated escrow, dispute resolution oracle, legal compliance wrapper (+$2,000–$10,000 per auction)

---

## 3. Private Perpetuals

### The Concept

Perpetual futures contracts with hidden position sizes, liquidation levels, and entry prices. On transparent chains, large positions are visible to liquidation bots and competing traders who can coordinate to push prices toward known liquidation thresholds.

### Market Landscape

**Aster Protocol** launched on mainnet March 2026 with ZK privacy features. It has already crossed $2B TVL and $10B daily volume — validating massive demand for privacy-enhanced perp trading. Simple Mode offers 1–1000x leverage; Pro Mode has hidden order books.

**edgeX** (by Amber Group) runs on StarkEx (a ZK rollup) and has processed $800B in cumulative volume with 190K+ users. It doesn't have position privacy but demonstrates that ZK infrastructure is production-ready for perp DEXs.

**Hyperliquid** (the dominant perp DEX with $40B+ daily volume) has no privacy. Position data for large traders is fully visible and widely used by rivals.

**The gap**: Aster proves demand, but its privacy model is circuit-level — not compliance-ready (no viewing keys, no selective disclosure). No existing perp DEX combines institutional-grade compliance with genuine position privacy.

### Why STRK20 / Starknet

- Position privacy via STRK20 notes: margin balances and position sizes are held as shielded notes. A trader's collateral ratio and position direction are cryptographically hidden.
- Liquidation challenge: liquidators need to know when a position is undercollateralized. Solution: the protocol generates a ZK proof that a position's collateral ratio is below threshold WITHOUT revealing the actual collateral amount. Liquidators can trigger liquidation without learning position size.
- Starknet's throughput (among the highest across L2s) and sub-second pre-confirmations handle the real-time demands of leveraged trading.

### Product: GhostPerp

A privacy-preserving perpetuals DEX where position sizes, leverage, and entry prices are cryptographically hidden.

**How it works:**

1. Trader deposits collateral into STRK20 pool.
2. Position is opened via Cairo contract: collateral note + position parameters (direction, leverage) are committed. Only the trader (and auditing entity via viewing key) can see the full position.
3. The funding rate and mark price oracle operate on publicly visible aggregate data (not individual positions).
4. Liquidation: the protocol continuously checks a ZK predicate — "is this position's margin ratio below threshold?" — without revealing the actual ratio. If true, liquidators are invited to close the position for a fee.
5. Profit/loss settlement: `UseNote` on position note + `CreateNote` for P&L proceeds.

**Target Users:** Crypto hedge funds (hide strategy from competitors), high-net-worth traders (prevent position targeting), institutional market makers (protect inventory from front-running).

**Business Model:** DEX protocol with fee tiers.

**Revenue Model:**
- Trading fee: 5–10 bps per trade (lower than Hyperliquid's 2.5 bps maker / 5 bps taker because privacy is the premium)
- Funding rate: protocol captures a small spread on funding payments
- Insurance fund: 10–20% of liquidation proceeds go to protocol treasury
- Premium relayer tier (priority matching for large traders): $10,000–$100,000/month

**Market Size:** Perp DEX total volume is $2.41T/quarter (2026). Capturing 0.1% at 7 bps average fee = $168M/quarter.

---

## 4. Private Lending

### The Concept

Lending markets where collateral amounts, loan sizes, and interest rates are hidden from the public. On transparent chains, large borrowers' collateral positions are visible — enabling coordinated oracle attacks and precision liquidation campaigns.

### Market Landscape

**Panther Protocol** has built DeFi Adaptors for private lending: users deposit into MASP, interact with lending protocols with encrypted balances. In beta, not production-scale.

**Zama** ($1B+ valuation) is building FHEVM — lending logic that executes on encrypted inputs. They published a "Confidential Lending" spec in February 2025. No live product yet.

**Morpho Protocol** ($8B+ TVL) offers permissionless isolated lending markets but has zero privacy — all collateral and loan amounts are fully public.

**The gap**: There is no production-deployed private lending protocol with compliance-grade audit trails. Every major lending protocol (Aave, Compound, Morpho) is fully transparent.

### Why STRK20 / Starknet

- Shielded collateral: collateral is deposited as STRK20 notes. The collateral value is hidden; the health ratio (collateral / debt) is proven via ZK predicate without revealing raw amounts.
- Encrypted interest rates: interest accrual is computed over encrypted balances using Cairo's arithmetic circuits.
- Liquidation: same ZK-predicate approach as GhostPerp — the protocol proves health ratio is below threshold without exposing actual balances.
- Viewing keys: lenders and auditors can verify solvency of the pool without seeing individual position details.

### Product: PrivaultLend

A private lending protocol where collateral values and loan sizes are hidden but solvency is cryptographically proven.

**How it works:**

1. Borrower deposits collateral as STRK20 shielded notes.
2. Borrower requests loan: Cairo contract validates (via Stwo proof) that collateral value ≥ required ratio, without publishing collateral amount.
3. Loan proceeds issued as new STRK20 notes.
4. Health ratio monitored via ZK predicate checks at each block.
5. On liquidation: liquidator gets fee for triggering; collateral note is split (borrower gets excess, protocol gets fee).

**Target Users:** Large borrowers who don't want to expose their collateral positions to oracle manipulation; institutional DeFi desks; DAO treasuries financing operations without balance sheet disclosure.

**Business Model:** Protocol-native with governance token.

**Revenue Model:**
- Interest rate spread: protocol captures 10–20% of interest paid by borrowers
- Liquidation fee: 5–15% of liquidated collateral goes to protocol treasury
- Origination fee: 0.1–0.5% of loan value on opening
- Institutional compliance tier (enhanced viewing key dashboard for auditors, tax reports): $5,000–$50,000/year per institution

---

## 5. Private P2P Trading

### The Concept

Peer-to-peer token trading where neither counterparty's identity nor the trade amount is visible to the public or to the other party before settlement.

### Market Landscape

**Bisq** is the dominant decentralized P2P Bitcoin exchange. No KYC, Tor-integrated, 150+ coins. Revenue model: donations. Volume is a fraction of CEX volume due to UX friction and liquidity limitations.

**Haveno** (Monero-focused Bisq fork) reached ~$2M volume in February 2025. Growing but niche. Both platforms suffer from the same limitation: liquidity is fragmented, settlement is slow, and the decentralized dispute resolution mechanism is clunky.

**The gap**: Neither Bisq nor Haveno supports ERC-20 tokens or DeFi assets. Neither has compliance-grade audit trails for institutional use. Both rely on Tor or Monero for privacy, not ZK proofs — meaning they can't offer selective disclosure to regulators.

### Why STRK20 / Starknet

- Atomic swap: two parties each lock assets in STRK20 shielded notes; a single Cairo transaction swaps the notes atomically. Neither party's identity or trade amount is exposed.
- Compliance: both parties can escrow viewing keys to their respective compliance entities without those entities being able to see each other's data.
- No oracle dependency: unlike AMM-based swaps, P2P trades are directly negotiated; STRK20 handles settlement without external price feeds.

### Product: Shade P2P

A private P2P trading marketplace for ERC-20 assets and stablecoins.

**How it works:**

1. Maker creates a trade offer: lock asset A as STRK20 note + post encrypted offer (amount of A, desired amount of B, expiry) via Starknet contract.
2. Taker finds offer via off-chain discovery layer (encrypted order book served over a decentralized network), verifies the Stwo proof of offer validity client-side.
3. Taker locks asset B as STRK20 note + submits matching proof.
4. Settlement: Cairo contract verifies both proofs + executes atomic swap of notes.
5. Neither party's address or amounts appear on-chain.

**Target Users:** Crypto-native traders seeking off-slippage OTC execution, HNWI seeking tax-efficient discreet trades, institutions requiring private settlement without off-chain counterparty risk.

**Business Model:** Protocol-level fees.

**Revenue Model:**
- Taker fee: 10 bps on each completed trade
- Maker rebate: −5 bps (incentivizes liquidity provision)
- Premium features: verified counterparty badges (KYC-proven by third party), priority discovery in order book (+$500/month)

---

## 6. Opportunity Markets

### The Concept

A marketplace where deal flow — investment opportunities, protocol partnerships, acquisition targets, token liquidity events — can be discovered and evaluated privately before commitment. Think AngelList for crypto, but where the identity of both the opportunity and the interested party are hidden until mutual interest is confirmed.

### Market Landscape

**Acquire.fi** is the only dedicated Web3 M&A marketplace, connecting buyers with revenue-generating crypto businesses. No privacy layer. Deloitte and JP Morgan have published research on tokenized deal flow and secondary market liquidity for tokenized fund shares, but no production platform exists.

**Status**: The market is almost entirely unbuilt. Most crypto deal flow is managed through private Telegram groups and backchannel introductions.

**The gap**: Significant information leakage occurs in deal sourcing — if a well-known fund is looking at protocol X, that signal alone moves markets. There is no "private deal room" equivalent on-chain.

### Why STRK20 / Starknet

- Blind interest signaling: a fund posts an encrypted expression of interest (EOI) for a category of asset without revealing their identity or specific target. Only the deal originator can decrypt the EOI, and only if they post a matching interest signal.
- Private due diligence escrow: documents are locked in an encrypted data vault; STRK20 payment gates document access with an on-chain access log (viewable only by the auditing entity).
- STRK20 escrow: deal deposits are held as shielded notes and released only when both parties confirm deal closure.

### Product: DarkFlow

A private deal flow marketplace for crypto investment opportunities.

**How it works:**

1. Deal originator lists an opportunity: encrypted term sheet + STRK20 escrow deposit.
2. Interested parties submit blind EOIs: encrypted indication of interest + STRK20 deposit (refundable if no match).
3. If originator and interested party both confirm interest, a "match" is established. Both parties' identities are revealed only to each other (not to the public).
4. Due diligence materials accessed via STRK20-gated encrypted data vault.
5. On deal close: STRK20 escrow releases to originator; finder's fee to marketplace.

**Target Users:** Crypto VCs, protocol treasuries seeking strategic acquisitions, token projects seeking private investors pre-announcement.

**Revenue Model:**
- Success fee: 1–3% of deal value on close
- Listing fee: $1,000–$10,000 per deal posted
- Due diligence data vault hosting: $500–$5,000/month per deal room

---

## 7. Private Prediction Markets

### The Concept

A prediction market where individual positions are hidden until market resolution, preventing position signaling and enabling genuine price discovery without social influence.

### Market Landscape

**Polymarket** has $2.48B volume (April 2026) and correctly predicted 31/34 Senate races (91% accuracy). **Kalshi** ($3.54B volume, CFTC-approved) is its primary rival. Both are fully transparent — all positions visible. Neither has privacy.

**The core tension**: Privacy in prediction markets is philosophically complex. The information-aggregation function of a prediction market works precisely because traders with information can signal that information via their positions. Hidden positions reduce information leakage, which is what traders want — but it also reduces the market's information aggregation efficiency.

**Resolution**: A hybrid model works. Positions are private during the open phase (preventing social signaling and bandwagon effects) but revealed in aggregate at resolution. Individual identities remain private; aggregate volume by outcome is disclosed when the market closes.

### Why STRK20 / Starknet

- Position privacy: each prediction position is a STRK20 note. The position direction and size are hidden from public view.
- Aggregate proof: at resolution, a ZK proof demonstrates the total stake on each side without revealing individual positions. Winners claim via `UseNote` on their position note.
- Compliance: regulators and auditors (e.g., CFTC equivalents) can verify total market volume via viewing keys without seeing individual traders.

### Product: SilentOdds

A prediction market where positions are private during the market's open phase and resolved via ZK aggregate proofs.

**How it works:**

1. Market creator specifies event, resolution condition, and oracle (e.g., Pragma on Starknet).
2. Traders take positions as STRK20 notes. Position direction (YES/NO) and amount hidden.
3. During open phase: only total locked value (sum of all positions) is visible. No breakdown by outcome.
4. At resolution: oracle posts outcome. Cairo contract generates ZK proof of aggregate stake by outcome (required for payout calculation) without revealing individual positions.
5. Winners submit `UseNote` + Stwo proof of winning position → `CreateNote` with payout.

**Target Users:** Traders in politically sensitive markets (elections, regulatory outcomes), institutional traders who don't want position signaling, retail traders seeking authentic price discovery uncontaminated by whale signaling.

**Revenue Model:**
- Platform fee: 2% of winning payout
- Market creation fee: $100–$1,000 per market (scales with max stake)
- Premium oracle tier (faster resolution, more event categories): $500/month subscription

---

## 8. Private Opinion Markets

### The Concept

A market where participants can buy and sell sentiment positions — "I believe X is true/will happen" — anonymously, and where the aggregate reveals collective belief without identifying who holds which view. Distinct from prediction markets (which require objective resolution criteria), opinion markets trade on subjective assessments.

### Market Landscape

There is no dominant private opinion market. **Zeitgeist** (Polkadot) has a futarchy model for governance decisions (markets on proposal outcomes). **Crypto sentiment aggregators** (CMC Sentiment, Fear & Greed Index) provide read-only signals, not tradeable markets. The space is nascent and the settlement problem (how do you resolve a subjective opinion?) is unsolved.

**A viable path**: Opinion markets that DON'T require resolution — where the price itself is the signal. Participants trade "I believe X" tokens that expire worthless, and the price trajectory reflects aggregate conviction. Revenue comes from the trading activity, not settlement.

### Why STRK20 / Starknet

- Anonymous position-taking: opinion positions as STRK20 notes prevent social pressure and reputational risk from publicly known views.
- Cairo contracts encode market mechanics (AMM-style opinion trading, Schelling point aggregation).
- Suitable for use cases like: anonymous governance sentiment before on-chain votes, anonymous DAO temperature checks, private analyst coverage markets.

### Product: GhostPulse

An anonymous opinion trading platform for crypto governance and market sentiment.

**How it works:**

1. Market creator posts a topic: "Should Protocol X change its fee structure?"
2. STRK20-denominated YES/NO tokens minted in a constant product AMM within the privacy pool.
3. Traders swap STRK20 notes for YES/NO tokens — all amounts private.
4. Price reflects aggregate sentiment; no individual positions disclosed.
5. Optional resolution: if an objective outcome occurs, winners redeem; otherwise tokens expire at 50/50 unless protocol governance accepts the market result as a signal.

**Target Users:** DAO contributors who want anonymous governance temperature checks, crypto analysts who want to stake claims without reputational exposure, media/research platforms wanting anonymous analyst consensus.

**Revenue Model:**
- AMM trading fee: 30 bps on each swap
- Market creation fee: $50–$500 per market
- Data licensing: anonymized aggregate sentiment data sold to research platforms and DAOs: $1,000–$10,000/month per feed

---

## Summary Table

| Use Case | Closest Competitor | STRK20 Advantage | Viability | Key Revenue |
|---|---|---|---|---|
| Dark Pools | Renegade Finance | Speed (Stwo), compliance, EVM composability | **High** | 2 bps protocol fee |
| Sealed-Bid Auctions | MACI (niche) | Native settlement, refund logic, compliance | **High** | 1–2% commission |
| Private Perpetuals | Aster Protocol | Compliance layer, Starknet throughput | **High** | 5–10 bps trading fee |
| Private Lending | Panther (beta) | Production-ready compliance, Stwo efficiency | **High** | Interest spread, liquidation fee |
| Private P2P Trading | Bisq (BTC only) | ERC-20 support, compliance, atomic settlement | **Medium** | 10 bps taker fee |
| Opportunity Markets | Acquire.fi (no privacy) | Blind matching, STRK20 escrow | **Medium** | 1–3% success fee |
| Private Prediction Markets | Polymarket (transparent) | Position privacy, ZK aggregate resolution | **Medium** | 2% platform fee |
| Private Opinion Markets | None (nascent) | Anonymous AMM, no resolution risk | **Low-Medium** | 30 bps trading fee |

---

## See Also

- [[chains/strk20|STRK20 Protocol]] — Technical architecture
- [[chains/starknet-use-cases|Core Use Cases]] — Payroll, donations, OTC, AI agents
- [[chains/starknet-usecases-gaming|Gaming & Governance]] — Poker, voting, Dark Forest
- [[chains/starknet-usecases-ai|AI & Machine Learning]] — Encrypted inference, autonomous agents
