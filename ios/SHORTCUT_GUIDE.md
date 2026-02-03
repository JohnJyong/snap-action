# 🍎 iOS Setup Guide (Shortcuts Automation)

Since iOS does not allow background apps to silently read your screenshots (for privacy reasons), we use **Siri Shortcuts** to bridge the gap.

## 🚀 Two Ways to Use SnapAction on iOS

### Method A: "Back Tap" Automation (Recommended)
Trigger SnapAction by double-tapping the back of your iPhone.

1.  **Create the Shortcut:**
    *   Open **Shortcuts** app.
    *   Create new Shortcut named `SnapAction`.
    *   Action 1: `Take Screenshot`.
    *   Action 2: `Get Image from Input`.
    *   Action 3: `Run Script over SSH` (if running locally) OR `Get Contents of URL` (if using a deployed API).
        *   *Note: For the Python MVP, you can expose your local server via `ngrok` and POST the image.*
    *   Action 4: `Show Notification` with the result.

2.  **Bind to Back Tap:**
    *   Settings -> Accessibility -> Touch -> Back Tap.
    *   **Double Tap** -> Select `SnapAction`.

### Method B: Share Sheet
Manually send an image to SnapAction.

1.  **Create the Shortcut:**
    *   Open **Shortcuts** app.
    *   Enable "Show in Share Sheet".
    *   Set Input to "Images".
    *   Action: Send Image to SnapAction API.

## 🛠️ Connecting to the Python Backend

To test this with the current Python code, you need to expose `main.py` as a web server.

1.  Modify `main.py` to use `Flask` or `FastAPI`.
2.  Run: `ngrok http 5000`
3.  In Shortcuts, use the `Post to URL` action with the ngrok address.
