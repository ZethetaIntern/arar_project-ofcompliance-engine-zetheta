# Part 2: Regulatory Mapping & Compliance Rules

## 1. AML (Anti-Money Laundering) Rules
* **Structuring Detection:** Identifies transactions just below reporting thresholds (e.g., $9,999 when the limit is $10,000).
* **High-Risk Jurisdictions:** Flags transactions originating from or destined to countries identified as high-risk by the FATF (Financial Action Task Force).
* **Velocity Checks:** Detects a high volume of transactions within a short timeframe for a single account.

## 2. KYC (Know Your Customer) & Identity
* **Sanction Screening:** Matches entity names (individuals or companies) against global PEP (Politically Exposed Persons) and Sanction lists.
* **Profile Consistency:** Flags discrepancies between declared occupation/income and transaction behavior.

## 3. Trade Surveillance
* **Market Manipulation:** Detects potential "Wash Trading" (buying and selling the same asset to create false volume).
* **Layering Detection:** Uses Neo4j to identify complex, multi-hop transactions designed to hide the source of funds.

## 4. Mapping Summary Table
| Regulation | Trigger | Logic |
| :--- | :--- | :--- |
| AML-01 | Transaction > $10k | Mandatory SAR Filing |
| AML-02 | Rapid Velocity | Flag for manual review |
| KYC-01 | Sanction List Match | Immediate account freeze |
| TRD-01 | Wash Trading | Alert compliance officer |
