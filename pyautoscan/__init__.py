"""
PyAutoScan - Windows Scanner Automation Tool

A Python-based Windows scanning automation tool for printer/scanner devices using WIA.

Author: Pandiyaraj Karuppasamy
Email: pandiyarajk@live.com
Date: 27-Aug-2025
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Pandiyaraj Karuppasamy"
__email__ = "pandiyarajk@live.com"
__license__ = "MIT"

from .basic_scan import auto_scan, images_to_pdf, image_format, image_quality
from .advanced_scan import auto_scan as advanced_auto_scan, load_config
from .scanner_info import get_scanner_info

__all__ = [
    "auto_scan",
    "advanced_auto_scan", 
    "images_to_pdf",
    "image_format",
    "image_quality",
    "load_config",
    "get_scanner_info",
]
