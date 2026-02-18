import streamlit as st
from source import *
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="QuLab: Lab 48: Incident Response Simulation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Lab 48: Incident Response Simulation")
st.divider()

# Initialization
if 'incident_data' not in st.session_state:
    st.session_state.incident_data = initialize_incident_data()

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Overview"

if 'phase_status' not in st.session_state:
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

# Sidebar Navigation
st.sidebar.title("AI Incident Response Protocol")
pages = [
    "Overview",
    "Detect",
    "Contain",
    "Investigate",
    "Remediate",
    "Document",
    "Prevent",
    "Final Report"
]

enabled_pages = [p for p in pages if st.session_state.phase_status.get(p, False)]

# If the current_page is not in enabled_pages (e.g., if it was just completed and
# the next page is not yet enabled), ensure it's selectable to avoid errors
if st.session_state.current_page not in enabled_pages and st.session_state.current_page in pages:
    enabled_pages.append(st.session_state.current_page)
    enabled_pages = sorted(list(set(enabled_pages)), key=lambda x: pages.index(x))

selected_page = st.sidebar.selectbox(
    "Navigate Phases",
    options=enabled_pages,
    index=enabled_pages.index(st.session_state.current_page) if st.session_state.current_page in enabled_pages else 0,
    key="sidebar_navigation"
)

# Update current_page based on sidebar selection
if selected_page != st.session_state.current_page:
    st.session_state.current_page = selected_page
    st.rerun()

# Main Content Area
if st.session_state.current_page == "Overview":
    st.markdown(f"# Case Study: Navigating a Critical Performance Degradation in AI Trading")
    st.markdown(f"As a CFA Charterholder and Investment Professional, you understand the critical role of technology in modern finance, especially the growing reliance on AI-driven trading strategies. However, this reliance also brings new operational risks. This simulation will guide you through a real-world scenario where the firm's AI-powered trading agent, managing a portion of client portfolios, experiences a significant and unexpected performance degradation.")
    st.markdown(f"Your role is to act as the primary incident responder, executing a structured, six-phase protocol to detect, contain, investigate, remediate, document, and ultimately prevent recurrence of a high-stakes AI model failure. This hands-on simulation emphasizes operational resilience, swift risk mitigation, and transparent reporting—all crucial for maintaining client trust and adhering to regulatory expectations in automated trading environments.")
    st.markdown(f"---")
    st.markdown(f"### The Six Phases of AI Incident Response:")
    st.markdown(f"1.  **Detect**: Automated monitoring triggers an alert.")
    st.markdown(f"2.  **Contain**: Activate a 'kill switch' and revert to fallback.")
    st.markdown(f"3.  **Investigate**: Uncover the root cause using diagnostic tools.")
    st.markdown(f"4.  **Remediate**: Develop and execute a fix for the model.")
    st.markdown(f"5.  **Document**: Generate a formal incident report.")
    st.markdown(f"6.  **Prevent**: Enhance controls for future resilience.")

    if st.button("Start Simulation"):
        st.session_state.current_page = "Detect"
        st.rerun()

