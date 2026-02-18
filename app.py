import streamlit as st
from source import *
from datetime import datetime
import pandas as pd

# -----------------------------
# Page + Sidebar
# -----------------------------
st.set_page_config(
    page_title="QuLab: Lab 48: Incident Response Simulation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Lab 48: Incident Response Simulation")
st.caption("Audience: CFA charterholders, portfolio managers, risk analysts • Focus: decision usefulness + governance-grade evidence")
st.divider()

# -----------------------------
# Policy constants (explicit + visible)
# -----------------------------
POLICY = {
    "MODEL_TIER": 1,
    "AUC_RED": 0.50,
    "AUC_YELLOW": 0.60,
    "ROLLING_WINDOW_DAYS_CURRENT": 90,   # as described in the scenario narrative
    "ROLLING_WINDOW_DAYS_RECOMMENDED": 30,
    "CONTAIN_TARGET_HOURS": 4,
    "PSI_STABLE_MAX": 0.10,
    "PSI_WATCH_MAX": 0.25,  # > 0.25 = material shift
}

# -----------------------------
# Initialization
# -----------------------------
if "incident_data" not in st.session_state:
    st.session_state.incident_data = initialize_incident_data()

if "current_page" not in st.session_state:
    st.session_state.current_page = "Overview"

if "phase_status" not in st.session_state:
    st.session_state.phase_status = {
        "Overview": True,
        "Detect": True,
        "Contain": False,
        "Investigate": False,
        "Remediate": False,
        "Document": False,
        "Prevent": False,
        "Final Report": False,
    }

# -----------------------------
# Sidebar navigation (gated)
# -----------------------------
st.sidebar.title("AI Incident Response Protocol")
pages = ["Overview", "Detect", "Contain", "Investigate",
         "Remediate", "Document", "Prevent", "Final Report"]
enabled_pages = [
    p for p in pages if st.session_state.phase_status.get(p, False)]

if st.session_state.current_page not in enabled_pages and st.session_state.current_page in pages:
    enabled_pages.append(st.session_state.current_page)
    enabled_pages = sorted(list(set(enabled_pages)),
                           key=lambda x: pages.index(x))

selected_page = st.sidebar.selectbox(
    "Navigate phases",
    options=enabled_pages,
    index=enabled_pages.index(
        st.session_state.current_page) if st.session_state.current_page in enabled_pages else 0,
)

if selected_page != st.session_state.current_page:
    st.session_state.current_page = selected_page
    st.rerun()

# -----------------------------
# Helper blocks (pedagogical, not technical)
# -----------------------------


def policy_box():
    st.info(
        f"""
**Monitoring policy (for this lab, Tier {POLICY['MODEL_TIER']}):**
- **RED:** Rolling AUC < **{POLICY['AUC_RED']:.2f}** → initiate containment (kill switch / fallback)
- **YELLOW:** Rolling AUC < **{POLICY['AUC_YELLOW']:.2f}** → escalate monitoring + begin drift diagnostics
- Rolling window currently assumed: **{POLICY['ROLLING_WINDOW_DAYS_CURRENT']} days**
- Recommended improvement: **{POLICY['ROLLING_WINDOW_DAYS_RECOMMENDED']} days** to reduce detection lag

**Why this matters:** AUC is treated here as a proxy for “directional edge” (ability to separate good vs bad trades).  
If discrimination collapses, continuing unchanged automation can compound losses.
"""
    )


def evidence_pack_box(items):
    with st.expander("Evidence pack (what you would attach for committee review)"):
        for it in items:
            st.write(f"- {it}")


def decision_translation(lines):
    st.markdown("#### Decision translation")
    for ln in lines:
        st.write(f"- {ln}")


