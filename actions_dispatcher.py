def handle_shopping(data):
    print(f"   [🛒 ACTION] Opening browser to search for: '{data['query']}'")
    # In a real app, this would trigger an Intent/DeepLink to Amazon, Google Shopping, etc.
    return f"https://www.google.com/search?q={data['query'].replace(' ', '+')}&tbm=shop"

def handle_navigation(data):
    loc = data.get('location_name', 'Unknown')
    print(f"   [🗺️ ACTION] Saving '{loc}' to Favorites...")
    # In real app: open google.navigation:q=...
    return f"geo:0,0?q={loc}"

def handle_schedule(data):
    title = data.get('event_title', 'New Event')
    time = data.get('start_time', 'TBD')
    print(f"   [📅 ACTION] Creating event '{title}' at {time}")
    # In real app: Insert into Calendar Provider
    return "content://com.android.calendar/events/insert..."

def dispatch(intent_json):
    intent = intent_json.get("intent")
    data = intent_json.get("data", {})
    
    print(f"⚡️ TRIGGER: {intent_json.get('ui_label')}")
    
    if intent == "SHOPPING":
        return handle_shopping(data)
    elif intent == "NAVIGATION":
        return handle_navigation(data)
    elif intent == "SCHEDULE":
        return handle_schedule(data)
    else:
        print("   [INFO] No specific action trigger.")
        return None
