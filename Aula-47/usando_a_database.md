
```javascript
async function dados() {
    await firebase.database().ref("nome").on("value", (snapshot) => {
        setNome(snapshot.val());
    })
}
```
o snapshot é uma "foto" do banco de dados, esse nome é uma convenção

=> o .on() a gente chama de "olheiro" ou listener da nossa database. Ele fica monitorando 24hr nossa database, para que a cada alteração na database ele já mude automaticamente na nossa aplicação

=> como ele fica 24hr vendo se tem alteração, é algo meio pesado. Por isso existe o .once() que verifica apenas uma única vez, se houver alteração no banco, ela não afetará no app, somente quando der um reload no app

await firebase.database().ref("nome").once("value", (snapshot)=>{
    setNome((snapshot.val()))
});

# FirebaseConection
```javascript
import firebase from 'firebase';
import "firebase/database";

let firebaseConfig = {
    apiKey: "",
    authDomain: "",
    databaseURL: "",
    projectId: "",
    storageBucket: "",
    messagingSenderId: "",
    appId: "",
    measurementId: ""
};
  
// Initialize Firebase

if (!firebase.apps.length) { // Isso aqui é pra não abrir duas conexões juntas, pois isso gera um erro
    firebase.initializeApp(firebaseConfig);
}
export default firebase;

```


# App.js
```javascript
import React, { useState, useEffect } from "react";
import firebase from "./src/FirebaseConection";


import { 
  View,
  Text
} from "react-native";

export default function App() {

  const [nome, setNome] = useState("Carregando");
  const [idade, setIdade] = useState("")

  useEffect(() => {

    async function dados() {
      await firebase.database().ref("usuarios/2/").on("value", (snapshot) => {
        setNome(snapshot.val().Nome);
        setIdade(snapshot.val().Idade);
      })
    }

    // async function dados() {
    //   await firebase.database().ref("nome").once("value", (snapshot)=>{
    //     setNome((snapshot.val()))
    //   });
    // }

    dados();
  }, [])

  function pegaNome() {
    firebase.database();
  }
  return(
    <View style={{marginTop: 25}}>
      <Text style={{fontSize: 25}}>Olá  {nome} </Text>
      <Text style={{fontSize: 25}}>Idade: {idade} </Text>
    </View>
  )
}
```