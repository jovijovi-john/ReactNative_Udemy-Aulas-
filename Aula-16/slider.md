Nessa aula estudaremos sobre slider, aquele que parece volume de musica, que da pra aumentar/diminuir:
    https://github.com/callstack/react-native-slider


=>> Instalação:

    expo install @react-native-community/slider

=> Importação

    import Slider from "@react-native-community/slider";

=> Uso:

    <Slider 
        minimumValue={}
        maximumValue={}
        onValueChange={}
        value={}
    />

    minimumValue => Menor valor possível
    maximumValue => Maior valor possível
    onValueChange => Função acionada quando o usuario muda o valor
    value => Valor que ele tá atualmente

=> Dá pra trocar as cores também. Tipo, sabe quando ta com fone no celular e quando deixa mais q um certo ponto(70%) a cor daquele slider muda? fica vermelho. Então, da pra fazer aquilo aqui.

    No caso, o minimunTrackTintColor pinta tudo que tiver atrás da bolinha, e o maximunTrackTintColor pinta o que está à frente

    
    <Slider 
        minimumValue={}
        maximumValue={}
        onValueChange={}
        value={}
        minimumTrackTintColor="#"  
    />

App.js:

import React, { Component } from "react";
import { 
  View, 
  StyleSheet, 
  Text
} from "react-native";

import Slider from "@react-native-community/slider"

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      valor: 5
    };
  }

  render(){

  
    return(
      <View style={styles.container}>

        <Slider 
          minimumValue={20}
          maximumValue={200}
          onValueChange={ (valorSelecionado) => this.setState({
            valor: valorSelecionado
          })}
          value={this.state.valor}
          minimumTrackTintColor={"#29ff82"}
          maximumTrackTintColor={"#9e0000"}
        />
        <Text style={{textAlign:"center", fontSize: 30}}>Você tem {this.state.valor.toFixed(1)} Kg</Text>
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

