# PyAutoScan

[![GitHub](https://img.shields.io/badge/GitHub-PyAutoScan-blue?style=for-the-badge&logo=github)](https://github.com/Pandiyarajk/pyautoscan)
[![PyPI version](https://img.shields.io/pypi/v/pyautoscan.svg)](https://pypi.org/project/pyautoscan/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Build PyAutoScan Executable](https://github.com/Pandiyarajk/pyautoscan/actions/workflows/build.yml/badge.svg)](https://github.com/Pandiyarajk/pyautoscan/actions/workflows/build.yml)


A Python-based Windows scanning automation tool for printer/scanner devices using WIA.

PyAutoScan simplifies the process of scanning documents with HP and other printer devices that support WIA (Windows Image Acquisition). It provides:

- One-click auto-scan with customizable quality (low/medium/high)
- Image-to-PDF conversion for multi-page documents
- Configurable settings via scan_config.ini (resolution, color mode, auto-crop, deskew, output folder, etc.)
- Automatic file naming with timestamps
- Scanner info extraction (model, driver properties, max resolution, supported features)
- Optional auto-crop & deskew for cleaner scans

Works with HP and other multi-function printer devices (MFP) that expose their scanner through WIA.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Pandiyarajk/pyautoscan.git
cd pyautoscan

# Install dependencies
pip install -r requirements.txt

# Test scanner connection
python scanner_info.py

# Start scanning
python basic_scan.py
```

## 🚀 Features

- **Basic Scanning**: Simple, fast scanning with configurable quality and format options
- **Advanced Scanning**: Enhanced scanning with auto-crop and deskew capabilities
- **Multiple Formats**: Support for JPG, PNG, TIFF, and PDF output
- **Quality Control**: Configurable DPI settings (150, 300, 600)
- **Scanner Detection**: Automatic scanner detection and information display
- **Configuration Management**: INI-based configuration for easy customization
- **PDF Conversion**: Convert multiple images to single PDF documents
- **Windows Integration**: Native Windows WIA (Windows Image Acquisition) support

## 📋 Requirements

- Windows 10/11
- Python 3.7+ (Tested on Python 3.13)
- Compatible scanner with WIA drivers (Tested on HP Printer scanner features)
- Required Python packages (see `requirements.txt`)

## 📋 Dependencies

- **pywin32**: Windows COM integration for WIA
- **Pillow**: Image processing and PDF creation
- **powerlogger**: Enhanced logging with Rich console output and file rotation

## 🛠️ Installation

### Option 1: Clone from GitHub
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pandiyarajk/pyautoscan.git
   cd pyautoscan
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify scanner connection:**
   ```bash
   python scanner_info.py
   ```

### Option 2: Install via pip (when published to PyPI)
```bash
pip install pyautoscan
```

### Option 3: Download Release
Download the latest release from [GitHub Releases](https://github.com/Pandiyarajk/pyautoscan/releases) for pre-built Windows executables.

## 📖 Usage

### Basic Scanning
```bash
python basic_scan.py
```

### Advanced Scanning
```bash
python advanced_scan.py
```

### Scanner Information
```bash
python scanner_info.py
```

### Configuration
Edit `scan_config.ini` to customize:
- Output directory
- File format preferences
- Quality settings
- Auto-processing options

## 🔧 Configuration

The `scan_config.ini` file allows you to customize:

```ini
[SCAN]
output_dir = Scans
file_format = jpg
quality = medium
auto_crop = true
deskew = true
color_mode = 1
combine_pdf = false
```

### Quality Settings
- **Low**: 150 DPI (fast, smaller files)
- **Medium**: 300 DPI (balanced)
- **High**: 600 DPI (high quality, larger files)

### Supported Formats
- **JPG**: Compressed, good for documents
- **PNG**: Lossless, good for images
- **TIFF**: High quality, large files
- **PDF**: Portable document format

## 📁 Project Structure

```
pyautoscan/
├── basic_scan.py          # Basic scanning functionality
├── advanced_scan.py       # Advanced scanning with auto-processing
├── scanner_info.py        # Scanner detection and information
├── scan_config.ini        # Configuration file
├── requirements.txt       # Python dependencies
├── setup.py               # PyPI distribution setup
├── README.md             # This file
├── CHANGELOG.md          # Version history
├── TESTING.md            # Testing documentation and results
├── LICENSE               # MIT License
├── .github/workflows/    # GitHub Actions CI/CD
├── .gitignore            # Git ignore file
├── run_scanner.bat       # Windows batch launcher
└── Scans/                # Output directory for scanned files
```

## 🔧 Development

### Repository
- **GitHub**: [https://github.com/Pandiyarajk/pyautoscan](https://github.com/Pandiyarajk/pyautoscan)
- **Issues**: [https://github.com/Pandiyarajk/pyautoscan/issues](https://github.com/Pandiyarajk/pyautoscan/issues)
- **Releases**: [https://github.com/Pandiyarajk/pyautoscan/releases](https://github.com/Pandiyarajk/pyautoscan/releases)

### Build Status
The project uses GitHub Actions for continuous integration:
- **Build**: Windows executables for Python 3.8-3.13
- **Test**: Automated testing on Windows with Python 3.13
- **Release**: Automatic builds on releases

## 🚀 Building Executables

### Using PyInstaller
```bash
# Install PyInstaller
pip install pyinstaller

# Build basic scanner
pyinstaller --onefile --windowed basic_scan.py

# Build advanced scanner
pyinstaller --onefile --windowed advanced_scan.py
```

**Note:** Successfully tested with Python 3.13 and HP Printer scanner features.

### Using GitHub Actions
The repository includes a GitHub Actions workflow that automatically builds Windows executables on each release.

## 🔍 Troubleshooting

### Common Issues

1. **"No scanner detected"**
   - Ensure scanner is connected and powered on
   - Verify WIA drivers are installed
   - Run `scanner_info.py` to test connection

2. **Permission errors**
   - Run as administrator if needed
   - Check Windows security settings

3. **Format not supported**
   - Verify scanner supports requested format
   - Check `scanner_info.py` output for supported formats

### Scanner Compatibility
This tool works with any scanner that supports Windows WIA (Windows Image Acquisition). Most modern scanners are compatible.

**Tested Hardware:**
- HP Printer scanner features (confirmed working)
- Windows WIA drivers
- Python 3.13 compatibility verified

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Repository**: [https://github.com/Pandiyarajk/pyautoscan](https://github.com/Pandiyarajk/pyautoscan)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Pandiyaraj Karuppasamy**  
Email: pandiyarajk@live.com  
Date: 27-Aug-2025

## 🙏 Acknowledgments

- Windows WIA (Windows Image Acquisition) API
- Python Imaging Library (PIL/Pillow)
- pywin32 for Windows COM integration
- [PowerLogger](https://pypi.org/project/powerlogger/) for enhanced logging capabilities

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on [GitHub](https://github.com/Pandiyarajk/pyautoscan/issues)
- Check the troubleshooting section above
- Verify your scanner compatibility

---

**Note**: This tool is designed specifically for Windows systems and requires a compatible scanner with WIA drivers.
