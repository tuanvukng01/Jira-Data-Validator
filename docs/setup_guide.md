# Setup Guide: Jira Data Validation Automation

## Prerequisites
Before setting up the project, ensure that you have the following installed on your system:

- **Python 3.8+**: The core programming language for this project.
- **pip**: Python package installer.

## Step 1: Clone the Repository
Start by cloning the project repository from GitHub to your local machine:

```bash
git clone https://github.com/yourusername/jira-data-validation.git
cd jira-data-validation

```
## Step 2: Set Up a Virtual Environment (Optional but Recommended)
It is recommended to create a virtual environment to manage project dependencies. This step is optional but highly recommended to avoid conflicts with other Python projects.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Step 3: Install Dependencies
Install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

## Step 4: Configure the Project
Edit the configuration file to include your Jira API credentials and project settings:

- Open the configs/config.yaml file.
- Replace the placeholders with your actual Jira domain, email, API token, and project key.

```yaml
jira:
  domain: 'https://your-jira-domain.atlassian.net'
  email: 'your_email@example.com'
  api_token: 'your_api_token'
  project_key: 'PROJ'  # Your Jira project key
output:
  data_path: 'data/jira_issues.csv'
  report_path: 'data/validation_report.txt'
```

## Step 5: Run the Pipeline
Execute the entire data validation pipeline with a single command:

```bash
python scripts/run_pipeline.py
```
This will:
- Fetch the latest issues from Jira and save them to a CSV file.
- Validate the data and generate a validation report.

## Step 6: Review the Output
After running the pipeline, review the following files:
- **data/jira_issues.csv**: The CSV file containing the fetched Jira data.
- **data/validation_report.txt**: The validation report summarizing the results of the data checks.

## Troubleshooting
If you encounter any issues during setup or execution, consider the following:
- **Dependencies**: Ensure all required packages are installed correctly.
- **Jira API**: Double-check your Jira API credentials and ensure your account has the necessary permissions.
- **File Paths**: Verify that the file paths in the configuration file are correct and accessible.

For further assistance, refer to the [Technical Details](technical_details.md) or reach out to the project maintainers.

