import unittest
import json
import sys
import os

# Add parent directory to path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer import IntentAnalyzer

class TestIntentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = IntentAnalyzer()

    def test_shopping_intent_simulation(self):
        """Test if a 'product' image triggers SHOPPING intent."""
        # Simulation relies on filename keywords
        result_json = self.analyzer.process("path/to/nike_shoe.png")
        result = json.loads(result_json)
        
        self.assertEqual(result['intent'], "SHOPPING")
        self.assertEqual(result['data']['category'], "Shoes")
        self.assertGreater(result['confidence'], 0.9)
        self.assertEqual(result['ui_label'], "🔍 Find Best Price")

    def test_navigation_intent_simulation(self):
        """Test if a 'map' image triggers NAVIGATION intent."""
        result_json = self.analyzer.process("path/to/tokyo_cafe_map.jpg")
        result = json.loads(result_json)
        
        self.assertEqual(result['intent'], "NAVIGATION")
        self.assertIn("location_name", result['data'])
        self.assertEqual(result['ui_label'], "📍 Navigate Here")

    def test_schedule_intent_simulation(self):
        """Test if a 'ticket' image triggers SCHEDULE intent."""
        result_json = self.analyzer.process("concert_ticket.png")
        result = json.loads(result_json)
        
        self.assertEqual(result['intent'], "SCHEDULE")
        self.assertIn("event_title", result['data'])
        self.assertEqual(result['ui_label'], "📅 Add to Calendar")

    def test_fallback_info_intent(self):
        """Test fallback to INFO for unrecognized images."""
        result_json = self.analyzer.process("random_screenshot.png")
        result = json.loads(result_json)
        
        self.assertEqual(result['intent'], "INFO")
        self.assertEqual(result['ui_label'], "Copy Text")

if __name__ == '__main__':
    unittest.main()
