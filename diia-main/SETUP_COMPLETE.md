# 🎯 Android APK XML Decoder - Complete Setup Guide

## What Was Created

I've created a complete toolkit to decode your binary Android XML files. Here's what's ready to use:

### 📋 Quick Reference

```
Your Location: C:\Users\yovra\Desktop\diia\

DECODER TOOLS:
├── 🟢 DECODE_XML.bat                ← START HERE (Windows)
├── 🐍 decode_apk_xml.py             ← OR run this with Python
├── 🐍 decode_xml_v2.py              ← Alternative version
├── 🐍 verify_setup.py               ← Check if everything works
└── 📖 DECODE_INSTRUCTIONS.md        ← Detailed guide

INPUT:
└── C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable\

OUTPUT (Created automatically):
└── C:\Users\yovra\Desktop\diia\resources\decoded_drawables\
```

## 🚀 How to Use

### Method 1: Windows Batch File (Easiest)
```
1. Open Windows File Explorer
2. Navigate to: C:\Users\yovra\Desktop\diia\
3. Find: DECODE_XML.bat
4. Double-click it
5. Wait for completion
6. Check: C:\Users\yovra\Desktop\diia\resources\decoded_drawables\
```

### Method 2: Command Prompt
```cmd
cd C:\Users\yovra\Desktop\diia
python decode_apk_xml.py
```

### Method 3: PowerShell
```powershell
cd C:\Users\yovra\Desktop\diia
python .\decode_apk_xml.py
```

### Verify Setup First (Optional)
```cmd
cd C:\Users\yovra\Desktop\diia
python verify_setup.py
```

## 📊 What Each Tool Does

### DECODE_XML.bat
- **Purpose**: Windows batch file wrapper
- **Best for**: Point-and-click operation
- **Pros**: No command line needed, auto-installs androguard
- **Run**: Double-click in File Explorer

### decode_apk_xml.py
- **Purpose**: Main decoder with full features
- **Best for**: Production use, detailed reporting
- **Pros**: Comprehensive error handling, progress tracking
- **Run**: `python decode_apk_xml.py`
- **Features**:
  - Auto-installs androguard if needed
  - Real-time progress counter
  - Summary statistics
  - Error logging

### verify_setup.py
- **Purpose**: Check if environment is ready
- **Best for**: Troubleshooting
- **Run**: `python verify_setup.py`
- **Checks**:
  - Python version
  - Directory existence
  - androguard installation
  - Decoder scripts presence

### analyze_xml.py
- **Purpose**: Analyze file formats without decoding
- **Best for**: Understanding file types
- **Run**: `python analyze_xml.py`

## ✅ Requirements

Before running, make sure you have:

- ✓ **Python 3.6 or higher**
  - Check: `python --version`
  - Get it: https://www.python.org/downloads/

- ✓ **Internet connection**
  - Needed to download androguard (one-time only)

- ✓ **Administrator access** (optional)
  - May be needed for pip install

## 📝 Step-by-Step Instructions

### Step 1: Install Python (if needed)
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or later
3. Run installer
4. **IMPORTANT**: Check "Add Python to PATH"
5. Click Install Now
6. Verify: Open Command Prompt and type `python --version`

### Step 2: Run the Decoder
**Option A - Batch File (Easiest):**
1. Open File Explorer
2. Go to C:\Users\yovra\Desktop\diia\
3. Double-click DECODE_XML.bat
4. Wait for completion

**Option B - Command Prompt:**
1. Press Win+R
2. Type: `cmd`
3. Type: `cd C:\Users\yovra\Desktop\diia`
4. Type: `python decode_apk_xml.py`
5. Press Enter

### Step 3: Check Results
1. Open File Explorer
2. Go to: C:\Users\yovra\Desktop\diia\resources\decoded_drawables\
3. You should see XML files with names like:
   - ic_home.xml
   - ic_tab_documents_selected.xml
   - ic_qr.xml
   - etc.

### Step 4: View Decoded XML
1. Right-click on any .xml file
2. Select "Open with" → "Notepad" (or your text editor)
3. You should see readable XML content

## 🐛 Troubleshooting

### Issue: "Python is not recognized"
**Solution:**
- Python is not installed or not in PATH
- Install Python from https://www.python.org/
- During installation, **CHECK** "Add Python to PATH"
- Restart your computer after installing
- Verify: `python --version`

### Issue: Script won't run or says "command not found"
**Solution:**
- Make sure you're in the right directory: `cd C:\Users\yovra\Desktop\diia`
- Try with full path: `python "C:\Users\yovra\Desktop\diia\decode_apk_xml.py"`
- Try with python3: `python3 decode_apk_xml.py`

