Flatlists são boas para listas de grande escala, listas que têm muita coisa para serem exibidas, pois ele só exibe/aloca os itens que estão sendo exibidos.

<Flatlist/> => Tem duas propriedades que são obrigatórias:
                data={}
                renderItem={}
            
            o data é a lista em si que ele vai receber
            e o renderItem é responsável por mostrar / renderizar a lista no nosso aplicativos

no react native, cade item deve ter uma key para que possamos identificá-lo posteriormente (num evento de clique por exemplo).

Precisamos utilizar a propriedade keyExtrator para dizer qual é a chave única. O flatlist ja configura automaticamente para termos um scroll

App.js:

import React, { Component } from "react";
import { 
  View,
  Text,
  StyleSheet,
  FlatList
} from "react-native";
class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      feed: [
        {id: "1", nome: "John", idade: 20, email: "jovi@jovi.com"}, 
        {id: "2", nome: "Zed", idade: 4, email: "zed@zedinho.com"},
        {id: "3", nome: "Hades", idade: 27, email: "deus_do_submundo@hades.com"},
        {id: "4", nome: "Zeno", idade: 53, email: "zenoSama@zeno.com"},
        {id: "5", nome: "Zeno", idade: 53, email: "zenoSama@zeno.com"},
        {id: "6", nome: "Zeno", idade: 53, email: "zenoSama@zeno.com"}
      ]
    }
  }
  render(){
    
    return(
      <View style={styles.container}>
        <FlatList 
          data={this.state.feed}
          keyExtractor={ (item) => { item.id } }
          renderItem={ ( {item} ) => <Pessoa data={ item }/> }
        />
      </View>
    );
  };
};

class Pessoa extends Component {

  render() {
    return(
      <View style={styles.areaPessoa}>
        <Text style={styles.textoPessoa}>Nome: {this.props.data.nome}</Text>
        <Text style={styles.textoPessoa}>Idade: {this.props.data.idade}</Text>
        <Text style={styles.textoPessoa}>Email: {this.props.data.email}</Text>
      </View>
    );
  };
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
  },

  areaPessoa: {
    backgroundColor: "#222",
    height: 200,
    marginBottom: 15
  },

  textoPessoa: {
    color: "#fff",
    fontSize: 20
  }
})

export default App;

