Instalação: npm install axios --save
Visualizar apis: JSON Viewer (chrome extension)
    
    Link da api: https://sujeitoprogramador.com/r-api/?api=filmes

    crie uma pasta (services) dentro de src para separar a base url dessas requisicoes q vamos fazer


Importação:

    import axios from "axios";

Usando:

    const api = axios.create({
        baseUrl: "https://sujeitoprogramador.com/"
    })

    a base url é so essa https://sujeitoprogramador.com/
    e não essa  https://sujeitoprogramador.com/r-api/?api=filmes
    pois apos o .com/ é uma nova requisição que ta buscando todos os filmes. Poderiamos ter uma outra requisição buscando apenas uma categoria então seria outro parâmetro.


Quando nosso aplicativo eu quero que ele vá la na url, na api, e busque todos aqueles filmes para estruturarmos dentro de uma lista. 

Logo o ciclo de vida que utilizaremos é o componentDidMount

    componentDidMount() {
        const response = api.get() // é .get() porque querermos trazer coisas da nossa api
    }

    e dentro desse .get passaremos a informação que queremos buscar, no caso r-api?api=filmes

    componentDidMount(){
        const response  = api.get("r-api?api=filmes")
    }

    quando fazemos isso, ele ta pegando a baseUrl e botando antes desse .get()
    como a requisição é algo assincrono, ele vai la na api, busca pra gente e traz para o nosso aplicativo, precisamos colocar antes desse ciclo de vida um async, e colocar um await no momento que ele faz a requisição, no caso antes de api.get

    async componentDidMount(){
        const response = await api.get("r-api?api=filmes")
    }

    => Quando o axios faz uma requisição, o valor da resposta fica no .data:
        response.data

    => Uma coisa importante é que o keyExtrator do flatlist so aceita a key em string!!!

## App.js: 


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

import api from "./src/services/api";
import Filmes from "./src/Filmes";

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      filmes: []
    };
  }

  async componentDidMount(){
    const response = await api.get("r-api/?api=filmes")
    
    this.setState({
      filmes: response.data
    })
  }

  render() {
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
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 30
  },


})

export default App;



## api.js:




import axios from "axios";

const api = axios.create({
    baseURL: "https://sujeitoprogramador.com/"
});

export default api