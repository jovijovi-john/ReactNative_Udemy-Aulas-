Nessa aula aprenderemos a usar os modals. São praticamente uma página mas não são uma página, é como se fosse um pop-up.

    Podemos utiliza-lo em componente separado ou no próprio componente.

Devemos importar o Modal do  react-native:
    import {Modal} from "reac-native";
    
         <Button title="Entrar" onPress={}/>
         no onPress precisamos chamar uma função que abra o modal na tela

Quando a visibilidade ta false, o modal não é exibido para o usuário
Quando a visibilidade for true, o modal vai ser exibido. Vamos controlar através da state

props:

    animationType="slide", subir de baixo pra cima
    animationType="fade"
    animationType="none"

    visible={}
    transparent={} => define se é transparent ou nao

Vamos componentizar agora:

    ./src/entrar.js

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
  FlatList,
  Button,
  Modal
} from "react-native";

import AsyncStorage from '@react-native-async-storage/async-storage';
import Entrar from "./src/entrar"

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      modalVisible: false
    };

    this.entrar = this.entrar.bind(this)
    this.sair = this.sair.bind(this)
  }

  entrar(){
    this.setState({
      modalVisible: true
    })
  }

  sair(){
    this.setState({
      modalVisible: false
    })
  }

  render() {
    return(
      <View style={styles.container}>
          <Button title="Entrar" onPress={this.entrar}/>

          <Modal animationType="slide" visible={this.state.modalVisible}>
            <View style={{margin: 15, flex:1, justifyContent: "center", alignItems: "center"}}>
              <Entrar sair={() => {this.sair()}}/>
            </View>
          </Modal>
      </View>
    );
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#ddd"
  }
})

export default App;



entrar.js: 

import React, { Component } from "react";
import { 
  View, 
  Text,
  Button,
} from "react-native";

import AsyncStorage from '@react-native-async-storage/async-storage';

export default class Entrar extends Component {


  render() {
    return(      
        <View style={{backgroundColor: "#222", height: 350, width: "100%", borderRadius: 15}}>
            <Text style={{textAlign: "center", paddingTop: 15,color: "#fff", fontSize: 28}}>Seja bem vindo!</Text>
            <Button title="sair" onPress={this.props.sair} />
        </View>
    );
  };
};


