import requests
from bs4 import BeautifulSoup

def print_google_doc_grid(url):
    # 1. Fetch the HTML content of the public Google Doc
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # 2. Parse the HTML table structure
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if not table:
        print("Could not find a table in the document.")
        return

    rows = table.find_all('tr')
    
    # Storage for parsed grid data
    grid_data = {}
    max_x = 0
    max_y = 0

    # 3. Iterate through rows (skipping the header row)
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            # Extract plain text and strip out potential formatting spaces
            x_text = cols[0].get_text().strip()
            char = cols[1].get_text() # Character could be a space, so keep exact string
            y_text = cols[2].get_text().strip()
            
            # Basic validation to ensure coordinates are valid integers
            try:
                x = int(x_text)
                y = int(y_text)
                
                # Store the character mapped to its coordinate tuple
                grid_data[(x, y)] = char
                
                # Keep track of the maximum dimensions of our grid
                if x > max_x: max_x = x
                if y > max_y: max_y = y
            except ValueError:
                # Skip rows that don't have valid numerical coordinates
                continue

    # Note on orientation: In standard screen graphics / typography systems, 
    # y=0 is often treated as the TOP row. If you run this and notice the characters
    # are upside down, change the range loop to: reversed(range(max_y + 1))
    
    # 4. Print the grid row by row (from y = 0 up to max_y)
    for y in range(max_y + 1):
        row_string = ""
        for x in range(max_x + 1):
            # Fetch character if it exists, otherwise fall back to a space
            row_string += grid_data.get((x, y), " ")
        print(row_string)

# Example usage:
##url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
print_google_doc_grid(url)