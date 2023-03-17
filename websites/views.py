from flask import Blueprint, render_template, redirect, url_for, request, flash
from .model import User
views = Blueprint('views', __name__)

user = User()


@views.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html', jumlah_data={
        'jurusan': len(user.get_collection('jurusan')),
        'mahasiswa': len(user.get_collection('mahasiswa')),
        'ruang': len(user.get_collection('ruang')),
        'fakultas': len(user.get_collection('fakultas')),
        'proyektor': len(user.get_collection('proyektor')),
        'peminjaman': len(user.get_collection('peminjaman')),
        'pengembalian': len(user.get_collection('pengembalian')),
    })


@views.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            return redirect(url_for('views.dashboard'))
        else:
            flash('Username atau Password salah')
    return render_template('login.html')


@views.route('/input-dosen', methods=['POST', 'GET'])
def input_dosen():
    if request.method == 'POST':
        random_string = user.random_string()
        kode_dosen = request.form['kode_dosen']
        nama = request.form['nama']
        user.add_document('dosen', random_string, {
            'id': random_string,
            'kode': kode_dosen,
            'nama': nama
        })

        return redirect(url_for('views.input_dosen'))
    return render_template('input_dosen.html', active='dosen')


@views.route('/data-dosen', methods=['POST', 'GET'])
def data_dosen():
    if request.method == 'POST':
        id = request.form['id']
        kode = request.form['kode_dosen']
        nama = request.form['nama']
        user.update_document('dosen', id, {
            'kode': kode,
            'nama': nama
        })
    return render_template('data_dosen.html',
                           active='dosen',
                           data=user.get_collection('dosen'))


@views.route('/data-dosen/delete/<id>', methods=['POST', 'GET'])
def delete_data_dosen(id):
    user.delete_document('dosen', id)
    return redirect(url_for('views.data_dosen'))


@views.route('/input-ruang', methods=['POST', 'GET'])
def input_ruang():
    if request.method == 'POST':
        random_string = user.random_string()
        kode = request.form['kode']
        nama = request.form['nama']
        lantai = request.form['lantai']
        user.add_document('ruang', random_string, {
            'id': random_string,
            'kode': kode,
            'nama': nama,
            'lantai': lantai,
        })

        return redirect(url_for('views.input_ruang'))
    return render_template('input_ruang.html', active='ruang')


@views.route('/data-ruang', methods=['POST', 'GET'])
def data_ruang():
    if request.method == 'POST':
        id = request.form['id']
        kode = request.form['kode']
        nama = request.form['nama']
        lantai = request.form['lantai']
        user.update_document('ruang', id, {
            'kode': kode,
            'nama': nama,
            'lantai': lantai
        })
    return render_template('data_ruang.html', active='ruang', data=user.get_collection('ruang'))


@views.route('/data-ruang/delete/<id>', methods=['POST', 'GET'])
def delete_data_ruang(id):
    user.delete_document('ruang', id)
    return redirect(url_for('views.data_ruang'))


@views.route('/input-fakultas', methods=['POST', 'GET'])
def input_fakultas():
    if request.method == 'POST':
        random_string = user.random_string()
        kode = request.form['kode']
        nama = request.form['nama']
        user.add_document('fakultas', random_string, {
            'id': random_string,
            'kode': kode,
            'nama': nama
        })

        return redirect(url_for('views.input_fakultas'))
    return render_template('input_fakultas.html', active='fakultas')


@views.route('/data-fakultas', methods=['POST', 'GET'])
def data_fakultas():
    if request.method == 'POST':
        id = request.form['id']
        kode = request.form['kode']
        nama = request.form['nama']
        user.update_document('fakultas', id, {
            'kode': kode,
            'nama': nama
        })
    return render_template('data_fakultas.html', active='fakultas', data=user.get_collection('fakultas'))


