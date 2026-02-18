# QuLab: Lab 48: AI Incident Response Simulation

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

This project, **"QuLab: Lab 48: Incident Response Simulation"**, is a Streamlit-based interactive lab designed to simulate a critical AI incident response scenario within an investment firm. Participants, acting as CFA Charterholders and Investment Professionals, are guided through a structured, six-phase protocol to manage a significant performance degradation in an AI-powered trading agent.

The simulation emphasizes operational resilience, swift risk mitigation, transparent reporting, and adherence to regulatory expectations in automated trading environments. It highlights the critical steps involved in detecting, containing, investigating, remediating, documenting, and preventing the recurrence of high-stakes AI model failures. This hands-on experience is crucial for understanding the practical challenges and best practices in AI governance and risk management in finance.

## Features

This Streamlit application provides a rich, interactive learning experience through the following key features:

*   **Six-Phase Incident Response Protocol**: Guides users through the industry-standard incident response lifecycle:
    1.  **Detect**: Initial alert and identification of an AI model performance issue.
    2.  **Contain**: Activating emergency measures (e.g., kill switch) to stop further damage.
    3.  **Investigate**: Root cause analysis using simulated diagnostic tools.
    4.  **Remediate**: Developing and executing a fix for the underlying problem.
    5.  **Document**: Generating a formal incident report for stakeholders and compliance.
    6.  **Prevent**: Implementing long-term controls and governance updates to prevent recurrence.
*   **Interactive Navigation**: A dynamic sidebar allows users to navigate through the incident response phases, with subsequent phases unlocking only after the current one is completed.
*   **Simulated Incident Details**: Presents realistic incident information including ID, affected model, severity, and key performance indicators like Area Under the Curve (AUC).
*   **Performance Visualization**: Includes a simulated line chart illustrating the AI model's performance degradation, highlighting critical thresholds.
*   **Quantified Impact Analysis**: Demonstrates how to quantify immediate financial impact and understand losses incurred due to model degradation.
*   **Diagnostic Tools Simulation**: Introduces concepts like Audit Log Analysis, SHAP (SHapley Additive exPlanations) values for feature importance, and Population Stability Index (PSI) for data drift detection, including their mathematical formulas:
    *   **Financial Impact Calculation**:
        $$ \text{Financial Impact} = \text{Cumulative Losses before Containment} - \text{Cumulative Losses under Fallback Strategy} $$
    *   **Population Stability Index (PSI)**:
        $$ \text{PSI} = \sum_{i=1}^{N} \left( (\text{Actual\_Prop}_i - \text{Expected\_Prop}_i) \times \ln\left(\frac{\text{Actual\_Prop}_i}{\text{Expected\_Prop}_i}\right) \right) $$
*   **Detailed Reporting**: Generates a comprehensive final incident report summarizing all phases, including root cause, financial impact, client/regulatory notifications, and prevention strategies.
*   **Role-Playing Experience**: Immerses the user in the role of an Investment Manager, making critical decisions throughout the incident.

## Getting Started

Follow these instructions to set up and run the Streamlit application on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository** (or download the project files):
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```
    *(If not using Git, just ensure `app.py` and `source.py` are in the same directory.)*

2.  **Install the required Python packages**:
    ```bash
    pip install streamlit pandas
    ```

3.  **Ensure `source.py` exists**: The application relies on a `source.py` file containing the backend logic for incident data initialization and phase progression functions. Make sure this file is present in the same directory as `app.py`.
    *(Assumed functions in `source.py`: `initialize_incident_data`, `contain_incident`, `investigate_incident`, `remediate_incident`, `document_incident`, `prevent_recurrence`, `generate_formal_report`)*

## Usage

To run the Streamlit application:

1.  Navigate to the project directory in your terminal.
2.  Execute the Streamlit command:
    ```bash
    streamlit run app.py
    ```
3.  Your web browser will automatically open to the application's local URL (usually `http://localhost:8501`).

**How to use the application:**

*   Start on the "Overview" page to understand the simulation's premise.
*   Click "Start Simulation" to begin the "Detect" phase.
*   Follow the instructions on each page, acknowledging alerts or performing actions as prompted by buttons.
*   Use the "Navigate Phases" dropdown in the sidebar to move between completed or currently active phases. New phases will unlock dynamically as you progress.
*   Complete all six phases to generate the final incident report.

## Project Structure

The project is structured with a clear separation of UI logic and backend simulation logic:

```
.
├── app.py                  # Main Streamlit application script, handles UI and state.
└── source.py               # Backend logic for incident data management and phase functions.
```

*   **`app.py`**:
    *   Sets up the Streamlit page configuration, title, and sidebar.
    *   Initializes `st.session_state` variables for incident data and phase status.
    *   Manages sidebar navigation and page routing.
    *   Renders the content for each phase of the incident response simulation.
    *   Calls functions from `source.py` to update incident data.
*   **`source.py`** (Assumed contents):
    *   `initialize_incident_data()`: Creates a dictionary to store all incident-related information.
    *   `contain_incident(data)`: Updates incident data with containment details.
    *   `investigate_incident(data)`: Updates incident data with investigation findings and root cause.
    *   `remediate_incident(data)`: Populates the remediation plan.
    *   `document_incident(data)`: Adds documentation specifics to the incident data.
    *   `prevent_recurrence(data)`: Details control enhancements and governance updates.
    *   `generate_formal_report(data)`: Compiles all incident data into a final report string.

## Technology Stack

*   **Streamlit**: For rapidly building the interactive web application and user interface.
*   **Python 3.x**: The core programming language.
*   **Pandas**: Used for data manipulation, particularly for creating the AUC line chart data.
*   **datetime**: For handling timestamps and durations within the simulation.

## Contributing

This project is primarily a lab exercise. However, if you have suggestions for improvements or find issues, feel free to:

1.  **Fork the repository**.
2.  **Create a new branch** (`git checkout -b feature/AmazingFeature`).
3.  **Make your changes**.
4.  **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
5.  **Push to the branch** (`git push origin feature/AmazingFeature`).
6.  **Open a Pull Request**.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (if applicable, otherwise state as "For educational use within QuantUniversity QuLabs").

*(If no specific LICENSE file exists, you can state: "This project is provided for educational purposes within QuantUniversity's QuLabs. All rights reserved by QuantUniversity.")*

## Contact

For questions, feedback, or further information regarding this QuLab project:

*   **QuantUniversity:** [www.quantuniversity.com](https://www.quantuniversity.com/)
*   **Contact Email:** [info@quantuniversity.com](mailto:info@quantuniversity.com)
*   **Project Lead (Example):** Dr. S. Mugunthan (mugunthan@quantuniversity.com)
