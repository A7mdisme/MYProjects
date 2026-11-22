# UTP Notifier

[Open UTP Notifier][app] to see your ULearn assignments due in the **next 14 days**. Each assignment appears in its own card with the title, course name, and deadline in Malaysia time. The nearest deadline appears first.

## How to use the app

### First-time users

1. Sign in to [UTP ULearn](https://ulearn.utp.edu.my/) with your student account.
2. Open the [ULearn Security keys page](https://ulearn.utp.edu.my/user/managetoken.php).
3. In the **Service** column, find the row labeled **Moodle mobile web service**.
4. In the **Operation** column of that same row, click **Reset**. Confirm if prompted, then copy the new token displayed on the next page.
5. [Open UTP Notifier][app], paste your token into the **ULearn token** field, and click **Show assignments**.

**Keep your token private.** Each student should use their own token. Resetting replaces the previous token, so if you already have a working one, you can go straight to the app.

### Returning users

[Open UTP Notifier][app], enter your existing token, and click **Show assignments**. You can use the same token while it remains valid. Click **Show assignments** again whenever you want to refresh the list.

## Which assignments appear?

The dashboard reads due dates recorded on ULearn assignments. An assignment can still appear after you submit it because the app filters by deadline. Dates mentioned only in announcements are outside this list.

The dashboard updates when you click **Show assignments**. This version does not send automatic phone notifications.

## Run the app on Windows

1. Install Python.
2. Download or clone this repository and open the folder containing this README in VS Code.
3. Open **Terminal → New Terminal** and run these commands one at a time:

```powershell
py -m pip install streamlit requests
py -m streamlit run UTP-NOTIFIER/app.py
```

The app opens in your browser. If it doesn’t open automatically, click the **Local URL** printed in the terminal. Keep the terminal open while using the local app. Press **Ctrl + C** to stop it.

## Deploy and share the app

1. Make sure `UTP-NOTIFIER/requirements.txt` lists `streamlit` and `requests` on separate lines.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) and click **Create app**.
3. Select the GitHub repository `A7mdisme/MYProjects` and the branch `main`.
4. Set **Main file path** to `UTP-NOTIFIER/app.py`, then click **Deploy**.
5. Once the app opens, click **Share → Copy link**. Use that address for the `[app]` link at the bottom of this README.

## Project files

| File | Purpose |
| --- | --- |
| `UTP-NOTIFIER/app.py` | Connects to ULearn and displays assignment cards in the browser. |
| `UTP-NOTIFIER/step1_connect.py` | Tests your ULearn connection from the terminal. |
| `UTP-NOTIFIER/step2_connect.py` | Lists upcoming assignment deadlines in the terminal. |
| `UTP-NOTIFIER/requirements.txt` | Lists the Python packages needed for deployment. |

[app]: https://YOUR-APP-NAME.streamlit.app
