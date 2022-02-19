nessa aula aprenderemos a unir a firebase auth com nossa database.

Por que?

    Supondo que queiramos criar um sistema de cadastro e não cadastrássemos apenas o email e senha, mas também o nome, idade e afins. Para isso precisaríamos da database para relacionar esses dados.

Para cada usuário criado, ele gera um id aleatório e único
    value.user.uid para acessar esse user identificator

# App.js

```javascript
import React, { useState } from 'react';
import { 
  View, 
  Text, 
  TouchableOpacity, 
  StyleSheet, 
  TextInput 
} from 'react-native';

import { useNavigation } from '@react-navigation/native';

import firebase from "../FirebaseConection";

export default function SignIn() {
    
  const navigation = useNavigation();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [nome, setNome] = useState("");

  async function cadastrar() {

    await firebase.auth().createUserWithEmailAndPassword(email, password)
    
    .then((value)=>{
      alert("Bem vindo: " + value.user.uid);
      firebase.database().ref("usuarios/").child(value.user.uid).set({
        nome: nome
      })

      setNome("");
      setPassword("");
      setEmail("");
      // navigation.navigate("TelaInicial", {email: email})
    })
    
    .catch((error) => {
      alert("Ops, algo deu errado! " + error);
      return;
    })
  }


  return (
    <View style={styles.container}>
      
      <View>
        <Text style={styles.text}>Nome</Text>
        <TextInput 
          style={styles.input}
          placeholder="Digite o seu nome"
          placeholderTextColor={"#aaa"}
          value={nome}
          onChangeText={value => setNome(value)}
        />

        <Text style={styles.text}>Email</Text>
        <TextInput 
          style={styles.input}
          placeholder="Digite o seu email"
          placeholderTextColor={"#aaa"}
          value={email}
          onChangeText={value => setEmail(value)}
        />
        
        <Text style={styles.text}>Senha</Text>
        <TextInput
          value={password}
          style={styles.input}
          placeholder="Digite a sua senha"
          placeholderTextColor={"#aaa"}
          onChangeText={value => setPassword(value)}
          secureTextEntry={true}
        />
      </View>
      
      <TouchableOpacity 
        style={styles.button}
        onPress={cadastrar}
      >

        <Text style={styles.textButton}>Cadastrar</Text>
      
      </TouchableOpacity>

    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'space-between',
    marginHorizontal: 10,
  },

  text: {
    fontSize: 16,
    color: "#000",
    fontWeight: "bold",
    marginVertical: 10
  },

  input: {
    height: 50,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 10,
    paddingLeft: 15,
    fontSize: 16,
    color: "#000"
  },
  
  button: {
    marginTop: 20,
    marginBottom: 35,
    height: 70,
    borderRadius: 10,
    alignItems: "center",
    justifyContent:"center",
    backgroundColor:"#111"
  },

  textButton: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
    textTransform: "uppercase"
  }
})
```