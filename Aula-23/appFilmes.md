
const {nome, foto} = this.props.data;

    serve pra pegar o nome e foto de this.props.data,
    assim nao precisamos escrever this.props.data.nome ou this.props.data.foto toda vez, mas sim nome ou foto

Criando Loading:

    Ver sobre o componente: ActivityIndicator
    é aquela bolinha que fica girando quando ta carregando

    <ActivityIndicator color={"#09A6FF"} size={40} />

# App.js:

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
  Modal,
  ActivityIndicator
} from "react-native";

import api from "./src/services/api";
import Filmes from "./src/Filmes";

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      filmes: [],
      loading: true
    };
  }

  async componentDidMount(){
    const response = await api.get("r-api/?api=filmes")

    this.setState({
      filmes: response.data,
      loading: false
    })
  }

  render() {

    if (this.state.loading) {
      return(
        <View style={{alignItems: "center", justifyContent: "center", flex: 1}}>
          <ActivityIndicator color={"#09A6FF"} size={40} />
        </View>
      )
    } else {
      return(
        <View style={styles.container}>
            <FlatList 
              style={styles} 
              data={this.state.filmes} 
              keyExtractor={(item) => item.id.toString()}
              renderItem={({item}) => <Filmes data={item}/>}
            />
        </View>
      );
    }
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 30
  },


})

export default App;



# Filmes/index.js

import React, { Component } from "react";
import { View, Text, StyleSheet, Image, TouchableOpacity} from "react-native";

export default class Filmes extends Component {

    render() {
        const {nome, foto} = this.props.data;
        return(
            <View>
                
                <View style={styles.card}>
                    <Text style={styles.titulo}>{nome}</Text>
                    <Image style={styles.capa} source={{uri: foto}}/>
                
                    <View style={styles.areaBotao}>
                        <TouchableOpacity style={styles.botao} onPress={() => {alert(nome)}}>
                            <Text style={styles.botaoTexto}>LEIA MAIS</Text>
                        </TouchableOpacity>
                    </View>
                </View>

            </View>
        )
    }
}

const styles = StyleSheet.create({
    card: {
        backgroundColor :"#fff",
        
        shadowColor: "#000",
        shadowOffset: {width: 0, height: 1},
        shadowOpacity: 0.8,
        elevation: 3,
        shadowRadius: 5,
        
        margin: 15,
        borderRadius: 5
    },

    titulo: {
        fontSize: 18,
        padding: 15 
    },

    capa: { 
        height: 250,
        zIndex: 2
    },

    areaBotao: {
        alignItems: "flex-end",
        marginTop: -40,
        zIndex: 9
    },

    botao: {
        width: 100,
        backgroundColor: "#09A6FF",
        opacity: 1,
        padding: 8,
        borderTopLeftRadius: 5,
        borderBottomLeftRadius: 5
    },

    botaoTexto: {
        textAlign: "center",
        color: "#fff"
    },
});

# api.js

import axios from "axios";

const api = axios.create({
    baseURL: "https://sujeitoprogramador.com/"
});

export default api