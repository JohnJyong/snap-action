import time
import os
import sys
from analyzer import IntentAnalyzer
import actions_dispatcher

# Simulated Watcher Directory
WATCH_DIR = "screenshots"

def main():
    if not os.path.exists(WATCH_DIR):
        os.makedirs(WATCH_DIR)
        
    print(f"👁️  SnapAction Service Started.")
    print(f"📂 Watching directory: ./{WATCH_DIR}/")
    print("📸 Drop a file named 'shoe.png', 'cafe.jpg', or 'ticket.png' to test...")
    
    analyzer = IntentAnalyzer()
    
    # State tracking to avoid reprocessing
    processed_files = set(os.listdir(WATCH_DIR))
    
    try:
        while True:
            current_files = set(os.listdir(WATCH_DIR))
            new_files = current_files - processed_files
            
            for filename in new_files:
                if filename.startswith("."): continue # skip hidden
                
                filepath = os.path.join(WATCH_DIR, filename)
                print("\n" + "="*40)
                print(f"📸 New Screenshot Detected: {filename}")
                
                # 1. Analyze
                import json
                result_json_str = analyzer.process(filepath)
                result = json.loads(result_json_str)
                
                # 2. Display 'Capsule' Intent
                print(f"🔮 Intent Detected: {result['intent']} ({result['confidence']*100:.0f}%)")
                print(f"💡 Capsule Text: \"{result['ui_label']}\"")
                
                # 3. Simulate User Click -> Dispatch Action
                print("👇 (User taps capsule...)")
                link = actions_dispatcher.dispatch(result)
                print(f"🔗 DeepLink: {link}")
                print("="*40)
                
            processed_files = current_files
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n🛑 Service Stopped.")

if __name__ == "__main__":
    main()
