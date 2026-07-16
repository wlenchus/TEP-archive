# GSR–IFFT Reference Directory (v1)
*A living, deduplicated, and citable markdown structure for the project.*

---
## Directory Tree
```
GSR-IFFT/
├── 00_Core/
│   ├── Core_Axioms_and_Conventions.md
│   ├── IFFT_to_GSR_Mechanics_and_Dynamics.md
│   ├── Evidence_Map.md
│   └── Glossary_and_Units.md
├── 10_Boundary/
│   ├── Boundary_Law_TEP_and_Tomography.md
│   ├── DtN_Formalism_and_PR.md
│   └── Budget_Curvature_Correspondence.md
├── 20_Thermo_Info/
│   ├── Amplitude_Intensity_and_Thermo.md
│   ├── Shannon_Capacity_and_Info_Cost.md
│   └── Generalized_Thermodynamic_Dynamics.md
├── 30_Kinematics/
│   ├── Inter_Frame_Lorentzian_Transforms.md
│   ├── Intra_System_Self_Boosts.md
│   └── Informational_Inertia_and_Dynamics.md
├── 40_Phenomenology/
│   ├── Knowledge_Coherence_Phenomena.md
│   └── Coherence_Risk_and_Erasure.md
├── 50_Field_Theory/
│   ├── Information_Flow_Field_Theory.md
│   └── Theta_Field_Model.md
├── 60_Applications/
│   └── YbRh2Si2_QCP_CaseStudy.md
├── 70_Assessment/
│   └── Critical_Assessment_and_Roadmap.md
├── 80_Support/
│   ├── Definitions_and_Equation_Index.md
│   └── Changelog.md
└── 90_Notes/
    └── _Archived_Originals.md
```

> **Canonical rule:** Only `00_Core/Core_Axioms_and_Conventions.md` defines symbols and units. Everywhere else: link back; no re-definitions.
>
> **Evidence tags:** (A) derived & checked · (B) model-consistent · (C) conjecture · (D) aspirational.
>
> **Equation IDs:** `[E m.n]` where `m` = section, `n` = index in that section.

---
## 00_Core

### Core_Axioms_and_Conventions.md
**Purpose.** Single source of truth for symbols, units, transforms, and evidence tags.  
**Scope.** Budget identity; angle/rapidity dictionary; P-like vs D-like transforms; regime thresholds; Gamma-of-Sigmas.  

#### Contents
1. **Budget identity** `[E1.1]` : `x^2 + u = 1` (A).  
2. **Angle/Rapidity** `[E1.2]` : `tan A = sinh ψ`, `sec A = cosh ψ`, `sin A = tanh ψ` (A).  
3. **P/D protocol** (B): parameter- vs state-acting transforms; composition notes.  
4. **Regime thresholds** (B): `l_*`, `f_*`, quadrant map in `(log l, log f)`.  
5. **Gamma-of-Sigmas** `[E5.1]` (B): multiplicative composition operator; worked `v = l f`.  
6. **Evidence & IDs** (A).  
7. **Glossary** (A).

**Sources to consolidate:** Core parts from *The Informational Universe*, *P-like and D-like exposition*, *Innovations*, *Refinements*, *Pre-Proposed Invariant Interval*, *Deriving Generalized Relativistic Transformations…*  
**Status:** Seeded (see existing canvas); import missing tables/examples.

---

### IFFT_to_GSR_Mechanics_and_Dynamics.md
**Purpose.** Canonical mechanics: energy landscape, EOM, symmetries, anisotropy.  
**Key results.** `E(A)=M0 sec A = M0 cosh ψ` `[E2.1]` (A); torque `T=-M0 sec A tan A` `[E2.2]` (A); EOM `[E3.1]` (B).  

#### Contents
1. **State space & parameters** (A).  
2. **Energy & torque** `[E2.1]`–`[E2.2]` (A).  
3. **EOM & decay laws** `[E3.1]`–`[E3.3]` (B).  
4. **Symmetries & Noether current** (B).  
5. **Anisotropy & bifurcations** `[E5.1]`–`[E5.3]` (B).

**Sources to consolidate:** *IFFT Dynamics*, *Informational Dynamics…*, *GSR–IFFT Integration*, *Innovations*, *Refinements*.  
**Status:** Seeded (see existing canvas); paste remaining derivations.

---

### Evidence_Map.md
**Purpose.** One-page matrix mapping each major claim to its derivation/data and tag.  

