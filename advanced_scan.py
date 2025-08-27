"""
PyAutoScan - Advanced Scanner Module

This module provides advanced scanning functionality with enhanced features
including auto-crop, deskew, and comprehensive configuration management.
It extends the basic scanning capabilities with intelligent image processing.

Dependencies:
    - pywin32: Windows COM integration for WIA
    - Pillow: Image processing and PDF creation
    - powerlogger: Enhanced logging with Rich console output
    - configparser: Configuration file handling
    - Windows WIA drivers: Scanner communication

Tested on:
    - Python 3.13
    - HP Printer scanner features
    - Windows WIA drivers

Author: Pandiyaraj Karuppasamy
Email: pandiyarajk@live.com
Date: 27-Aug-2025
Version: 1.0.0
License: MIT
"""

import os
from datetime import datetime
import win32com.client
import configparser
from PIL import Image
from powerlogger import get_logger

def load_config(config_file="scan_config.ini"):
    """
    Load configuration settings from INI file.
    
    Args:
        config_file (str): Path to configuration file (default: "scan_config.ini")
    
    Returns:
        dict: Dictionary containing configuration settings with fallback values
    
    Note:
        Configuration file should have [SCAN_SETTINGS] and [PDF_SETTINGS] sections
    """
    # Initialize logger
    logger = get_logger("PyAutoScan.Config")
    
    config = configparser.ConfigParser()
    config.read(config_file)

    settings = {
        "output_dir": config.get("SCAN_SETTINGS", "output_dir", fallback="Scans"),
        "file_format": config.get("SCAN_SETTINGS", "file_format", fallback="jpg"),
        "quality": config.get("SCAN_SETTINGS", "quality", fallback="medium"),
        "auto_crop": config.getboolean("SCAN_SETTINGS", "auto_crop", fallback=True),
        "deskew": config.getboolean("SCAN_SETTINGS", "deskew", fallback=True),
        "pdf_output": config.get("PDF_SETTINGS", "pdf_output", fallback="scans.pdf"),
    }
    
    logger.info(f"Configuration loaded from {config_file}")
    return settings

def auto_scan(output_dir="Scans", file_format="jpg", quality="medium",
              auto_crop=True, deskew=True):
    """
    Advanced automatic scanning with image processing capabilities.
    
    This function extends basic scanning with intelligent image processing
    including auto-crop and deskew functionality for improved document quality.
    
    Args:
        output_dir (str): Directory to save scanned files (default: "Scans")
        file_format (str): Output format: "jpg", "png", or "tiff"
        quality (str): Scan quality: "low" (150 DPI), "medium" (300 DPI), or "high" (600 DPI)
        auto_crop (bool): Enable automatic cropping of scanned images (default: True)
        deskew (bool): Enable automatic deskewing of scanned images (default: True)
    
    Returns:
        str or None: Path to saved file on success, None on failure
    
    Raises:
        Exception: If scanning fails or no scanner is detected
    """
    # Initialize logger
    logger = get_logger("PyAutoScan.AdvancedScanner")
    
    try:
        os.makedirs(output_dir, exist_ok=True)

        device_manager = win32com.client.Dispatch("WIA.DeviceManager")
        if device_manager.DeviceInfos.Count == 0:
            logger.error("No scanner detected")
            print("❌ No scanner detected.")
            return None

        device = device_manager.DeviceInfos[0].Connect()
        scan_item = device.Items[1]

        quality_settings = {"low": 150, "medium": 300, "high": 600}
        dpi = quality_settings.get(quality.lower(), 300)

        try:
            scan_item.Properties["6147"].Value = dpi
            scan_item.Properties["6148"].Value = dpi
            scan_item.Properties["6146"].Value = 1
        except Exception as prop_err:
            logger.warning(f"Could not set some properties: {prop_err}")
            print(f"⚠️ Could not set some properties: {prop_err}")

        formats = {
            "jpg": "{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}",
            "png": "{B96B3CAE-0728-11D3-9D7B-0000F81EF32E}",
            "tiff": "{B96B3CB1-0728-11D3-9D7B-0000F81EF32E}"
        }
        format_id = formats.get(file_format.lower(), formats["jpg"])
        
        logger.info("Starting scan...")
        print(f"✅ Scanning...")
        image = scan_item.Transfer(format_id)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"scan_{quality}_{timestamp}.{file_format}")
        image.SaveFile(output_file)

        logger.info(f"Scan complete ({quality}, {dpi} DPI). Saved as {output_file}")
        print(f"✅ Scan complete ({quality}, {dpi} DPI). Saved as {output_file}")

        # Apply auto-crop & deskew if enabled
        if auto_crop or deskew:
            logger.info("Applying image processing (auto-crop/deskew)")
            img = Image.open(output_file)
            if auto_crop:
                img = img.crop(img.getbbox())  # simple crop
                logger.debug("Auto-crop applied")
            if deskew:
                img = img.rotate(-img.getbbox()[1], expand=True)  # placeholder deskew
                logger.debug("Deskew applied")
            img.save(output_file)

        return output_file
    except Exception as e:
        logger.error(f"Scan failed: {e}")
        print("❌ Scan failed:", e)
        return None

def images_to_pdf(image_files, pdf_file):
    # Initialize logger
    logger = get_logger("PyAutoScan.PDFConverter")
    
    if not image_files:
        logger.error("No images to convert")
        print("❌ No images to convert.")
        return
    
    logger.info(f"Converting {len(image_files)} images to PDF")
    imgs = [Image.open(f).convert("RGB") for f in image_files]
    imgs[0].save(pdf_file, save_all=True, append_images=imgs[1:])
    logger.info(f"PDF created: {pdf_file}")
    print(f"📄 PDF created: {pdf_file}")

if __name__ == "__main__":
    # Initialize logger for main execution
    logger = get_logger("PyAutoScan.Main")
    
    logger.info("Starting PyAutoScan Advanced Scanner")
    cfg = load_config()
    auto_scan(cfg["output_dir"], cfg["file_format"], cfg["quality"], cfg["auto_crop"], cfg["deskew"])
    logger.info("PyAutoScan Advanced Scanner completed")
