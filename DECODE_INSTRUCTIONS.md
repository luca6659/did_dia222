# Android APK XML Decoder Instructions

## Problem
You have binary XML files in `C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable\` that need to be converted to readable XML format.

## Solution

### Method 1: Using androguard (Recommended)

**Step 1: Install androguard**
```bash
pip install androguard
```

**Step 2: Run the decoder script**
```bash
python "C:\Users\yovra\Desktop\diia\decode_xml_v2.py"
```

This script will:
- Install androguard automatically if not present
- Read all binary XML files from the drawable directory
- Decode them to readable text XML
- Save them to `C:\Users\yovra\Desktop\diia\resources\decoded_drawables\`

### Method 2: Using apktool (Java-based)

**Requirements:**
- Java 8+ installed
- Download apktool

**Steps:**
```bash
# Download apktool (if not already available)
# From: https://bitbucket.org/iBotPeaches/apktool/downloads/

# Decode the drawable resources
java -jar apktool.jar d -r -s -f -o output_folder "C:\Users\yovra\Desktop\diia\resources\apk_extracted"
```

### Method 3: Manual execution

**Open Command Prompt (cmd.exe) and run:**

```bash
cd C:\Users\yovra\Desktop\diia
python decode_xml_v2.py
```

Then press Enter and wait for the script to complete.

## Expected Output

Once decoded, you'll have readable XML files in:
```
C:\Users\yovra\Desktop\diia\resources\decoded_drawables\
```

These will include:
- Tab bar icons (ic_tab_*)
- QR code icons (ic_qr*)
- Home icons (ic_home*)
- Button and control resources
- Drawable animations and vectors

## Troubleshooting

### If Python is not found
- Make sure Python is installed and in your PATH
- Try using `python3` instead of `python`
- Or use the full path to your Python executable

### If androguard installation fails
- Make sure you have internet connection
- Try: `pip install --upgrade androguard`
- Alternative: Use apktool method instead

### If you see "No module named 'androguard'"
- Install it: `pip install androguard`
- Check Python version: `python --version` (should be 3.6+)

## Files Created

The decode script has created the following files in this directory:
- `decode_xml.py` - Initial version
- `decode_xml_v2.py` - Improved version with better error handling
- `analyze_xml.py` - Analysis tool to check file types
- `run_decoder.bat` - Batch file to run the decoder

## Next Steps

1. Run the decoder script using one of the methods above
2. Check the output directory for decoded XML files
3. The XML files will be human-readable and can be edited/analyzed

## References

- androguard documentation: https://androguard.readthedocs.io/
- apktool documentation: https://ibotpeaches.github.io/Apktool/
- Android binary XML format info: https://android.googlesource.com/platform/frameworks/base/+/refs/heads/master/libs/androidfw/include/androidfw/ResourceTypes.h
