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

$('#no_proyektor').on('change', function () {
  const no_proyektor = $(this).val();

  getCollection(db, 'peminjaman').then((peminjaman) => {
    const proyektor = peminjaman.find(item => item.nomor_peminjaman === no_proyektor);
    const perangkat_lainnya = proyektor.perangkat_lainnya
    if (proyektor) {
      document.getElementById('nama_proyektor').value = proyektor.proyektor;
      document.getElementById('matakuliah').value = proyektor.matakuliah;
      document.getElementById('ruang').value = proyektor.ruang;
      document.getElementById('dosen').value = proyektor.dosen;

      var kabel_hdmi = document.getElementById("kabel_hdmi");
      var kabel_vga = document.getElementById("kabel_vga");
      var kabel_dvi = document.getElementById("kabel_dvi");
      var lensa_pendukung = document.getElementById("lensa_pendukung");
      var case_pelindung = document.getElementById("case_pelindung");
      var remote = document.getElementById("remote");
      var layar = document.getElementById("layar");

      kabel_hdmi.checked = perangkat_lainnya['kabel hdmi']
      kabel_vga.checked = perangkat_lainnya['kabel vga']
      kabel_dvi.checked = perangkat_lainnya['kabel dvi']
      lensa_pendukung.checked = perangkat_lainnya['lensa pendukung']
      case_pelindung.checked = perangkat_lainnya['case pelindung']
      remote.checked = perangkat_lainnya['remote']
      layar.checked = perangkat_lainnya['layar']
   }
  });
});
