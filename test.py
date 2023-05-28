perangkat_lainnya = {'remote': False, 'kabel vga': False, 'lensa pendukung': False,
                     'kabel hdmi': True, 'kabel dvi': True, 'case pelindung': True, 'layar': True}

print(" | ".join([key for key, value in perangkat_lainnya.items() if value]))
