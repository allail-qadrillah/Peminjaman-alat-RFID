from websites.model import User

user = User()

# MELAKUKAN SCAN
user.update_value_rtdb(key='id', value='17970112128304')
# user.update_value_rtdb(key='id', value='1797018304')


def cek_proyektor(id_proyektor, nama, nomor, kondisi):
    status = False
    for proyektor in user.get_collection("proyektor"):
        if proyektor.get('id_proyektor') == id_proyektor and proyektor.get('nama') == nama and proyektor.get('kondisi') == kondisi and proyektor.get('nomor') == nomor:
            status = True
            break
    return status

def get_matakuliah_from_jurusan(id_kartu):
    list_matakuliah = []
    founded = False
    for mahasiswa in user.get_collection('mahasiswa'):
        if not founded:
            if mahasiswa.get('id_kartu') == id_kartu:
                founded = True
                for matakuliah in user.get_collection('matakuliah'):
                    if matakuliah.get('jurusan') == mahasiswa.get('nama_jurusan'):
                        list_matakuliah.append( matakuliah.get('nama') )
    return list_matakuliah


# print(get_matakuliah_from_jurusan('1797018304'))
