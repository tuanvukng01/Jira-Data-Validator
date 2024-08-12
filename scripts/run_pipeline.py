import fetch_jira_issues
import validate_data


def run_pipeline():
    print("Starting Jira Data Fetch and Validation Pipeline")

    # Fetch data
    print("Fetching Jira issues...")
    fetch_jira_issues.main()

    # Validate data
    print("Validating fetched data...")
    validate_data.main()

    print("Pipeline completed successfully!")


if __name__ == '__main__':
    run_pipeline()