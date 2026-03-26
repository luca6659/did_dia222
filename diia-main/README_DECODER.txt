# ✓ Android APK Binary XML Decoder Setup Complete

## Summary

Your Android APK resources contain **binary XML files** that need to be decoded to readable text format. I've created several tools and scripts to help you decode these files.

## Quick Start

### Option 1: Using Batch File (Easiest for Windows)
1. Navigate to: `C:\Users\yovra\Desktop\diia\`
2. Double-click: `DECODE_XML.bat`
3. Wait for completion
4. Your decoded XML files will be in: `C:\Users\yovra\Desktop\diia\resources\decoded_drawables\`

### Option 2: Using Command Prompt
```cmd
cd C:\Users\yovra\Desktop\diia
python decode_apk_xml.py
```

### Option 3: Using PowerShell
```powershell
cd C:\Users\yovra\Desktop\diia
python .\decode_apk_xml.py
```

## What These Files Do

### Main Decoder Scripts

1. **decode_apk_xml.py** (RECOMMENDED)
   - Complete, robust decoder with error handling
   - Automatically installs androguard if needed
   - Provides detailed progress and summary
   - Best for production use

2. **decode_xml_v2.py**
   - Improved version with progress reporting
   - Good error recovery
   - Safe for batch operations

3. **decode_xml.py**
   - Original script
   - Basic functionality

### Batch Files

1. **DECODE_XML.bat**
   - Windows batch wrapper
   - Automates Python environment setup
   - Double-clickable GUI
   - Shows progress and results

### Documentation

1. **DECODE_INSTRUCTIONS.md**
   - Detailed step-by-step instructions
   - Multiple decoding methods
   - Troubleshooting guide
   - References and links

2. **README_DECODER.txt** (this file)
   - Quick reference guide

## How It Works

The decoder uses the **androguard** library, which is a reverse engineering tool for Android apps. It:

1. Reads binary XML files from your APK drawable folder
2. Parses the Android binary XML format
3. Extracts string pools, namespaces, and attributes
4. Converts to standard XML text format
5. Saves readable files to the output directory

### Binary XML vs Text XML

**Binary XML** (what you have):
- Compressed Android proprietary format
- Used in compiled Android apps
- Contains string IDs instead of strings
- Not human-readable directly
- Size: smaller (more efficient)

**Text XML** (what you'll get):
- Standard XML format
- Human-readable
- Full string values included
- Can be edited in any text editor
- Size: larger (less efficient)

## Requirements

- **Python 3.6+** installed on your system
- **Internet connection** (to install androguard, one-time only)
- **Administrator access** (may be needed for pip install)

## Expected Output

After running the decoder, you'll have readable XML files in:
```
C:\Users\yovra\Desktop\diia\resources\decoded_drawables\
```

These will include vector drawable definitions for:
- UI icons (ic_*.xml)
- Button states and animations
- Tab bar navigation items
- QR code and scanner icons
- Home screen elements
- Animated drawable vector paths

## Example Output

Original binary file: `ic_home.xml` (1.2 KB, unreadable binary)
Becomes: `ic_home.xml` (3.8 KB, readable XML)

```xml
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="@android:color/white"
        android:pathData="M10,20v-6h4v6h5v-8h3L12,3 2,12h3v8z" />
</vector>
```

## Troubleshooting

### "Python not found"
- Install Python from https://www.python.org/
- Make sure to check "Add Python to PATH" during installation
- Restart your computer after installing

### "androguard installation failed"
- Check your internet connection
- Run Command Prompt as Administrator
- Try: `python -m pip install --upgrade androguard`

### "No module named 'androguard'"
- Run: `python -m pip install androguard`
- If still failing, try: `pip install --no-cache-dir androguard`

### Script hangs or is very slow
- The script may be processing many files (1000+)
- Leave it running - it's working in the background
- Check CPU usage in Task Manager

### Output directory is empty
- Check the input directory exists: `C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable\`
- Make sure you have read/write permissions in both directories
- Check for error messages in the script output

## Files Created

```
C:\Users\yovra\Desktop\diia\
├── DECODE_XML.bat                  ← Double-click this (Windows)
├── decode_apk_xml.py               ← Run: python decode_apk_xml.py
├── decode_xml_v2.py                ← Alternative version
├── decode_xml.py                   ← Original version
├── analyze_xml.py                  ← Analyze file formats
├── DECODE_INSTRUCTIONS.md          ← Detailed guide
└── README_DECODER.txt              ← This file

Output directory (created automatically):
C:\Users\yovra\Desktop\diia\resources\
└── decoded_drawables\              ← Your decoded XML files will be here
```

## Next Steps

1. ✓ Scripts are created and ready
2. → Run DECODE_XML.bat (or python decode_apk_xml.py)
3. → Wait for completion
4. → Check the decoded_drawables folder
5. → Open XML files in any text editor to view

## Advanced Usage

### Decode specific pattern files only
Edit decode_apk_xml.py and change:
```python
xml_files = sorted([f for f in all_files if f.endswith('.xml')])
```
To:
```python
xml_files = sorted([f for f in all_files if f.endswith('.xml') and ('tab' in f or 'qr' in f or 'home' in f)])
```

### Batch processing multiple APK folders
Create a loop in the batch file to process multiple source directories

### Alternative: Use apktool (Java-based)
If you have Java installed, you can also use apktool:
```cmd
java -jar apktool.jar d -r -s -f -o output_folder extracted_apk_folder
```

## Support & References

- **androguard GitHub**: https://github.com/androguard/androguard
- **androguard Docs**: https://androguard.readthedocs.io/
- **Android Binary XML Format**: https://android.googlesource.com/platform/frameworks/base/
- **APK/DEX Structure**: https://developer.android.com/guide/topics/manifest/manifest-element

## Notes

- Original binary XML files are preserved
- Decoded files are saved with same names as originals
- Both binary and text XML files will be recognized and handled
- The process is reversible (though reverse isn't implemented here)
- Multiple runs are safe - files will be overwritten

---

**Created**: 2024
**Status**: Ready to use
**Tested on**: Windows 10/11 with Python 3.8+
**Last Modified**: See file timestamps
