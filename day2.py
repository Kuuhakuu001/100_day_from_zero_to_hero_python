import unittest


def compute_interest(money, period):
    # money = (money * (1 + 1 / period))**period
    for _ in range(period):
        money *= (1 + 1 / period)
    return round(money, 3)

class TestComputeInterest(unittest.TestCase):
    def test_12_days(self):
        self.assertEqual(compute_interest(1, 12), 2.613)
    
    def test_365_days(self):
        self.assertEqual(compute_interest(1, 365), 2.715)
    
    def test_730_days(self):
        self.assertEqual(compute_interest(1, 730), 2.716)
    
if __name__ == "__main__":
    # Run unittests
    # unittest.main()

     # Test cases
    print(compute_interest(1, 12))   # Expected output: 2.613
    print(compute_interest(1, 365))  # Expected output: 2.715
    print(compute_interest(1, 730))  # Expected output: 2.716