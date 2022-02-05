Nessa aula aprenderemos a por um scroll no nosso aplicativo, deixas as telas scrolláveis.

    criamos 4 Views com tamanho fixo, logo nem todas aparecem na tela mas sabemos que todas estão ali. Para podermos visualizá-las necessitaremos de um scroll. No react native temos um componente para isso chamado ScrollView.

        import { ScrollView } from "react-native"

    tudo que colocarmos dentro desse ScrollView será possivel scrollar

    
=> O ScrollView também tem suas propriedades

    para desabilitar a barra de rolagem vertical: showsVerticalScrollIndicator = false. Por default ela vem como true

=> Também podemos inverter essa lista para horizontal, igual os storys do insta. Precisamos definir uma largura para os elementos (Views nesse caso).

    para isso, definimos a propriedade horizontal={true}, por default vem setada como false.

    => para desabilitar a barra de rolagem horizontal: showshorizontalScrollIndicator = false. Por default ela vem como true quando alteramos para scrollagem horizontal.

=> Na próxima aula veremos sobre Flatlist, listas mais complexas. No ScrollView, ele renderiza tudo de uma vez. Nesse caso todas as 4 views, no Flatlist não, ele so vai renderizar o que está sendo exibido, assim temos uma economia de memória absurda.

App.js:

import React, { Component } from "react";
import { 
  View,
  Text,
  TextInput,
  StyleSheet,
  TouchableOpacity,
  ScrollView
} from "react-native";
class App extends Component {

  render(){
    
    return(
      <View style={styles.container}>
        <ScrollView horizontal={true} showsHorizontalScrollIndicator={false}>
          <View style={styles.box1}></View>
          <View style={styles.box2}></View>
          <View style={styles.box3}></View>
          <View style={styles.box4}></View>
        </ScrollView>
        <ScrollView horizontal={true} showsHorizontalScrollIndicator={false}>
          <View style={styles.box4}></View>
          <View style={styles.box3}></View>
          <View style={styles.box2}></View>
          <View style={styles.box1}></View>
        </ScrollView>
        <ScrollView horizontal={true} showsHorizontalScrollIndicator={false}>
          <View style={styles.box2}></View>
          <View style={styles.box1}></View>
          <View style={styles.box4}></View>
          <View style={styles.box3}></View>
        </ScrollView>
        <ScrollView horizontal={true} showsHorizontalScrollIndicator={false}>
          <View style={styles.box1}></View>
          <View style={styles.box2}></View>
          <View style={styles.box3}></View>
          <View style={styles.box4}></View>
        </ScrollView>
      </View>
    );
  };
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },

  box1: {
    backgroundColor: "red",
    height: 250,
    width: 150
  },

  box2: {
    backgroundColor: "blue",
    height: 250,
    width: 150
  },

  box3: {
    backgroundColor: "green",
    height: 250,
    width: 150
  }, 

  box4: {
    backgroundColor: "yellow",
    height: 250,
    width: 150
  }
})

export default App;