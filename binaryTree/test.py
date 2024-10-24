import requests

def parse_google_doc_data(url):
    # Assuming that the Google Doc provides the text in a raw, shareable format
    response = requests.get(url)
    
    if response.status_code == 200:
        # The document's content is assumed to be simple text with x-coordinates, y-coordinates, and characters
        data = response.text
        return data
    else:
        raise Exception("Failed to retrieve document")

def decode_secret_message(url):
    data = parse_google_doc_data(url)

    # Split the document into lines
    lines = data.splitlines()

    # Initialize an empty list to store coordinates and characters
    grid_data = []
    
    max_x = 0
    max_y = 0
    
    # Parse each line assuming a format of "x-coordinate, character, y-coordinate"
    for line in lines:
        parts = line.split()
        if len(parts) == 3:
            x = int(parts[0])
            char = parts[1]
            y = int(parts[2])
            
            # Keep track of the max x and y to define grid size
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            
            # Append the parsed data to grid_data
            grid_data.append((x, char, y))

    # Create an empty 2D grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Place the characters into the grid based on their coordinates
    for x, char, y in grid_data:
        grid[y][x] = char

    # Prepare the output
    result = []
    for row in grid:
        result.append(''.join(row))
    return result

# Using the provided Google Doc URL
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hy2sP0ntssyFdubmMQm8IwJwfyw6NPjimlRYs_FOYXtqrYqjhb85jBUebk9swPXh_a5TJ5KI/pub"

# Run the function and capture the output
output = decode_secret_message(google_doc_url)
output
