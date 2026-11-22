from datetime import datetime, timedelta, timezone
from getpass import getpass

import requests

url = "https://ulearn.utp.edu.my/webservice/rest/server.php"
token = getpass("Enter your token: ").strip()

data = {
    "wstoken": token,
    "wsfunction": "mod_assign_get_assignments",
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
            print("Fields ULearn returned:", list(result.keys()))   
        except ValueError:
            print("ULearn replied, but the reply was not valid JSON.")
        else:
            if "courses" in result:
                malaysia_time = timezone(timedelta(hours=8))
                now = datetime.now(malaysia_time)
                cutoff = now + timedelta(weeks=2)
                count = 0

                for course in result["courses"]:
                    for assignment in course["assignments"]:
                        if assignment["duedate"] > 0:
                            due = datetime.fromtimestamp(assignment["duedate"], malaysia_time)

                            if now <= due <= cutoff:
                                print(course["fullname"], "-", assignment["name"])
                                print("Due:", due.strftime("%d %b %Y at %I:%M %p"), "(Malaysia time)")
                                count += 1

                print("Assignments due within the next 2 weeks:", count)

                functions = result.get("functions", [])
                print("Number of functions:", len(functions))

                for function in functions:
                    name = function["name"]
                    if name in ("mod_assign_get_assignments", "mod_assign_get_submission_status"):
                        print("Available:", name)
            else:
                print("Moodle response:", result.get("errorcode", "Unknown response"))