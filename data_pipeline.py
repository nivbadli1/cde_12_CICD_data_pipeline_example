import pandas as pd

def process_data(input_file, output_file):
    # Load data from CSV
    data = pd.read_csv(input_file)

    # Perform data transformations (for example, doubling the values in a 'value' column)
    data['value'] = data['value'] * 2
    
    # Introduce a mistake: Add values instead of doubling them
    # data['value'] = data['value'] + 2  # This line is incorrect
    
    # Export processed data to a new CSV
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "output_data.csv"
    process_data(input_file, output_file)
    # dummy change
