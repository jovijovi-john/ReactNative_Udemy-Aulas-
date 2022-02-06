se quiser que apenas números sejam passados, defina dentro do InputText a seguinte propriedade:

    <InputText
        keyboardType="numeric"
    />

App.js:
 
import React, { Component } from "react";
import { 
  View, 
  StyleSheet, 
  Text,
  Switch,
  TextInput,
  TouchableOpacity
} from "react-native";

import { Picker } from "@react-native-picker/picker";
import Slider from "@react-native-community/slider";
class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      nome: "",
      idade: "",
      sexo: 0,
      sexos: [
        {value: 0, sexName:"Masculino"},
        {value: 1, sexName: "Feminino"}
      ],
      limite: 600,
      estudante: false
    };

    this.enviarDados = this.enviarDados.bind(this)
  }

  enviarDados(){
    if (this.state.idade === "" || this.state.nome === ""){
      alert("Preencha todos os dados corretamente!")
    } else {
      alert(
        "Conta aberta com sucesso!!!" + "\n\n" +
        "Nome: " + this.state.nome + "\n" +
        "Idade: " + this.state.idade + "\n" +
        "Sexo: " + this.state.sexos[this.state.sexo].sexName + "\n" +
        "Limite Conta: " + this.state.limite.toFixed(2) + "\n" + 
        "Conta Estudante: " + (this.state.estudante ? "Ativo" : "Inativo")
      )
    }
  }

  render(){

    let sexoItems = this.state.sexos.map((sexo, key) => {
      return <Picker.Item key={sexo.value} value={sexo.value} label={sexo.sexName}/>
    })
    return(
      <View style={styles.container}>

        <Text style={styles.tituloApp}>Banco Agiota</Text>
        
        {/* Nome */}
        <View>
          <Text style={styles.label}>Nome:</Text>
          <TextInput 
            style={styles.input}
            placeholder="Digite seu nome completo"
            onChangeText={(value) => this.setState({
              nome: value
            })}
          />
        </View>

        {/* Idade */}
        <View>
          <Text style={styles.label}>Idade: </Text>
          <TextInput 
            style={[styles.inputIdade, styles.input]} 
            placeholder="Informe sua idade"
            keyboardType="numeric"
            onChangeText={ (value) => {
              this.setState({ idade: value})
            }}
          />
        </View>

        {/* Sexo */}
        <View >
          <Text style={styles.label}>Sexo: </Text>
          <Picker
            selectedValue={this.state.sexo}
            onValueChange={value => this.setState({
              sexo: value
            })}
          >
            {sexoItems}
          </Picker>
        </View>
            
        {/* Limite */}
        <View> 
          <View style={styles.limitArea}>
            <Text style={styles.limitText}>Limite:  </Text>
            <Text style={[styles.limitText, {color: "#00aa00"}]}>R$ {this.state.limite.toFixed(0)}</Text>
          </View>
          <Slider 
            onValueChange={value => this.setState({
              limite: value
            })}
            style={{marginTop: 15 }}
            minimumValue={600}
            maximumValue={1200}
          />

        </View>

        {/* Estudante */}
        <View style={styles.areaEstudante}>
          <Text style={{fontSize: 16, fontWeight: "bold"}}>Estudante: </Text>
          <Switch 
            value={this.state.estudante}
            onValueChange={value => this.setState({estudante: value})}
          />
        </View>

        <TouchableOpacity
          style={styles.button} 
          onPress={this.enviarDados}
        >
          <Text style={styles.textButton}>Abrir Conta</Text>
        </TouchableOpacity>
      </View>
    );
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 40,
    paddingHorizontal: 20
  },
  
  tituloApp: {
    textAlign: "center",
    fontSize: 25,
    fontWeight: "bold"
  },

  label: {
    marginTop: 30,
    fontWeight: "bold",
    fontSize: 16
  },

  input:{
    height: 45,
    borderWidth: 1,
    borderColor: "#c2c2c2",
    borderRadius: 10,
    paddingLeft: 10,
    marginTop: 5
  },

  limite: {
    marginTop: 10,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center"
  },

  areaEstudante: {
    flexDirection: "row",
    alignItems: "center"
  },

  limitArea: {
    flexDirection: "row",
    alignItems: "center",
    marginTop: 15
  },
  
  limitText: {
    fontSize: 16, fontWeight: "bold"
  },

  button: {
    marginTop: 20,
    borderWidth: 1,
    height: 60,
    borderRadius: 10,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#333"
  },
  textButton:{
     fontSize: 20,
     fontWeight: 'bold',
     color: '#fff'
  },


})

export default App;

