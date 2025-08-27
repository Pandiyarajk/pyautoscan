"""
PyAutoScan - Basic Scanner Module

This module provides basic scanning functionality with configurable quality
and format options. It supports multiple output formats including JPG, PNG,
TIFF, and PDF.

Dependencies:
    - pywin32: Windows COM integration for WIA
    - Pillow: Image processing and PDF creation
    - powerlogger: Enhanced logging with Rich console output
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
from typing import Optional, List
import win32com.client
from PIL import Image
from powerlogger import get_logger

def auto_scan(output_dir: str = "Scans", file_format: str = "jpg", quality: str = "medium") -> Optional[str]:
    """
    Automatically scan documents using the first available scanner.
    
    Args:
        output_dir (str): Directory to save scanned files (default: "Scans")
        file_format (str): Output format: "jpg", "png", "tiff", or "pdf"
        quality (str): Scan quality: "low" (150 DPI), "medium" (300 DPI), or "high" (600 DPI)
    
    Returns:
        str or None: Path to saved file on success, None on failure
    
    Raises:
        Exception: If scanning fails or no scanner is detected
    """
    # Initialize logger
    logger = get_logger("PyAutoScan.BasicScanner")
    
    try:
        # Ensure output folder exists
        os.makedirs(output_dir, exist_ok=True)

        # Connect to WIA device manager
        device_manager = win32com.client.Dispatch("WIA.DeviceManager")

        if device_manager.DeviceInfos.Count == 0:
            logger.error("No scanner detected")
            print("ERROR: No scanner detected.")
            return None

        # Use the first available scanner
        device = device_manager.DeviceInfos[0].Connect()

        # Access the scanner item (usually item[1] is the flatbed)
        scan_item = device.Items[1]

        # Quality settings (DPI)
        quality_settings = {
            "low": 150,
            "medium": 300,
            "high": 600
        }
        dpi = quality_settings.get(quality.lower(), 300)  # default medium

        # Set scan properties
        try:
            scan_item.Properties["6147"].Value = dpi  # Horizontal Resolution DPI
            scan_item.Properties["6148"].Value = dpi  # Vertical Resolution DPI
            scan_item.Properties["6146"].Value = 1    # Color Intent (1=Color, 2=Gray, 4=B/W)
        except Exception as prop_err:
            logger.warning(f"Could not set some properties: {prop_err}")
            print(f"WARNING: Could not set some properties: {prop_err}")

        # WIA format IDs
        formats = {
            "jpg": "{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}",
            "png": "{B96B3CAE-0728-11D3-9D7B-0000F81EF32E}",
            "tiff": "{B96B3CB1-0728-11D3-9D7B-0000F81EF32E}"
        }

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if file_format.lower() == "pdf":
            # Always scan to an image first (jpg intermediate)
            temp_file = os.path.join(output_dir, f"scan_{quality}_{timestamp}.jpg")
            image = scan_item.Transfer(formats["jpg"])
            image.SaveFile(temp_file)

            # Convert to PDF
            pdf_file = os.path.join(output_dir, f"scan_{quality}_{timestamp}.pdf")
            pil_img = Image.open(temp_file)
            pil_img.save(pdf_file, "PDF", resolution=dpi)
            os.remove(temp_file)  # remove temp JPG
            logger.info(f"Scan complete ({quality}, {dpi} DPI). Saved as {pdf_file}")
            print(f"SUCCESS: Scan complete ({quality}, {dpi} DPI). Saved as {pdf_file}")
            return pdf_file

        else:
            # Acquire in requested format
            format_id = formats.get(file_format.lower(), formats["jpg"])
            image = scan_item.Transfer(format_id)

            output_file = os.path.join(output_dir, f"scan_{quality}_{timestamp}.{file_format}")
            image.SaveFile(output_file)

            logger.info(f"Scan complete ({quality}, {dpi} DPI). Saved as {output_file}")
            print(f"SUCCESS: Scan complete ({quality}, {dpi} DPI). Saved as {output_file}")
            return output_file

    except Exception as e:
        logger.error(f"Scan failed: {e}")
        print("ERROR: Scan failed:", e)
        return None


# Enum-like classes for format and quality constants
class image_format:
    """Supported image formats for scanning."""
    JPG = "jpg"      # JPEG format (compressed, good for documents)
    PNG = "png"      # PNG format (lossless, good for images)
    TIFF = "tiff"    # TIFF format (high quality, large files)
    PDF = "pdf"      # PDF format (portable document format)

class image_quality:
    """Supported scan quality levels with corresponding DPI values."""
    LOW = "low"      # 150 DPI (fast, smaller files)
    MEDIUM = "medium" # 300 DPI (balanced quality/size)
    HIGH = "high"    # 600 DPI (high quality, larger files)


def images_to_pdf(image_files: List[str], output_pdf: str) -> Optional[str]:
    """
    Convert a list of image files into a single multi-page PDF.
    
    This function takes multiple image files and combines them into a single
    PDF document, with each image as a separate page. Useful for creating
    multi-page documents from individual scans.
    
    Args:
        image_files: List of image file paths to combine
        output_pdf: Output PDF file path
    
    Returns:
        Path to created PDF on success, None on failure
    
    Raises:
        Exception: If PDF creation fails
    """
    if not image_files:
        print("ERROR: No images provided for PDF conversion.")
        return None

    try:
        if os.path.exists(output_pdf):
            os.remove(output_pdf)

        # Open first image
        first_img = Image.open(image_files[0]).convert("RGB")

        # Open rest of the images and convert to RGB
        img_list = [Image.open(img).convert("RGB") for img in image_files[1:]]

        # Save all into one PDF
        first_img.save(output_pdf, save_all=True, append_images=img_list)

        print(f"SUCCESS: PDF created with {len(image_files)} pages: {output_pdf}")
        return output_pdf
    except Exception as e:
        print("ERROR: Failed to create PDF:", e)
        return None


if __name__ == "__main__":
    """
    Main execution block - demonstrates basic scanning functionality.
    
    This example shows how to:
    1. Perform a basic scan with specified settings
    2. Optionally convert the scan to PDF
    """
    # Initialize logger for main execution
    logger = get_logger("PyAutoScan.Main")
    
    # Example: Save in "Scans/" as low quality JPG
    file_name1 = auto_scan(output_dir="Scans", file_format=image_format.JPG, quality=image_quality.LOW)
    
    if file_name1:
        logger.info(f"Scan completed successfully: {file_name1}")
        print(f"SUCCESS: Scan completed successfully: {file_name1}")
        
        # Optional: Convert to PDF (uncomment to enable)
        # image_files = [file_name1]
        # pdf_result = images_to_pdf(image_files, "Scans/scan_pdf.pdf")
        # if pdf_result:
        #     logger.info(f"PDF created: {pdf_result}")
        #     print(f"SUCCESS: PDF created: {pdf_result}")
    else:
        logger.error("Scan failed. Check scanner connection and try again")
        print("ERROR: Scan failed. Check scanner connection and try again.")