def checkpoint_true_false(question, true_label="Yes", false_label="No", correct=True, explanation_correct="", explanation_incorrect=""):
    choice = st.radio(
        question, [true_label, false_label], horizontal=True, index=None)
    if choice is None:
        return
    user_is_correct = (choice == true_label) if correct else (
        choice == false_label)
    if user_is_correct:
        st.success(explanation_correct if explanation_correct else "Correct.")
    else:
        st.info(explanation_incorrect if explanation_incorrect else "Not quite—recheck the policy and assumptions above.")


# -----------------------------
# Pages
# -----------------------------
if st.session_state.current_page == "Overview":
    st.markdown(
        "# Simulation: When an AI Trading Model Starts Losing Money—What You Do Next")

    st.markdown(
        """
You are the primary incident responder for an AI-assisted trading system that impacts client portfolios.
This simulation teaches a **disciplined, phase-based decision workflow** that prioritizes:

1) **Capital protection first** (containment)  
2) **Causal proof second** (investigation with evidence)  
3) **Controlled change + governance** (remediate, document, prevent)

You will complete **six phases** and produce **one deliverable**: a Final Report suitable for governance review.
"""
    )

    st.markdown("---")
    st.markdown("### The Six Phases + Deliverable")
    st.markdown("1. **Detect**: Confirm the signal is real and policy-relevant.")
    st.markdown("2. **Contain**: Stop the bleed; revert to validated fallback.")
    st.markdown(
        "3. **Investigate**: Prove cause (regime shift vs data/process break).")
    st.markdown("4. **Remediate**: Restore edge without creating new risk.")
    st.markdown("5. **Document**: Make it audit-ready.")
    st.markdown("6. **Prevent**: Reduce detection lag and regime risk.")
    st.markdown(
        "**Deliverable:** Final Incident Report (board/committee-ready).")

    st.markdown("---")
    st.markdown("### Micro-example (finance-native)")
    st.write(
        "AUC falling from ~0.58 to ~0.42 is like going from a modest edge to worse-than-coin-flip discrimination—"
        "if position sizing stays unchanged, expected P&L can deteriorate quickly."
    )

    if st.button("Start Simulation"):
        st.session_state.current_page = "Detect"
        st.rerun()

