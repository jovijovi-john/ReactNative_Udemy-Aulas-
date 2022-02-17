Vamos aprender a listar os registros (Trabalhando com listas)

Isso aqui é para ir incrementando um estado de array: 
     setUsuarios(oldArray => [...oldArray, data ]);

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

import Listagem from "./src/Listagem";

export default function App() {

  const [nome, setNome] = useState("");
  const [cargo, setCargo] = useState("");
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    async function dados() {
      await firebase.database().ref("usuarios").on("value", (snapshot) => {
        setUsuarios([]);
        snapshot.forEach((childItem) => {
          let data = {
            key: childItem.key,
            nome: childItem.val().nome,
            cargo: childItem.val().cargo
          };

          setUsuarios(oldArray => [...oldArray, data ]);
        })

        setUsuarios(oldArray => [...oldArray].reverse())
        setLoading(false);
      })
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

      {loading ? 
      (
        <ActivityIndicator color="#121212" size={45}/> 
      ) :
        <FlatList 
          keyExtractor={item => item.key}
          data={usuarios}
          renderItem={ ({item}) => (<Listagem data={item} />)}
        />
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

# Listagem.js

```javascript
import React from "react";
import {
    View,
    Text,
    StyleSheet
} from "react-native";

export default function Listagem({ data }) {
    return(
        <View style={styles.container}>
            <Text style={styles.texto}>{data.nome}</Text>
            <Text style={styles.texto}>{data.cargo}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: "#121212",
        flex: 1,
        padding: 10,
        marginTop: 10,
        marginBottom: 5
    },
    
    texto: {
        fontSize: 17,
        color: "#fff"
    }
})
```