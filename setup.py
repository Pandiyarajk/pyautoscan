"""
PyAutoScan - Windows Scanner Automation Tool
Setup configuration for PyPI distribution
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pyautoscan",
    version="1.0.0",
    author="Pandiyaraj Karuppasamy",
    author_email="pandiyarajk@live.com",
    description="A Python-based Windows scanning automation tool for printer/scanner devices using WIA",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pandiyarajk/pyautoscan",
    project_urls={
        "Bug Tracker": "https://github.com/Pandiyarajk/pyautoscan/issues",
        "Documentation": "https://github.com/Pandiyarajk/pyautoscan#readme",
        "Source Code": "https://github.com/Pandiyarajk/pyautoscan",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Graphics :: Capture :: Scanners",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "pyinstaller>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pyautoscan=basic_scan:auto_scan",
            "pyautoscan-advanced=advanced_scan:auto_scan",
            "pyautoscan-info=scanner_info:get_scanner_info",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "scanner",
        "scanning",
        "windows",
        "wia",
        "automation",
        "printer",
        "document",
        "image",
        "pdf",
        "ocr",
        "deskew",
        "auto-crop",
    ],
    platforms=["Windows"],
    license="MIT",
    license_files=["LICENSE"],
)
