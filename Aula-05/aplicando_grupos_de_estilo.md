=>> para criar grupos de estilo no RN, precisamos importar  o StyleSheet

    import {StyleSheet} from "react-native";
    ...
    ... 
        const styles = StyleSheet.create({

        })

=>> também é possivel fazer com que um componente tenha mais de um grupo de estilo. Para isso, basta colocar styles={[]} com um colchete dentro, assim é so ir passando cada um dos estilos como uma posição desse array. Exemplo:

  render(){
    
    return(
      <View style={styles.container}>

        <Text style={[ styles.textoPrincipal, styles.alinhaTexto ]}>Escuta o que eu digo</Text>
        <Text style={styles.textoPrincipal}>O flamengo é seleção!</Text>

      </View>
      
    );
  };

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#000",
    justifyContent: "center",
    flex: 1
  },

  textoPrincipal: {
    fontSize: 25,
    color: "#ff0000"
  },

  alinhaTexto: {
    textAlign: "right"
  }
  
});

>> em App.js:

import React, { Component } from "react";
import { 
  View,
  Text,
  Button,
  StyleSheet
} from "react-native";


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      nome: ""
    };

    this.entrar = this.entrar.bind(this);
  }

  entrar(nome){
    this.setState({
      nome: nome
    })
  }
  
  render(){
    
    return(
      <View style={styles.container}>

        <Text style={styles.textoPrincipal}>Eu sou texto 1</Text>
        <Text>Eu sou texto 2</Text>
        <Text>Eu sou texto 3</Text>
        <Text>Eu sou texto 4</Text>

      </View>
      
    );
  };
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#000",
    alignItems: "center",
    justifyContent: "center",
    flex: 1
  },

  textoPrincipal: {
    fontSize: 25,
    color: "#ff0000"
  }
  
});

export default App;