elif st.session_state.current_page == "Detect":
    st.markdown("## Detect: Confirm the Signal Is Real (and Policy-Relevant)")
    policy_box()

    st.markdown(
        """
**Your job in this phase:** determine whether the monitoring signal meets escalation/containment policy and whether the metric is interpretable for decisions.
"""
    )

    st.markdown("### Incident facts (from the alert object)")
    st.markdown(
        f"**Incident ID:** {st.session_state.incident_data['incident_id']}")
    st.markdown(
        f"**Model:** {st.session_state.incident_data['model']} (Tier {st.session_state.incident_data.get('tier', POLICY['MODEL_TIER'])})")
    st.markdown(
        f"**Severity (declared):** {st.session_state.incident_data['severity']}")
    st.markdown(
        f"**Detected by:** {st.session_state.incident_data.get('detected_by', 'Monitoring dashboard')}")
    st.markdown(
        f"**Alert timestamp:** {st.session_state.incident_data['phase_1_detect']['alert_timestamp']}")
    st.markdown(
        f"**Notified:** {', '.join(st.session_state.incident_data['phase_1_detect']['notified'])}")

    st.markdown("---")
    st.markdown("### Metric snapshot (with explicit provenance)")
    auc_baseline = float(
        st.session_state.incident_data["phase_1_detect"]["auc_baseline"])
    auc_current = float(
        st.session_state.incident_data["phase_1_detect"]["auc_current"])
    delta_auc = auc_current - auc_baseline

    st.metric("Validated AUC (baseline window)",
              f"{auc_baseline:.2f}", help="Baseline = last validated/approved period in the scenario")
    st.metric("Live AUC (current window)", f"{auc_current:.2f}", delta=f"{delta_auc:.2f}",
              help="Current = live rolling window estimate in the scenario")

    # Explicitly address the trigger-text mismatch as a governance learning point
    trigger_text = st.session_state.incident_data["phase_1_detect"]["trigger"]
    st.markdown("### Alert trigger text (as logged)")
    st.code(trigger_text, language="text")

    if "0.70" in trigger_text:
        st.warning(
            f"""
**Governance note (intentional learning point):**  
The logged trigger mentions **0.70**, but the lab policy box above uses **RED={POLICY['AUC_RED']:.2f}** and **YELLOW={POLICY['AUC_YELLOW']:.2f}**.
This is an example of **monitoring configuration drift / stale documentation**—a common real-world failure mode.

**What you should do as responder:** rely on the **current approved policy** (the box above), then document the inconsistency as a control gap.
"""
        )

    # Simulated time-series
    st.markdown("### AUC trend (illustrative time series)")
    auc_time_points = ["2024-10-25", "2024-10-28", "2024-10-31", "2024-11-01"]
    auc_values = [0.59, 0.58, 0.55, auc_current]
    auc_data = pd.DataFrame(
        {"Time": pd.to_datetime(auc_time_points), "AUC": auc_values})
    st.line_chart(auc_data.set_index("Time"), y="AUC")

    st.markdown(
        f"""
**Interpretation:** The level relative to thresholds matters more than small day-to-day noise.  
- **RED threshold:** {POLICY['AUC_RED']:.2f}  
- **YELLOW threshold:** {POLICY['AUC_YELLOW']:.2f}
"""
    )

    decision_translation(
        [
            "If Live AUC breaches RED, you should assume the model’s edge is impaired and initiate containment (kill switch / fallback).",
            "If Live AUC is YELLOW but not RED, escalate monitoring frequency and begin drift diagnostics before losses compound.",
        ]
    )

    with st.expander("Why AUC here (without model-engineering detail)"):
        st.markdown(
            """
In this simulation, AUC is treated as a **proxy** for the system’s ability to separate “good vs bad trades”
(e.g., profitable vs unprofitable outcomes). When discrimination collapses, the system behaves like it has **no edge**.

**Watch-out:** AUC does not prove *why* the model failed. It only says performance discrimination degraded.
Your next phase isolates cause (regime shift vs data/process break).
"""
        )

    evidence_pack_box(
        [
            "AUC trend chart with thresholds annotated",
            "Baseline vs current window definition (dates, sample size assumptions)",
            "Alert log showing trigger text (and note any documentation mismatch)",
        ]
    )

    st.markdown("---")
    checkpoint_true_false(
        question=f"Checkpoint: Does Live AUC ({auc_current:.2f}) meet the **RED** containment threshold ({POLICY['AUC_RED']:.2f})?",
        true_label="Yes, contain now",
        false_label="No, just monitor",
        correct=True,
        explanation_correct="Correct: Live AUC is below the RED threshold → containment is justified to protect capital.",
        explanation_incorrect="Recheck: Live AUC is below the RED threshold in this lab policy, which triggers containment.",
    )

    if st.button("Acknowledge Alert & Proceed to Containment"):
        st.session_state.phase_status["Contain"] = True
        st.session_state.current_page = "Contain"
        st.rerun()

