import os
import re
from datetime import datetime

# Calculate Uptime
birthdate = datetime(2004, 9, 3)
now = datetime.now()

# Rough calculation for years, months, days
uptime_days = (now - birthdate).days
years = int(uptime_days // 365.2425)
months = int((uptime_days % 365.2425) // 30.436)
days = int((uptime_days % 365.2425) % 30.436)

uptime_str = f"{years} years, {months} months, {days} days"

# The dynamic terminal template
terminal_text = f"""```text
         _,.-------.,_             magoma@thinkpad -------------------------------
     ,;~'             '~;,         OS: ............... Kubuntu (Linux)
   ,;                     ;,       Uptime: ........... {uptime_str}
  ;                         ;      Host: ............. Lenovo ThinkPad T495
 ,'                         ',     Role: ............. Security Engineer & Full-Stack
,;                           ;,    Education: ........ B.Sc. Artificial Intelligence
; ;      .           .      ; ;    
| ;   ______       ______   ; |    Languages.Code: ... Go, Python, JavaScript, Bash
|  `/~"     ~" . "~     "~\'  |    Languages.Human: .. Technical English
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |    
 |   |        | |        |   |     Interests.Core: ... Cybersec, Digital Forensics, UI/UX
 |   l       / | \       !   |     Interests.Tech: ... n8n, Elastic SIEM, Docker
 .~  (__,.--" .^. "--.,__)  ~.     Hobbies: .......... Football, Reading, Video Games
 |     ---;' / | \ `;---     |     
  \__.       \/^\/       .__/      Contact.Email: .... ma.gomaa394@gmail.com
   V| \                 / |V       Contact.Web: ...... magoma.me
    | |T~\___!___!___/~T| |        Contact.X: ........ @magoma394
    | |`IIII_I_I_I_IIII'| |        
    |  \,III I I I III,/  |        
     \   `~~~~~~~~~~'    /         
       \   .       .   /           
         \.    ^    ./             
           ^~~~^~~~^               
```"""

# Read the current README
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

# Replace the content between the tags
pattern = r"(<!-- START_TERMINAL -->\n).*?(\n<!-- END_TERMINAL -->)"
new_readme = re.sub(pattern, rf"\g<1>{terminal_text}\g<2>", readme_content, flags=re.DOTALL)

# Write the changes
with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_readme)