elif st.session_state.current_page == "Detect":
    st.markdown(f"## Phase 1: Detect - Initial Alert on the Monitoring Dashboard")
    st.markdown(f"As an Investment Manager, your day begins with a critical alert from the firm's AI model monitoring dashboard. The 'Trading RL Agent v1.2,' a high-tier model, has flagged a `HIGH` severity incident: its performance, measured by Area Under the Curve (AUC), has significantly dropped. This isn't just a statistical anomaly; it signals potential unexpected losses in client portfolios. Your immediate task is to acknowledge this automated alert, verify its details, and prepare for rapid action. The prompt detection of such incidents is paramount in preventing further financial harm and maintaining client trust. The AUC is a key metric for classification models, indicating their ability to distinguish between positive and negative classes (e.g., profitable vs. unprofitable trades). A drop suggests the model is no longer making reliable predictions.")
    st.markdown(f"### Incident Details:")
    st.markdown(f"**Incident ID:** {st.session_state.incident_data['incident_id']}")
    st.markdown(f"**Model:** {st.session_state.incident_data['model']}")
    st.markdown(f"**Severity:** {st.session_state.incident_data['severity']}")
    st.markdown(f"**Trigger:** {st.session_state.incident_data['phase_1_detect']['trigger']}")
    st.markdown(f"**Baseline AUC:** {st.session_state.incident_data['phase_1_detect']['auc_baseline']:.2f}")
    st.markdown(f"**Current AUC:** {st.session_state.incident_data['phase_1_detect']['auc_current']:.2f}")

    # Simulate an AUC performance graph with a red alert threshold
    auc_time_points = ['2024-10-25', '2024-10-28', '2024-10-31', '2024-11-01']
    auc_values = [0.59, 0.58, 0.55, st.session_state.incident_data['phase_1_detect']['auc_current']]
    auc_data = pd.DataFrame({'Time': pd.to_datetime(auc_time_points), 'AUC': auc_values})
    st.line_chart(auc_data.set_index('Time'), y='AUC')
    st.markdown(f"The `RED alert` threshold for this Tier 1 model is set at an AUC of 0.50. The model's current AUC of {st.session_state.incident_data['phase_1_detect']['auc_current']:.2f} is significantly below this, triggering the critical alert.")

    if st.button("Acknowledge Alert & Proceed to Containment"):
        st.session_state.phase_status["Contain"] = True 
        st.session_state.current_page = "Contain"
        st.rerun()

elif st.session_state.current_page == "Contain":
    st.markdown(f"## Phase 2: Contain - Activating the Kill Switch and Quantifying Immediate Impact")
    st.markdown(f"Upon confirming the alert, your priority as an Investment Manager is to contain the damage. This involves activating a 'kill switch' to immediately freeze the model's new trading decisions and revert to a validated, rule-based fallback strategy. This action ensures no additional client harm occurs while a full investigation is launched. Simultaneously, you must quantify the estimated immediate financial impact—the losses incurred due to the model's degradation up to the point of containment. This quantification is vital for internal reporting, potential client communication, and regulatory compliance.")
    st.markdown(f"The target for Tier 1 models like this is containment within 4 hours. The swiftness of your response directly mitigates financial exposure, which can be expressed as:")
    st.markdown(r"$$ \text{Financial Impact} = \text{Cumulative Losses before Containment} - \text{Cumulative Losses under Fallback Strategy} $$")
    st.markdown(r"where $\text{Financial Impact}$ represents the estimated additional losses due to the model's degradation, $\text{Cumulative Losses before Containment}$ are the cumulative losses incurred while the AI model was underperforming, and $\text{Cumulative Losses under Fallback Strategy}$ are the theoretical cumulative losses if a stable backup strategy had been in place during the same period.")
    st.markdown(f"This value helps the firm understand the direct financial cost of the incident.")

    if st.button("Activate Kill Switch & Contain Incident", disabled=not st.session_state.phase_status["Contain"]):
        st.session_state.incident_data = contain_incident(st.session_state.incident_data)
        st.session_state.phase_status["Investigate"] = True 
        st.session_state.current_page = "Investigate"
        st.rerun()

    if 'phase_2_contain' in st.session_state.incident_data and st.session_state.incident_data['phase_2_contain']:
        st.markdown(f"### Containment Actions Taken:")
        st.markdown(f"**Action:** {st.session_state.incident_data['phase_2_contain']['action']}")
        st.markdown(f"**Timestamp:** {st.session_state.incident_data['phase_2_contain']['timestamp']}")
        st.markdown(f"**Time to Contain:** {st.session_state.incident_data['phase_2_contain']['time_to_contain']} (Target: < 4 hours)")
        st.markdown(f"**Fallback Strategy:** {st.session_state.incident_data['phase_2_contain']['fallback']}")
        st.markdown(f"**Estimated Immediate Client Impact:** {st.session_state.incident_data['phase_2_contain']['estimated_client_impact']}")