**Schema.** | Claim | Eq(s) | Tag | Where derived | Where tested | Notes |

**Seeds.**  
- `E(A)=M0 sec A` → `[E2.1]` → (A) → Mechanics §2 → Boundary calibration (TEP) → torque/decay fits.  
- TEP→DtN PR/reciprocity → Boundary §1 → (B) → circuit/network analogs.  
- BCC Abel pair `[B4.1–B4.2]` → Boundary §4 → (B) → tomography pipeline prototype.  
- YbRh2Si2 exponent ζ ≈ 0.68 → Applications → (B) → fit replication.

---

### Glossary_and_Units.md
**Purpose.** Central glossary + units/dimensions.  
**Action.** Import the units table from Core and expand with any new symbol before use elsewhere.

---
## 10_Boundary

### Boundary_Law_TEP_and_Tomography.md
**Purpose.** TEP/PHP statements, reciprocity/PR, tomography program.  
**Contents.**  
1) TEP definition & conditions (B).  
2) PHP (boundary sufficiency) (B).  
3) Tomography pipeline outline (B).  
**Sources.** *TEP & Passive Holography — Working Notes*, *Innovations*.

### DtN_Formalism_and_PR.md
**Purpose.** Formal Λ: Dirichlet→Neumann, positivity, reciprocity.  
**Contents.** Definitions, inner-products, PR proofs; calibration of `M0` at `A=0`.  
**Sources.** *TEP notes*, *Innovations*.

### Budget_Curvature_Correspondence.md
**Purpose.** BCC kernel & inversion; GH/Wigner fold.  
**Contents.** Abel pair `[B4.1–B4.2]` (B); noncircular harmonics; examples.  
**Sources.** *Innovations*, *The State of Novelty for Threshold Calculus Relativity*.

---
## 20_Thermo_Info

### Amplitude_Intensity_and_Thermo.md
**Purpose.** A↔I mapping; oscillator/impedance unification; critical behavior.  
**Contents.** Linear response; effective temperature `Θ`; mean‑field exponents (B).  
**Sources.** *Amplitudes, Intensities, and the Mechanics of Reality*, *Refinements*.

### Shannon_Capacity_and_Info_Cost.md
**Purpose.** Channel capacity in GSR variables; energetic cost of coherence.  
**Contents.** `x^2 = S/(S+N)`; `C/B = log2(G^2(x))`; `S=N x^2 G^2(x)` (B).  
**Sources.** *GSR, Shannon Capacity, and the Energetic Cost of Signal Coherence*.

### Generalized_Thermodynamic_Dynamics.md
**Purpose.** Entropy–coherence coupling; non‑adiabatic processes.  
**Contents.** `dS/dψ_L = −k_SL cosh ψ_L`; First‑Law consistency (B).  
**Sources.** *REVISION 5 — Advanced Progress & Emerging Thermodynamic Connections*.

---
## 30_Kinematics

### Inter_Frame_Lorentzian_Transforms.md
**Purpose.** Derive SR‑compatible transforms from perspective postulates.  
**Contents.** Linearity/isotropy → invariant interval; rapidity addition (A/B).  
**Sources.** *Deriving Generalized Relativistic Transformations…*, *Pre‑Proposed Invariant Interval*, *Reconciling the Proposed Invariant Interval…*.

### Intra_System_Self_Boosts.md
**Purpose.** Internal SO(2) rotations; self‑boost law and symmetry breaking.  
**Contents.** Conditions `α=β`, `V=V(C)`; Noether current; soft breaking (B).  
**Sources.** *GSR–IFFT Integration*, *IFFT Dynamics*, *Innovations*.

### Informational_Inertia_and_Dynamics.md
**Purpose.** EOM for A(t); decay regimes; anisotropy & bifurcations.  
**Contents.** Mechanics §2–§5 imports; stability criteria; hysteresis (B).  
**Sources.** *Informational Dynamics…*, *Refinements*.

---
## 40_Phenomenology

### Knowledge_Coherence_Phenomena.md
**Purpose.** Coherence risk; knowledge evaporation; erasure.  
**Contents.** Risk vs `M_info`; energetic maintenance cost; testable predictions (B).  
**Sources.** *Coherence Risk, Knowledge Stability, and Erasure*.

### Coherence_Risk_and_Erasure.md
**Purpose.** Quantify thresholds and failure modes; safeguards.  
**Contents.** Failure envelopes; boundary‑driven stabilization (B).  
**Sources.** *Coherence Risk…*, *Physics Framework Consolidation Report_* (critique bits).

