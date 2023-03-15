import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-app.js";
initializeApp({
  apiKey: "AIzaSyAdm9MlbEGvt5w5kNYe3UJjqLeiB7ziRJE",
  authDomain: "web-peminjaman-alat-using-rfid.firebaseapp.com",
  projectId: "web-peminjaman-alat-using-rfid",
  storageBucket: "web-peminjaman-alat-using-rfid.appspot.com",
  messagingSenderId: "929165816271",
  appId: "1:929165816271:web:a8c57a77144ce5bc2da2ba",
  measurementId: "G-HNHG9TMPDH",
  databaseURL: 'https://web-peminjaman-alat-using-rfid-default-rtdb.asia-southeast1.firebasedatabase.app'
});

import { getDatabase, set, ref, onValue, get, child } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-database.js";
import { getFirestore, collection, getDocs } from 'https://www.gstatic.com/firebasejs/9.17.2/firebase-firestore.js'
const db = getFirestore()
const rtdb = getDatabase()

function getCollection(db, colRef) {
  return getDocs(collection(db, colRef))
    .then((snapshot) => {
      let data = []
      snapshot.docs.forEach(doc => {
        data.push({ ...doc.data(), id: doc.id })
      });
      return data
    });
}

function tidakTerdaftar() {
  document.getElementById('main').innerHTML = 'Maaf Kartu Tidak Terdaftar!!!'
  document.getElementById('main').className = 'mt-5'
  document.getElementById('second').innerHTML = 'Silahkan Daftarkan Kartu Terlebih Dahulu'
  document.getElementById('image').remove() = ''
}

function loading() {
  document.getElementById('loading').innerHTML = 'mengecek kartu ...'
}

window.scanKartu = () => {
  loading()
  // update scan == 1
  set(ref(rtdb, '/scan'), 1)

  // dapatkan value dari id
  const intervalId = setInterval(() => {
    get(child(ref(rtdb), 'id'))
      .then((snapshot) => {
        const id = snapshot.val();
        if (id !== 0) {
          clearInterval(intervalId);
          set(ref(rtdb, '/scan'), 0)
          console.log(`Data id berhasil didapatkan: ${id}`);
          // cek id
          getCollection(db, 'mahasiswa').then((mahasiswa) => {
            if (mahasiswa.find(m => m.id_kartu === id)) {
              console.log('Terdaftar')
              // tampilkan modal pilihan menu
              $(document).ready(function () {
                $("#myModal").modal('show');
              });


            } else {
              // window.location.assign('/input-mahasiswa')
              console.log("tidak Terdaftar")
            }
          });


        }

      })
      .catch((error) => {
        console.log(`Terjadi kesalahan saat mendapatkan data id: ${error}`);
      });
  }, 1000);


}

