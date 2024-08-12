# Jira Data Validation Automation

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## Overview
This project automates the process of validating data extracted from Jira. It aims to ensure data consistency and accuracy within project management workflows, reducing the need for manual data checks.

## Features
- **Data Extraction**: Fetches issues from Jira using specific JQL queries.
- **Data Validation**: Checks the data for missing values, ensures status fields match expected values, and generates a validation report.
- **Pipeline Automation**: Runs the entire process through a single script for ease of use.
- **Exploratory Analysis**: Provides a Jupyter notebook for visualizing and analyzing the data.

## Project Structure
```plaintext
/project-root
├── /configs          # Configuration files
├── /data             # Example data and generated reports
├── /docs             # Documentation files
├── /notebooks        # Jupyter notebooks for data analysis
├── /scripts          # Core Python scripts
├── /tests            # Unit tests for the scripts
├── README.md         # Project overview and instructions
├── requirements.txt  # Python dependencies
└── .gitignore        # Files and directories to ignore in git

```
## Installation

### Prerequisites
- **Python 3.8+**: The core programming language for this project.
- **pip**: Python package installer.

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/jira-data-validation.git
cd jira-data-validation
```

2. Set up a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the project:
- Edit the configs/config.yaml file to include your Jira API credentials and project settings.

5. Run the pipeline:
```bash
python scripts/run_pipeline.py
```

## Usage
- **Data Extraction**: Extracts data from Jira and saves it as a CSV file.
- **Data Validation**: Validates the extracted data and generates a validation report.
- **Exploratory Analysis**: Use the Jupyter notebook in the notebooks directory to explore and visualize the data.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.