elif st.session_state.current_page == "Contain":
    st.markdown("## Contain: Stop the Bleed + Estimate Incremental Loss")

    st.markdown(
        f"""
**Goal:** prevent additional harm while investigation runs.  
For Tier {POLICY['MODEL_TIER']} systems, the containment target is **< {POLICY['CONTAIN_TARGET_HOURS']} hours**.
"""
    )

    st.markdown(
        """
Containment means:
- Freeze new model-driven trading decisions (kill switch)
- Revert to a validated fallback strategy
- Produce an **incremental impact estimate** with explicit assumptions (no unexplained numbers)
"""
    )

    st.markdown("---")
    st.markdown("### Financial impact definition (kept explicit)")

    # ---- DO NOT REMOVE / ALTER FORMULA BLOCK (per user instruction) ----
    st.markdown(
        r"$$ \text{Financial Impact} = \text{Cumulative Losses before Containment} - \text{Cumulative Losses under Fallback Strategy} $$")
    st.markdown(r"where $\text{Financial Impact}$ represents the estimated additional losses due to the model's degradation, $\text{Cumulative Losses before Containment}$ are the cumulative losses incurred while the AI model was underperforming, and $\text{Cumulative Losses under Fallback Strategy}$ are the theoretical cumulative losses if a stable backup strategy had been in place during the same period.")
    # -------------------------------------------------------------------

    with st.expander("How we get a number (worked toy example)"):
        st.markdown(
            """
To avoid “magic” numbers, we use a counterfactual comparison:
- **Observed path:** what actually happened before containment
- **Fallback path:** what would have happened under a validated backup, holding key constraints constant

**Key assumptions (state them):**
- Same capital base, same universe, same risk limits
- Same transaction cost model (or explicitly different)
- Fallback is validated for similar liquidity/market conditions
"""
        )
        toy = pd.DataFrame(
            {
                "Scenario": ["Observed (degraded model)", "Counterfactual (fallback)"],
                "Cumulative P&L over window": [-3.1, -0.8],
            }
        )
        st.table(toy)
        st.write("Toy incremental impact = (−3.1) − (−0.8) = **−2.3** (in $M units).")

    if st.button("Activate Kill Switch & Contain Incident", disabled=not st.session_state.phase_status["Contain"]):
        st.session_state.incident_data = contain_incident(
            st.session_state.incident_data)
        st.session_state.phase_status["Investigate"] = True
        st.session_state.current_page = "Investigate"
        st.rerun()

    if st.session_state.incident_data.get("phase_2_contain"):
        c = st.session_state.incident_data["phase_2_contain"]
        if c:
            st.markdown("---")
            st.markdown(
                "### Containment record (what you can defend in committee)")
            st.markdown(f"**Action:** {c.get('action', '')}")
            st.markdown(f"**Timestamp:** {c.get('timestamp', '')}")
            st.markdown(
                f"**Time to contain:** {c.get('time_to_contain', '')} (Target: < {POLICY['CONTAIN_TARGET_HOURS']} hours)")
            st.markdown(f"**Fallback strategy:** {c.get('fallback', '')}")
            st.markdown(
                f"**Estimated immediate client impact:** {c.get('estimated_client_impact', '')}")

            decision_translation(
                [
                    "If time-to-contain exceeds target, treat it as a control failure and escalate to governance.",
                    "If incremental impact is material, prepare client communication and expand exposure review beyond the model itself.",
                ]
            )

            evidence_pack_box(
                [
                    "Timestamped kill-switch confirmation",
                    "Fallback activation proof (order routing / position constraints)",
                    "Incremental loss estimate methodology + assumptions",
                ]
            )

