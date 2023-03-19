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
    if (proyektor) {
      document.getElementById('nama_proyektor').value = proyektor.proyektor;
      document.getElementById('matakuliah').value = proyektor.matakuliah;
      document.getElementById('ruang').value = proyektor.ruang;
      document.getElementById('dosen').value = proyektor.dosen;
    }
  });
});
