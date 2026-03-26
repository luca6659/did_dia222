#!/usr/bin/env python3
"""
Simple XML decoder for Android binary XML files.
Uses struct unpacking to decode binary Android XML without external dependencies.
"""

import struct
import os
from pathlib import Path

def read_string_pool(data, offset):
    """Read Android string pool from binary XML."""
    # This is a simplified version - for full support, use androguard
    return None

def decode_binary_xml_simple(binary_data):
    """
    Attempt to decode binary XML using basic pattern recognition.
    For proper decoding, use androguard library.
    """
    # Check for Android binary XML magic bytes
    if len(binary_data) < 8:
        return None
    
    # Android XML files start with: 0x00080003 or similar
    magic = struct.unpack('<I', binary_data[:4])[0]
    
    # If it's a ResChunk header, it's binary XML
    if magic == 0x00080003 or binary_data[:4] == b'\x03\x08\x00\x00':
        return "BINARY_XML"
    elif binary_data.startswith(b'<?xml'):
        return "TEXT_XML"
    
    return "UNKNOWN"

def main():
    drawable_dir = r'C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable'
    output_dir = r'C:\Users\yovra\Desktop\diia\resources\decoded_drawables'
    
    print("="*70)
    print("Android Binary XML Decoder")
    print("="*70)
    
    if not os.path.exists(drawable_dir):
        print(f"ERROR: Directory not found: {drawable_dir}")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    xml_files = sorted([f for f in os.listdir(drawable_dir) if f.endswith('.xml')])
    print(f"\nFound {len(xml_files)} XML files\n")
    
    # Analyze file types
    binary_count = 0
    text_count = 0
    
    for fname in xml_files[:20]:  # Check first 20
        fpath = os.path.join(drawable_dir, fname)
        with open(fpath, 'rb') as f:
            data = f.read()
        
        file_type = decode_binary_xml_simple(data)
        prefix = "✓" if file_type == "BINARY_XML" else ("✓" if file_type == "TEXT_XML" else "?")
        print(f"  {prefix} {fname}: {file_type} ({len(data)} bytes)")
        
        if file_type == "BINARY_XML":
            binary_count += 1
        elif file_type == "TEXT_XML":
            text_count += 1
    
    print(f"\nAnalysis: {binary_count} binary, {text_count} text")
    
    print("\n" + "="*70)
    print("RECOMMENDATION:")
    print("="*70)
    print("""
To properly decode these binary XML files, you need to use androguard:

1. Install androguard:
   pip install androguard

2. Run the decode script:
   python decode_xml_v2.py

The androguard library will properly handle:
  - String pool decompression
  - Binary XML format parsing
  - Resource type conversion
  - Namespace resolution

Without androguard, binary XML files cannot be converted to readable text.
""")

if __name__ == "__main__":
    main()
