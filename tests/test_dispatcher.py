import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import actions_dispatcher

class TestActionsDispatcher(unittest.TestCase):
    
    def test_dispatch_shopping(self):
        """Test URL generation for shopping intent."""
        intent = {
            "intent": "SHOPPING",
            "data": {"query": "MacBook Pro M4"}
        }
        link = actions_dispatcher.dispatch(intent)
        self.assertEqual(link, "https://www.google.com/search?q=MacBook+Pro+M4&tbm=shop")

    def test_dispatch_navigation(self):
        """Test Geo URI generation for navigation intent."""
        intent = {
            "intent": "NAVIGATION",
            "data": {"location_name": "Eiffel Tower"}
        }
        link = actions_dispatcher.dispatch(intent)
        self.assertEqual(link, "geo:0,0?q=Eiffel Tower")

    def test_dispatch_schedule(self):
        """Test Calendar Intent generation."""
        intent = {
            "intent": "SCHEDULE",
            "data": {"event_title": "Meeting", "start_time": "2026-01-01 10:00"}
        }
        link = actions_dispatcher.dispatch(intent)
        self.assertTrue(link.startswith("content://com.android.calendar"))

    def test_dispatch_unknown(self):
        """Test fallback for unknown intent."""
        intent = {
            "intent": "UNKNOWN_TYPE",
            "data": {}
        }
        link = actions_dispatcher.dispatch(intent)
        self.assertIsNone(link)

if __name__ == '__main__':
    unittest.main()
