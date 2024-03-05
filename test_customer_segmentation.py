import unittest
from customer_segmentation import calculate_segment, process_data

class TestCustomerSegmentation(unittest.TestCase):
    def test_calculate_segment_low(self):
        self.assertEqual(calculate_segment(50), 'Low')

    def test_calculate_segment_medium(self):
        self.assertEqual(calculate_segment(250), 'Medium')

    def test_calculate_segment_high(self):
        self.assertEqual(calculate_segment(700), 'High')

if __name__ == '__main__':
    unittest.main()