elif st.session_state.current_page == "Investigate":
    st.markdown(f"## Phase 3: Investigate - Uncovering the Root Cause with Diagnostic Tools")
    st.markdown(f"With the incident contained, your focus shifts to understanding *why* the model failed. As an Investment Manager, you direct the data science and risk teams to utilize diagnostic tools for root cause analysis. This involves examining simulated audit logs, SHAP (SHapley Additive exPlanations) values, and data drift monitors. The goal is to pinpoint the exact cause, such as a critical market regime shift (e.g., a Fed rate cut cycle) that the model was not trained for, or a change in feature importance that indicates fundamental shifts in market dynamics. This phase informs targeted remediation.")
    st.markdown(f"A key tool here is the **Population Stability Index (PSI)**, which helps detect data drift. PSI quantifies the magnitude of distribution shifts between a baseline and a current population of data. A high PSI value indicates a significant change in the data's characteristics, suggesting that the model might be operating on data it wasn't trained for or that the underlying relationships have changed. The formula for PSI is:")
    st.markdown(r"$$ \text{PSI} = \sum_{i=1}^{N} \left( (\text{Actual\_Prop}_i - \text{Expected\_Prop}_i) \times \ln\left(\frac{\text{Actual\_Prop}_i}{\text{Expected\_Prop}_i}\right) \right) $$")
    st.markdown(r"where $N$ is the number of bins, $\text{Actual\_Prop}_i$ is the proportion of observations in bin $i$ for the current population, and $\text{Expected\_Prop}_i$ is the proportion for the baseline population. A PSI of 0.42, as observed in our incident, typically signifies a major population shift.")
    st.markdown(f"### Simulated Diagnostic Findings:")
    st.markdown(f"**Audit Log Analysis (D4-T1-C3):** Confirmed model recommendations were systematically wrong-directional from Oct 15 onward.")
    st.markdown(f"**SHAP Analysis (D4-T3-C1):** Momentum feature SHAP values flipped sign, confirming regime-dependent behavior. * (Visualization of SHAP values here would show the feature importance reversing direction.) *")
    st.markdown(f"**Distribution Shift Test (D4-T1-C1):** PSI = 0.42 on input features, confirming major population shift. * (A PSI trend chart would clearly depict this data drift.) *")

    if st.button("Complete Investigation & Identify Root Cause", disabled=not st.session_state.phase_status["Investigate"]):
        st.session_state.incident_data = investigate_incident(st.session_state.incident_data)
        st.session_state.phase_status["Remediate"] = True 
        st.session_state.current_page = "Remediate"
        st.rerun()

    if 'phase_3_investigate' in st.session_state.incident_data and st.session_state.incident_data['phase_3_investigate']:
        st.markdown(f"### Investigation Summary:")
        st.markdown(f"**Root Cause:** {st.session_state.incident_data['phase_3_investigate']['root_cause']}")
        st.markdown(f"**Tools Used:**")
        for tool in st.session_state.incident_data['phase_3_investigate']['tools_used']:
            st.markdown(f"  - {tool}")
        st.markdown(f"**Timeline:** {st.session_state.incident_data['phase_3_investigate']['timeline']}")
        st.markdown(f"**Reason for Delayed Alert:** {st.session_state.incident_data['phase_3_investigate']['why_delayed']}")
        st.markdown(f"**Quantified Financial Impact:** {st.session_state.incident_data['phase_3_investigate']['client_impact']['financial_impact']}")

elif st.session_state.current_page == "Remediate":
    st.markdown(f"## Phase 4: Remediation - Developing a Strategy to Fix the Model")
    st.markdown(f"Based on the investigation, your next step as an Investment Manager is to formulate a clear remediation plan. Since the root cause was a market regime shift that rendered the existing model ineffective, the proposed fixes involve retraining the RL agent with new, relevant market data (specifically, the 2024 rate-cut data), adding a new regime-detection layer to its logic for adaptive behavior, and adjusting the monitoring window to detect future drifts faster. This phase is about outlining concrete steps to restore the model's performance and prevent similar failures. Revalidation with stress tests is also crucial before redeployment.")

    if 'phase_4_remediate' not in st.session_state.incident_data or not st.session_state.incident_data['phase_4_remediate']:
        st.session_state.incident_data = remediate_incident(st.session_state.incident_data)

    st.markdown(f"### Proposed Remediation Plan:")
    st.markdown(f"The data science team proposes the following actions:")
    for action in st.session_state.incident_data['phase_4_remediate']['actions']:
        st.markdown(f"- {action}")
    st.markdown(f"**Revalidation Requirements:** {st.session_state.incident_data['phase_4_remediate']['revalidation']}")
    st.markdown(f"**Estimated Timeline for Fixes:** {st.session_state.incident_data['phase_4_remediate']['estimated_timeline']}")

    if st.button("Approve Remediation Plan & Proceed to Documentation", disabled=not st.session_state.phase_status["Remediate"]):
        st.session_state.phase_status["Document"] = True
        st.session_state.current_page = "Document"
        st.rerun()

