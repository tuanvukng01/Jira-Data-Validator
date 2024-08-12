import unittest
from unittest.mock import patch, Mock
import scripts.fetch_jira_issues as fetch_jira_issues

class TestFetchJiraIssues(unittest.TestCase):

    @patch('fetch_jira_issues.requests.get')
    def test_fetch_jira_issues(self, mock_get):
        # Mocking the API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'issues': [
                {
                    'key': 'PROJ-001',
                    'fields': {
                        'summary': 'Issue with login functionality',
                        'status': {'name': 'To Do'},
                        'created': '2024-08-01T08:23:45Z',
                        'updated': '2024-08-02T12:00:00Z'
                    }
                }
            ]
        }
        mock_get.return_value = mock_response

        # Call the function
        issues = fetch_jira_issues.fetch_jira_issues('project = PROJ')

        # Assertions
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]['key'], 'PROJ-001')
        self.assertEqual(issues[0]['fields']['summary'], 'Issue with login functionality')
        self.assertEqual(issues[0]['fields']['status']['name'], 'To Do')

if __name__ == '__main__':
    unittest.main()