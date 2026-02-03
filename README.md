# SnapAction (截图行动派) 📸⚡️

> **Turn Screenshots into Actions, Instantly.**
> 
> *A Cross-Platform Concept for On-Device AI Intent Capsules.*

## 🚀 Overview

SnapAction is an AI-powered background service that detects user intent from screenshots and offers immediate actions via a "Capsule" UI.

| Platform | Status | Tech Stack |
| :--- | :--- | :--- |
| **Python (Core)** | ✅ Prototype | Python, `analyzer.py`, `actions_dispatcher.py` |
| **Android** | 🚧 Concept | Kotlin, `ContentObserver`, Gemini Nano |
| **iOS** | 🚧 Concept | Swift, SwiftUI, Shortcuts Integration |
| **Web** | ✅ Demo | HTML5, JavaScript (Mock) |

## 📂 Project Structure

```bash
snap-action/
├── main.py              # 🐍 Python Watcher Service (MVP)
├── android/             # 🤖 Android App Source (Kotlin)
├── ios/                 # 🍎 iOS App Source (Swift)
├── web/                 # 🌐 Web Demo (HTML/JS)
└── actions_dispatcher.py # 🧠 Core Logic
```

## 🛠️ Usage Guide

### 1. Python Core (CLI)
Run the watcher on your desktop to process images in a folder.
```bash
# Install deps
pip install -r requirements.txt

# Run
python main.py

# Test
# Drop 'shoe.png' into the 'screenshots/' folder.
```

### 2. Web Demo (Browser)
A simple drag-and-drop interface to visualize the UI.
1. Go to `snap-action/web/`
2. Open `index.html` in Chrome/Safari.
3. Drag an image (rename it to `shoe.jpg` or `map.png` to trigger intents) into the box.

### 3. Android (Developer)
The Android code uses a `ContentObserver` to listen for new media.
*   **Path:** `android/app/src/main/java/com/snapaction/ScreenshotService.kt`
*   **Key Logic:** When `MediaStore` updates, we get the URI and pass it to the local inference engine.

### 4. iOS (Developer)
Due to sandboxing, iOS requires user initiation or Shortcuts.
*   **Path:** `ios/SnapAction/ContentView.swift`
*   **Logic:** A button to "Import Last Screenshot" and analyze it.

## 🐳 Docker (Run Anywhere)
Don't want to install Python? Use Docker.
```bash
docker build -t snap-action .
docker run -v $(pwd)/screenshots:/app/screenshots -it snap-action
```

## 🤝 Contributing
1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
