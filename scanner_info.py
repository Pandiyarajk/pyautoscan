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

# Sample output:
'''
python.exe scanner_info.py
📌 Scanner Details:
   Unique Device ID: {6BDD1FC6-810F-11D0-BEC7-08002BE2092F}\0004
   Manufacturer: HP
   Description: HP Smart Tank 520_540 series (USB)
   Type: 65538
   Port: \\.\Usbscan0
   Name: HP Smart Tank 520_540 series (USB)
   Server: local
   Remote Device ID:
   UI Class ID: {7C1E2309-A535-45b1-94B3-9A020EE600C7}
   Hardware Configuration: 0
   BaudRate:
   STI Generic Capabilities: 49
   WIA Version: 2.0
   Driver Version: 0.0.0.0
   PnP ID String: \\?\usb#vid_03f0&pid_4554&mi_00#6&383b597f&2&c000#{6bdd1fc6-810f-11d0-bec7-08002be2092f}
   STI Driver Version: 3

⚙️ Supported Features:
   Item Name: {'ID': 4098, 'Value': 'Scan', 'Type': 16, 'SubType': 0}
   Full Item Name: {'ID': 4099, 'Value': '0004\\Root\\Scan', 'Type': 16, 'SubType': 0}
   Item Flags: {'ID': 4101, 'Value': 532483, 'Type': 5, 'SubType': 0}
   Color Profile Name: {'ID': 4120, 'Value': 'C:\\WINDOWS\\system32\\spool\\drivers\\color\\sRGB Color Space Profile.icm', 'Type': 16, 'SubType': 2, 'Values': ['C:\\WINDOWS\\system32\\spool\\drivers\\color\\sRGB Color Space Profile.icm']}
   Access Rights: {'ID': 4102, 'Value': 3, 'Type': 5, 'SubType': 0}
   Filename extension: {'ID': 4123, 'Value': 'bmp', 'Type': 16, 'SubType': 0}
   Compression: {'ID': 4107, 'Value': 0, 'Type': 5, 'SubType': 2, 'Values': [0]}
   Data Type: {'ID': 4103, 'Value': 3, 'Type': 5, 'SubType': 2, 'Values': [3, 2, 0]}
   Bits Per Pixel: {'ID': 4104, 'Value': 24, 'Type': 5, 'SubType': 2, 'Values': [24, 8, 1]}
   Channels Per Pixel: {'ID': 4109, 'Value': 3, 'Type': 5, 'SubType': 0}
   Bits Per Channel: {'ID': 4110, 'Value': 8, 'Type': 5, 'SubType': 0}
   Planar: {'ID': 4111, 'Value': 0, 'Type': 5, 'SubType': 0}
   Current Intent: {'ID': 6146, 'Value': 0, 'Type': 5, 'SubType': 3}
   Horizontal Resolution: {'ID': 6147, 'Value': 200, 'Type': 5, 'SubType': 2, 'Values': [75, 100, 150, 200, 300, 400, 600, 1200]}
   Vertical Resolution: {'ID': 6148, 'Value': 200, 'Type': 5, 'SubType': 2, 'Values': [75, 100, 150, 200, 300, 400, 600, 1200]}
   Horizontal Start Position: {'ID': 6149, 'Value': 0, 'Type': 5, 'SubType': 1, 'Min': 0, 'Max': 1695, 'Step': 1}
   Vertical Start Position: {'ID': 6150, 'Value': 0, 'Type': 5, 'SubType': 1, 'Min': 0, 'Max': 2333, 'Step': 1}
   Horizontal Extent: {'ID': 6151, 'Value': 1700, 'Type': 5, 'SubType': 1, 'Min': 5, 'Max': 1700, 'Step': 1}
   Vertical Extent: {'ID': 6152, 'Value': 2338, 'Type': 5, 'SubType': 1, 'Min': 5, 'Max': 2338, 'Step': 1}
   Pixels Per Line: {'ID': 4112, 'Value': 1700, 'Type': 5, 'SubType': 0}
   Number of Lines: {'ID': 4114, 'Value': 2338, 'Type': 5, 'SubType': 0}
   Bytes Per Line: {'ID': 4113, 'Value': 0, 'Type': 5, 'SubType': 0}
   Item Size: {'ID': 4116, 'Value': 0, 'Type': 5, 'SubType': 0}
   Buffer Size: {'ID': 4118, 'Value': 262144, 'Type': 5, 'SubType': 0}
   Photometric Interpretation: {'ID': 6153, 'Value': 0, 'Type': 5, 'SubType': 2, 'Values': [0]}
   Brightness: {'ID': 6154, 'Value': 0, 'Type': 5, 'SubType': 1, 'Min': -1000, 'Max': 1000, 'Step': 1}
   Contrast: {'ID': 6155, 'Value': 0, 'Type': 5, 'SubType': 1, 'Min': -1000, 'Max': 1000, 'Step': 1}
   Threshold: {'ID': 6159, 'Value': 128, 'Type': 5, 'SubType': 1, 'Min': 0, 'Max': 255, 'Step': 1}
   Orientation: {'ID': 6156, 'Value': 0, 'Type': 5, 'SubType': 2, 'Values': [0]}
   Media Type: {'ID': 4108, 'Value': 2, 'Type': 5, 'SubType': 2, 'Values': [128, 2]}
   Preferred Format: {'ID': 4105, 'Value': '{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}', 'Type': 15, 'SubType': 0}
   Format: {'ID': 4106, 'Value': '{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}', 'Type': 15, 'SubType': 0}
'''