import json

def flatten_metrics(json_data):
    for key, value in json_data.items():
        # Check if the value is a dictionary and recursively flatten it
        if isinstance(value, dict):
            flatten_metrics(value)
        # If the value is a list of lists, convert it to a list of single values
        elif isinstance(value, list):
            for i in range(len(value)):
                # If the element is a list, replace it with the first element
                if isinstance(value[i], list) and len(value[i]) == 1:
                    value[i] = value[i][0]

# Function to read, flatten, and save the modified JSON file
def flatten_json_file(input_file, output_file):
    # Load the JSON data from the input file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Flatten the nested lists
    flatten_metrics(data)
    
    # Save the modified JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage:
input_file = 'combined_learning_model_results.json'  # Replace with your input file path
output_file = 'combined_learning_model_results.json'  # Replace with your desired output file path
flatten_json_file(input_file, output_file)