elif st.session_state.current_page == "Investigate":
    st.markdown(
        "## Investigate: Prove the Cause (Regime Shift vs Data/Process Error)")

    st.markdown(
        """
**Goal:** separate *facts* from *interpretation* and produce evidence that can withstand skepticism.
You are trying to answer:

1) Is this a **market regime shift**?  
2) Is this a **data/process break**?  
3) Is this a **model behavior instability** (feature relationships flipped)?
"""
    )

    st.markdown("---")
    st.markdown("### Data drift diagnostic: Population Stability Index (PSI)")

    # ---- DO NOT REMOVE / ALTER FORMULA BLOCK (per user instruction) ----
    st.markdown(r"$$ \text{PSI} = \sum_{i=1}^{N} \left( (\text{Actual\_Prop}_i - \text{Expected\_Prop}_i) \times \ln\left(\frac{\text{Actual\_Prop}_i}{\text{Expected\_Prop}_i}\right) \right) $$")
    st.markdown(r"where $N$ is the number of bins, $\text{Actual\_Prop}_i$ is the proportion of observations in bin $i$ for the current population, and $\text{Expected\_Prop}_i$ is the proportion for the baseline population. A PSI of 0.42, as observed in our incident, typically signifies a major population shift.")
    # -------------------------------------------------------------------

    with st.expander("PSI interpretation bands (make the rule explicit)"):
        st.markdown(
            f"""
**Interpretation (policy/heuristic used in this lab):**
- PSI < {POLICY['PSI_STABLE_MAX']:.2f}: stable (no material drift)
- {POLICY['PSI_STABLE_MAX']:.2f}–{POLICY['PSI_WATCH_MAX']:.2f}: watch (moderate drift)
- > {POLICY['PSI_WATCH_MAX']:.2f}: **material shift** → performance is less reliable; remediation should be regime-aware
"""
        )

    st.markdown("### Simulated diagnostic findings (facts first)")
    st.write("**Fact 1 — Audit log:** Recommendations were systematically wrong-directional from Oct 15 onward.")
    st.write(
        "**Fact 2 — Drift test:** PSI = 0.42 on inputs → material population shift.")
    st.write(
        "**Fact 3 — Model behavior:** Momentum feature contribution flipped direction (sign flip).")

    with st.expander("Evidence-style summary (separating facts vs interpretation)"):
        st.markdown(
            """
**Facts**
- Wrong-direction recommendations starting Oct 15  
- PSI=0.42 indicates material distribution shift  
- Feature effect sign flip suggests instability/regime dependency  

**Interpretation (hypothesis to validate)**
- Market regime shift changed the payoff of momentum-like signals
"""
        )

    st.markdown("### Micro-table: sign flip (illustrative)")
    flip_tbl = pd.DataFrame(
        {
            "Feature": ["Momentum"],
            "Pre-incident effect (direction)": ["Positive contribution to expected return"],
            "Post-incident effect (direction)": ["Negative contribution (contrarian)"],
            "So what?": ["Signal relationship reversed → retrain/regime-aware gating needed"],
        }
    )
    st.table(flip_tbl)

    decision_translation(
        [
            "If PSI is material and feature relationships flip, assume the model’s learned relationships are not stable in the new environment.",
            "Do not redeploy purely on recent fit—require regime-aware validation to avoid ‘overfitting the last regime.’",
        ]
    )

    evidence_pack_box(
        [
            "PSI value + bands + feature contributors (top-5) [in production]",
            "Audit log excerpt showing wrong-direction calls (timestamped)",
            "Feature behavior summary (sign flip table / SHAP plot in production)",
        ]
    )

    st.markdown("---")
    checkpoint_true_false(
        question="Checkpoint: Does PSI=0.42 fall into the ‘material shift’ band under the lab’s PSI interpretation rule?",
        true_label="Yes (material shift)",
        false_label="No (normal variation)",
        correct=True,
        explanation_correct="Correct: PSI above the material threshold implies the input population meaningfully shifted.",
        explanation_incorrect="Recheck the PSI bands: 0.42 is well above the material-shift threshold.",
    )

    if st.button("Complete Investigation & Identify Root Cause", disabled=not st.session_state.phase_status["Investigate"]):
        st.session_state.incident_data = investigate_incident(
            st.session_state.incident_data)
        st.session_state.phase_status["Remediate"] = True
        st.session_state.current_page = "Remediate"
        st.rerun()

    inv = st.session_state.incident_data.get("phase_3_investigate", {})
    if inv:
        st.markdown("---")
        st.markdown("### Investigation summary (record)")
        st.markdown(f"**Root cause (stated):** {inv.get('root_cause', '')}")
        st.markdown("**Tools used:**")
        for tool in inv.get("tools_used", []):
            st.markdown(f"- {tool}")
        st.markdown(f"**Timeline:** {inv.get('timeline', '')}")
        st.markdown(f"**Why delayed:** {inv.get('why_delayed', '')}")
        st.markdown(
            f"**Quantified financial impact (carried forward):** {inv.get('client_impact', {}).get('financial_impact', '')}")

