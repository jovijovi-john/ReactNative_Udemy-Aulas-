Picker é um componente que podemos utilizar em formulários, buscas, etc. Veremos como utilizá-lo nessa aula.

=> Instalação:

    Para instalar o picker pelo expo: expo install @react-native-picker/picker

=> Documentação:

    https://docs.expo.dev/versions/latest/sdk/picker/

=> Importação:

    import {Picker} from '@react-native-picker/picker';

=> Uso:

    Picker.Item é um item dentro daquele picker

=> Props:

    - style
    - selectedValue
    - onValueChange
    - testId
    - enabled
    - promp
    - itemStyle
    - mode

=> mão na massa:

    <Picker.Item key={} value={} label=""/>

    key => para diferenciar cada item, um identificador único
    value => valor que vai ter quando alguem selecionar
    label => o que vai aparecer
    
        <Picker>
          <Picker.Item key={1} value={1} label="Calabresa" />
          <Picker.Item key={2} value={2} label="Brigadeiro" />
          <Picker.Item key={3} value={3} label="Mussarela" />
          <Picker.Item key={4} value={4} label="Frango com Catupiry" />
          <Picker.Item key={5} value={5} label="4 Queijos" />
          <Picker.Item key={6} value={6} label="Portuguesa" />
          <Picker.Item key={7} value={7} label="Camarão" />
        </Picker>
    
    entretanto, quando selecionarmos qualquer uma dessas opções, não vai mudar. Precisamos fazer algumas alterações NO PICKER

    <Picker selectedValue={}>
        o selectedValue vai pegar lá do nosso state

    o selectedValue vai setar como selecionado a key que for passada para ele

      <Picker 
          selectedValue={this.state.pizza}
          onValueChange={ (itemValue, itemIndex) => this.setState({
            pizza: itemValue
          })}
        >
          <Picker.Item key={1} value={1} label="Calabresa" />
          <Picker.Item key={2} value={2} label="Brigadeiro" />
          <Picker.Item key={3} value={3} label="Mussarela" />
          <Picker.Item key={4} value={4} label="Frango com Catupiry" />
          <Picker.Item key={5} value={5} label="4 Queijos" />
          <Picker.Item key={6} value={6} label="Portuguesa" />
          <Picker.Item key={7} value={7} label="Camarão" />
        </Picker>

        <Text style={styles.pizzas}>Você escolheu: Pizza Calabresa</Text>
        <Text style={styles.pizzas}>R$: 59,90</Text>
        <Text style={{fontSize: 30}}>{this.state.pizza}</Text>

    => Renderização dinâmica / Renderização mapeada:

App.js:

import React, { Component } from "react";
import { 
  View, 
  StyleSheet, 
  Text
} from "react-native";

import {Picker} from '@react-native-picker/picker';

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      pizza: 0,
      pizzas: [
                {key: 1, nome: "Calabresa", valor: 35.90},
                {key: 2, nome: "Brigadeiro", valor: 25.90},
                {key: 3, nome: "Mussarela", valor: 38.00},
                {key: 4, nome: "Frango com Catupiry", valor: 37.50},
                {key: 5, nome: "4 Queijos", valor: 50.00},
                {key: 6, nome: "Portuguesa", valor: 45.00},
                {key: 7, nome: "Camarão", valor: 55.00}
      ]
    };
  }

  render(){

    let pizzasItem = this.state.pizzas.map( (value, key) => {
      return <Picker.Item key={key} value={key} label={value.nome}/>
    })
    
    return(
      <View style={styles.container}>
        <Text style={styles.logo}>Menu Pizza</Text>

        <Picker 
          selectedValue={this.state.pizza}
          onValueChange={ (itemValue, itemIndex) => this.setState({
            pizza: itemValue
          })}
        >
          
          {pizzasItem}

        </Picker>

        <Text style={styles.pizzas}>Você escolheu: {this.state.pizzas[this.state.pizza].nome}</Text>
        <Text style={styles.pizzas}>R$: {this.state.pizzas[this.state.pizza].valor.toFixed(2)}</Text>
        <Text style={{fontSize: 30}}>{this.state.pizza}</Text>
      </View>
    );
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 30
  },

  logo: {
    textAlign: "center",
    fontSize: 28,
    fontWeight: "bold"
  },

  pizzas: {
    marginTop: 15,
    fontSize: 28,
    textAlign: "center"
  }
})

export default App;


