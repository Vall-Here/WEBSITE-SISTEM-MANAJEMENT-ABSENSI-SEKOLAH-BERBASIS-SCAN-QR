import re

html_path = r'e:\project\laravel\Educonnect\docs\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Replace the menuItems array with clean clean string
clean_menu_items = """const menuItems = [
            { file: 'absensi-qr.md', label: 'Absensi QR Code' },
            { file: 'portal-orang-tua.md', label: 'Portal Orang Tua' },
            { file: 'auto-alpha-holidays.md', label: 'Auto-Alpha & Libur' },
            { file: 'rekap-laporan.md', label: 'Rekap & Laporan' },
            { file: 'arsip-kelas.md', label: 'Arsip Kelas & Data' }
        ];"""

html = re.sub(r'const menuItems = \[[\s\S]*?\];', clean_menu_items, html)

# Remove any emoji or garbled text from download button
html = re.sub(r'<a href="\${url}" download="\${fileId}" class="btn-download">[\s\S]*?</a>', 
             '<a href="${url}" download="${fileId}" class="btn-download">Download Dokumen Panduan Lengkap (.md)</a>', 
             html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
