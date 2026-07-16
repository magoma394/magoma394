import os
from datetime import datetime

birthdate = datetime(2004, 9, 3)
now = datetime.now()
uptime_days = (now - birthdate).days
years = int(uptime_days // 365.2425)
months = int((uptime_days % 365.2425) // 30.436)
days = int((uptime_days % 365.2425) % 30.436)
uptime_str = f"{years} years, {months} months, {days} days"

with open('ascii-art.txt', 'r', encoding='utf-8') as f:
    ascii_lines = f.read().splitlines()

# Trim to exact bounds
min_idx = min(line.find('█') for line in ascii_lines if '█' in line)
max_idx = max(line.rfind('█') for line in ascii_lines if '█' in line)
ascii_lines = [line[min_idx:max_idx+1] for line in ascii_lines if line.strip()]

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

avatar_font_size = 7
avatar_line_height = 8
avatar_char_width = 4.2

text_font_size = 14
text_line_height = 20
text_char_width = 8.4

width = 950
height = 500

svg_content = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">',
    f'<rect width="{width}" height="{height}" fill="#0d1117" rx="15"/>',
    '<circle cx="30" cy="30" r="8" fill="#ff5f56"/>',
    '<circle cx="60" cy="30" r="8" fill="#ffbd2e"/>',
    '<circle cx="90" cy="30" r="8" fill="#27c93f"/>'
]

# Left column: Avatar (White)
svg_content.append(f'  <g font-family="Courier New, monospace" font-size="{avatar_font_size}px" fill="#ffffff" xml:space="preserve">')
y = 60
for line in ascii_lines:
    escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    svg_content.append(f'    <text x="30" y="{y}">{escaped_line}</text>')
    y += avatar_line_height
svg_content.append('  </g>')

# Right column: Text
svg_content.append(f'  <g font-family="Courier New, monospace" font-size="{text_font_size}px" fill="#c9d1d9" xml:space="preserve">')
y_start = 60 + (len(ascii_lines) * avatar_line_height - len(terminal_text_lines) * text_line_height) // 2
y = y_start
x_offset = 30 + (max_idx - min_idx + 1) * avatar_char_width + 40

for line in terminal_text_lines:
    escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    svg_content.append(f'    <text x="{x_offset}" y="{y}">{escaped_line}</text>')
    y += text_line_height
svg_content.append('  </g>')

svg_content.append('</svg>')

with open('terminal.svg', 'w', encoding='utf-8') as f:
    f.write("\n".join(svg_content))

print("Created terminal.svg")
