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

# The dynamic terminal template with the new solid block ASCII art side-by-side
terminal_text = f"""<div align="center">
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border: none; width: 100%; max-width: 950px;">
<tr style="border: none;">
<!-- Left Column: Solid Block Hacker Avatar -->
<td align="left" valign="top" style="border: none; padding-right: 15px; font-family: monospace; font-size: 6.5px; line-height: 1.05; letter-spacing: 0.5px; white-space: pre; color: #00d4ff;">
                                       ██████████████████████
                                  ██████████████    ██████████████
                              ████████                        ████████
                          ███████                                  ███████
                        █████                                          █████
                     █████                   ██████████                   █████
                   █████                  ████████████████                  █████
                 █████                 █████████████████████                  █████
                ████                 ██████████████████████████                 ████
              ████                 █████████████████████████████                  ████
             ████                 ████████████████████████████████                 ████
            ███                 ███████████████████████████████████                  ███
          ████                 ███████████████        ███████████████                 ███
         ████                 ████████████                ████████████                 ███
         ███                 ██████████                      ██████████                 ███
        ███                 █████████                          █████████                 ███
       ███                 ████████                              ████████                 ███
      ████                ███████                                  ██████                 ███
      ███                 ██████    ███████████      ██████████     ██████                 ███
     ███                 ██████    █████████████████████████████     ██████                ███
     ███                ██████                                        █████                 ███
     ███                █████                                          █████                ███
    ███                 █████     █                              █     █████                ███
    ███                 ████      ██           ██████           ██     █████                 ███
    ███                 ████      █████    █████    █████    █████     █████                 ███
    ███                 ████      ████████████  ███   ████████████     █████                 ███
    ███                 █████     ███████████  ██████  ██████████      █████                 ███
    ███                  █████     ███████████   ██  ████████████     █████                  ███
    ███                  ██████     ████████████    ████████████     █████                   ███
    ███                   ██████     ██████████████████████████     █████                   ███
     ███                    █████     ███████████████████████      █████                    ███
     ███                     ██████     ███████████████████      ██████                     ███
     ████               ███    ██████     ████████████████     █████     ██                ███
      ███             ███████     █████     ████████████    ██████     ██████              ███
       ███           ██████████     ██████    ████████    █████     ███████████           ███
       ████        ███████████████     █████    ████    █████     ███████████████        ███
        ███       ███████████████████   █████    ██   ██████   ███████████████████      ████
         ███     █████████████████████  ███ ███      ███ ███  █████████████████████    ████
          ███   ██████████████████████  ███   ██    @@   ███  █████████████████████   ████
           ████  █████████████████████  ███    ██ ██     ███  █████████████████████  ████
            ████  ████████████████████  ███     ████     ███  ███████████████████   ████
              ███   ██████████████████  ███     ████     ███  ██████████████████  ██??
               ████   ████████████████  ███     ████     ███  ████████████████   ████
                 ████   ██████████████  ███     ████     ███  ██████████████   ████
                  █████   ████████████  ███     ████    ████  ████████████   ████
                    █████    █████████  ███     ████     ███  █████████   █████
                       █████    ██████          ████          ██████    █████
                         ███████    ██          ████          ██    ██████
                            ████████             ██             ███████
                                ███████████              ███████████
                                     █████████████████████████
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
