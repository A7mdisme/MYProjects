print("Running this file:", __file__)
from getpass import getpass

import requests

url = "https://ulearn.utp.edu.my/webservice/rest/server.php"
token = getpass("Enter your token: ").strip()

data = {
    "wstoken": token,
    "wsfunction": "core_webservice_get_site_info",
    "moodlewsrestformat": "json",
}

try:
        response = requests.post(url, data=data, timeout=15, allow_redirects=False)
except requests.RequestException:
        print("Could not reach ULearn. Check your connection and try again.")
else:
    if response.status_code != 200:
        print("ULearn returned HTTP status", response.status_code)
    else:
        try:
            result = response.json()
        except ValueError:
            print("ULearn replied, but the reply was not valid JSON.")
        else:
            if "fullname" in result:
                print("Connected to ULearn as", result["fullname"])

                functions = result.get("functions", [])
                print("Number of functions:", len(functions))

                for function in functions:
                    name = function["name"]
                    if name in ("mod_assign_get_assignments", "mod_assign_get_submission_status"):
                        print("Available:", name)
            else:
                print("Moodle response:", result.get("errorcode", "Unknown response"))