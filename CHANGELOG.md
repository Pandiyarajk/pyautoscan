# Changelog

All notable changes to PyAutoScan will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-27

### Added
- Initial release of PyAutoScan
- GitHub repository: [https://github.com/Pandiyarajk/pyautoscan](https://github.com/Pandiyarajk/pyautoscan)
- Basic scanning functionality with configurable quality and format options
- Advanced scanning with auto-crop and deskew capabilities
- Scanner detection and information utilities
- Configuration management via INI files
- Support for multiple output formats (JPG, PNG, TIFF, PDF)
- Quality control with DPI settings (150, 300, 600)
- PDF conversion and multi-page PDF creation
- Windows WIA (Windows Image Acquisition) integration
- Comprehensive error handling and user feedback
- Timestamp-based file naming for organized output

### Testing & Compatibility
- Successfully tested on HP Printer scanner features
- Verified compatibility with Python 3.13
- Confirmed Windows WIA driver integration

### Features
- **basic_scan.py**: Core scanning functionality with format and quality options
- **advanced_scan.py**: Enhanced scanning with image processing features
- **scanner_info.py**: Scanner detection and capability analysis
- **scan_config.ini**: Centralized configuration management
- **Scans/**: Organized output directory structure

### Technical Details
- Built with Python 3.7+ compatibility (Tested on Python 3.13)
- Uses pywin32 for Windows COM integration
- PIL/Pillow for image processing and PDF creation
- ConfigParser for INI file handling
- Windows-specific WIA API integration
- Successfully tested on HP Printer scanner features

### Supported Platforms
- Windows 10/11
- Requires compatible scanner with WIA drivers

---

## [Unreleased]

### Planned Features
- Batch scanning capabilities
- OCR (Optical Character Recognition) integration
- Cloud storage integration
- GUI interface
- Multi-scanner support
- Advanced image processing filters
- Scheduled scanning
- Network scanner support

### Planned Improvements
- Performance optimizations
- Enhanced error handling
- Better scanner compatibility
- Unit tests and CI/CD
- Documentation improvements
- Localization support

---

## Repository Information

- **GitHub**: [https://github.com/Pandiyarajk/pyautoscan](https://github.com/Pandiyarajk/pyautoscan)
- **Issues**: [https://github.com/Pandiyarajk/pyautoscan/issues](https://github.com/Pandiyarajk/pyautoscan/issues)
- **Releases**: [https://github.com/Pandiyarajk/pyautoscan/releases](https://github.com/Pandiyarajk/pyautoscan/releases)
- **Author**: Pandiyaraj Karuppasamy
- **Email**: pandiyarajk@live.com
- **License**: MIT
- **Last Updated**: August 27, 2025
