"""
Извлекает SVG pathData из бинарных Android XML файлов без androguard.
Парсит текстовые строки прямо из бинарника.
"""
import re, os

DRAWABLE = r"C:\Users\yovra\Desktop\diia\resources\apk_extracted\res\drawable"
OUTPUT = r"C:\Users\yovra\Desktop\diia\resources\decoded_drawables"
os.makedirs(OUTPUT, exist_ok=True)

FILES = [
    "ic_tab_feed_selected.xml",
    "ic_tab_feed_unselected.xml", 
    "ic_tab_documents_selected.xml",
    "ic_tab_documents_unselected.xml",
    "ic_tab_services_selected.xml",
    "ic_tab_services_unselected.xml",
    "ic_tab_menu_selected.xml",
    "ic_tab_menu_unselected.xml",
    "trident_white.xml",
    "trident.xml",
    "ic_logo_diia_gerb_white.xml",
    "ic_qr.xml",
    "ic_qr_white.xml",
    "ic_ps_bonds.xml",
    "ic_home.xml",
    "ic_homedoc.xml",
    "ic_failed_connection.xml",
    "ic_search.xml",
    "ic_search_black.xml",
    "ic_notifications.xml",
    "ic_menu.xml",
    "ic_menu_services.xml",
    "ic_document.xml",
    "usermale.xml",
    "qr_scan.xml",
    "ic_arrow.xml",
    "ic_arrow_back.xml",
    "diia_ic_scanner.xml",
    "ic_check_shield.xml",
]

# Regex для pathData (SVG path commands)
path_re = re.compile(rb'(M[\d\.\-,\s]+(?:[MLHVCSQTAZ][\d\.\-,\s]*)*Z?)', re.IGNORECASE)
# Regex для числовых значений (width/height/viewport)
num_attrs = re.compile(rb'(height|width|viewportWidth|viewportHeight|fillColor|strokeColor|strokeWidth)')

results = {}

for fname in FILES:
    fpath = os.path.join(DRAWABLE, fname)
    if not os.path.exists(fpath):
        print(f"[!] Не найден: {fname}")
        continue
    
    with open(fpath, 'rb') as f:
        data = f.read()
    
    # Extract all readable strings
    strings = re.findall(rb'[\x20-\x7E]{4,}', data)
    
    paths = []
    for s in strings:
        s_str = s.decode('ascii', errors='ignore')
        # pathData starts with M and contains coordinates
        if re.match(r'^M[\d\.\-]', s_str) and len(s_str) > 10:
            paths.append(s_str)
    
    # Write result
    out_path = os.path.join(OUTPUT, fname.replace('.xml', '.txt'))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"File: {fname}\n")
        f.write(f"Paths found: {len(paths)}\n\n")
        for i, p in enumerate(paths):
            f.write(f"Path {i+1}:\n{p}\n\n")
    
    results[fname] = paths
    print(f"[OK] {fname}: {len(paths)} paths")
    for i, p in enumerate(paths):
        preview = p[:80] + ('...' if len(p) > 80 else '')
        print(f"     path{i+1}: {preview}")

# Summary
print(f"\n{'='*60}")
print(f"Обработано: {len(results)} файлов")
print(f"Результат: {OUTPUT}")
print(f"\nДля использования в SVG:")
print(f'<svg viewBox="0 0 24 24"><path d="..." fill="#000"/></svg>')

# Also write a combined HTML preview
html_path = os.path.join(OUTPUT, "preview.html")
with open(html_path, 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html><html><head><style>')
    f.write('body{font-family:sans-serif;background:#f0f0f0;padding:20px}')
    f.write('.grid{display:grid;grid-template-columns:repeat(auto-fill,120px);gap:16px}')
    f.write('.item{background:#fff;border-radius:12px;padding:12px;text-align:center}')
    f.write('.item svg{width:48px;height:48px;display:block;margin:0 auto 8px}')
    f.write('.item span{font-size:10px;word-break:break-all}')
    f.write('</style></head><body>')
    f.write('<h1>Decoded Дія Icons</h1><div class="grid">')
    
    for fname, paths in results.items():
        if paths:
            f.write(f'<div class="item">')
            f.write(f'<svg viewBox="0 0 24 24">')
            for p in paths:
                f.write(f'<path d="{p}" fill="#000"/>')
            f.write(f'</svg>')
            f.write(f'<span>{fname.replace(".xml","")}</span>')
            f.write(f'</div>')
    
    f.write('</div></body></html>')

print(f"\nHTML превью: {html_path}")