### Issue: "No module named 'androguard'"
**Solution:**
- Install androguard manually:
  ```cmd
  python -m pip install androguard
  ```
- Or let the script install it automatically

### Issue: androguard installation fails
**Solution:**
- Check internet connection
- Try upgrading pip first:
  ```cmd
  python -m pip install --upgrade pip
  python -m pip install androguard
  ```
- Run Command Prompt as Administrator
- Try with different pip options:
  ```cmd
  pip install --no-cache-dir androguard
  ```

### Issue: Output directory is empty
**Solution:**
- Check source directory exists: `C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable\`
- Check it contains XML files
- Run verify_setup.py to diagnose
- Check file permissions in source directory
- Try running script as Administrator

### Issue: Script runs but seems hung
**Solution:**
- Script may be processing large number of files
- Check CPU usage in Task Manager (should be active)
- Wait - this is normal for 1000+ files
- Don't interrupt unless sure it's stuck (5+ minutes of no activity = stuck)

### Issue: Only partial results decoded
**Solution:**
- Some files may have failed (see error output)
- This is normal - not all binary formats may decode
- Check the summary at the end for count
- Failed files are likely already in text XML format

## 🔍 Verification Steps

### Verify Python is installed
```cmd
python --version
```
Expected: `Python 3.x.x`

### Verify androguard is installed
```cmd
python -c "import androguard; print('OK')"
```
Expected: `OK`

### Verify source directory has files
```cmd
dir "C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable" | find ".xml"
```
Expected: List of .xml files

### Verify decoder scripts exist
```cmd
dir "C:\Users\yovra\Desktop\diia\*.py"
```
Expected: List includes decode_apk_xml.py, verify_setup.py, etc.

## 📚 What Will Be Decoded

The tool will decode vector drawables used for:
- Tab bar icons (ic_tab_*)
- Menu icons (ic_menu_*)
- QR code icons (ic_qr*)
- Button states (mtrl_*, abc_*)
- UI elements and animations
- Notification icons
- Navigation elements

Example output:
```xml
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="@android:color/white"
        android:pathData="M12,2C6.48,2 2,6.48 2,12s4.48,10 10,10 10,-4.48 10,-10S17.52,2 12,2m0,3c1.66,0 3,1.34 3,3s-1.34,3 -3,3 -3,-1.34 -3,-3 1.34,-3 3,-3m0,14.2c-2.5,0 -4.71,-1.28 -6,-3.22 0.03,-1.99 4,-3.08 6,-3.08 1.99,0 5.97,1.09 6,3.08 -1.29,1.94 -3.5,3.22 -6,3.22z" />
</vector>
```

## 📖 Documentation Files

- **README_DECODER.txt**: Comprehensive guide
- **DECODE_INSTRUCTIONS.md**: Alternative detailed instructions
- **This file**: Quick setup and reference

## 🔗 Related Tools

If you need advanced features:

### apktool (Java-based alternative)
```cmd
java -jar apktool.jar d -r -s resources\apk_extracted
```

### androguard (Python alternative)
```python
from androguard.core.axml import AXMLPrinter
axml = AXMLPrinter(open("file.xml", "rb").read())
print(axml.get_xml())
```

## ⏱️ Expected Runtime

- **First run**: 2-5 minutes (includes androguard installation)
- **Subsequent runs**: 30 seconds - 2 minutes (depending on file count)
- **Speed factors**:
  - Number of XML files (you have 1000+)
  - Computer speed
  - Disk speed

## 📊 Success Indicators

You'll know it worked when you see:
- ✓ Progress counter showing processed files
- ✓ Summary showing "X decoded, 0 failed"
- ✓ Output directory contains XML files
- ✓ XML files open in text editor and show XML content

## 🎓 Educational Note

This decoder shows how Android compiles XML resources:
- **Source**: Human-readable XML
- **APK storage**: Binary format (compressed, indexed, efficient)
- **Decoded**: Back to human-readable format

This process is fundamental to Android reverse engineering and app analysis.

## 📞 Support

If you get stuck:
1. Run `python verify_setup.py` to diagnose issues
2. Check the troubleshooting section above
3. Read DECODE_INSTRUCTIONS.md for more details
4. Check androguard documentation: https://androguard.readthedocs.io/

---

## Summary

```
✓ Python 3.6+ installed
✓ Source files ready: C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable\
✓ Decoder scripts created: DECODE_XML.bat + Python scripts
✓ Documentation ready: README_DECODER.txt + DECODE_INSTRUCTIONS.md

NEXT STEP: Run DECODE_XML.bat or python decode_apk_xml.py

EXPECTED OUTPUT: C:\Users\yovra\Desktop\diia\resources\decoded_drawables\
```

You're ready to go! 🚀
