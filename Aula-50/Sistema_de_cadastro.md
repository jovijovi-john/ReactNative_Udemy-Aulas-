Iremos configurar um sistema de cadastro e depois de login utilizando o sistema de autenticação do firebase

Firebase => Authentication

    * Email / Password:
  
        Permite que os usuários se inscrevam usando o endereço de e-mail e a senha deles. Nossos SDKs também fornecem verificação de endereço de e-mail, recuperação de senha e componentes essenciais para alteração do endereço de e-mail. 

        obs: não ativamos o link do email (login sem senha)


    Para usá-lo, precisamos configurar o arquivo de configurações do firebase para importar o firebase/auth:
        import "firebase/auth";

    ```javascript    
    async function cadastrar() {
        await firebase.auth().createUserWithEmailAndPassword(email, password);
    }
    ```
    esse createUserWithEmailAndPasword devolve uma promisse: um caso de sucesso e um caso de erro.
    .then() é quando da tudo certo, então ele vai devolver alguma coisa dentro desse then

        await firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((value) => {
            alert("usuario criado: " + value.user.nome)
        })

    o .catch() é quando alguma coisa da errado, e nele também recebemos uma função anônima

        .catch((error) => {

        })

    o próprio firebase disponibiliza alguns casos de erro, alguns códigos: erro quando a senha for muito pequena, erro quando o email for inválido  para a gente conseguir tratar isso na nossa aplicação

# App.js

```javascript
import React, { useState, useEffect } from "react";
import firebase from "./src/FirebaseConection";


import { 
  View,
  Text,
  StyleSheet,
  TextInput,
  Button,
  FlatList,
  ActivityIndicator
} from "react-native";


export default function App() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function cadastrar() {
    await firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((value) => {
      alert("Usuario criado: " + value.user.email);
    })
    .catch((error) => {
      
      if (error.code === "auth/weak-password"){
        alert("Sua senha deve ter pelo menos 6 caracteres");
        return;
      }
      
      if (error.code === "auth/invalid-email"){
        // Email inválido

        alert("Email inválido!")
        return;
      
      } else {

        alert("Ops, algo deu errado!");
        return;
      }
    })

    setEmail("");
    setPassword("");
  }

  return(
    <View style={styles.container}>
      <Text style={styles.texto}>Nome</Text>
      <TextInput 
        value={email}
        style={styles.input}
        underlineColorAndroid="transparent"
        onChangeText={(text) => {setEmail(text)}}
        placeholder="Digite o email"
        placeholderTextColor={"#888"}
      />
      
      <Text style={styles.texto}>Senha</Text>
      <TextInput 
        value={password}
        style={styles.input}
        underlineColorAndroid="transparent"
        onChangeText={(text) => {setPassword(text)}}
        placeholder="Digite a senha"
        placeholderTextColor={"#888"}
      />

      <Button 
        title="Cadastrar"
        onPress={cadastrar}
      />


      </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    padding: 10
  },

  texto: {
    fontSize: 20,
    color: "#000"
  },

  input: {
    marginBottom: 10,
    padding: 10,
    borderWidth: 1,
    borderColor: "#121212",
    height: 45 ,
    fontSize: 17,
    color: "#000",
  }
})
```

# FirebaseConection.js

```javascript
import firebase from 'firebase';
import "firebase/database";
import "firebase/auth";

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

