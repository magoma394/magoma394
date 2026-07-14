import os
import re
from datetime import datetime

def main():
    # Calculate Uptime
    birthdate = datetime(2004, 9, 3)
    now = datetime.now()
    
    uptime_days = (now - birthdate).days
    years = int(uptime_days // 365.2425)
    months = int((uptime_days % 365.2425) // 30.436)
    days = int((uptime_days % 365.2425) % 30.436)
    
    uptime_str = f"{years} years, {months} months, {days} days"
    
    # Read ASCII Art
    try:
        with open('ascii-art.txt', 'r', encoding='utf-8') as f:
            ascii_lines = f.read().splitlines()
    except FileNotFoundError:
        print("Error: ascii-art.txt not found. Please ensure it exists in the same directory.")
        return
        
    # Trim common leading whitespace to save horizontal space
    min_spaces = min(len(line) - len(line.lstrip()) for line in ascii_lines if line.strip())
    ascii_lines = [line[min_spaces:] for line in ascii_lines]
    
    # Pad all lines to max width so we can append text cleanly
    max_width = max(len(line) for line in ascii_lines)
    ascii_lines = [line.ljust(max_width) for line in ascii_lines]
    
    terminal_text_lines = [
        "magoma@thinkpad -------------------------------",
        "OS: ............... Kubuntu (Linux)",
        f"Uptime: ........... {uptime_str}",
        "Host: ............. Lenovo ThinkPad T495",
        "Role: ............. Security Engineer & Full-Stack",
        "Education: ........ B.Sc. Artificial Intelligence",
        "",
        "Languages.Code: ... Go, Python, JavaScript, Bash",
        "Languages.Human: .. Technical English",
        "",
        "Interests.Core: ... Cybersec, Digital Forensics, UI/UX",
        "Interests.Tech: ... n8n, Elastic SIEM, Docker",
        "Hobbies: .......... Football, Reading, Video Games",
        "",
        "Contact.Email: .... ma.gomaa394@gmail.com",
        "Contact.Web: ...... magoma.me",
        "Contact.X: ........ @magoma394"
    ]
    
    # Vertically center the text block next to the ASCII art
    start_line = (len(ascii_lines) - len(terminal_text_lines)) // 2
    
    # Append the text to the right side of the ASCII art with 6 spaces padding
    for i, text in enumerate(terminal_text_lines):
        ascii_lines[start_line + i] += "      " + text
        
    combined_terminal = "\n".join(ascii_lines)
    
    # Create the injected markdown
    terminal_text = f"""<!-- START_TERMINAL -->
```text
{combined_terminal}
```
<!-- END_TERMINAL -->"""

    # Update README.md
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found.")
        return

    # Regex to replace content between START_TERMINAL and END_TERMINAL
    pattern = re.compile(r"<!-- START_TERMINAL -->.*?<!-- END_TERMINAL -->", re.DOTALL)
    
    if not pattern.search(readme_content):
        print("Error: Could not find START_TERMINAL and END_TERMINAL tags in README.md")
        return

    new_readme_content = pattern.sub(terminal_text, readme_content)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
        
    print("README.md successfully updated!")

if __name__ == "__main__":
    main()
