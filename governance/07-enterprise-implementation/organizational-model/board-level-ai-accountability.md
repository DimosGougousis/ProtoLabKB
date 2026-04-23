# Board-Level AI Accountability

> **Purpose:** Guide for establishing and operationalizing board-level accountability for AI governance in regulated FinTechs, satisfying DNB expectations for meaningful board oversight.
>
> **Regulatory Basis:** DNB Good Practice for AI in the Financial Sector; Wft Section 3:8 (fitness/geschiktheid), Section 3:9 (propriety/betrouwbaarheid), Section 3:15 (four-eyes principle/vierogenbeginsel), Section 3:17 (sound business operations); EU AI Act Article 4 (AI literacy); SAFEST items A-01, K-01 through K-04.
>
> **Key Principle:** DNB expects a named board member with explicit accountability for AI governance. This person must genuinely understand the AI systems -- they cannot delegate understanding.

---

## 1. DNB Expectation: Named Board Member with AI Accountability

### What DNB Requires

SAFEST item A-01 states: *"Named board member(s) with explicit accountability for AI governance and AI risk. Documented in board mandate/charter."*

This means:

1. **Named, not implied.** The board mandate must explicitly assign AI governance accountability to a specific person. "The board collectively oversees AI" is insufficient.
2. **Documented.** The assignment must appear in the board charter, mandate letter, or equivalent governance document. Verbal agreements do not count.
3. **Genuine understanding.** The named board member must be able to explain how the organization's AI systems work at a strategic level -- risks, limitations, failure modes, and business implications (K-01).
4. **Active oversight.** The board member must actively engage with AI governance -- reviewing reports, asking challenging questions, and making informed decisions. Passive receipt of dashboards is not oversight.

### Who Should It Be?

| Board Role | Suitability | Considerations |
|-----------|-------------|----------------|
| **CTO (if on board)** | High | Strongest technical understanding; but risk of 1st line bias -- ensure 2nd line challenge is robust |
| **CEO** | Medium | Sets tone from the top; but may lack technical depth for meaningful challenge |
| **CRO (if on board)** | High | Natural fit for risk oversight; may need AI technical upskilling |
| **Independent Non-Executive Director with tech background** | High | Strong independence; brings external perspective; may need company-specific AI upskilling |
| **CFO** | Lower | Unless AI is core to financial operations; typically better suited for budget oversight |

`[RECOMMENDATION]` For most FinTechs, the CTO or a technically literate non-executive director is the strongest choice. If the CTO is the named board member, ensure the CRO provides independent challenge.

### Board Mandate Template

Include the following language in the board mandate of the named member:

> **AI Governance Accountability**
>
> `[NAME]`, in their capacity as `[ROLE]`, bears explicit accountability for AI governance and AI risk management at `[COMPANY NAME]`. This includes:
>
> (a) Ensuring an effective AI governance framework is established, maintained, and operating as intended;
>
> (b) Overseeing that all AI systems comply with applicable regulations (EU AI Act, GDPR, DORA, Wft, Wwft) and internal policies;
>
> (c) Ensuring the board receives accurate, timely, and comprehensive reporting on AI system performance, risk, fairness, and compliance;
>
> (d) Escalating material AI-related risks to the full board;
>
> (e) Satisfying themselves that the organization has adequate skills, resources, and processes for responsible AI development and deployment;
>
> (f) Representing AI governance matters in interactions with DNB and other regulators.

---

## 2. Board AI Literacy Requirements

### SAFEST Skills Pillar Requirements

SAFEST items K-01 through K-04 set specific expectations for board and senior management AI understanding:

| Item | Requirement | What DNB Will Test |
|------|------------|-------------------|
| K-01 | Board AI competency: evidence of strategic-level AI understanding | Can the board member explain how each AI system works, its risks, and limitations? |
| K-02 | Board AI risk reporting: regular board reporting on AI performance and risk | Are reports produced? Are they read? Do they prompt board action? |
| K-03 | Suitability preparation (geschiktheidstoets): board members rehearsed for DNB interviews | Can the board member answer AI-specific questions in the DNB fitness interview? |
| K-04 | Senior management AI understanding: CTO, CRO, CCO, MLRO can articulate AI system details | Can each key manager explain the AI systems relevant to their domain? |

