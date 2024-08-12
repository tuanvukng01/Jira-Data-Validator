# Technical Details: Jira Data Validation Automation

## Project Architecture
The project is structured into several key components, each handling a specific aspect of the data validation pipeline:

1. **Data Extraction (`fetch_jira_issues.py`)**
   - This script interacts with the Jira API using an HTTP request to fetch issues based on a JQL query.
   - The data is processed and stored in a CSV file for subsequent validation.

2. **Data Validation (`validate_data.py`)**
   - This script loads the CSV file containing Jira data and performs various validation checks.
   - The checks include:
     - **Missing Data**: Identifies any missing values in critical fields.
     - **Status Validation**: Ensures that all issue statuses match expected values (e.g., "To Do", "In Progress", "Done").
   - The results are compiled into a validation report.

3. **Pipeline Execution (`run_pipeline.py`)**
   - This script serves as the main entry point, orchestrating the data extraction and validation processes.
   - It ensures that all components are executed in sequence, making it easy to run the entire workflow with a single command.

## Code Breakdown
### `fetch_jira_issues.py`
- **Configuration Management**: 
  - Utilizes `yaml` to load Jira API credentials and project settings from a configuration file.
- **Data Fetching**:
  - Sends a GET request to Jira's REST API endpoint.
  - Parses the JSON response and extracts relevant fields into a pandas DataFrame.
- **Output**:
  - Saves the DataFrame as a CSV file for further analysis.

### `validate_data.py`
- **Data Loading**:
  - Reads the CSV file into a pandas DataFrame.
- **Validation Checks**:
  - Iterates through each column, identifying any missing data.
  - Compares issue statuses against a predefined list of acceptable values.
- **Reporting**:
  - Generates a text-based validation report summarizing the findings.

### `run_pipeline.py`
- **Integration**:
  - Combines the functionality of `fetch_jira_issues.py` and `validate_data.py`.
  - Provides a unified interface for running the entire data validation pipeline.

## Design Decisions
- **YAML Configuration**: Chosen for its simplicity and readability, YAML is used to manage configuration settings separately from the codebase, allowing for easy adjustments without modifying the scripts.
- **Pandas DataFrame**: Leveraged for its powerful data manipulation capabilities, making it easy to perform complex validation checks efficiently.
- **Modular Structure**: The project is designed with modularity in mind, enabling easy expansion or modification of individual components without affecting the overall system.

## Potential Enhancements
- **Automated Scheduling**: Integrate with a task scheduler (e.g., cron, Windows Task Scheduler) to automate the pipeline execution at regular intervals.
- **Error Handling**: Improve the robustness of the scripts by adding more detailed error handling and logging.
- **Extended Validation**: Expand the validation logic to include additional checks, such as verifying data relationships or performing cross-references with other data sources.