elif st.session_state.current_page == "Document":
    st.markdown(f"## Phase 5: Documentation - Generating the Formal Incident Report")
    st.markdown(f"As an Investment Manager, a comprehensive and formal incident report is a critical deliverable. This report synthesizes all information gathered from the detection, containment, investigation, and remediation phases. It's presented to the AI Governance Committee, relevant stakeholders, and potentially used for client and regulatory notifications. The report ensures transparency, accountability, and serves as a vital record for audit purposes and future learning. It must clearly articulate the incident timeline, root cause, quantified financial impact, client notification details, regulatory status, and the remediation plan.")

    if st.button("Generate Formal Report Draft & Proceed to Prevention", disabled=not st.session_state.phase_status["Document"]):
        st.session_state.incident_data = document_incident(st.session_state.incident_data)
        st.session_state.phase_status["Prevent"] = True
        st.session_state.current_page = "Prevent"
        st.rerun()

    if 'phase_5_document' in st.session_state.incident_data and st.session_state.incident_data['phase_5_document']:
        st.markdown(f"### Draft Incident Report Details:")
        st.markdown(f"**Report Date (Draft):** {st.session_state.incident_data['phase_5_document']['report_date']}")
        st.markdown(f"**Presented To:** {st.session_state.incident_data['phase_5_document']['presented_to']}")
        st.markdown(f"**Client Notification Status:** {st.session_state.incident_data['phase_5_document']['client_notification']}")
        st.markdown(f"**Regulatory Notification Status:** {st.session_state.incident_data['phase_5_document']['regulatory_notification']}")

elif st.session_state.current_page == "Prevent":
    st.markdown(f"## Phase 6: Prevention - Enhancing Controls for Future Resilience")
    st.markdown(f"The final phase, and arguably the most crucial for long-term operational resilience, is prevention. As an Investment Manager, you lead the discussion on control enhancements to prevent similar incidents. This includes shortening the rolling AUC monitoring window for faster detection, adding a regime-detection trigger to the dashboard for proactive alerts, implementing mandatory regime-change stress tests, and even automating the kill-switch mechanism under specific conditions. This commitment to continuous improvement, including governance updates like re-tiering models or requiring regime-aware validation, reinforces the firm's AI governance framework and safeguards future client portfolios. This is a continuous improvement loop, feeding back into the overall AI governance lifecycle.")

    if 'phase_6_prevent' not in st.session_state.incident_data or not st.session_state.incident_data['phase_6_prevent']:
        st.session_state.incident_data = prevent_recurrence(st.session_state.incident_data)

    st.markdown(f"### Proposed Control Enhancements:")
    st.markdown(f"Based on the lessons learned, the following enhancements are proposed:")
    for enhancement in st.session_state.incident_data['phase_6_prevent']['control_enhancements']:
        st.markdown(f"- {enhancement}")
    st.markdown(f"**Proposed Governance Update:** {st.session_state.incident_data['phase_6_prevent']['governance_update']}")

    if st.button("Approve Prevention Plan & Finalize Report", disabled=not st.session_state.phase_status["Prevent"]):
        st.session_state.phase_status["Final Report"] = True
        st.session_state.current_page = "Final Report"
        st.rerun()

elif st.session_state.current_page == "Final Report":
    st.markdown(f"## Final Incident Report with Comprehensive Prevention Details")
    st.markdown(f"Now that all six phases are complete, including defining the preventive measures, it's time to generate the *final* version of the incident report. This report is a comprehensive document that chronicles the entire incident from initial detection to the proposed long-term prevention strategies. As an Investment Manager, submitting this final report signifies the completion of the incident response process and initiates the implementation of control enhancements and governance updates, closing the loop on AI model risk management. This full cycle of incident response is critical for regulatory compliance, maintaining investor confidence, and ensuring the firm's operational resilience in the face of AI failures.")
    st.markdown(f"### AI Trading Incident Report")
    st.text(generate_formal_report(st.session_state.incident_data))

# License
st.caption('''
---
## QuantUniversity License

© QuantUniversity 2026  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
''')
