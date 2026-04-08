# PRIVADA: Private User-Centric Data Aggregation

**Category:** [[_index#research-papers|Research Papers]]
**File:** `raw/papers/2026-579.pdf`
**Authors:** Betül Aşkın Özdemir, Beyza Bozdemir, Ionut Groza, Melek Onen
**Institutions:** COSIC KU Leuven; Digital Security EURECOM
**Related:** [[concepts/cryptographic-primitives]], [[research/random-robust-ss]]

---

## Abstract

PRIVADA introduces a **privacy-preserving data aggregation** system using Secure Multi-Party Computation (MPC) in the SPDZ framework. It enables multiple data customers to query aggregated statistics from a dataset of users while preserving individual privacy — achieving a **12–15x speedup** over the state of the art.

---

## Problem Statement

Data aggregation (computing sums, averages, counts over user data) is enormously valuable for analytics. But it creates a fundamental tension:
- Data customers want accurate aggregate statistics.
- Users want their individual data to remain private.
- Traditional approaches either (a) reveal raw data to the aggregator, or (b) use differential privacy/cryptographic methods that are too slow for practical use.

PRIVADA solves the performance bottleneck while maintaining strong cryptographic privacy guarantees.

---

## Key Technical Contributions

### 1. MPC in the SPDZ Framework
SPDZ is a secure multi-party computation protocol for arithmetic sharing with malicious security. PRIVADA uses SPDZ to allow a set of parties to compute aggregate functions over private inputs without any party learning individual values.

### 2. Multiple Data Customers
Unlike prior work focused on single-customer aggregation, PRIVADA supports **multiple simultaneous data customers** with different query requirements and selective disclosure controls. Users can choose which customers receive which aggregated statistics.

### 3. Additively Homomorphic Encryption (AHE)
Used for efficient aggregation: encrypted values can be added without decryption, enabling batch processing of many users' data simultaneously.

### 4. Malicious Security Model
PRIVADA is provably secure against malicious adversaries — parties who deviate from the protocol cannot learn individual user data or corrupt aggregation results.

### 5. Performance
- **12–15x faster** than state-of-the-art alternatives.
- Achieves practical performance for real-world deployment.

---

## Privacy Guarantees

PRIVADA provides three layers of privacy:

| Layer | Guarantee |
|---|---|
| Input privacy | Individual user data remains secret from all parties |
| User anonymity | Aggregator cannot link results to specific users |
| Output privacy | Data customers receive only authorized aggregate results |

---

## Applications

- Privacy-preserving analytics platforms
- Medical/health data aggregation (multiple researchers accessing patient data summaries)
- Financial reporting with privacy (bank transaction statistics without individual exposure)
- Federated learning preprocessing

---

## Relevance to Privacy Blockchain Ecosystem

PRIVADA represents a direction for **off-chain privacy infrastructure** that complements on-chain ZK protocols. While most papers in this collection focus on blockchain-native privacy, PRIVADA addresses the adjacent problem of aggregating private data — relevant for any system collecting statistics over a user base with privacy requirements.

---

## Backlinks

Source: `raw/papers/2026-579.pdf`
