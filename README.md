# SnapAction (截图行动派) 📸⚡️

> **Turn Screenshots into Actions, Instantly.**
> 
> *A Proof-of-Concept for an On-Device AI Intent Capsule System.*

## 🚀 Vision
SnapAction is a background service that listens for screenshot events, analyzes the image content locally using multimodal AI, and offers immediate, context-aware actions via a non-intrusive "Intent Capsule" UI.

## 🧠 Core Logic (The "Brain")
This repository contains the **Python Prototype** of the intent analysis engine. 

### Supported Intents
1.  **🛍️ Shopping (Product)**
    *   **Trigger:** Screenshot contains a physical product (clothes, gadgets, furniture).
    *   **Action:** Extract search terms -> Open Price Comparison / Shopping Search.
2.  **📍 Navigation (Place)**
    *   **Trigger:** Screenshot contains a storefront, street view, or address text.
    *   **Action:** Extract place name/address -> Save to Maps / Navigate.
3.  **📅 Scheduling (Event)**
    *   **Trigger:** Screenshot contains a poster, date/time, or invitation.
    *   **Action:** Extract title & time -> Add to Calendar.

## 🛠️ Architecture (Production vs Prototype)

| Component | Production (Mobile App) | This Prototype (Python) |
| :--- | :--- | :--- |
| **Listener** | `BroadcastReceiver` (Android) / Shortcuts (iOS) | `File Watcher` (Simulated) |
| **Model** | Gemini Nano / Phi-3-mini (On-Device NPU) | Gemini Pro API (Cloud Simulation) |
| **UI** | System Overlay / Dynamic Island | Console Output / Log |

## 📦 Project Structure
```bash
snap-action/
├── main.py              # Event loop simulating screenshot capture
├── analyzer.py          # The Vision LLM Prompt & Logic
├── actions/
│   ├── shopping.py      # Price comparison logic
│   ├── maps.py          # Geocoding logic
│   └── calendar.py      # .ics generation logic
└── requirements.txt     # Dependencies
```

## ⚡️ Quick Start
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the watcher:
    ```bash
    python main.py
    ```
3.  Drop an image into the `screenshots/` folder to test!

## 🔒 Privacy First
In the production version, **NO images leave the device**. The "Brain" runs locally. This prototype uses Cloud APIs purely for demonstration purposes.
