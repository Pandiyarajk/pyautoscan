"""
Tests for basic_scan module
"""
import unittest
from unittest.mock import patch, MagicMock
from pyautoscan.basic_scan import auto_scan, images_to_pdf, image_format, image_quality


class TestBasicScan(unittest.TestCase):
    """Test cases for basic scanning functionality"""

    def test_image_format_constants(self):
        """Test image format constants"""
        self.assertEqual(image_format.JPG, "jpg")
        self.assertEqual(image_format.PNG, "png")
        self.assertEqual(image_format.TIFF, "tiff")
        self.assertEqual(image_format.PDF, "pdf")

    def test_image_quality_constants(self):
        """Test image quality constants"""
        self.assertEqual(image_quality.LOW, "low")
        self.assertEqual(image_quality.MEDIUM, "medium")
        self.assertEqual(image_quality.HIGH, "high")

    @patch('pyautoscan.basic_scan.win32com.client.Dispatch')
    def test_auto_scan_no_scanner(self, mock_dispatch):
        """Test auto_scan when no scanner is detected"""
        mock_manager = MagicMock()
        mock_manager.DeviceInfos.Count = 0
        mock_dispatch.return_value = mock_manager

        result = auto_scan()
        self.assertIsNone(result)

    def test_images_to_pdf_no_images(self):
        """Test images_to_pdf with no images"""
        result = images_to_pdf([], "test.pdf")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