@views.route('/data-fakultas/delete/<id>', methods=['POST', 'GET'])
def delete_data_fakultas(id):
    user.delete_document('fakultas', id)
    return redirect(url_for('views.data_fakultas'))


@views.route('/input-jurusan', methods=['POST', 'GET'])
def input_jurusan():
    if request.method == 'POST':
        random_string = user.random_string()
        kode = request.form['kode']
        nama = request.form['nama']
        fakultas = request.form['fakultas']
        user.add_document('jurusan', random_string, {
            'id': random_string,
            'kode': kode,
            'nama': nama,
            'nama_fakultas': fakultas,
        })

        return redirect(url_for('views.input_jurusan'))
    return render_template('input_jurusan.html', active='jurusan', data_fakultas=user.get_collection('fakultas'))


@views.route('/data-jurusan', methods=['POST', 'GET'])
def data_jurusan():
    if request.method == 'POST':
        id = request.form['id']
        kode = request.form['kode']
        nama = request.form['nama']
        fakultas = request.form['fakultas']
        user.update_document('jurusan', id, {
            'kode': kode,
            'nama': nama,
            'fakultas': fakultas
        })
    return render_template('data_jurusan.html', active='jurusan', data=user.get_collection('jurusan'))


@views.route('/data-jurusan/delete/<id>', methods=['POST', 'GET'])
def delete_data_jurusan(id):
    user.delete_document('jurusan', id)
    return redirect(url_for('views.data_jurusan'))


@views.route('/input-mahasiswa', methods=['POST', 'GET'])
def input_mahasiswa():
    if request.method == 'POST':
        random_string = user.random_string()
        id_kartu = request.form['id_kartu']
        nim = request.form['nim']
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        user.add_document('mahasiswa', random_string, {
            'id': random_string,
            'id_kartu': id_kartu,
            'nim': nim,
            'nama': nama,
            'nama_jurusan': jurusan,
        })

        return redirect(url_for('views.input_mahasiswa'))
    

    return render_template('input_mahasiswa.html', active='mahasiswa', 
                            data_jurusan=user.get_collection('jurusan'), 
                            id = user.get_value_rtdb('id'))


@views.route('/data-mahasiswa', methods=['POST', 'GET'])
def data_mahasiswa():
    if request.method == 'POST':
        id = request.form['id']
        id_kartu = request.form['id_kartu']
        nim = request.form['nim']
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        user.update_document('mahasiswa', id, {
            'id_kartu': id_kartu,
            'nama': nama,
            'nim': nim,
            'nama_jurusan': jurusan
        })
    return render_template('data_mahasiswa.html', active='mahasiswa',
                           data=user.get_collection('mahasiswa'),
                           data_jurusan=user.get_collection('jurusan'))


@views.route('/data-mahasiswa/delete/<id>', methods=['POST', 'GET'])
def delete_data_mahasiswa(id):
    user.delete_document('mahasiswa', id)
    return redirect(url_for('views.data_mahasiswa'))


@views.route('/input-matakuliah', methods=['POST', 'GET'])
def input_matakuliah():
    if request.method == 'POST':
        random_string = user.random_string()
        nama = request.form['nama']
        kode = request.form['kode']
        sks = request.form['sks']
        user.add_document('matakuliah', random_string, {
            'id': random_string,
            'nama': nama,
            'kode': kode,
            'sks': sks
        })

        return redirect(url_for('views.input_matakuliah'))
    return render_template('input_matakuliah.html', active='matakuliah')


@views.route('/data-matakuliah', methods=['POST', 'GET'])
def data_matakuliah():
    if request.method == 'POST':
        id = request.form['id']
        kode = request.form['kode']
        nama = request.form['nama']
        sks = request.form['sks']
        user.update_document('matakuliah', id, {
            'kode': kode,
            'nama': nama,
            'sks': sks
        })
    return render_template('data_matakuliah.html', active='matakuliah', data=user.get_collection('matakuliah'),)


