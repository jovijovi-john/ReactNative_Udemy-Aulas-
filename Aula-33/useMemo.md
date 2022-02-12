# useMemo

Ajuda a manter a performance das nossas aplicações e tomar um cuidado onde a gente aplica calculos pra não fazer renderizações desnecessárias

importação:

    import { useMemo } from "react";
    
Não entendi algumas coisas muito bem. Veja a aula 47 do curso se quiser utilizar isto melhor

# App.js:

    import React, { useEffect, useState, useMemo} from "react";
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
          />

          <TouchableOpacity style={styles.btn} onPress={alteraNome}>
            <Text style={styles.btnText}>Altera nome</Text>
          </TouchableOpacity>

          <Text style={styles.texto}>{nome}</Text>
          <Text style={styles.texto}>Tem {letrasNome} letras</Text>
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