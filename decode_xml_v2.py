#!/usr/bin/env python3
"""Decode binary XML files from Android APK resources - with better error handling."""

import os
import sys
import subprocess

# First, try to install androguard if not available
try:
    from androguard.core.axml import AXMLPrinter
except ImportError:
    print("Installing androguard...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "androguard"])
    from androguard.core.axml import AXMLPrinter

drawable_dir = r'C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable'
output_dir = r'C:\Users\yovra\Desktop\diia\resources\decoded_drawables'

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Get list of files to decode
all_files = os.listdir(drawable_dir)
print(f"Found {len(all_files)} files in drawable directory")

# Decode all XML files
target_files = sorted([f for f in all_files if f.endswith('.xml')])
print(f"Found {len(target_files)} XML files to decode\n")

success_count = 0
fail_count = 0
failed_files = []

for i, fname in enumerate(target_files, 1):
    filepath = os.path.join(drawable_dir, fname)
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            
        # Try to decode with androguard
        try:
            axml = AXMLPrinter(data)
            xml_text = axml.get_xml()
            
            # Save decoded file
            out_path = os.path.join(output_dir, fname)
            with open(out_path, 'wb') as out:
                out.write(xml_text if isinstance(xml_text, bytes) else xml_text.encode('utf-8'))
            
            print(f'[{i:3d}/{len(target_files)}] ✓ {fname}')
            success_count += 1
        except Exception as decode_error:
            # Check if already text XML
            if data.startswith(b'<?xml'):
                out_path = os.path.join(output_dir, fname)
                with open(out_path, 'wb') as out:
                    out.write(data)
                print(f'[{i:3d}/{len(target_files)}] ✓ {fname} (already text XML)')
                success_count += 1
            else:
                raise decode_error
                
    except Exception as e:
        print(f'[{i:3d}/{len(target_files)}] ✗ {fname} - {str(e)[:50]}')
        failed_files.append((fname, str(e)))
        fail_count += 1

print(f"\n{'='*70}")
print(f"Decode Complete: {success_count} succeeded, {fail_count} failed")
print(f"Output directory: {output_dir}")

if failed_files and len(failed_files) <= 5:
    print(f"\nFailed files:")
    for fname, error in failed_files:
        print(f"  - {fname}: {error[:100]}")

# List some sample decoded files
if success_count > 0:
    decoded_files = os.listdir(output_dir)
    print(f"\nSample decoded files:")
    for fname in sorted(decoded_files)[:5]:
        fpath = os.path.join(output_dir, fname)
        size = os.path.getsize(fpath)
        print(f"  - {fname} ({size} bytes)")
    if len(decoded_files) > 5:
        print(f"  ... and {len(decoded_files) - 5} more files")