@views.route('/data-matakuliah/delete/<id>', methods=['POST', 'GET'])
def delete_data_matakuliah(id):
    user.delete_document('matakuliah', id)
    return redirect(url_for('views.data_matakuliah'))


@views.route('/input-proyektor', methods=['POST', 'GET'])
def input_proyektor():
    if request.method == 'POST':
        random_string = user.random_string()
        id_proyektor = request.form['id_proyektor']
        nama = request.form['nama']
        nomor = request.form['nomor']
        kondisi = request.form['kondisi']
        user.add_document('proyektor', random_string, {
            'id': random_string,
            'id_proyektor': id_proyektor,
            'nama': nama,
            'nomor': nomor,
            'kondisi': kondisi,
            'dipinjam': False
        })

        return redirect(url_for('views.input_proyektor'))
    return render_template('input_proyektor.html', active='proyektor')


@views.route('/data-proyektor', methods=['POST', 'GET'])
def data_proyektor():
    if request.method == 'POST':
        id = request.form['id']
        id_proyektor = request.form['id_proyektor']
        nama = request.form['nama']
        nomor = request.form['nomor']
        kondisi = request.form['kondisi']
        user.update_document('proyektor', id, {
            'id_proyektor': id_proyektor,
            'nama': nama,
            'kondisi': kondisi,
            'nomor': nomor
        })
    return render_template('data_proyektor.html', active='proyektor', data=user.get_collection('proyektor'))


@views.route('/data-proyektor/delete/<id>', methods=['POST', 'GET'])
def delete_data_proyektor(id):
    user.delete_document('proyektor', id)
    return redirect(url_for('views.data_proyektor'))


@views.route('/input-peminjaman', methods=['POST', 'GET'])
def input_peminjaman():
    if request.method == 'POST':
        random_string = user.random_string()
        waktu = request.form['waktu'].replace('T', '/')
        nama = request.form['nama']
        nomor = request.form['nomor']
        proyektor = request.form['proyektor']
        matakuliah = request.form['matakuliah']
        matakuliah = request.form['matakuliah']
        ruang = request.form['ruang']
        dosen = request.form['dosen']

        user.add_document('peminjaman', random_string, {
            'id': random_string,
            'waktu': waktu,
            'nama': nama,
            'nomor_peminjaman': nomor,
            'proyektor': proyektor,
            'matakuliah': matakuliah,
            'matakuliah': matakuliah,
            'ruang': ruang,
            'dosen': dosen,
            'status': True
        })
        user.change_status_proyektor(nama_proyektor=proyektor)

        return redirect(url_for('views.input_peminjaman'))

    proyektor_tersedia = [proyektor for proyektor in user.get_collection(
        'proyektor') if proyektor['dipinjam'] == False]
    
    mahasiswa = user.find_mahasiswa() if user.find_mahasiswa() is not None else {'mahasiswa': ''}
    user.update_value_rtdb('id', "0")

    return render_template('input_peminjaman.html', active='peminjaman',
                           jumlah_peminjam=len(
                               user.get_collection('peminjaman')),
                           data_proyektor=proyektor_tersedia,
                           data_matakuliah=user.get_collection('matakuliah'),
                           dosen=user.get_collection('matakuliah'),
                           data_ruang=user.get_collection('ruang'),
                           data_dosen=user.get_collection('dosen'),
                           mahasiswa= mahasiswa
                           )