elif st.session_state.current_page == "Remediate":
    st.markdown("## Remediate: Restore Edge Without Creating a New Risk")

    st.markdown(
        """
**Goal:** convert diagnosis into controlled change, with explicit revalidation gates.
This is a governance decision, not just a modeling decision.
"""
    )

    if not st.session_state.incident_data.get("phase_4_remediate"):
        st.session_state.incident_data = remediate_incident(
            st.session_state.incident_data)

    rem = st.session_state.incident_data["phase_4_remediate"]

    st.markdown("---")
    st.markdown("### Remediation plan (grouped for clarity)")
    st.markdown("**Model adaptation**")
    for a in rem.get("actions", []):
        if "Retrain" in a or "regime" in a.lower():
            st.markdown(f"- {a}")

    st.markdown("**Monitoring redesign**")
    for a in rem.get("actions", []):
        if "window" in a.lower() or "monitor" in a.lower():
            st.markdown(f"- {a}")

    st.markdown("**Validation gates**")
    st.markdown(f"- {rem.get('revalidation', '')}")

    st.markdown(f"**Estimated timeline:** {rem.get('estimated_timeline', '')}")

    with st.expander("Watch-outs (common mistakes)"):
        st.markdown(
            """
- **Overfitting the latest regime:** a fix that looks great now may fail when conditions revert.
- **Ignoring transaction costs/turnover:** regained “edge” may vanish net of costs.
- **Weak go/no-go criteria:** redeployment should require pre-specified performance + stress pass conditions.
"""
        )

    decision_translation(
        [
            "If validation gates are ambiguous, do not restart automation—governance risk dominates.",
            "If remediation increases turnover materially, reassess net performance and liquidity constraints.",
        ]
    )

    evidence_pack_box(
        [
            "Pre-specified go/no-go criteria (metrics + stress tests)",
            "Net-of-cost performance evidence (not just gross backtest)",
            "Regime coverage summary (tests across multiple market environments)",
        ]
    )

    if st.button("Approve Remediation Plan & Proceed to Documentation", disabled=not st.session_state.phase_status["Remediate"]):
        st.session_state.phase_status["Document"] = True
        st.session_state.current_page = "Document"
        st.rerun()

elif st.session_state.current_page == "Document":
    st.markdown("## Document: Make It Audit-Ready")

    st.markdown(
        """
**Goal:** create a stand-alone narrative that a skeptical reviewer can audit.
A reader should answer in 60 seconds:
- What happened?
- What did it cost?
- Why were decisions reasonable?
- What changed to prevent recurrence?
"""
    )

    with st.expander("Required ‘no-magic-number’ checklist"):
        st.markdown(
            """
- Monitoring thresholds and window definition (RED/YELLOW + rolling window)
- Baseline vs current measurement windows (and why)
- Financial impact method + assumptions (counterfactual definition)
- Drift/diagnostic rules (PSI bands, evidence)
- Decisions, timestamps, sign-offs (who approved what)
"""
        )

    if st.button("Generate Formal Report Draft & Proceed to Prevention", disabled=not st.session_state.phase_status["Document"]):
        st.session_state.incident_data = document_incident(
            st.session_state.incident_data)
        st.session_state.phase_status["Prevent"] = True
        st.session_state.current_page = "Prevent"
        st.rerun()

    doc = st.session_state.incident_data.get("phase_5_document", {})
    if doc:
        st.markdown("---")
        st.markdown("### Draft report metadata (record)")
        st.markdown(f"**Report date (draft):** {doc.get('report_date', '')}")
        st.markdown(f"**Presented to:** {doc.get('presented_to', '')}")
        st.markdown(
            f"**Client notification status:** {doc.get('client_notification', '')}")
        st.markdown(
            f"**Regulatory notification status:** {doc.get('regulatory_notification', '')}")

        st.warning(
            "Guardrail: if you claim 'no filing required', you should also document the firm's internal materiality/escalation policy."
        )

