Vamos criar um sistema de login nessa aula

    => Ao invés de usar um createUserWithEmailAndPassword(), usamos:
        signInWithEmailAndPassword()

        Ele também é uma promisse

    => A função de logout também é assíncrona, isso porque temos que esperar o firebase ir lá e deslogar esse usuário que tá logado

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
  const [user, setUser] = useState("");

  async function logar() {

    await firebase.auth().signInWithEmailAndPassword(email, password)
    
    .then((value) => {
      alert("Bem vindo: " + value.user.email);
      setUser(value.user.email)
    })

    .catch((error) => {
      alert("Ops, algo deu errado!");
      return;
    });

    setEmail("");
    setPassword("");
  }

  async function logout() {
    await firebase.auth().signOut();
    setUser("");
    alert("Deslogado com sucesso")
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
        title="Acessar"
        onPress={logar}
      />
      
      <Text style={{marginTop: 20, fontSize: 23, marginBottom: 20, textAlign: "center", color: "#000"}}>
        {user}
      </Text>
      
      { user.length > 0 ? 
        (
          <Button 
            title="Logout"
            onPress={logout}
          />
        ) : (
          <Text style={{marginTop: 20, fontSize: 23, marginBottom: 20, textAlign: "center", color: "#000"}}>
            Nenhum usuario está logado
          </Text>
        )
      }


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