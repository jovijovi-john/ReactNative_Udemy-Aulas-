Aprenderemos a salvar dados localmente e sobre ciclos de vida no react

Vamos salvar um nome no celular, e quando eu fechar o aplicativo e abrir novamente o nome está salvo e será carregado.

Precisamos instalar o AsyncStorage, pois o react native separou o pacote dele então precisamos instalar. 
    https://docs.expo.dev/versions/latest/sdk/async-storage/
    npm install @react-native-async-storage/async-storage
    <!-- npm install @react-native-community/async-storage --save  -->

Importação:
    import AsyncStorage from '@react-native-async-storage/async-storage';

Importar:

    import {Keyboard} from "react-native"
    conseguimos controlar o keyboard do TextInput


    Keyboard.dismiss(); => fecha o teclado

Ciclos de vida:

    toda vez que um componente é mostrado na tela, temos um ciclo de vida pra isso
    toda vez que uma state é atualizada, temos um ciclo de vida pra isso:
        se a state nome for atualizada, faz alguma coisa ai

    Ele fica monitorando lá. Também há ciclos de vida para quando o componente é desmontado (encerrado)


    IMPORTANTE:

        //ComponentDidMount - Quando o componente é montado em tela
                ou seja, toda vez que o componente é montado ele executa essa função, exemplo:
                
                    componentDidMount(){
                        alert("Oláaaaaaa meu app")
                    }

        //ComponentDidUpdate - Toda vez que um state é atualizado, fazer algo...

            componentDidUpdate(prevProps, prevState){}
            
                prevProps => props anteriores, se mudaram...
                prevState => estado anterior dele ser alterado 

            como não vamos utilizar o prevProps, podemos substituilo por um underline:

            componentDidUpdate(_, prevState){}

            // se o estado anterior for diferente do que ta agora
            if(prevState != nome){
                AsyncStorage.setItem("nome", nome);
            }

            como ele é assíncrono (async), precisamos utilizar o async await. Assim ele será uma função assíncrona. Aonde eu quiser que ele espere, usamos o await. o async fica na frente da função. 

            
            async componentDidUpdate(prevProps, prevState){
                let nome = this.state.nome;

                // se o estado anterior for diferente do que ta agora
                if(prevState != nome){
                    await AsyncStorage.setItem("nome", nome);
                    // olha, espera pra mim porque essa requisição pode demorar um pouquinho, então espera ai
                }
            }

        => Quando o componente for montado, vamos la no banco e buscar o nome:

            async componentDidMount(){
                await AsyncStorage.getItem("nome").then((value) => {
                    this.setState({nome: value});
                })
            }

            o .then() é uma função de callback que é retornada em caso de sucesso.
            .then((value) => {}) value é o valor devolvido pelo getItem() se deu sucesso.

  }


App.js:

import React, { Component } from "react";
import { 
  View, 
  StyleSheet, 
  Text,
  Image,
  TouchableOpacity,
  TextInput,
  Keyboard,
  FlatList
} from "react-native";

import AsyncStorage from '@react-native-async-storage/async-storage';

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      input: "",
      nome: ""
    };

    this.gravaNome = this.gravaNome.bind(this)
  }

  gravaNome(){
    this.setState({
      nome: this.state.input
    });

    alert("Salvo com sucesso!");
    Keyboard.dismiss();
  }
  
  async componentDidMount(){
    await AsyncStorage.getItem("nome").then((value) => {
      this.setState({nome: value});
    })
  }

  async componentDidUpdate(_, prevState){
    const nome = this.state.nome;

    // se o estado anterior for diferente do que ta agora
    if(prevState != nome){
      await AsyncStorage.setItem("nome", nome);
    }
  }

  render() {
    return(
      <View style={styles.container}>
         
        <View style={styles.viewInput}>
          <TextInput 
            style={styles.input}
            value={this.state.input}
            onChangeText={(value) => this.setState({input: value})}
            underlineColorAndroid="transparent"
          />

          <TouchableOpacity onPress={this.gravaNome}>
            <Text style={styles.botao}>
            +
            </Text>
          </TouchableOpacity>

        </View>
        
        <Text style={styles.nome}>
          {this.state.nome}
        </Text>
      </View>
    );
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 40,
    alignItems: "center"
  },

  viewInput: {
    flexDirection: "row",
    alignItems: "center"
  },

  input: {
    width: 350,
    height: 40,
    borderColor: "#000",
    borderWidth: 1,
    padding: 10
  },

  botao: {
    backgroundColor: "#222",
    height: 40,
    color: "#fff",
    padding: 10,
    marginLeft: 4 
  },

  nome: {
    fontSize: 30,
    textAlign: "center",
    textAlign: "center"
  }



})

export default App;

