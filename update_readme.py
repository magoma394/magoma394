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
            ascii_art = f.read().strip('\n') # keep spaces, remove empty newlines at ends
    except FileNotFoundError:
        print("Error: ascii-art.txt not found. Please ensure it exists in the same directory.")
        return
    
    # Create the injected HTML
    terminal_text = f"""<!-- START_TERMINAL -->
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border: none; width: 100%; max-width: 950px;">
<tr style="border: none;">
<!-- Left Column: Solid Block Hacker Avatar -->
<td align="left" valign="top" style="border: none; padding-right: 15px; font-family: monospace; font-size: 6.5px; line-height: 1.05; letter-spacing: 0.5px; white-space: pre; color: #00d4ff;">
{ascii_art}
</td>
<!-- Right Column: System Specs -->
<td align="left" valign="middle" style="border: none; padding-left: 15px;">

```text
magoma@thinkpad -------------------------------
OS: ............... Kubuntu (Linux)
Uptime: ........... {uptime_str}
Host: ............. Lenovo ThinkPad T495
Role: ............. Security Engineer & Full-Stack
Education: ........ B.Sc. Artificial Intelligence

Languages.Code: ... Go, Python, JavaScript, Bash
Languages.Human: .. Technical English

Interests.Core: ... Cybersec, Digital Forensics, UI/UX
Interests.Tech: ... n8n, Elastic SIEM, Docker
Hobbies: .......... Football, Reading, Video Games

Contact.Email: .... ma.gomaa394@gmail.com
Contact.Web: ...... magoma.me
Contact.X: ........ @magoma394
```
</td>
</tr>
</table>
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
