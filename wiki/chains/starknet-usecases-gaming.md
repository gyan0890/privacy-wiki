# STRK20 Use Cases: Gaming, Entertainment & Governance

**Category:** [[_index#privacy-first-chains|Privacy-First Chains]]
**Related:** [[chains/strk20]], [[chains/starknet-use-cases]], [[chains/starknet]]

---

## Overview

Starknet already has a mature on-chain gaming ecosystem (Dojo Engine, Loot Survivor, 51+ gaming projects by 2025). STRK20 adds the privacy layer that has been missing: hidden game state, anonymous wagering, and verifiable fairness without transparency. This page covers seven use cases spanning games, provably fair lotteries, and governance — all native to Starknet's architecture.

---

## 1. Encrypted On-Chain Voting

### The Concept

On-chain voting where individual votes are hidden during the voting period (preventing bandwagon effects and strategic voting) but cryptographically tallied at close. The result is verifiable by anyone; the individual votes remain private.

### Market Landscape

**MACI** (Minimal Anti-Collusion Infrastructure) is the leading ZK voting primitive. It encrypts votes via ECDH and tallies off-chain with on-chain ZK verification. Used by clr.fund (quadratic funding) and adopted in Gitcoin Grants rounds. Its limitation: a trusted coordinator must tally votes. If the coordinator is compromised, privacy fails.

**Vocdoni** (acquired by Aragon for ~$1M in 2021) is the most deployed governance platform. It has run hundreds of elections for city councils, DAOs, political parties, and sports clubs. Its DAVINCI protocol (2025) enables unstoppable elections with sequencer staking. Revenue model: SaaS for organizations + token staking.

**Snapshot** integrated **Shutter Network** for "Shielded Voting" in 2024 — votes are encrypted via threshold cryptography and revealed simultaneously at proposal close. This eliminates the "ape the whale" problem where late voters copy large token holder positions.

**The gap**: Snapshot's shielded voting relies on threshold decryption (off-chain key holders). It's not fully trustless. MACI's trusted coordinator is a similar limitation. Neither is natively Cairo/STARK-based.

### Why STRK20 / Starknet

- Votes are STRK20 notes: each vote is a shielded note representing a voting token. The direction (YES/NO/abstain) and weight are encrypted.
- Stwo prover: vote validity proofs generated client-side. Each voter submits a proof that their vote weight ≤ their token balance without revealing balance.
- Tally: at proposal close, Cairo contract generates a ZK aggregate proof of vote counts. No trusted tallier required.
- Starknet's native account abstraction enables gasless voting (paymaster covers fees).

### Product: CloakVote

A trustless private governance platform for Starknet DAOs.

**How it works:**

1. DAO creates proposal: voting token, duration, threshold. Proposal contract minted.
2. Voters deposit governance tokens as STRK20 notes during a "commitment phase."
3. Voters submit encrypted votes + Stwo proof of eligibility (token balance ≥ minimum).
4. At close: Cairo contract generates ZK tally proof from all committed notes. Tally published; individual votes remain encrypted.
5. Proposal status (passed/rejected) stored on-chain with verifiable proof.

**Target Users:** Starknet DAOs, any EVM-based DAO wanting privacy (via Starknet L2 bridge), political organizations running on-chain referenda, corporate shareholder votes.

**Business Model:** SaaS + token staking.

**Revenue Model:**
- DAO subscription: $500–$5,000/month based on governance token market cap
- Per-proposal fee: $50–$500 for non-subscriber organizations
- Sequencer staking rewards: infrastructure providers stake tokens to earn proposal processing fees
- Enterprise governance (corporations, political parties): $20,000–$200,000/year with legal compliance wrapper

---

## 2. Confidential Token Standard (C-STRK)

### The Concept

A privacy extension to any Starknet token that hides transfer amounts and balances by default, analogous to Solana's Confidential Transfer extension (C-SPL) but with Starknet's STARK-native proving and STRK20's compliance layer.

### Market Landscape

**Solana Confidential Transfer (Token-2022)** is the direct parallel. It uses ElGamal encryption + homomorphic ZK proofs to hide balances and amounts. Currently disabled on mainnet pending security audit (as of early 2026). Arcium is building **C-SPL** on top — adding MPC encrypted shared state so multiple parties can perform operations on encrypted balances.

**Circle Confidential ERC-20** (Ethereum whitepaper) proposes FHE-based confidential wrapped tokens. No live deployment.

**zERC20 (EIP-7503)** is live on Ethereum, BNB, Base, and Arbitrum. It implements a "Zero-Knowledge Wormhole" for hidden sender-recipient relationships. However it's not a standard — it's a specific wrapper protocol.

**STRK20 is Starknet's equivalent** — but it's more mature than any EVM equivalent because it's built natively into the chain's token infrastructure with Cairo proving.

### Why STRK20 / Starknet

STRK20 is already the C-STRK standard. The value is in the adoption and composability. Any ERC-20-equivalent token on Starknet can adopt STRK20 privacy. This page focuses on the specific product surface: a developer toolkit to make any Starknet token confidential with a single line of configuration.

### Product: ConfidentialKit

A developer SDK and Cairo library for making any Starknet ERC-20 confidential.

**How it works:**

1. Token developer integrates the ConfidentialKit Cairo library into their token contract.
2. Token gains: hidden transfer amounts, shielded balances, viewing keys for compliance.
3. Users interact with the token normally — the privacy layer is transparent to the UX.
4. Optional: selective disclosure mode where users can prove their balance is within a range (e.g., "I have ≥ 1000 tokens") for governance or airdrop eligibility without revealing exact balance.

**Target Users:** Stablecoin issuers (USDC/USDT equivalents on Starknet), DAO token issuers, DeFi protocol native tokens.

**Business Model:** Developer tooling + certification.

**Revenue Model:**
- SDK license for private deployments: $10,000–$100,000/year
- Compliance certification (audited privacy implementation): $50,000–$200,000 per token
- Viewing key management SaaS: $1,000–$10,000/month per token protocol

---

## 3. Private Online Poker

### The Concept

Decentralized poker where the deck is cryptographically shuffled and dealt using the Mental Poker protocol — no trusted dealer, no server holds card state, and the hand is provably fair. Players hold STRK20 notes as their stack; pot assignments are handled by Cairo contracts.

### Market Landscape

**Virtue Poker** is the only licensed blockchain poker platform (Malta Gaming Authority). Founded 2015, incubated by ConsenSys, raised $5M + $20M ICO in May 2021. Advisors include Phil Ivey, Joe Lubin, and Dan Coleman (world champion poker player). Deployed on Ethereum and BSC.

Virtue Poker uses the **Mental Poker protocol**: each player performs a round of encryption/shuffling without trusting any central party. A Byzantine Fault Tolerant consensus validates the final hand. The result: provably fair poker with no house dealer.

**zkShuffle** (Manta Network) is an open-source Solidity implementation of Mental Poker. It provides JavaScript SDK + Solidity contracts. Used by zkHoldem (Texas Hold'em on-chain).

**The challenge**: Interactive shuffle protocols require all players to be online simultaneously. Virtue Poker struggled with user acquisition and latency. The high barrier (crypto wallet + proof generation) limits casual player adoption.

**The opportunity**: Serious poker players — who generate the vast majority of poker platform revenue via high-stakes games — are exactly the audience for whom privacy (hiding hand history, bankroll, win rate from table sharks) is a primary concern. Virtue Poker was pitched at the wrong audience (casual crypto users). The right audience is serious grinders.

### Why STRK20 / Starknet

- Stwo prover: Mental Poker shuffle validation proofs generated on the client device in milliseconds. This solves the latency problem that plagued earlier ZK poker implementations.
- STRK20 pot management: each player's chip stack is a STRK20 note. Pot contributions are `UseNote` actions; winners receive `CreateNote` payouts. All chip accounting is private — other players can't see exact stack sizes except as visible bet sizing on the table.
- Starknet's account abstraction: session keys allow the poker client to sign moves without a wallet popup for each action (critical for real-time gameplay).
- Turn-based implementation: Starknet's ~13 second finality is acceptable for turn-based poker (not a blocker for Texas Hold'em with typical 30-second action clocks).

### Product: DarkFelt

A private on-chain poker room targeting serious players (mid-to-high stakes).

**How it works:**

1. Player creates a session key (temporary, scoped to the poker contract) via Starknet AA.
2. Player buys in: STRK20 `Deposit` + `CreateNote` for chip stack.
3. Hand: deal is executed via Mental Poker shuffle (all players participate in encrypted shuffle, Stwo proof validates shuffle fairness).
4. Each action (bet, call, raise, fold) is a Cairo contract call, signed by session key.
5. At showdown: players reveal their hand commitments. Cairo contract evaluates winner.
6. Pot assigned: winner's `CreateNote`, losers' notes consumed.
7. Stack sizes hidden between hands — opponents see only bet sizing.

**Target Users:** Mid-stakes and high-stakes online poker players ($0.5/$1 through $25/$50 NL Hold'em), poker grinders who want hand history privacy, crypto-native players tired of KYC on traditional poker sites.

**Business Model:** Rake-based.

**Revenue Model:**
- Rake: 2–5% of each pot, capped at $5 per hand (standard poker economics). At 100 hands/hour across 100 concurrent tables: $50,000–$100,000/hour at full scale.
- VPN-alternative premium: players in restricted jurisdictions pay privacy premium (+0.5% rake)
- Tournament entries: $100–$10,000 buy-ins with 10% house take on total prize pool

---

## 4. Private Blackjack

### The Concept

Provably fair blackjack where the deck state is cryptographically committed and revealed using Verifiable Random Functions (VRF) or Mental Poker-style commitment schemes. Bet amounts held as STRK20 notes; win/loss private from other players.

### Market Landscape

**ZKasino** is a dedicated gaming L2 for provably fair games including blackjack, roulette, baccarat, dice, and slots. It claims 2,000+ TPS, sub-second finality, and zero gas fees for players. Uses VRF + ZK proofs to ensure fairness.

**Aptosino** on Aptos has a live fully decentralized blackjack module with all game logic on-chain via smart contracts.

**The key insight**: Blackjack differs from poker in a critical way. Blackjack is player vs. house (not player vs. player), so the "Mental Poker" multi-party shuffle is not required. The house's deck just needs to be verifiably fair — achievable with VRF. This makes on-chain blackjack simpler to implement than poker.

**Privacy value in blackjack**: Serious blackjack players (card counters, advantage players) benefit from bet-amount privacy. If a high roller's STRK20 note amounts are hidden, the house cannot track individual betting patterns and "flat back" (cap) winning players.

### Why STRK20 / Starknet

- VRF requirement: Starknet doesn't yet have Chainlink VRF, but collaborative randomness via validator committees or StarkWare's verifiable randomness infrastructure is achievable. Alternatively: commit-reveal scheme where dealer pre-commits to a shuffled deck hash and reveals progressively.
- STRK20 bet privacy: bet amounts are STRK20 notes — the house sees a bet was placed but not its size until settlement. Other players at the table see nothing.
- Cairo game logic: blackjack rules (hit/stand/double/split/insurance) implemented as Cairo contract.
- Low fees: <$0.20 per hand on Starknet vs. infeasible on Ethereum mainnet.

### Product: MaskedCards

A private blackjack casino on Starknet with provably fair dealing and anonymous bets.

**How it works:**

1. Player deposits STRK20 notes as bankroll.
2. Each hand: player commits bet amount via `UseNote` on a shielded note.
3. Dealer (Cairo contract) generates a new hand from a VRF-seeded deck commitment.
4. Player makes decisions (hit/stand/double/split) via session key.
5. Resolution: hand outcome evaluated by Cairo contract. Winner receives `CreateNote` payout; loser's note is consumed.
6. No on-chain record of individual bet amounts — only aggregates visible to auditors via viewing keys.

**Target Users:** Advantage players and card counters (bet privacy from house), high-roller recreational players (privacy from analytics), crypto-native casual gamblers wanting provable fairness.

**Business Model:** House edge.

**Revenue Model:**
- House edge: 0.5–1% (significantly lower than Las Vegas's 0.5–2% blackjack house edge, achievable because overhead is minimal)
- With $1M in daily wagering, house edge revenue = $5,000–$10,000/day
- VIP tier (higher bet limits, rebates): premium subscription $500–$5,000/month

---

## 5. Private Raffles

### The Concept

On-chain raffles where ticket holders are anonymous, the draw is verifiably fair, and winners claim prizes privately. Used for NFT drops, exclusive access events, community allocations, and charitable fundraising.

### Market Landscape

**Trueluck** is a multi-chain raffle protocol using Chainlink VRF for provably fair winner selection. It supports cross-chain raffles via Stargate and LayerZero, with smart contracts governing entry rules, ticket prices, and slot limits. Live on Ethereum, BNB, Polygon, and Abstract.

**GET Protocol** uses Chainlink VRF for fair distribution of rare ticket drops for events.

**The standard**: Chainlink VRF is the de facto random number standard for on-chain raffles. The gap is privacy — all current raffles have fully public participant lists.

**Why privacy matters for raffles**: NFT projects, protocol token allocations, and exclusive community drops suffer from sybil attacks precisely because ticket holder identities are public. Bots farm raffles by creating thousands of wallets. Private raffles where holder identities are hidden make sybil farming expensive — you can't verify which wallets are farming because all tickets look identical.

### Why STRK20 / Starknet

- Ticket as STRK20 note: each raffle ticket is a note. The note owner (ticket holder) is hidden from public view.
- Proof of eligibility: a buyer can prove they hold a ticket without revealing their address. Multiple ticket purchases from the same underlying identity can be limited via ZK identity checks (Starknet ID / Worldcoin integration).
- Verifiable randomness: Starknet's VRF infrastructure (or collaborative randomness via validator committee) selects winner from the commitment set without revealing the full ticket list.
- Sybil resistance: combine private tickets with proof-of-humanity (Worldcoin Orb, Starknet ID biometric) to limit one ticket per human without revealing which human holds which ticket.

### Product: BlindDraw

A private raffle protocol for NFT drops and token allocations on Starknet.

**How it works:**

1. Raffle creator deploys a BlindDraw contract: prize, ticket price, max tickets, duration, optional sybil limit (1 ticket per verified human).
2. Participants buy tickets: each ticket purchase mints a STRK20 note with a unique ticket commitment.
3. At close: Starknet verifiable randomness selects a winning commitment index.
4. Winner claims: submits Stwo proof that they hold the winning ticket note → `UseNote` → receives prize.
5. Losing ticket notes are burned (refund optional).
6. Ticket holder list never published.

**Target Users:** NFT project teams running fair launches, DeFi protocols distributing token allocations, event organizers selling exclusive access, charities running fundraising draws.

**Business Model:** Per-raffle fee + protocol fee on ticket sales.

**Revenue Model:**
- Protocol fee: 2–3% of total ticket sales
- Raffle setup fee: $100–$1,000 per raffle
- Enterprise tier (custom branding, white-label, legal compliance): $5,000–$50,000/year

---

## 6. Dark Forest: Fog-of-War Strategy Gaming

### The Concept

Dark Forest is a real-time strategy game where the universe map is hidden — players must explore and discover planets using computational proof-of-work. Each planet's coordinates are known only to the player who discovered them, enforced by ZK proofs (not by a central server).

### Market Landscape

**Dark Forest** (by Gubsheep, now 0xPARC) is the canonical implementation. Built in 2020 on Ethereum, it attracted 10,000+ players. Backed by Paradigm, Y Combinator, Bessemer, and the Thiel Fellowship (total ~$100K). The game is in maintenance mode since 2022 — not because demand disappeared, but because Ethereum's gas costs made real-time gameplay uneconomical at scale.

The core mechanic: planet coordinates are hashed; players must brute-force hash collisions to discover new planets. A ZK proof of valid hash is submitted on-chain to "claim" a planet. Opponents can't know where your planets are without their own computational search.

**The opportunity**: Dark Forest on Starknet is not a theoretical product — it is a known, beloved game with an existing player base, a working ZK architecture, and a clear technical blocker (gas costs) that Starknet directly solves.

### Why STRK20 / Starknet

- Stwo is 1,000× faster than Ethereum's Groth16 prover: hash-proof generation that took seconds on Ethereum takes milliseconds on Starknet. Real-time gameplay becomes feasible.
- Cairo native fog-of-war: planet coordinate proofs written directly in Cairo — no Circom or separate circuit DSL.
- STRK20 resource economy: in-game resources (silver, energy) held as STRK20 notes. Hidden resource levels add a second layer of fog — opponents don't know your planet's productive capacity.
- Low fees: planetary attack transactions cost <$0.20 on Starknet vs. $5–$50 on Ethereum mainnet.
- Starknet gaming ecosystem: Dojo Engine, Loot Survivor, and 51+ gaming projects already on Starknet. Dark Forest has an existing home.

### Product: Dark Forest Reborn (Starknet Edition)

A Starknet-native reimplementation of Dark Forest with STRK20 resource economy and competitive seasons.

**How it works:**

1. Universe is procedurally generated at season start. Planet coordinate hash function uses a season-specific secret.
2. Players explore: compute hash collisions to discover planet coordinates, generate Stwo proof of valid discovery.
3. Claim planet: submit proof on-chain. Planet registered to player's STRK20 privacy address (hidden from opponents).
4. Resource production: planets produce STRK20 resource notes (silver, energy) — amounts hidden.
5. Attacks: attacker commits energy from a STRK20 note, generates Stwo proof of attack validity, submits. Defender's planet ownership challenged.
6. Season end: leaderboard calculated from on-chain planet ownership proofs.

**Target Users:** Starknet gaming community, ZK-gaming enthusiasts, competitive RTS players, 0xPARC / Dark Forest alumni community.

**Business Model:** Season-based competitive play.

**Revenue Model:**
- Season entry fee: $10–$100 per player per season
- In-game cosmetics: planet skins, ship designs (NFTs): 10% royalty on secondary sales
- Spectator mode: live game state viewer (subscribers can watch the observable universe without playing): $5–$20/month
- Esports sponsorships: branded seasons, tournament prize pools

---

## 7. Private Battleships

### The Concept

On-chain Battleships where ship placements are committed via Merkle tree hashes and each hit/miss is proven via ZK without revealing the full board. A commitment scheme ensures neither player can retroactively change their ship positions.

### Market Landscape

Every existing implementation is academic or a hackathon project:

- **MIT**: Fully decentralized Battleship using ZK proofs for move validation.
- **ZK-Battleships-Solana**: Solana Grizzlython Honorable Mention.
- **zkbattleship** (Ethereum): Circom + zk-SNARKs. Board hashes on-chain; ZK proof of each hit/miss.
- **BattleZips**: Aztec ecosystem version.
- **zkBattleship on Bitcoin**: First interactive ZK tutorial on Bitcoin.

None have commercial deployments or meaningful user bases. The use case is primarily educational — demonstrating how commit-reveal ZK proofs work for hidden information games. The academic value is higher than the commercial value for vanilla Battleships.

**The commercial opportunity**: Battleships-style mechanics applied to new contexts — naval strategy, territory control, dark fleet compositions — where hidden placement is core game design, not just a demo mechanic.

### Why STRK20 / Starknet

- Client-side Stwo proofs: hit/miss validation proofs generated in milliseconds on the player's device.
- Cairo game logic: board state management in Cairo is straightforward (10×10 grid as a felt252 mapping).
- STRK20 wagering: match stakes held as STRK20 notes, released to winner at game end.
- Starknet gaming community: natural deployment home alongside Dojo Engine games.

### Product: FleetShadow

A competitive hidden-fleet strategy game for Starknet, extending Battleships mechanics into a multi-fleet territorial game with stakes.

**How it works:**

1. Each player commits a fleet configuration as a Merkle root (ship positions hashed without revealing placement).
2. Game proceeds turn by turn: each attack is a coordinate guess. Defender generates Stwo proof of "hit" or "miss" + publishes proof (not coordinates).
3. Board commitment is verifiable at game end — any dispute about historical hits/misses is provable from the on-chain proof record.
4. STRK20 match stake (both players deposit) released to winner at game conclusion.
5. Tournament mode: 8/16/32 player brackets with progressive prize pools.

**Target Users:** Competitive on-chain gamers, crypto gaming communities, Dojo ecosystem players, casual wagering audience.

**Business Model:** Wagering platform with tournament entry fees.

**Revenue Model:**
- Tournament entry fee: $5–$100 per tournament
- Stake matching fee: 1–2% of wagered amount on ranked matches
- NFT fleet cosmetics: ship skins, special ability tokens
- Sponsorships: branded tournament seasons from crypto protocols

---

## Summary Table

| Use Case | Existing Market | STRK20 Advantage | Starknet Fit | Viability |
|---|---|---|---|---|
| Encrypted Voting | Vocdoni, Snapshot+Shutter, MACI | Trustless tally, no coordinator | **Excellent** | **High** |
| Confidential Token Standard | Solana C-SPL (disabled), zERC20 | Native STARK proving, compliance | **Excellent** | **High** |
| Private Poker | Virtue Poker ($5M raised) | Stwo speed, STRK20 stacks | **Good** | **Medium** |
| Private Blackjack | ZKasino, Aptosino | STRK20 bet privacy, low fees | **Good** | **Medium** |
| Private Raffles | Trueluck (Chainlink VRF) | Sybil resistance, ticket privacy | **Good** | **High** |
| Dark Forest | Original (ETH, 10K players) | Gas costs solved, Stwo speed | **Excellent** | **High** |
| Battleships / FleetShadow | Academic only | Cairo circuits, STRK20 wagering | **Good** | **Medium** |

---

## See Also

- [[chains/strk20|STRK20 Protocol]] — Technical architecture
- [[chains/starknet-use-cases|Core Use Cases]] — Payroll, donations, OTC, AI agents
- [[chains/starknet-usecases-defi|DeFi Use Cases]] — Dark pools, perpetuals, lending
- [[chains/starknet-usecases-social|Identity & Social]] — Private social graphs, messaging
