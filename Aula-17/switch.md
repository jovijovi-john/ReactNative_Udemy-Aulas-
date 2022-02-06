Toggle button, aquele de ligar e desligar

=> Importação:

    import { Switch } from "react-native";

=> Uso: 

    <Switch 
        value={}
        onValueChange={}
        thumbColor={}
    />

    value => true || false (valor que está no momento)

    onValueChange => sempre que trocar o valor (ligar ou desligar)
    thumbColor => Altera a cor da bolinha

App.js:

import React, { Component } from "react";
import { 
  View, 
  StyleSheet, 
  Text,
  Switch
} from "react-native";

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      status: false
    };
  }

  render(){

    return(
      <View style={styles.container}>
        <Switch 
          value={this.state.status}
          onValueChange={value => this.setState({
            status: value
          })}
          thumbColor={"#3f0fff"}
        />

        <Text style={ {textAlign: "center", fontSize: 20} }>
          { (this.state.status) ? "Ligado": "Desligado" }
          </Text>
      </View>
    );
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 30
  }
})

export default App;

