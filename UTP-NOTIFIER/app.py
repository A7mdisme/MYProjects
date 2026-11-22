from datetime import datetime, timedelta, timezone

import requests
import streamlit as st


def call_ulearn(token, function_name):
    url = "https://ulearn.utp.edu.my/webservice/rest/server.php"

    data = {
        "wstoken": token,
        "wsfunction": function_name,
        "moodlewsrestformat": "json",
    }

    response = requests.post(url, data=data, timeout=15, allow_redirects=False)

    if response.status_code != 200:
        raise ValueError(f"ULearn returned HTTP status {response.status_code}.")

    result = response.json()

    if "errorcode" in result:
        raise ValueError(f"ULearn returned an error: {result['errorcode']}")

    return result


st.title("Assignments Due")
st.caption("Next 2 weeks · Malaysia time")

with st.form("ulearn_login"):
    token = st.text_input("ULearn token", type="password").strip()
    show_assignments = st.form_submit_button("Show assignments")

if not show_assignments:
    st.stop()

if not token:
    st.warning("Enter your ULearn token first.")
    st.stop()

try:
    account = call_ulearn(token, "core_webservice_get_site_info")
    st.success(f"Connected to ULearn as {account['fullname']}")

    assignment_data = call_ulearn(token, "mod_assign_get_assignments")
    courses = assignment_data["courses"]

except requests.RequestException:
    st.error("Could not reach ULearn. Check your connection and try again.")
    st.stop()
except ValueError as error:
    st.error(str(error))
    st.stop()
except KeyError:
    st.error("ULearn replied, but the expected account or course information was missing.")
    st.stop()

malaysia_time = timezone(timedelta(hours=8))
now = datetime.now(malaysia_time)
cutoff = now + timedelta(weeks=2)

upcoming = []

for course in courses:
    for assignment in course["assignments"]:
        if assignment["duedate"] > 0:
            due = datetime.fromtimestamp(assignment["duedate"], malaysia_time)

            if now <= due <= cutoff:
                upcoming.append((due, assignment["name"], course["fullname"]))

if not upcoming:
    st.info("No assignments are due in the next two weeks.")

for due, assignment_name, course_name in sorted(upcoming):
    with st.container(border=True):
        st.subheader(assignment_name)
        st.write(course_name)
        st.write("Due:", due.strftime("%d %b %Y at %I:%M %p"))