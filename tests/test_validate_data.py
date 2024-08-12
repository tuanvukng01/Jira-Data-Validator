import unittest
import pandas as pd
import scripts.validate_data as validate_data

class TestValidateData(unittest.TestCase):

    def test_validate_data(self):
        # Create a sample DataFrame
        data = {
            'Key': ['PROJ-001', 'PROJ-002'],
            'Summary': ['Issue with login functionality', 'UI bug on homepage'],
            'Status': ['To Do', 'In Progress'],
            'Created': ['2024-08-01T08:23:45Z', '2024-08-03T09:30:10Z'],
            'Updated': ['2024-08-02T12:00:00Z', '2024-08-03T14:45:23Z']
        }
        df = pd.DataFrame(data)

        # Run the validation
        report = validate_data.validate_data(df)

        # Assertions
        self.assertEqual(len(report), 1)
        self.assertEqual(report[0], 'All data is valid!')

if __name__ == '__main__':
    unittest.main()