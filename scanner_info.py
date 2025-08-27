"""
PyAutoScan - Scanner Information Utility

This module provides scanner detection and capability analysis.
It displays detailed information about connected scanners including
supported features, properties, and configuration options.

Dependencies:
    - pywin32: Windows COM integration for WIA
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

import win32com.client
from powerlogger import get_logger

def get_scanner_info():
    # Initialize logger
    logger = get_logger("PyAutoScan.ScannerInfo")
    
    try:
        device_manager = win32com.client.Dispatch("WIA.DeviceManager")

        if device_manager.DeviceInfos.Count == 0:
            logger.error("No scanner detected")
            print("❌ No scanner detected.")
            return None

        device_info = device_manager.DeviceInfos[0]  # first scanner
        device = device_info.Connect()

        # Collect available device properties
        scanner_details = {}
        for prop in device_info.Properties:
            try:
                scanner_details[prop.Name] = prop.Value
            except Exception:
                scanner_details[prop.Name] = "Not Available"

        # Collect supported features with safe checks
        supported_features = {}
        for item in device.Items:
            for prop in item.Properties:
                try:
                    feature = {
                        "ID": prop.PropertyID,
                        "Value": prop.Value,
                        "Type": prop.Type,
                        "SubType": prop.SubType
                    }
                    # Only add min/max if subtype supports it
                    if prop.SubType == 1:  # WIA_PROP_RANGE
                        feature["Min"] = prop.SubTypeMin
                        feature["Max"] = prop.SubTypeMax
                        feature["Step"] = prop.SubTypeStep
                    elif prop.SubType == 2:  # WIA_PROP_LIST
                        feature["Values"] = list(prop.SubTypeValues)

                    supported_features[prop.Name] = feature
                except Exception as e:
                    supported_features[prop.Name] = f"Error reading: {e}"

        logger.info("Scanner information retrieved successfully")
        return {
            "ScannerDetails": scanner_details,
            "SupportedFeatures": supported_features
        }

    except Exception as e:
        logger.error(f"Failed to get scanner info: {e}")
        print("❌ Failed to get scanner info:", e)
        return None


if __name__ == "__main__":
    # Initialize logger for main execution
    logger = get_logger("PyAutoScan.Main")
    
    logger.info("Starting PyAutoScan Scanner Information Utility")
    info = get_scanner_info()
    if info:
        logger.info("Scanner information displayed successfully")
        print("📌 Scanner Details:")
        for k, v in info["ScannerDetails"].items():
            print(f"   {k}: {v}")

        print("\n⚙️ Supported Features:")
        for k, v in info["SupportedFeatures"].items():
            print(f"   {k}: {v}")
    else:
        logger.error("Failed to retrieve scanner information")
    
    logger.info("PyAutoScan Scanner Information Utility completed")
