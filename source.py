from datetime import datetime, timedelta

# Note: The original notebook code included imports for 'json' and 'pandas',
# but these modules are not actually used in the provided logic.
# They have been removed to minimize unnecessary dependencies.

def initialize_incident_data():
    """
    Initializes a synthetic incident object for a Trading RL Agent performance collapse.
    This object simulates the real-world alert and diagnostic information a CFA professional
    would encounter.
    """
    incident = {
        'incident_id': 'AI-INC-2024-007',
        'model': 'Trading RL Agent v1.2',
        'tier': 1,
        'severity': 'HIGH',
        'date_detected': '2024-11-01',
        'detected_by': 'Monitoring Dashboard (AUC RED alert)',
        'phase_1_detect': {
            'trigger': 'Rolling AUC dropped below 0.70 threshold',
            'auc_baseline': 0.58,
            'auc_current': 0.42,
            'alert_timestamp': '2024-11-01 06:15:00',
            'notified': ['AI Governance Officer', 'Head of Trading', 'Model Risk Management']
        },
        # Remaining phases will be populated/updated as we progress
        'phase_2_contain': {},
        'phase_3_investigate': {},
        'phase_4_remediate': {},
        'phase_5_document': {},
        'phase_6_prevent': {},
    }
    return incident

def contain_incident(incident):
    """
    Simulates the containment phase: activating a kill switch and reverting to fallback.
    Updates the incident object with containment details and estimated financial impact.
    """
    containment_timestamp = (datetime.strptime(incident['phase_1_detect']['alert_timestamp'], '%Y-%m-%d %H:%M:%S') + timedelta(hours=2, minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
    time_to_contain = "2h 15m"
    estimated_impact = "$2.3M additional losses vs backup strategy over degradation period"

    incident['phase_2_contain'] = {
        'action': 'Kill switch activated - model frozen',
        'timestamp': containment_timestamp,
        'time_to_contain': time_to_contain,
        'fallback': 'Reverted to rule-based momentum strategy (validated backup)',
        'positions_reviewed': 'All open positions from last 5 trading days reviewed by senior trader',
        'estimated_client_impact': estimated_impact,
    }
    return incident

def investigate_incident(incident):
    """
    Simulates the investigation phase using diagnostic tools.
    Updates the incident object with root cause analysis findings, SHAP insights, and PSI results.
    """
    investigation_details = {
        'root_cause': 'Market regime shift: Fed rate cut cycle began in September. RL agent trained on rate-hiking regime (2022-2024) learned patterns that reversed in the new easing cycle. Momentum signals that worked in tightening became contrarian in easing.',
        'tools_used': [
            'Audit log analysis (D4-T1-C3): confirmed model recommendations were systematically wrong-directional from Oct 15 onward',
            'SHAP analysis (D4-T3-C1): momentum feature SHAP values flipped sign, confirming regime-dependent behavior',
            'Distribution shift test (D4-T1-C1): PSI = 0.42 on input features, confirming major population shift'
        ],
        'timeline': 'Degradation began Oct 15 (rate cut announcement). Dashboard alerted Nov 1 (17 calendar days exposure).',
        'why_delayed': 'Rolling window (90-day) smoothed the AUC drop. A shorter 30-day window would have alerted 10 days earlier.',
        'client_impact': {
            'total_decisions_affected': 'N/A (performance incident, financial impact is aggregate)',
            'estimated_unfair_denials': 'N/A (performance incident)',
            'groups_affected': 'N/A (performance incident)',
            'financial_impact': incident['phase_2_contain']['estimated_client_impact'] # Re-use quantified impact
        }
    }
    incident['phase_3_investigate'] = investigation_details
    return incident

def remediate_incident(incident):
    """
    Simulates the remediation phase, proposing specific fixes based on the identified root cause.
    Updates the incident object with proposed actions, revalidation requirements, and timelines.
    """
    remediation_details = {
        'actions': [
            'Retrain RL agent including 2024 rate-cut data',
            'Add regime-detection layer: if regime indicator flips, auto-switch to conservative mode',
            'Reduce rolling AUC window from 90 to 30 days for faster detection',
            'Add regime-specific backtesting before redeployment'
        ],
        'revalidation': 'Full D4-T1-C1 stress test + D4-T1-C2 validation required before reactivation',
        'estimated_timeline': '30 days to retrain + 15 days for validation',
    }
    incident['phase_4_remediate'] = remediation_details
    return incident

def document_incident(incident):
    """
    Simulates the documentation phase by generating a formal incident report.
    Populates the incident object with report-specific metadata.
    """
    report_date = datetime.now().strftime('%Y-%m-%d')
    client_notification_details = "Affected portfolio clients notified that model-assisted trading was temporarily suspended. Performance impact disclosed in quarterly letter."
    regulatory_notification_status = "Internal documentation only (no regulatory filing required for this incident type under current rules, but logged for examination readiness)."

    incident['phase_5_document'] = {
        'report_date': report_date,
        'presented_to': 'AI Governance Committee, Head of Trading, Model Risk Management',
        'client_notification': client_notification_details,
        'regulatory_notification': regulatory_notification_status,
    }
    return incident

def prevent_recurrence(incident):
    """
    Simulates the prevention phase, proposing control enhancements and governance updates.
    Updates the incident object with these measures.
    """
    prevention_details = {
        'control_enhancements': [
            'Shorter monitoring window (90 -> 30 day rolling AUC)',
            'Regime-detection trigger added to monitoring dashboard',
            'Mandatory regime-change stress test added to validation protocol',
            'Kill-switch automation: auto-freeze if AUC < 0.50 for 3 consecutive days',
            'Quarterly review of backup strategy adequacy'
        ],
        'governance_update': 'Updated tiering: RL trading models now require regime-aware validation as standard for Tier 1 approval',
    }
    incident['phase_6_prevent'] = prevention_details
    return incident

def generate_formal_report(incident):
    """
    Generates a comprehensive formal incident report from the incident data.
    """
    report_output = []
    report_output.append("=" * 80)
    report_output.append(f"FORMAL AI MODEL INCIDENT REPORT - {incident['incident_id']}")
    report_output.append("=" * 80)
    report_output.append(f"Report Date: {incident['phase_5_document']['report_date']}")
    report_output.append(f"Presented To: {incident['phase_5_document']['presented_to']}")
    report_output.append("\n--- INCIDENT OVERVIEW ---")
    report_output.append(f"Incident ID: {incident['incident_id']}")
    report_output.append(f"Model: {incident['model']} (Tier {incident['tier']})")
    report_output.append(f"Severity: {incident['severity']}")
    report_output.append(f"Date Detected: {incident['date_detected']}")
    report_output.append(f"Detected By: {incident['detected_by']}")

    report_output.append("\n--- TIMELINE ---")
    report_output.append(f"Detected: {incident['phase_1_detect']['alert_timestamp']}")
    report_output.append(f"Contained: {incident['phase_2_contain']['timestamp']} (Time to Contain: {incident['phase_2_contain']['time_to_contain']})")
    if 'timeline' in incident['phase_3_investigate']:
        report_output.append(f"Degradation Started: {incident['phase_3_investigate']['timeline'].split('.')[0]}")
    report_output.append(f"Estimated Remediation Timeline: {incident['phase_4_remediate']['estimated_timeline']}")

    report_output.append("\n--- ROOT CAUSE ---")
    report_output.append(f"{incident['phase_3_investigate']['root_cause']}")
    report_output.append("Diagnostic Tools Used:")
    for tool in incident['phase_3_investigate']['tools_used']:
        report_output.append(f"  - {tool}")
    report_output.append(f"Reason for Delayed Alert: {incident['phase_3_investigate']['why_delayed']}")

    report_output.append("\n--- CLIENT IMPACT ---")
    report_output.append(f"Estimated Financial Impact: {incident['phase_3_investigate']['client_impact']['financial_impact']}")
    report_output.append(f"Client Notification: {incident['phase_5_document']['client_notification']}")

    report_output.append("\n--- REMEDIATION PLAN ---")
    for action in incident['phase_4_remediate']['actions']:
        report_output.append(f"  - {action}")
    report_output.append(f"Revalidation: {incident['phase_4_remediate']['revalidation']}")

    report_output.append("\n--- PREVENTIVE MEASURES (Proposed) ---")
    # This section needs to gracefully handle cases where phase_6_prevent might be empty or not yet populated
    if 'phase_6_prevent' in incident and incident['phase_6_prevent']:
        if 'control_enhancements' in incident['phase_6_prevent']:
            for enhancement in incident['phase_6_prevent']['control_enhancements']:
                report_output.append(f"  - {enhancement}")
        if 'governance_update' in incident['phase_6_prevent']:
            report_output.append(f"Governance Update: {incident['phase_6_prevent']['governance_update']}")
    else:
        report_output.append("  - No specific preventive measures documented yet.")

    report_output.append("\n--- REGULATORY STATUS ---")
    report_output.append(f"Regulatory Notification: {incident['phase_5_document']['regulatory_notification']}")

    report_output.append("\n--- SIGN-OFF ---")
    report_output.append(f"AI Governance Officer: _______________________ Date: ____________")
    report_output.append(f"CRO: ___________________________________ Date: ____________")
    report_output.append(f"CLO: ___________________________________ Date: ____________")
    report_output.append(f"Board Risk Committee Chair: _______________ Date: ____________")
    report_output.append("=" * 80)

    return "\n".join(report_output)


def simulate_incident_response():
    """
    Orchestrates the entire AI model incident response simulation.
    It calls each phase function sequentially, updates the incident object,
    and prints relevant details for each stage of the process.
    """
    current_incident = initialize_incident_data()

    # --- PHASE 1: DETECT & ALERT ---
    print(f"*** CRITICAL AI MODEL ALERT DETECTED ***")
    print(f"Incident ID: {current_incident['incident_id']}")
    print(f"Model: {current_incident['model']}")
    print(f"Severity: {current_incident['severity']}")
    print(f"Date Detected: {current_incident['date_detected']} at {current_incident['phase_1_detect']['alert_timestamp'].split(' ')[1]}")
    print(f"Trigger: {current_incident['phase_1_detect']['trigger']}")
    print(f"Baseline AUC: {current_incident['phase_1_detect']['auc_baseline']:.2f}")
    print(f"Current AUC: {current_incident['phase_1_detect']['auc_current']:.2f}")
    print(f"Notified: {', '.join(current_incident['phase_1_detect']['notified'])}")

    # --- PHASE 2: CONTAIN ---
    current_incident = contain_incident(current_incident)
    print(f"\n--- PHASE: CONTAIN ---")
    print(f"Action: {current_incident['phase_2_contain']['action']}")
    print(f"Timestamp: {current_incident['phase_2_contain']['timestamp']}")
    print(f"Time to Contain: {current_incident['phase_2_contain']['time_to_contain']} (Target: < 4 hours)")
    print(f"Fallback Strategy: {current_incident['phase_2_contain']['fallback']}")
    print(f"Estimated Client Impact: {current_incident['phase_2_contain']['estimated_client_impact']}")

    # --- PHASE 3: INVESTIGATE ---
    current_incident = investigate_incident(current_incident)
    print(f"\n--- PHASE: INVESTIGATE ---")
    print(f"Root Cause: {current_incident['phase_3_investigate']['root_cause']}")
    print(f"Tools Used:")
    for tool in current_incident['phase_3_investigate']['tools_used']:
        print(f"  - {tool}")
    print(f"Timeline: {current_incident['phase_3_investigate']['timeline']}")
    print(f"Reason for Delayed Alert: {current_incident['phase_3_investigate']['why_delayed']}")
    print(f"Quantified Financial Impact (from Investigate): {current_incident['phase_3_investigate']['client_impact']['financial_impact']}")

    # --- PHASE 4: REMEDIATE ---
    current_incident = remediate_incident(current_incident)
    print(f"\n--- PHASE: REMEDIATE ---")
    print(f"Proposed Remediation Actions:")
    for action in current_incident['phase_4_remediate']['actions']:
        print(f"  - {action}")
    print(f"Revalidation Requirements: {current_incident['phase_4_remediate']['revalidation']}")
    print(f"Estimated Timeline for Fixes: {current_incident['phase_4_remediate']['estimated_timeline']} (Target: < 30 days)")

    # --- PHASE 5: DOCUMENT ---
    current_incident = document_incident(current_incident)
    print(f"\n\nGenerating INITIAL Incident Report (before prevention phase):")
    # Generates a report reflecting phases 1-5, phase 6 will be empty
    print(generate_formal_report(current_incident))

    # --- PHASE 6: PREVENT ---
    current_incident = prevent_recurrence(current_incident)
    print(f"\n--- PHASE: PREVENT ---")
    print(f"Proposed Control Enhancements:")
    for enhancement in current_incident['phase_6_prevent']['control_enhancements']:
        print(f"  - {enhancement}")
    print(f"Governance Update: {current_incident['phase_6_prevent']['governance_update']}")

    # --- FINAL REPORT ---
    print(f"\n\nGenerating FINAL Incident Report with all phases completed:")
    # Generates a final report including all phases, including prevention measures
    print(generate_formal_report(current_incident))

    return current_incident # Return the final incident object

if __name__ == "__main__":
    # This block ensures that the simulation runs when the file is executed directly.
    # When this file is imported into another script (e.g., app.py), this block will not execute,
    # allowing the functions to be called individually or via simulate_incident_response() as needed.
    final_incident_status = simulate_incident_response()
    print("\nIncident response simulation completed.")