### Minimum AI Literacy for Board Members

Every board member (not just the named AI accountability holder) should understand:

| Topic | Depth Required | Evidence |
|-------|---------------|----------|
| What AI/ML the company uses and why | Strategic: can name each system and its business purpose | Board paper discussion, meeting minutes |
| How AI decisions affect customers | Strategic: can explain impact pathways | Board Q&A recorded in minutes |
| Key risks of AI (bias, drift, failure, adversarial attack) | Conceptual: can describe each risk category and its relevance | Training attendance records |
| Regulatory landscape (EU AI Act, DORA, DNB SAFEST) | Awareness: knows key obligations and timelines | Board briefing records |
| What happens when AI fails | Strategic: can describe fallback procedures at a high level | Board review of fallback documentation |

### Board AI Competency Development Program

| Activity | Frequency | Responsible | SAFEST Item |
|----------|-----------|-------------|------------|
| Board AI briefing session: overview of AI systems, risks, and governance | Semi-annually | CTO / Head of AI | K-01 |
| AI deep-dive workshop: hands-on demonstration of a specific AI system | Annually | Head of AI/ML Engineering | K-01 |
| Regulatory update: EU AI Act, DORA, DNB developments | Quarterly | Head of Compliance | K-01, K-03 |
| AI incident tabletop exercise: simulate an AI failure scenario | Annually | CISO / CRO | K-01, A-15 |
| External AI governance training: courses, conferences, peer exchange | Annually | Each board member | K-12 |
| DNB fitness interview rehearsal: mock interview with AI-specific questions | Before DNB meeting | External advisor | K-03 |

---

## 3. Board Reporting Template for AI Governance

The AI Governance Committee should produce this report quarterly for the board. The named board member with AI accountability is responsible for ensuring the report is produced, reviewed, and acted upon (K-02).

### Quarterly AI Governance Board Report

```
============================================================
AI GOVERNANCE QUARTERLY REPORT
Period: [Q1/Q2/Q3/Q4] [YEAR]
Prepared by: AI Governance Committee
For: Board of Directors
Classification: Confidential
============================================================

1. EXECUTIVE SUMMARY
   - Overall governance health: [GREEN / AMBER / RED]
   - Key decisions taken this quarter: [list]
   - Key risks to flag: [list]
   - Items requiring board decision: [list]

2. AI SYSTEM INVENTORY (S-01)
   +------------------+--------+----------+--------+
   | System           | Risk   | Status   | Change |
   |                  | Tier   |          |        |
   +------------------+--------+----------+--------+
   | [System name]    | High   | Active   | --     |
   | [System name]    | Limited| Active   | New    |
   | [System name]    | Minimal| Retired  | --     |
   +------------------+--------+----------+--------+
   Total systems: [N] | High-risk: [N] | New this quarter: [N]

3. PERFORMANCE AND RISK (S-03, S-12)
   - Models meeting performance thresholds: [N/N] ([%])
   - Data drift alerts triggered: [N]
   - Models requiring retraining: [N]
   - Key performance concern: [narrative]

4. FAIRNESS AND ETHICS (F-11, E-02)
   - Bias alerts triggered: [N]
   - Bias alerts resolved: [N]
   - Fairness metrics within thresholds: [N/N] ([%])
   - Ethical review requests: [N]
   - Ethical reviews resulting in use case rejection: [N]

5. INCIDENTS (A-15, A-18)
   +----------+----------+---------+-------------+--------+
   | Date     | System   | Severity| Description | Status |
   +----------+----------+---------+-------------+--------+
   | [date]   | [system] | [1-4]   | [brief]     | [open/ |
   |          |          |         |             | closed]|
   +----------+----------+---------+-------------+--------+
   - DORA-reportable incidents: [N]
   - Root cause analyses completed: [N]

6. COMPLIANCE STATUS
   - EU AI Act readiness: [% complete against roadmap]
   - DORA compliance: [status]
   - Open audit findings: [N] (overdue: [N])
   - Regulatory interactions this quarter: [list]

7. SKILLS AND TRAINING (K-09, K-11)
   - AI literacy training completion rate: [%]
   - Role-specific training completion rate: [%]
   - Key competency gaps identified: [list]

8. THIRD-PARTY AI (K-13, S-18)
   - Third-party AI vendors: [N]
   - Vendor risk assessments current: [N/N]
   - Concentration risk concerns: [narrative]

9. RECOMMENDATIONS AND DECISIONS REQUIRED
   [List items requiring board decision with
    background, options, and Committee recommendation]

10. GOVERNANCE IMPROVEMENT PLAN
    - Progress against annual plan: [% complete]
    - Key improvements delivered this quarter: [list]
    - Next quarter priorities: [list]
```

