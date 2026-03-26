"""
Декодер иконок из APK Дії.
Запусти: pip install androguard && python decode_icons.py
"""
import os, sys, zipfile, shutil, glob as globmod

try:
    from androguard.core.axml import AXMLPrinter
except ImportError:
    print("[*] Устанавливаю androguard...")
    os.system(f'"{sys.executable}" -m pip install androguard')
    from androguard.core.axml import AXMLPrinter

BASE = r"C:\Users\yovra\Desktop\diia"
DRAWABLE = os.path.join(BASE, "resources", "apk_extracted", "res", "drawable")
OUTPUT = os.path.join(BASE, "resources", "decoded_drawables")
os.makedirs(OUTPUT, exist_ok=True)

# --- Шаг 1: Проверяем XAPK ---
xapk_files = globmod.glob(os.path.join(BASE, "*.xapk")) + globmod.glob(os.path.join(BASE, "resources", "*.xapk"))
if xapk_files:
    xapk = xapk_files[0]
    print(f"[*] Найден XAPK: {os.path.basename(xapk)}")
    xapk_extract = os.path.join(BASE, "resources", "xapk_extracted")
    if not os.path.exists(xapk_extract):
        print("[*] Распаковываю XAPK...")
        os.makedirs(xapk_extract, exist_ok=True)
        with zipfile.ZipFile(xapk, 'r') as z:
            z.extractall(xapk_extract)
        print(f"    Извлечено: {len(os.listdir(xapk_extract))} файлов")
    
    # XAPK содержит APK внутри — ищем base.apk или *.apk
    for root, dirs, files in os.walk(xapk_extract):
        for f in files:
            if f.endswith('.apk'):
                apk_path = os.path.join(root, f)
                apk_out = os.path.join(BASE, "resources", f"apk_from_xapk_{f.replace('.apk','')}")
                if not os.path.exists(apk_out):
                    print(f"[*] Распаковываю {f}...")
                    os.makedirs(apk_out, exist_ok=True)
                    try:
                        with zipfile.ZipFile(apk_path, 'r') as z2:
                            z2.extractall(apk_out)
                        print(f"    Извлечено: {len(os.listdir(apk_out))} элементов")
                        # Если в этом APK есть res/drawable — добавим к основному
                        extra_drawable = os.path.join(apk_out, "res", "drawable")
                        if os.path.isdir(extra_drawable):
                            print(f"    Найдена папка drawable в {f}!")
                            count = 0
                            for item in os.listdir(extra_drawable):
                                src = os.path.join(extra_drawable, item)
                                dst = os.path.join(DRAWABLE, item)
                                if not os.path.exists(dst):
                                    shutil.copy2(src, dst)
                                    count += 1
                            if count:
                                print(f"    Скопировано {count} новых файлов в drawable")
                    except Exception as e:
                        print(f"    Ошибка: {e}")

# --- Шаг 2: Декодируем ВСЕ XML из drawable ---
print(f"\n[*] Декодирую бинарные XML из: {DRAWABLE}")

# Ключевые иконки
PRIORITY = [
    "ic_tab_feed_selected", "ic_tab_feed_unselected",
    "ic_tab_documents_selected", "ic_tab_documents_unselected", 
    "ic_tab_services_selected", "ic_tab_services_unselected",
    "ic_tab_menu_selected", "ic_tab_menu_unselected",
    "ic_tab_menu_selected_badge", "ic_tab_menu_unselected_badge",
    "ic_home", "ic_homedoc",
    "ic_qr", "ic_qr_white", "ic_doc_qr_selected", "qr_scan", "qr_scan_white",
    "trident", "trident_white", "ic_logo_diia_gerb_white",
    "ic_ps_bonds", "ic_failed_connection",
    "ic_arrow", "ic_arrow_back", "ic_arrow_fill",
    "ic_search", "ic_search_black", "diia_search_icon",
    "ic_notifications", "ic_menu_notifications_action",
    "ic_menu", "ic_menu_services", "ic_menu_history",
    "usermale", "userfemale", "ic_users",
    "ic_document", "ic_add_document",
    "diia_ic_scanner", "diia_ic_barcode_scan",
    "ic_keyboard_scan", "ic_flash_scan",
    "ic_check_shield", "ic_ps_bonds",
    "ic_ps_tax_services", "ic_ps_medical_services",
    "ic_ps_court_services", "ic_ps_car_services",
    "gradient_bond_card",
]

decoded = 0
failed = 0
priority_done = []

for fname in sorted(os.listdir(DRAWABLE)):
    if not fname.endswith(".xml"):
        continue
    base = os.path.splitext(fname)[0]
    
    path = os.path.join(DRAWABLE, fname)
    try:
        with open(path, "rb") as f:
            data = f.read()
        
        # Пропускаем уже текстовые XML
        if data[:5] == b'<?xml':
            continue
            
        axml = AXMLPrinter(data)
        xml_bytes = axml.get_xml()
        
        out = os.path.join(OUTPUT, fname)
        with open(out, "wb") as f:
            f.write(xml_bytes)
        
        decoded += 1
        is_priority = base in PRIORITY
        if is_priority:
            priority_done.append(base)
            print(f"  ★ {fname}")
        elif decoded <= 20 or decoded % 100 == 0:
            print(f"  ✓ {fname}")
    except Exception as e:
        failed += 1

# Также декодируем mipmap (webp иконки приложения)
mipmap_dirs = globmod.glob(os.path.join(BASE, "resources", "apk_extracted", "res", "mipmap-*"))
mipmap_out = os.path.join(OUTPUT, "mipmap")
os.makedirs(mipmap_out, exist_ok=True)
mipmap_count = 0
for md in mipmap_dirs:
    folder_name = os.path.basename(md)
    for f in os.listdir(md):
        src = os.path.join(md, f)
        dst = os.path.join(mipmap_out, f"{folder_name}_{f}")
        if not os.path.exists(dst):
            shutil.copy2(src, dst)
            mipmap_count += 1

# Копируем PNG из drawable
for fname in os.listdir(DRAWABLE):
    if fname.endswith(('.png', '.webp', '.jpg')):
        src = os.path.join(DRAWABLE, fname)
        dst = os.path.join(OUTPUT, fname)
        if not os.path.exists(dst):
            shutil.copy2(src, dst)

print(f"\n{'='*50}")
print(f"Декодировано XML: {decoded}")
print(f"Ошибки: {failed}")
print(f"Mipmap иконки: {mipmap_count}")
print(f"Приоритетные: {len(priority_done)}/{len(PRIORITY)}")
print(f"\nПриоритетные иконки:")
for p in priority_done:
    print(f"  ★ {p}")
missing = set(PRIORITY) - set(priority_done)
if missing:
    print(f"\nНе найдены:")
    for m in sorted(missing):
        print(f"  ? {m}")
print(f"\nРезультат в: {OUTPUT}")
