#!/usr/bin/env python3
"""Decode binary XML files from Android APK resources."""

import os
import sys

# Try to import androguard
try:
    from androguard.core.axml import AXMLPrinter
    print("androguard imported successfully")
except ImportError as e:
    print(f"Error importing androguard: {e}")
    print("Attempting to install androguard...")
    os.system("pip install androguard")
    try:
        from androguard.core.axml import AXMLPrinter
        print("androguard installed and imported successfully")
    except ImportError as e:
        print(f"Failed to import androguard after installation: {e}")
        sys.exit(1)

drawable_dir = r'C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable'
output_dir = r'C:\Users\yovra\Desktop\diia\resources\decoded_drawables'

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Get list of files to decode
all_files = os.listdir(drawable_dir)
print(f"Found {len(all_files)} files in drawable directory")

# Decode specific patterns (tab, qr, home, etc.) or all XML files
target_files = [f for f in all_files if f.endswith('.xml')]
print(f"Found {len(target_files)} XML files")

success_count = 0
fail_count = 0
failed_files = []

for fname in target_files:
    filepath = os.path.join(drawable_dir, fname)
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            # Check if it looks like binary XML (starts with specific magic bytes)
            if data[:4] == b'\x00\x08\x00\x70' or data[:4] == b'\x00\x10\x08\x00':
                axml = AXMLPrinter(data)
                xml_text = axml.get_xml()
                out_path = os.path.join(output_dir, fname + '.decoded')
                with open(out_path, 'wb') as out:
                    out.write(xml_text)
                print(f'✓ Decoded: {fname}')
                success_count += 1
            else:
                # Try anyway - might be text XML already
                try:
                    axml = AXMLPrinter(data)
                    xml_text = axml.get_xml()
                    out_path = os.path.join(output_dir, fname + '.decoded')
                    with open(out_path, 'wb') as out:
                        out.write(xml_text)
                    print(f'✓ Decoded: {fname}')
                    success_count += 1
                except Exception as e:
                    # Check if it's already text XML
                    try:
                        if data.startswith(b'<?xml'):
                            out_path = os.path.join(output_dir, fname + '.decoded')
                            with open(out_path, 'wb') as out:
                                out.write(data)
                            print(f'✓ Already XML: {fname}')
                            success_count += 1
                        else:
                            failed_files.append((fname, str(e)))
                            fail_count += 1
                    except:
                        failed_files.append((fname, "Unknown format"))
                        fail_count += 1
    except Exception as e:
        print(f'✗ Failed: {fname} - {e}')
        failed_files.append((fname, str(e)))
        fail_count += 1

print(f"\n{'='*60}")
print(f"Decode completed!")
print(f"Success: {success_count}, Failed: {fail_count}")
print(f"Output directory: {output_dir}")

if failed_files:
    print(f"\nFailed files ({len(failed_files)}):")
    for fname, error in failed_files[:10]:  # Show first 10
        print(f"  - {fname}: {error}")
    if len(failed_files) > 10:
        print(f"  ... and {len(failed_files) - 10} more")