@views.route('/data-peminjaman', methods=['POST', 'GET'])
def data_peminjaman():
    if request.method == 'POST':
        id = request.form['id']
        waktu = request.form['waktu'].replace('T', '/')
        nama = request.form['nama']
        nomor = request.form['nomor']
        proyektor = request.form['proyektor']
        matakuliah = request.form['matakuliah']
        matakuliah = request.form['matakuliah']
        ruang = request.form['ruang']
        dosen = request.form['dosen']
        user.update_document('peminjaman', id, {
            'waktu': waktu,
            'nama': nama,
            'nomor': nomor,
            'proyektor': proyektor,
            'matakuliah': matakuliah,
            'matakuliah': matakuliah,
            'ruang': ruang,
            'dosen': dosen,
        })

    proyektor_tersedia = [proyektor for proyektor in user.get_collection(
        'proyektor') if proyektor['dipinjam'] == False]
    return render_template('data_peminjaman.html', active='peminjaman',
                           data=user.get_collection('peminjaman'),
                           jumlah_peminjam=len(
                               user.get_collection('peminjaman')),
                           data_proyektor=proyektor_tersedia,
                           data_matakuliah=user.get_collection('matakuliah'),
                           dosen=user.get_collection('matakuliah'),
                           data_ruang=user.get_collection('ruang'),
                           data_dosen=user.get_collection('dosen')
                           )


@views.route('/data-peminjaman/delete/<id>', methods=['POST', 'GET'])
def delete_data_peminjaman(id):
    user.delete_document('peminjaman', id)
    return redirect(url_for('views.data_peminjaman'))


@views.route('/input-pengembalian', methods=['POST', 'GET'])
def input_pengembalian():
    if request.method == 'POST':
        random_string = user.random_string()
        waktu = request.form['waktu']
        nama = request.form['nama']
        nomor = request.form['nomor']
        proyektor = request.form['proyektor']
        matakuliah = request.form['matakuliah']
        matakuliah = request.form['matakuliah']
        ruang = request.form['ruang']
        dosen = request.form['dosen']

        user.add_document('pengembalian', random_string, {
            'id': random_string,
            'waktu': waktu,
            'nama': nama,
            'nomor': nomor,
            'proyektor': proyektor,
            'matakuliah': matakuliah,
            'matakuliah': matakuliah,
            'ruang': ruang,
            'dosen': dosen,
            'status': True
        })
        user.change_status_proyektor(nama_proyektor=proyektor)

        return redirect(url_for('views.input_pengembalian'))

    mahasiswa = user.find_mahasiswa()
    peminjaman = user.find_peminjaman()
    user.update_value_rtdb('id', "0")

    return render_template('input_pengembalian.html', active='pengembalian',
                            mahasiswa = mahasiswa,
                            peminjaman= peminjaman)


@views.route('/data-pengembalian', methods=['POST', 'GET'])
def data_pengembalian():
    if request.method == 'POST':
        id = request.form['id']
        waktu = request.form['waktu'].replace('T', '/')
        nama = request.form['nama']
        nomor = request.form['nomor']
        proyektor = request.form['proyektor']
        matakuliah = request.form['matakuliah']
        matakuliah = request.form['matakuliah']
        ruang = request.form['ruang']
        dosen = request.form['dosen']
        user.update_document('pengembalian', id, {
            'waktu': waktu,
            'nama': nama,
            'nomor': nomor,
            'proyektor': proyektor,
            'matakuliah': matakuliah,
            'matakuliah': matakuliah,
            'ruang': ruang,
            'dosen': dosen,
        })

    proyektor_tersedia = [proyektor for proyektor in user.get_collection(
        'proyektor') if proyektor['dipinjam'] == False]
    return render_template('data_pengembalian.html', active='pengembalian',
                           data=user.get_collection('pengembalian'),
                           jumlah_peminjam=len(
                               user.get_collection('pengembalian')),
                           data_proyektor=proyektor_tersedia,
                           data_matakuliah=user.get_collection('matakuliah'),
                           dosen=user.get_collection('matakuliah'),
                           data_ruang=user.get_collection('ruang'),
                           data_dosen=user.get_collection('dosen')
                           )


@views.route('/data-pengembalian/delete/<id>', methods=['POST', 'GET'])
def delete_data_pengembalian(id):
    user.delete_document('pengembalian', id)
    return redirect(url_for('views.data_pengembalian'))
