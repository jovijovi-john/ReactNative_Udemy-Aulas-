# useEffect

o useEffect substitui nossos ciclos de vida (componentDidMount, componentDidUpdate).

Antes precisávamos ter esse componente em clase para termos os ciclos de vida, agora não é mais necessário com o uso de hooks

    => O componentDidMount servia para quando nosso componente fosse renderizado ele chamava esse componentDidMount 

    => O componentDidUpdate era acionado quando nosso componente fosse atualizado.

Importação: 

    import React, { useEffect } from "react";

Vamos utilizar o asyncStorage para quando digitarmos um nome, por exemplo, ele salvar no asyncStorage.
E toda vez que atualizarmos nosso component ele ir lá e buscar do asyncStorage


# asyncStorage

Nova importação:

    import AsyncStorage from '@react-native-async-storage/async-storage';

# useEffect:

    // o primeiro parâmetro no useEffect é uma função, e o segundo é um array de state
    useEffect( () => {})

    ex: 
        useEffect(() => {}, [nome]) quando o state nome for alterado, vai executar aquela função

# componentDidUpdate:

    useEffect(() => {
        async function saveStore() {
            await AsyncStorage.setItem("nomes", nome)
        }
    }, [nome])

# componentDidMount:
    
    // no array de dependecias / states, não passamos nada, assim ele vai ser acionado assim que o componente for renderizado

    useEffect(() => {
        async    
    },[])

# componentWillAmount:

    // passa um array vazio de dependencias e na função bota um return, dentro desse return vai ser o que deve acontecer quando aquele componente for "desmontado

     useEffect(() => {
        async function saveStore() {
            await AsyncStorage.setItem("nomes", nome)
        }

        return (
            // aqui fica o componentWillAmount
        )
    }, [nome])

## App.js:

    import React, { useEffect, useState } from "react";
    import { 
      View,
      Text,
      StyleSheet,
      TouchableOpacity,
      TextInput,
      Keyboard
    } from "react-native";
    
    import AsyncStorage from "@react-native-async-storage/async-storage";
    
    
    export default function App() {
    
      const [nome, setNome] = useState("");
      const [input, setInput] = useState("");
    
      //componentDidMount
    
      useEffect(() => {
        async function getStorage(){
          const nomeStorage = await AsyncStorage.getItem("nomes");
    
          if (nomeStorage !== null) {
            setNome(nomeStorage);
          }
        }
    
        getStorage();
    
        // return () => {}
      }, [])
    
    
      // componentDidUpdate
      useEffect(() => {
        async function saveStore() {
          await AsyncStorage.setItem("nomes", nome)
        }
    
        saveStore();
      }, [nome])
    
      function alteraNome(){
        setNome(input);
        setInput("");
        Keyboard.dismiss();
      }
    
      return(
        <View style={styles.container}>
    
          <TextInput 
            style={styles.input} 
            placeholder="Digite seu nome" 
            value={input}
            onChangeText={ (textoDigitado) => {
              setInput(textoDigitado)
            }}
          />
    
          <TouchableOpacity style={styles.btn} onPress={alteraNome}>
            <Text style={styles.btnText}>Altera nome</Text>
          </TouchableOpacity>
    
          <Text style={styles.texto}>{nome}</Text>
        </View>
      )
    }
    
    const styles = StyleSheet.create({
      container: {
        flex: 1, 
        marginTop: 120
      },
    
      input: {
        borderWidth: 1,
        borderColor:"#000",
        margin: 20,
        height: 50,
        borderRadius: 25,
        paddingLeft: 25,
        fontSize: 18
      },
    
      texto: {
        color: "#000",
        fontSize: 35,
        marginVertical: 30,
        textAlign: "center"
      },
    
      btn: {
        backgroundColor: "#222",
        alignItems: "center",
        marginHorizontal: 10,
        marginHorizontal: 140,
        borderRadius: 50,
        height: 50,
        justifyContent: 'center'
      },
    
      btnText: {
        color: "#fff",
        fontSize: 18
      }
    })