---
## 50_Field_Theory

### Information_Flow_Field_Theory.md
**Purpose.** Two‑field IFFT (ψ_K, ψ_P); constraints; quanta.  
**Contents.** Lagrangian, constraint `|ψ_K|^2+|ψ_P|^2=C`; α/β symmetry; gauge sketch (C).  
**Sources.** *A Comprehensive Theoretical Synthesis…*, *A Critical Analysis and Strategic Augmentation…*.

### Theta_Field_Model.md
**Purpose.** θ‑soliton action charge Q_total as source of scale‑inertia.  
**Contents.** Soliton solutions; `m_scale ∝ Q_total`; ISO(1,N) remarks (C).  
**Sources.** *Strategic Augmentation…* (θ‑field parts), related notes.

---
## 60_Applications

### YbRh2Si2_QCP_CaseStudy.md
**Purpose.** Data‑model map; ζ exponent; B_scale.  
**Contents.** Reproducible fits; scripts/data pointers; anisotropy notes (B).  
**Sources.** *YbRh2Si2 QCP Data Retrieval*.

---
## 70_Assessment

### Critical_Assessment_and_Roadmap.md
**Purpose.** Red‑team risks; falsifiable deltas; timeline.  
**Contents.** What’s derived vs conjectural; kill‑switch criteria; milestone tests.  
**Sources.** Merge of both critique/assessment docs.

---
## 80_Support

### Definitions_and_Equation_Index.md
**Purpose.** Global index of symbols and equation IDs with locations.  
**Action.** Auto‑update as PR check.

### Changelog.md
**Purpose.** Track moves/merges; `superseded-by` pointers for all 90_Notes items.

---
## 90_Notes

### _Archived_Originals.md
**Purpose.** Index of legacy docs with “Superseded by …” banners and exact section pointers.  
**Populate with:** All originals provided (titles retained) and a link to target sections above.

---
# Source → Target Merge Map (for deduplication)
- **Innovations in the GSR–IFFT Framework Beyond the Original Foundations (.docx)** → 00_Core (Gamma‑of‑Sigmas; thresholds), 10_Boundary (TEP/PHP, BCC), 30_Kinematics (self‑boosts), 30_Kinematics/Mechanics (EOM).
- **Refinements and Extensions in GSR‑IFFT (.docx)** → thresholds & exponents (20_Thermo_Info), birefringence/bifurcations (30_Kinematics), empirical dual character (60_Applications).
- **Deriving Generalized Relativistic Transformations…** + **Pre‑Proposed/Reconciling Invariant Interval** → 30_Kinematics/Inter_Frame_Lorentzian_Transforms.md.
- **GSR, Shannon Capacity, and the Energetic Cost of Signal Coherence** → 20_Thermo_Info/Shannon_Capacity_and_Info_Cost.md.
- **TEP & Passive Holography — Working Notes** → 10_Boundary/Boundary_Law_TEP_and_Tomography.md + DtN_Formalism_and_PR.md + Budget_Curvature_Correspondence.md.
- **Amplitudes, Intensities, and the Mechanics of Reality** → 20_Thermo_Info/Amplitude_Intensity_and_Thermo.md.
- **IFFT Dynamics… / Informational Dynamics… / GSR‑IFFT Integration…** → 30_Kinematics/Informational_Inertia_and_Dynamics.md (plus 00_Core mechanics definitions already seeded).
- **Coherence Risk, Knowledge Stability, and Erasure** → 40_Phenomenology/*.md.
- **A Comprehensive Theoretical Synthesis… / A Critical Analysis and Strategic Augmentation…** → 70_Assessment/Critical_Assessment_and_Roadmap.md and 50_Field_Theory/*.md.

---
# Contribution Rules (to avoid “vibe physics”)
1) **One‑definition rule.** Symbols live only in `00_Core/Core_Axioms_and_Conventions.md`.
2) **Evidence labels everywhere.** Claims and lemmas carry (A/B/C/D). Conjectures live in clearly marked boxes with falsifiable deltas.
3) **Equation IDs.** Use `[E m.n]` consistently and reference by ID rather than restating.
4) **Units & dimensions.** New symbols require a units entry before merging.
5) **Kill metaphors; show math.** Prefer lemmas/proofs; analogies only in parentheticals.

