o useRef nos permite referenciar alguma coisa e trabalhar em cima desse atributo referenciando ele diretamente

queremos criar um botao e quando clicarmos nele ele abre o teclado e fique piscando logo para digitarmos alguma coisa. Ou seja, abrir o input assim que clicar no botão.

importação:

    import {useRef} from "react";

    useRef(<valor default>)

# App.js

    import React, { useEffect, useState, useMemo, useRef} from "react";
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
      const nomeInput = useRef("null")
    
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
    
      function novoNome() {
        // nomeInput.current.clear()  => para apagar o conteudo do input
        // nomeInput.current.blur()  => para tirar o foco do input
        nomeInput.current.focus()
      }
    
      const letrasNome = useMemo(()=>{
        console.log("Mudou letra");
        return nome.length
      }, [nome.length])
    
    
      return(
        <View style={styles.container}>
    
          <TextInput 
            style={styles.input} 
            placeholder="Digite seu nome" 
            value={input}
            onChangeText={ (textoDigitado) => {
              setInput(textoDigitado)
            }}
            ref={nomeInput}
          />
    
          <TouchableOpacity style={styles.btn} onPress={alteraNome}>
            <Text style={styles.btnText}>Altera nome</Text>
          </TouchableOpacity>
    
          <Text style={styles.texto}>{nome}</Text>
          <Text style={styles.texto}>Tem {letrasNome} letras</Text>
    
          <TouchableOpacity onPress={novoNome}>
            <Text>Novo nome</Text>
          </TouchableOpacity>
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