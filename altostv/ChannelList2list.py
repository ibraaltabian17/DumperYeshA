import json

# Function to extract channel IDs and format the output
def process_channels(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
        channel_entries = [
            f"visionplus;{channel['display_name']['#text'].replace(' ', '')}.Id" for channel in data['channels']
        ]
    
    # Write the output to a file
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(channel_entries))

# Example usage
input_file = 'input.json'   # Replace with your input file name
output_file = 'output.txt'    # Replace with your desired output file name
process_channels(input_file, output_file)

print(f"Processed data has been saved to {output_file}")
