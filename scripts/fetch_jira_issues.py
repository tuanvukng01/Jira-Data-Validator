import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
import yaml

# Load configuration
with open('../configs/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Configuration variables
JIRA_DOMAIN = config['jira']['domain']
API_TOKEN = config['jira']['api_token']
EMAIL = config['jira']['email']
PROJECT_KEY = config['jira']['project_key']
OUTPUT_PATH = config['output']['data_path']


# Function to fetch issues from Jira
def fetch_jira_issues(jql_query):
    url = f'{JIRA_DOMAIN}/rest/api/2/search'
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    headers = {
        'Accept': 'application/json'
    }
    params = {
        'jql': jql_query,
        'maxResults': 1000,
    }

    response = requests.get(url, headers=headers, params=params, auth=auth)

    if response.status_code == 200:
        return response.json()['issues']
    else:
        raise Exception(f'Failed to fetch Jira issues: {response.status_code} {response.text}')


# Example JQL query
jql_query = f'project = {PROJECT_KEY} ORDER BY created DESC'

# Fetch issues
issues = fetch_jira_issues(jql_query)

# Convert to DataFrame
data = []
for issue in issues:
    data.append({
        'Key': issue['key'],
        'Summary': issue['fields']['summary'],
        'Status': issue['fields']['status']['name'],
        'Created': issue['fields']['created'],
        'Updated': issue['fields']['updated']
    })

df = pd.DataFrame(data)
df.to_csv(OUTPUT_PATH, index=False)
print(f'Data successfully fetched and saved to {OUTPUT_PATH}')