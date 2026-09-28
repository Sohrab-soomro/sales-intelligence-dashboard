# Sales Intelligence Control Center — North Region (Bundle Upsell Sciences)

> **⚠️ DATA PRIVACY & DUMMY DATA DISCLAIMER**  
> All Excel workbooks (`.xlsx`) included in this repository contain **100% synthetic, randomly generated dummy data** created strictly for portfolio demonstration and testing purposes.  
> - **No real financial, recharge, or subscriber figures** are present.  
> - **All territory codes (MBUs), Franchise IDs (FIDs), supervisor names (`(Demo)`), and locations** are fictional placeholders.  
> - **No proprietary or confidential telecom records** are stored anywhere in this repository.

---

## Overview

A single-page, zero-backend **Sales & Bundle Upsell Intelligence Control Center** built with vanilla JavaScript, Chart.js, and SheetJS (`xlsx`). All workbook parsing, cross-sheet reconciliation, and multi-month intelligence calculations happen entirely in the browser.

### Key Capabilities
- **Executive Regional Overview**: Real-time KPI cards, retailer health comparison across Sub-regions / MBUs / FIDs, and interactive daily performance trend comparisons.
- **Multi-Month Bundle Intelligence Engine**:
  - **Bundle Momentum**: Automatically classifies bundles into `RISING`, `STABLE`, `DECLINING`, `EMERGING`, and `DORMANT` using weighted 3-month historical baselines (50/30/20), linear trend slopes, and transition consistency.
  - **Bundle Priority Score (0–100)**: Composite scoring across Momentum, Confidence, Commercial Value, Validity Growth, Activation Share Headroom, and Regional Adoption Gaps.
  - **Validity Trend Analysis**: Tracks structural mix shifts across `Daily`, `Weekly`, `Monthly`, `90 Days`, `100 Days`, `Social`, `Data`, `Voice`, and `Sharing` packages.
  - **Next Best Action (NBA)**: Generates evidence-backed territory and bundle recommendations (Rising Acceleration, High-Value Decline Protection, Regional Replication, and Inactive Retailer Targeting).
- **MBU & FID Intelligence Views**: Sortable rankings, recharge channel mix (`APC`, `OTAR`, `Missed Call`, `Self-Care`), and top-bundle contribution breakdowns.
- **Opportunity Finder**: Interactive threshold slider to flag high-priority inactive retailer pools against regional benchmarks.
- **Automated Data Quality Checks**: Built-in verification for subtotal exclusion, duplicate IDs, EVC base coverage, and RAW-to-Summary reconciliation.

---

## Included Synthetic Sample Workbooks (Dummy Data)

To test the multi-month intelligence engine, load all four sample workbooks together in the dashboard loader screen:

1. `N2_Bundle_Upsell_Sciences_OCT-25_MASTER.xlsx` *(Historical Month 3 — Oct 2025 synthetic dummy data)*
2. `N2_Bundle_Upsell_Sciences_NOV-25_MASTER.xlsx` *(Historical Month 2 — Nov 2025 synthetic dummy data)*
3. `N2_Bundle_Upsell_Sciences_DEC-25_MASTER_V3.3.xlsx` *(Historical Month 1 — Dec 2025 synthetic dummy data)*
4. `upadted N2 file.xlsx` *(Current Period — Jan 2026 synthetic dummy data)*

---

## How to Run Locally

1. Clone or download this repository.
2. Open `index.html` (or `Jazz_Sales_Intelligence_Dashboard.html`) in any modern browser (Chrome, Edge, Firefox).
3. Drag and drop the 4 sample `.xlsx` files into the upload zone to launch the full multi-period dashboard.
