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
        
    # Trim common leading whitespace to save space
    min_spaces = min(len(line) - len(line.lstrip()) for line in ascii_lines if line.strip())
    ascii_lines = [line[min_spaces:] for line in ascii_lines]
    
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
    
    # Generate SVG Content
    char_width = 8.4
    line_height = 18
    font_size = 14
    
    width = 1350
    height = 1040
    
    svg_content = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">',
        f'<rect width="{width}" height="{height}" fill="#0d1117" rx="15"/>',
        '<circle cx="30" cy="30" r="8" fill="#ff5f56"/>',
        '<circle cx="60" cy="30" r="8" fill="#ffbd2e"/>',
        '<circle cx="90" cy="30" r="8" fill="#27c93f"/>',
        f'<g font-family="Courier New, monospace" font-size="{font_size}px" xml:space="preserve">'
    ]
    
    # Left column: ASCII
    svg_content.append('  <g fill="#00d4ff">')
    y = 70
    for line in ascii_lines:
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        svg_content.append(f'    <text x="30" y="{y}">{escaped_line}</text>')
        y += line_height
    svg_content.append('  </g>')
    
    # Right column: Text
    svg_content.append('  <g fill="#c9d1d9">')
    y_start = 70 + (len(ascii_lines) - len(terminal_text_lines)) // 2 * line_height
    y = y_start
    max_ascii_len = max(len(l) for l in ascii_lines)
    x_offset = 30 + max_ascii_len * char_width + 40
    
    for line in terminal_text_lines:
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        svg_content.append(f'    <text x="{x_offset}" y="{y}">{escaped_line}</text>')
        y += line_height
    svg_content.append('  </g>')
    
    svg_content.append('</g>')
    svg_content.append('</svg>')
    
    # Write SVG
    with open('terminal.svg', 'w', encoding='utf-8') as f:
        f.write("\\n".join(svg_content))
    print("Created terminal.svg successfully!")
    
    # Create the injected markdown referencing the SVG
    terminal_text = f"""<!-- START_TERMINAL -->
<div align="center">
  <img src="./terminal.svg" width="100%" alt="Dynamic Terminal Profile" />
</div>
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
