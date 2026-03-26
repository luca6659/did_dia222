#!/usr/bin/env python3
"""
Complete Android Binary XML Decoder
Decodes binary XML files extracted from APK to readable text format
Usage: python decode_apk_xml.py
"""

import os
import sys
import subprocess

def install_androguard():
    """Install androguard if not already installed."""
    try:
        import androguard
        return True
    except ImportError:
        print("Installing androguard...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "androguard"])
            print("✓ androguard installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("✗ Failed to install androguard")
            return False

def decode_xml_files():
    """Main decoder function."""
    
    # Import androguard
    try:
        from androguard.core.axml import AXMLPrinter
    except ImportError:
        print("ERROR: androguard not available")
        if not install_androguard():
            print("\nPlease install androguard manually:")
            print("  pip install androguard")
            return False
        from androguard.core.axml import AXMLPrinter
    
    # Define paths
    drawable_dir = r'C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable'
    output_dir = r'C:\Users\yovra\Desktop\diia\resources\decoded_drawables'
    
    print("\n" + "="*80)
    print("ANDROID BINARY XML DECODER")
    print("="*80)
    print(f"Source: {drawable_dir}")
    print(f"Output: {output_dir}")
    print("="*80 + "\n")
    
    # Validate directories
    if not os.path.exists(drawable_dir):
        print(f"ERROR: Source directory not found: {drawable_dir}")
        return False
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all XML files
    all_files = os.listdir(drawable_dir)
    xml_files = sorted([f for f in all_files if f.endswith('.xml')])
    
    print(f"Found {len(xml_files)} XML files to process\n")
    print("Progress:")
    print("-" * 80)
    
    success = 0
    failed = 0
    skipped = 0
    errors = []
    
    for idx, filename in enumerate(xml_files, 1):
        filepath = os.path.join(drawable_dir, filename)
        outpath = os.path.join(output_dir, filename)
        
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            
            # Check if file is already text XML
            if data.startswith(b'<?xml'):
                with open(outpath, 'wb') as f:
                    f.write(data)
                print(f"[{idx:4d}/{len(xml_files)}] ✓ {filename:50s} [TEXT]")
                success += 1
                continue
            
            # Decode binary XML
            try:
                axml = AXMLPrinter(data)
                xml_string = axml.get_xml()
                
                # Handle both string and bytes return types
                if isinstance(xml_string, str):
                    xml_bytes = xml_string.encode('utf-8')
                else:
                    xml_bytes = xml_string
                
                # Write decoded XML
                with open(outpath, 'wb') as f:
                    f.write(xml_bytes)
                
                print(f"[{idx:4d}/{len(xml_files)}] ✓ {filename:50s} [BINARY]")
                success += 1
                
            except Exception as e:
                errors.append((filename, str(e)))
                print(f"[{idx:4d}/{len(xml_files)}] ✗ {filename:50s} ERROR: {str(e)[:30]}")
                failed += 1
        
        except Exception as e:
            errors.append((filename, str(e)))
            print(f"[{idx:4d}/{len(xml_files)}] ✗ {filename:50s} ERROR: {str(e)[:30]}")
            failed += 1
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total files:    {len(xml_files)}")
    print(f"Decoded:        {success}")
    print(f"Failed:         {failed}")
    print(f"Skipped:        {skipped}")
    print(f"Success rate:   {100*success//len(xml_files)}%")
    print(f"Output dir:     {output_dir}")
    print("="*80)
    
    if errors and len(errors) <= 10:
        print("\nErrors:")
        for filename, error in errors:
            print(f"  {filename}: {error}")
    
    # Verify output
    decoded_files = os.listdir(output_dir)
    print(f"\nDecoded files in output directory: {len(decoded_files)}")
    if decoded_files:
        print("\nSample files (first 5):")
        for f in sorted(decoded_files)[:5]:
            size = os.path.getsize(os.path.join(output_dir, f))
            print(f"  {f} ({size} bytes)")
        if len(decoded_files) > 5:
            print(f"  ... and {len(decoded_files) - 5} more")
    
    return failed == 0

if __name__ == "__main__":
    try:
        success = decode_xml_files()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nDecoding cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nFATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
