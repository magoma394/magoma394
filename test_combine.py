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

min_spaces = min(len(line) - len(line.lstrip()) for line in ascii_lines if line.strip())
ascii_lines = [line[min_spaces:] for line in ascii_lines]
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

start_line = (len(ascii_lines) - len(terminal_text_lines)) // 2

for i, text in enumerate(terminal_text_lines):
    ascii_lines[start_line + i] += "      " + text

print("\n".join(ascii_lines))