elif st.session_state.current_page == "Prevent":
    st.markdown("## Prevent: Reduce Detection Lag and Regime Risk")

    st.markdown(
        """
**Goal:** convert lessons into durable controls with explicit trade-offs.
Tighter monitoring reduces missed detections but can increase false alarms—your thresholds should be defensible.
"""
    )

    if not st.session_state.incident_data.get("phase_6_prevent"):
        st.session_state.incident_data = prevent_recurrence(
            st.session_state.incident_data)

    prev = st.session_state.incident_data["phase_6_prevent"]

    st.markdown("---")
    st.markdown("### Proposed control enhancements (with interpretation)")
    for enh in prev.get("control_enhancements", []):
        st.markdown(f"- {enh}")

    st.markdown(f"**Governance update:** {prev.get('governance_update', '')}")

    with st.expander("Monitoring trade-off (CFA-native framing)"):
        st.markdown(
            """
Think like a risk limit:
- Too loose → detection lag → losses compound
- Too tight → false positives → unnecessary shutdowns / opportunity cost

A robust policy states the tolerated **false-alarm rate** and the tolerated **loss exposure** from delay.
"""
        )

    decision_translation(
        [
            "If rules are tightened, define acceptable false-alarm rate (Type I) vs missed-detection risk (Type II).",
            "If kill-switch is automated, specify authority, override conditions, and post-mortem requirements.",
        ]
    )

    evidence_pack_box(
        [
            "Revised monitoring policy (thresholds + window + breach logic)",
            "False-alarm/backtest of monitoring rule historically (in production)",
            "Updated validation protocol including regime coverage",
        ]
    )

    if st.button("Approve Prevention Plan & Finalize Report", disabled=not st.session_state.phase_status["Prevent"]):
        st.session_state.phase_status["Final Report"] = True
        st.session_state.current_page = "Final Report"
        st.rerun()

elif st.session_state.current_page == "Final Report":
    st.markdown("## Final Report: Board-Ready Summary + Evidence Trail")

    st.markdown(
        """
**Goal:** deliver a single coherent artifact.
Structure should separate:
- Executive summary (fast read)
- Evidence (methods + assumptions)
- Decisions + sign-offs (accountability)
"""
    )

    # Create a simple executive summary above the full report text
    inc = st.session_state.incident_data
    auc_baseline = inc["phase_1_detect"]["auc_baseline"]
    auc_current = inc["phase_1_detect"]["auc_current"]
    impact = inc.get("phase_2_contain", {}).get(
        "estimated_client_impact", "N/A")
    root = inc.get("phase_3_investigate", {}).get("root_cause", "N/A")

    st.markdown("### Executive Summary (committee-ready)")
    st.write(
        f"- Incident: {inc['incident_id']} • Model: {inc['model']} (Tier {inc.get('tier', POLICY['MODEL_TIER'])})")
    st.write(
        f"- Performance signal: AUC fell from {auc_baseline:.2f} (validated) to {auc_current:.2f} (live)")
    st.write(
        f"- Containment: kill switch + fallback activated • Estimated incremental impact: {impact}")
    st.write(f"- Root cause (stated): {root}")
    st.write(
        "- Prevention: tightened monitoring + regime-aware validation + governance update")

    st.markdown("---")
    st.markdown("### Full Incident Report (generated)")

    # Generate the report
    full_report = generate_formal_report(st.session_state.incident_data)
    st.text(full_report)

    # Add download button
    st.download_button(
        label="📥 Download Final Report",
        data=full_report,
        file_name=f"incident_report_{inc['incident_id']}.txt",
        mime="text/plain",
        help="Download the complete incident report as a text file"
    )

# -----------------------------
# License (unchanged)
# -----------------------------
st.caption(
    """
---
## QuantUniversity License

© QuantUniversity 2026  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
"""
)
