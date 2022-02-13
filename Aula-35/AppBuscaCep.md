Vamos fazer requisições HTTP com componentes funcionais, e não com classes.

    => Componente novo:

        SafeAreaView, serve pra não ficar atrás da statusbar no IOS
    
!!! Essa requisição pode falhar, então é importante colocar nosso código dentro de um bloco try


{ cepUser &&} significa que só vai renderizar caso tenha alguma coisa de cepUser, ou seja, ele não seja null.

# App.js:

    import React, { useState, useRef } from "react";
    import {
      View,
      Text,
      TextInput,
      TouchableOpacity,
      StyleSheet,
      SafeAreaView,
      Keyboard
    } from "react-native";

    import api from "./src/services/api";

    export default function App() {

      const [cep, setCep] = useState("");
      const inputRef = useRef(null);
      const [cepUser, setCepUser] = useState(null);

      async function buscar(){
        if(cep === ""){
          alert("Digite um cep válido!");
          return;
        }

        try {  
          const response = await api.get(`/${cep}/json`);
          console.log(response.data)
          setCepUser(response.data)
          Keyboard.dismiss();
        } catch (error) {
          console.log("Error: " + error)
        }

      }
    
      function limpar(){
        inputRef.current.clear();
        inputRef.current.focus();
        setCepUser(null);
      }

      return(
        <SafeAreaView style={styles.container}>
           <View style={styles.centerContainerView}>
            <Text style={styles.text}>Digite o cep desejado</Text>
            <TextInput 
              style={styles.input} 
              placeholder="79003241"
              value={cep}
              onChangeText={value => setCep(value)}
              keyboardType="numeric"
              ref={inputRef}
            />
          </View>

          <View style={styles.areaBtn}>
            <TouchableOpacity 
              style={[styles.button, {backgroundColor: "#1d75cd"}]}
              onPress={buscar}
            >
              <Text style={styles.buttonText}>Buscar</Text>
            </TouchableOpacity>

            <TouchableOpacity style={[styles.button, {backgroundColor: "#cb0000"}]} onPress={limpar }>
              <Text style={styles.buttonText}>Limpar</Text>
            </TouchableOpacity>
          </View>

          { cepUser &&
            <View style={styles.resultado}>
            <Text style={styles.itemText}>CEP: {cepUser.cep}</Text>
            <Text style={styles.itemText}>Logradouro: {cepUser.logradouro}</Text>
            <Text style={styles.itemText}>Bairro: {cepUser.bairro}</Text>
            <Text style={styles.itemText}>Cidade: {cepUser.localidade}</Text>
            <Text style={styles.itemText}>Estado: {cepUser.uf}</Text>
          </View>
          }
        </SafeAreaView>
      )
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1
      },

      centerContainerView: {
        marginTop: 40,
        alignItems: "center",
        justifyContent: 'center'
      },

      text: {
        marginTop: 25,
        marginBottom: 15,
        fontSize: 25,
        fontWeight: "bold"
      },

      input: {
        backgroundColor: "#fff",
        borderWidth: 1,
        borderColor: "#ddd",
        borderRadius: 5,
        width: "90%",
        padding: 12,
        fontSize: 18
      },

      areaBtn: {
        flexDirection: "row",
        alignItems: "center",
        marginTop: 15,
        justifyContent: "space-around"
      },

      button: {
        height: 50,
        justifyContent: "center",
        alignItems: "center",
        paddingHorizontal: 20,
        borderRadius: 5
      },

      buttonText: {
        fontSize: 20,
        color: "#fff"
      },

      resultado: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center"
      },

      itemText: {
        fontSize: 22
      }
    })

# api.js

    import axios from "axios";
    
    const api = axios.create({
        baseURL: "https://viacep.com.br/ws/"
    })
    
    export default api;