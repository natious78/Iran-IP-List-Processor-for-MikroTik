import requests

# URL of the .rsc file
url = "https://raw.githubusercontent.com/MrAriaNet/Get-IP-Iran/main/list.rsc"

# Output file path
output_file = "iran_ip_list.txt"

def process_rsc_content(content):
    lines = content.strip().splitlines()

    # Skip the first two lines
    processed_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith(":do { add address=") and "list=" in line:
            # Extract address
            try:
                address_part = line.split("add address=")[1].split(" list=")[0].strip()
                processed_line = f"add address={address_part} list=Iran"
                processed_lines.append(processed_line)
            except IndexError:
                continue  # Skip malformed lines
    return processed_lines

def main():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request failed

        processed_lines = process_rsc_content(response.text)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("/ip firewall address-list\n")
            for line in processed_lines:
                f.write(line + "\n")

        print(f"Processed {len(processed_lines)} lines and saved to {output_file}")

    except requests.RequestException as e:
        print(f"Failed to fetch the file: {e}")

if __name__ == "__main__":
    main()
