import pandas as pd
import yaml

# Load configuration
with open('../configs/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Configuration variables
DATA_PATH = config['output']['data_path']
REPORT_PATH = config['output']['report_path']

# Function to validate the data
def validate_data(df):
    validation_report = []

    # Check for missing data
    for column in df.columns:
        missing_values = df[column].isnull().sum()
        if missing_values > 0:
            validation_report.append(f'{column}: {missing_values} missing values')

    # Example validation: Check if status is one of the expected values
    expected_statuses = ['To Do', 'In Progress', 'Done']
    invalid_statuses = df[~df['Status'].isin(expected_statuses)]
    if not invalid_statuses.empty:
        validation_report.append(f'Invalid status values found:\n{invalid_statuses}')

    if not validation_report:
        validation_report.append('All data is valid!')

    return validation_report

# Load data
df = pd.read_csv(DATA_PATH)

# Validate data
report = validate_data(df)
for line in report:
    print(line)

# Save the report
with open(REPORT_PATH, 'w') as f:
    for line in report:
        f.write(line + '\n')

print(f'Validation report saved to {REPORT_PATH}')