import json
import os

# Mocking the AI call for the prototype. 
# In a real scenario, this would import google.generativeai or use a local ONNX runtime.

class IntentAnalyzer:
    def __init__(self):
        self.system_prompt = """
        You are the backend AI for 'SnapAction'. Your job is to analyze screenshots and determine the user's INTENT.
        
        Classify the image into exactly one of these categories:
        - SHOPPING (The user likely wants to buy what's in the image)
        - NAVIGATION (The user likely wants to go to the place in the image)
        - SCHEDULE (The user likely wants to remember an event/time)
        - INFO (General text/receipts, etc. - Ignore for now)
        
        Output strictly JSON in this format:
        {
            "intent": "SHOPPING" | "NAVIGATION" | "SCHEDULE" | "INFO",
            "confidence": 0.0-1.0,
            "data": {
                // If SHOPPING:
                "query": "exact product name to search",
                "category": "shoes/tech/etc"
                
                // If NAVIGATION:
                "location_name": "name of place",
                "address": "visible address or inferred area"
                
                // If SCHEDULE:
                "event_title": "title of event",
                "start_time": "YYYY-MM-DD HH:MM",
                "end_time": "YYYY-MM-DD HH:MM" (optional)
            },
            "ui_label": "Short text to show on the capsule button (e.g. 'Compare Prices', 'Save to Maps')"
        }
        """

    def analyze(self, image_path):
        print(f"🧠 Analyzing image: {image_path}...")
        
        # SIMULATION: 
        # Since I cannot run the actual Vision model in this offline python script without an API key in the env,
        # I will simulate the response based on the filename for demonstration purposes.
        # In production, replace this with: `model.generate_content([self.system_prompt, img])`
        
        filename = os.path.basename(image_path).lower()
        
        if "shoe" in filename or "bag" in filename or "product" in filename:
            return {
                "intent": "SHOPPING",
                "confidence": 0.95,
                "data": {
                    "query": "Nike Air Jordan 1 High Chicago",
                    "category": "Shoes"
                },
                "ui_label": "🔍 Find Best Price"
            }
            
        elif "cafe" in filename or "restaurant" in filename or "map" in filename:
            return {
                "intent": "NAVIGATION",
                "confidence": 0.92,
                "data": {
                    "location_name": "Starbucks Reserve Roastery",
                    "address": "Tokyo, Japan"
                },
                "ui_label": "📍 Navigate Here"
            }
            
        elif "ticket" in filename or "invite" in filename or "poster" in filename:
            return {
                "intent": "SCHEDULE",
                "confidence": 0.88,
                "data": {
                    "event_title": "Coldplay Concert World Tour",
                    "start_time": "2026-04-15 19:00"
                },
                "ui_label": "📅 Add to Calendar"
            }
            
        else:
            return {
                "intent": "INFO",
                "confidence": 0.5,
                "data": {},
                "ui_label": "Copy Text"
            }

    def process(self, image_path):
        result = self.analyze(image_path)
        return json.dumps(result, indent=2, ensure_ascii=False)
