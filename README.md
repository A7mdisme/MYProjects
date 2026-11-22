# UTP Notifier

UTP Notifier shows your ULearn assignments due in the **next 14 days**. Each assignment appears in a separate card with its title, course name, and deadline in Malaysia time. The nearest deadline appears first.

## How to use the app

1. Open the app in your browser.
2. Enter your personal ULearn token and click **Show assignments**.
3. Review your upcoming deadlines. Click **Show assignments** again whenever you want to refresh the list.

To find your token, sign in to ULearn and open the [Security keys page](https://ulearn.utp.edu.my/user/managetoken.php). Look for **Moodle mobile web service**. Keep your token private and only enter it in a deployment you trust.

## Run it on Windows

Install Python, download or clone this repository, and open the `MYProjects` folder in VS Code. In the terminal, run:

```powershell
py -m pip install streamlit requests
py -m streamlit run UTP-NOTIFIER/app.py
```

The app opens in your browser. If it doesn’t open automatically, click the **Local URL** shown in the terminal.

## Deploy and share it

1. Make sure `UTP-NOTIFIER/requirements.txt` lists `streamlit` and `requests` on separate lines.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) and click **Create app**.
3. Select the repository `A7mdisme/MYProjects` and the branch `main`.
4. Set the **Main file path** to `UTP-NOTIFIER/app.py` and click **Deploy**.
5. Open the deployed app and choose **Share → Copy link**. Each friend uses their own ULearn token to view their assignments.

## Project files

| File | Purpose |
| --- | --- |
| `UTP-NOTIFIER/app.py` | Runs the complete dashboard and displays assignment cards. |
| `UTP-NOTIFIER/step1_connect.py` | Tests the ULearn connection from the terminal. |
| `UTP-NOTIFIER/step2_connect.py` | Lists upcoming assignment deadlines in the terminal. |
| `UTP-NOTIFIER/requirements.txt` | Lists the Python packages needed for deployment. |

## What the deadline list includes

The app reads deadlines recorded on ULearn assignments. An assignment you’ve already submitted can still appear until its deadline passes. The dashboard refreshes when you click **Show assignments**. This version does not send automatic phone notifications. 


**Live website:** [Open UTP Notifier](PASTE_YOUR_STREAMLIT_URL_HERE)

