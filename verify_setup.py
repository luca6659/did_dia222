#!/usr/bin/env python3
"""
Verification script to check if everything is set up correctly for decoding
"""

import os
import sys
import subprocess

def check_python():
    """Check Python version."""
    print("1. Checking Python installation...")
    version = sys.version_info
    print(f"   ✓ Python {version.major}.{version.minor}.{version.micro} found")
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("   ✗ WARNING: Python 3.6+ required, but you have Python {}.{}".format(
            version.major, version.minor))
        return False
    return True

def check_directories():
    """Check if directories exist."""
    print("\n2. Checking directories...")
    
    source = r'C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable'
    output_base = r'C:\Users\yovra\Desktop\diia\resources'
    
    if os.path.exists(source):
        xml_count = len([f for f in os.listdir(source) if f.endswith('.xml')])
        print(f"   ✓ Source directory exists: {source}")
        print(f"     └─ Contains {xml_count} XML files")
    else:
        print(f"   ✗ Source directory NOT found: {source}")
        return False
    
    if os.path.exists(output_base):
        print(f"   ✓ Output base directory exists: {output_base}")
    else:
        print(f"   ✗ Output base directory NOT found: {output_base}")
        return False
    
    return True

def check_androguard():
    """Check if androguard is installed."""
    print("\n3. Checking androguard library...")
    try:
        import androguard
        print(f"   ✓ androguard is installed (version: {androguard.__version__ if hasattr(androguard, '__version__') else 'unknown'})")
        return True
    except ImportError:
        print("   ✗ androguard is NOT installed")
        print("     → Run: python -m pip install androguard")
        return False

def check_pip():
    """Check if pip is available."""
    print("\n4. Checking pip...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"   ✓ pip is available")
            print(f"     └─ {result.stdout.strip()}")
            return True
        else:
            print("   ✗ pip is not working properly")
            return False
    except Exception as e:
        print(f"   ✗ Error checking pip: {e}")
        return False

def check_decoder_scripts():
    """Check if decoder scripts exist."""
    print("\n5. Checking decoder scripts...")
    
    scripts = [
        (r'C:\Users\yovra\Desktop\diia\decode_apk_xml.py', 'Main decoder (recommended)'),
        (r'C:\Users\yovra\Desktop\diia\decode_xml_v2.py', 'Alternative decoder'),
        (r'C:\Users\yovra\Desktop\diia\DECODE_XML.bat', 'Windows batch file'),
    ]
    
    all_exist = True
    for script_path, description in scripts:
        if os.path.exists(script_path):
            size = os.path.getsize(script_path)
            print(f"   ✓ {description}: {script_path} ({size} bytes)")
        else:
            print(f"   ✗ {description}: NOT found at {script_path}")
            all_exist = False
    
    return all_exist

def main():
    """Run all checks."""
    print("="*80)
    print("ANDROID APK XML DECODER - VERIFICATION SCRIPT")
    print("="*80)
    print()
    
    checks = [
        ("Python", check_python),
        ("Directories", check_directories),
        ("Pip", check_pip),
        ("androguard", check_androguard),
        ("Decoder scripts", check_decoder_scripts),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"   ✗ Error during {name} check: {e}")
            results.append((name, False))
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {name}")
    
    print(f"\nTotal: {passed}/{total} checks passed")
    
    print("\n" + "="*80)
    if passed == total:
        print("✓ READY TO DECODE!")
        print("\nRun one of these commands:")
        print("  1. python decode_apk_xml.py")
        print("  2. DECODE_XML.bat (Windows GUI)")
        print("  3. python decode_xml_v2.py (Alternative)")
        return 0
    else:
        print("✗ SETUP INCOMPLETE - Please fix the issues above")
        
        if not any(name == "androguard" and result for name, result in results):
            print("\nTo install androguard:")
            print("  python -m pip install androguard")
        
        return 1

if __name__ == "__main__":
    sys.exit(main())
