from flask import Blueprint, render_template, redirect, url_for, request
from .model import User
views = Blueprint('views', __name__)

user = User()


@views.route('/', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')


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
    return render_template('data_ruang.html',active='ruang',data=user.get_collection('ruang'))
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
    return render_template('data_fakultas.html')


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
            'nama': fakultas,
        })

        return redirect(url_for('views.input_jurusan'))
    return render_template('input_jurusan.html', active='jurusan', data_fakultas = user.get_collection('fakultas'))


@views.route('/data-jurusan', methods=['POST', 'GET'])
def data_jurusan():
    return render_template('data_jurusan.html')


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
    return render_template('input_mahasiswa.html', active='mahasiswa', data_jurusan=user.get_collection('jurusan'))


@views.route('/data-mahasiswa', methods=['POST', 'GET'])
def data_mahasiswa():
    return render_template('data_mahasiswa.html')


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
    return render_template('data_matakuliah.html')


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
    return render_template('data_proyektor.html')


@views.route('/input-peminjaman', methods=['POST', 'GET'])
def input_peminjaman():
    return render_template('input_peminjaman.html')


@views.route('/data-peminjaman', methods=['POST', 'GET'])
def data_peminjaman():
    return render_template('data_peminjaman.html')
