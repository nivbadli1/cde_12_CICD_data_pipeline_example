import unittest
import pandas as pd
from data_pipeline import process_data

class TestDataPipeline(unittest.TestCase):

    def test_process_data(self):
        # Create a temporary DataFrame for testing
        data = {'id': [1, 2, 3], 'value': [10, 20, 30]}
        df = pd.DataFrame(data)

        # Save DataFrame to CSV
        input_file = 'test_input_data.csv'
        df.to_csv(input_file, index=False)

        # Process the data
        output_file = 'test_output_data.csv'
        process_data(input_file, output_file)

        # Load processed data
        processed_data = pd.read_csv(output_file)

        # Check if values are doubled
        expected_data = {'id': [1, 2, 3], 'value': [20, 40, 60]}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(processed_data, expected_df)

if __name__ == '__main__':
    unittest.main()
