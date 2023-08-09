from websites.model import User

user = User()

# MELAKUKAN SCAN
# user.update_value_rtdb(key='id', value='1797018304')


def cek_proyektor(id_proyektor, nama, nomor, kondisi):
    status = False
    for proyektor in user.get_collection("proyektor"):
        if proyektor.get('id_proyektor') == id_proyektor and proyektor.get('nama') == nama and proyektor.get('kondisi') == kondisi and proyektor.get('nomor') == nomor:
            status = True
            break
    return status

print(cek_proyektor(id_proyektor="6544534",nama="EPSON 54",nomor="87",kondisi="Baik"))
print()
print(cek_proyektor(id_proyektor="1S2",nama="LCD",nomor="1",kondisi="Baik"))