---

## 4. What the Board Should Review Quarterly

Beyond the standard quarterly report, the board should actively engage with:

| Review Item | Purpose | Questions to Ask |
|------------|---------|-----------------|
| **AI system inventory changes** | Ensure new AI systems are properly governed | "Was this system classified correctly? Did it go through the full governance process?" |
| **High-risk model performance trends** | Detect degradation before it causes harm | "Is model X trending in the right direction? What happens if it crosses the threshold?" |
| **Fairness monitoring exceptions** | Ensure bias is detected and addressed | "Which customer groups are affected? What is the remediation timeline?" |
| **Incident post-mortems** | Ensure lessons are learned | "What systemic issue does this incident reveal? How do we prevent recurrence?" |
| **Regulatory compliance gaps** | Stay ahead of regulatory enforcement | "Are we on track for EU AI Act compliance by August 2026?" |
| **Third-party AI concentration** | Manage vendor dependency risk | "What happens if our primary AI vendor has an outage? Do we have alternatives?" |
| **Audit findings** | Ensure governance controls are working | "Why are there overdue findings? What is the remediation plan?" |
| **Training completion** | Ensure skills keep pace with AI deployment | "Are we deploying AI faster than we are training our people?" |

---

## 5. Red Flags the Board Should Watch For

These patterns indicate governance is not functioning effectively. Any of these should trigger immediate board attention:

### Structural Red Flags

| Red Flag | What It Indicates | SAFEST Link |
|----------|------------------|------------|
| AI systems deployed without Committee approval | Governance bypass; 1st line operating without oversight | A-03 |
| No independent model validation performed this quarter | 2nd line not functioning; self-review risk | S-19 |
| Board member with AI accountability cannot explain key AI systems | Nominal accountability without substance; DNB will detect this | K-01 |
| Internal audit has not reviewed AI governance in 12+ months | 3rd line gap; no independent assurance | A-02 |
| RACI matrix does not exist or is outdated | Unclear responsibilities; accountability gaps | A-04 |

### Operational Red Flags

| Red Flag | What It Indicates | SAFEST Link |
|----------|------------------|------------|
| Same model performance metrics reported every quarter with no variation | Monitoring may not be real; dashboard may be static | S-03, T-17 |
| Zero AI incidents reported in 12+ months | Underreporting, not zero incidents; incident detection may be broken | A-15 |
| Fairness monitoring shows zero alerts ever | Monitoring may not be calibrated; thresholds may be too lenient | F-11 |
| Training completion rate is high but no one can answer AI-specific questions | Training is check-the-box, not effective | K-09, K-11 |
| All AI systems classified as "minimal risk" | Risk classification may be too lenient to avoid governance burden | S-01 |

### Cultural Red Flags

| Red Flag | What It Indicates | SAFEST Link |
|----------|------------------|------------|
| Engineering team views governance as an obstacle | Governance not integrated; see [governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) | A-04 |
| Compliance team cannot explain how a specific AI model works | Skills gap between lines of defense | K-07 |
| "Move fast" used to justify skipping governance steps | Tone from the top does not support governance | E-01 |
| Ethical concerns raised but never resulting in use case modification | Ethics function may be performative | E-02, E-04 |
| Governance Committee meetings regularly cancelled or shortened | Governance not prioritized at leadership level | A-03 |

---

## 6. DNB Fitness Interview Preparation: AI-Specific Questions

During the licensing process, DNB will interview each policymaker (dagelijks beleidsbepaler) individually to assess fitness (geschiktheid) under Wft Section 3:8. For AI-intensive FinTechs, expect AI-specific questions. The named board member with AI accountability should be prepared for deeper questioning.

