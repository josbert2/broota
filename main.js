import * as firebase from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, signInAnonymously, GoogleAuthProvider, createUserWithEmailAndPassword, signOut } from "firebase/auth";
;
import { getFunctions, httpsCallable } from "firebase/functions";
import * as functions from "firebase/functions";
//import { getFunctions, httpsCallable } from "firebase/functions";
import { collection, getDocs, getFirestore } from "firebase/firestore";

const apiKeyDev = "AIzaSyBPeZj4gyMQ1PDbIxLpZd4kTF3nSs3CNMY";
const apiKeyProd = "AIzaSyBHBNWPNPGF33TnGCKbY_6Tw_LTdTcYYIA";

//init firebase
const firebaseConfig = {
    apiKey: apiKeyProd,
    authDomain: "scanner-mevacuno.firebaseapp.com",
    databaseURL: "https://scanner-mevacuno-default-rtdb.firebaseio.com",
    projectId: "scanner-mevacuno",
    storageBucket: "scanner-mevacuno.appspot.com",
    messagingSenderId: "905265252494",
    appId: "1:905265252494:web:9fe489d234adf51c1f61df",
    measurementId: "G-H7HNX8T66Y"
};

const app = firebase.initializeApp(firebaseConfig);
const auth = getAuth(app);







//const fs = getFunctions(app);
var a = null
var b = null
var c = null
var f = null
var w = null
var ext = null
var type = "CEDULA"
var run = 16099446
var ser = 105308094
var mrz = 105308094285042502504258



//const omicron = httpsCallable('omicroscannerCedula')

//let result = await omicron({ a, b, c, f, w, ext, type, ser, mrz, run });

const func = httpsCallable(getFunctions(app), 'omicroscannerCedula')
console.log(func)
const respuestas = func({ a, b, c, f, w, ext, type, ser, mrz, run })


console.log(respuestas)



