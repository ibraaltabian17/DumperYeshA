import subprocess, json,os


print(f"Getting Channel List")
# Define the command to run
command = ["python3", "~/epg_grabber/epg_grabber/cli.py", "--show", "visionplus_id"]

# Run the command and capture the output
result = subprocess.run(command, capture_output=True, text=True)

# Save the output to a text file
with open("channels.json", "w") as file:
    file.write(result.stdout)

# Optionally, check for errors
if result.stderr:
    print("Error:", result.stderr)

print(f"extracting channel IDs and format the output")
# Function to extract channel IDs and format the output
def process_channels(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
        channel_ids = [channel['id'] for channel in data['channels']]
    
    # Create the output structure
    output_data = {
        "configs": [
            {
                "site": "visionplus_id",
                "channels": channel_ids
            }
        ]
    }
    
    # Write the output to a file
    with open(output_file, 'w') as outfile:
        json.dump(output_data, outfile, indent=4)

# Example usage
input_file = 'channels.json'   # Replace with your input file name
output_file = 'config.json'    # Replace with your desired output file name
process_channels(input_file, output_file)

print(f"Processed data has been saved to {output_file}")

os.system('python3 ~/epg_grabber/epg_grabber/cli.py local --file config.json --output apa.xml --workers 2 --days 7')