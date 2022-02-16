# Insert Update Delete

    Nessa aula aprenderemos a inserir, alterar e deletar dados a partir do nosso app.

* Inserir um nó:

    ```javascript
    await firebase.database().ref("tipo").set("Cliente");
    ```

    // o ref é a key e o set é o value
    se esse nó já existia, ele atualiza

    ```javascript
    await firebase.database().ref("tipo").set("Vendedor");
    ```

* Apagar um nó

    ```javascript
    await firebase.database().ref("tipo").remove();
    ```

* Inserir um novo usuário
     
    ```javascript
    await firebase.database().ref("usuarios").child(3).set({
        nome: "José",
        cargo: "Programador"
    })
    ```

    // E se quiséssemos só atualizar o nome? porque se passar so o nome ele vai APAGAR todo o resto do objeto

    ```javascript
    await firebase.database().ref("usuarios").child(3).update({
        nome: "Augusto"
    })
    ```
* Para criar uma key que nunca vai se repetir:
* 
  ```javascript
    let usuarios = firebase.database().ref("usuarios");
    let chave = usuarios.push().key();
  ```

# App.js

```javascript
import React, { useState, useEffect } from "react";
import firebase from "./src/FirebaseConection";


import { 
  View,
  Text,
  StyleSheet,
  TextInput,
  Button
} from "react-native";

export default function App() {

  const [nome, setNome] = useState("Carregando");
  const [cargo, setCargo] = useState("")

  useEffect(() => {

    async function dados() {
    }      

    dados()
  }, [])

  async function cadastrar() {

    if (nome !== "" & cargo !== "") {
      let usuarios = await firebase.database().ref("usuarios");
      let chave = usuarios.push().key;

      usuarios.child(chave).set({
        nome: nome,
        cargo: cargo
      })

      alert("Cadastrado com sucesso!");
      setNome('');
      setCargo('');
    }

  }

  return(
    <View style={styles.container}>
      <Text style={styles.texto}>Nome</Text>
      <TextInput 
        value={nome}
        style={styles.input}
        underlineColorAndroid="transparent"
        onChangeText={(text) => {setNome(text)}}
        placeholder="Digite o nome"
        placeholderTextColor={"#888"}
      />
      
      <Text style={styles.texto}>Cargo</Text>
      <TextInput 
        value={cargo}
        style={styles.input}
        underlineColorAndroid="transparent"
        onChangeText={(text) => {setCargo(text)}}
        placeholder="Digite o cargo"
        placeholderTextColor={"#888"}
      />

      <Button 
        title="Novo funcionário"
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
