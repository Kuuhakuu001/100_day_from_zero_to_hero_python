import unittest


def calculate_can_chi_calendar(year):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

    can_idx = year % 10
    chi_idx = year % 12

    return can[can_idx] + " " + chi[chi_idx]


class TestCalculateCanChiCalendar(unittest.TestCase):
    def test_2024(self):
        self.assertEqual(calculate_can_chi_calendar(2024), "Giáp Thìn")

    def test_2023(self):
        self.assertEqual(calculate_can_chi_calendar(2023), "Quý Mão")

    def test_1997(self):
        self.assertEqual(calculate_can_chi_calendar(1997), "Đinh Sửu")

if __name__ == "__main__":
    # Run unittests
    # unittest.main()

    # Test cases
    print(calculate_can_chi_calendar(2024))  # Output: Giáp Thìn
    print(calculate_can_chi_calendar(2023))  # Output: Quý Mão
    print(calculate_can_chi_calendar(1997))  # Output: Đinh Sửu