### Questions Every Policymaker Should Be Able to Answer

| Question | What DNB Assesses | Preparation Source |
|----------|------------------|-------------------|
| "Walk me through how your AI system makes a [payment/AML/fraud] decision." | Can you explain your own technology at a strategic level? | Model cards (T-12), system documentation |
| "What happens if your AI model fails at 2 AM on a Sunday?" | Do you have fallback procedures? Have they been tested? | Fallback documentation (S-13), incident response plan (A-15) |
| "How do you know your AI does not discriminate?" | Do you have bias testing? Is it meaningful? | Bias testing results (F-03), fairness monitoring (F-11) |
| "Who in your organization validates AI models independently?" | Is there genuine second-line independence? | 3LoD documentation (A-02), validation reports (S-19) |
| "How does your board stay informed about AI risks?" | Is board oversight real or nominal? | Board reports (K-02), meeting minutes |

### Additional Questions for the Named AI Accountability Holder

| Question | What DNB Assesses | Preparation Source |
|----------|------------------|-------------------|
| "Explain the key risks of your highest-risk AI system." | Deep understanding, not just surface knowledge | Risk assessments, model cards (T-12) |
| "When was the last time you overruled or challenged an AI governance decision?" | Active oversight, not rubber-stamping | Board minutes, Committee minutes |
| "What would you do if you discovered your AML model was systematically missing a specific typology?" | Incident response understanding, regulatory awareness | Incident response plan (A-15), escalation procedures (A-10) |
| "How does your AI governance scale as you grow from 100 to 100,000 customers?" | Forward-looking governance planning | Adoption playbook, governance improvement plan |
| "What is your biggest AI risk right now?" | Honest self-assessment, awareness of weaknesses | AI risk dashboard, quarterly board reports |

---

## 7. Board Governance Calendar

| Month | Board AI Activity | Deliverable |
|-------|------------------|-------------|
| January | Annual AI governance strategy session | Updated AI governance policy, annual audit plan |
| February | Q4 AI governance report review | Board minutes recording review and decisions |
| March | AI competency development (workshop/training) | Training records, updated competency assessment |
| April | -- | -- |
| May | Q1 AI governance report review | Board minutes recording review and decisions |
| June | AI incident tabletop exercise | Exercise report, lessons learned |
| July | -- | -- |
| August | Q2 AI governance report review | Board minutes recording review and decisions |
| September | Regulatory readiness assessment | Gap analysis, remediation plan |
| October | -- | -- |
| November | Q3 AI governance report review | Board minutes recording review and decisions |
| December | Annual governance effectiveness self-assessment | Self-assessment report, improvement plan |

---

## 8. Implementation Checklist

| # | Item | SAFEST Item | Status |
|---|------|------------|--------|
| 1 | Named board member with AI accountability identified | A-01 | [ ] |
| 2 | AI accountability documented in board mandate/charter | A-01 | [ ] |
| 3 | Board AI competency development program established | K-01 | [ ] |
| 4 | Quarterly board reporting template adopted | K-02 | [ ] |
| 5 | First quarterly board report produced | K-02 | [ ] |
| 6 | DNB fitness interview rehearsal completed (all policymakers) | K-03 | [ ] |
| 7 | Senior management AI understanding documented | K-04 | [ ] |
| 8 | Board governance calendar established | K-01 | [ ] |
| 9 | Red flag monitoring process in place | A-01 | [ ] |
| 10 | Annual governance effectiveness self-assessment scheduled | A-03 | [ ] |

---

## Cross-References

- **Three Lines of Defense:** [three-lines-of-defense-for-ai.md](three-lines-of-defense-for-ai.md) -- defines the organizational structure that reports to the board
- **AI Governance Committee Charter:** [ai-governance-committee-charter.md](ai-governance-committee-charter.md) -- the Committee produces the board reports described here
- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- determines which AI systems require board-level approval
- **Adoption Playbook:** [../risk-based-adoption/adoption-playbook.md](../risk-based-adoption/adoption-playbook.md) -- phases board engagement over the 12-month rollout
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
