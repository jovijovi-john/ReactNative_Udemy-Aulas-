Nesse caso, a view que está por fora está se adaptando ao que tem dentro dela

    <View style={styles.mainContainer}>
        <View style={styles.container}>

        </View>
    </View>
      
=>> Para ocupar toda a tela, basta passar um flex: 1 nas propriedades de estilo

 render(){
    
    return(
      <View style={styles.mainContainer}>
          <View style={styles.container}></View>
          <View style={styles.container2}></View>
          <Text style={{color: "#00a2c7"}}>Hello World</Text>
      </View>
      
    );
  };
};

const styles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    backgroundColor: "grey"
  },

  container: {
    flex: 1,
    backgroundColor: "red"
  },

  container2: {
    flex: 1,
    backgroundColor: "black"
  }
})
export default App;

=> nesse caso acima, a view principal está com flex 1, ou seja, ocupa a tela toda. Entretanto, duas das suas views filhas também estão com flex 1, e o que resultará?

    =>> como as duas filhas estão com flex 1, ambas terão o mesmo tamanho. Já o text que nao tem flex 1, terá um tamanho diferente delas.

=> considere esse flex ai como o grid template (collumns ou rows), os 1fr 1fr 1fr são basicamente a mesma coisa.

ex:

    const styles = StyleSheet.create({
    mainContainer: {
        flex: 1,
        backgroundColor: "grey"
    },

    container: {
        flex: 1,
        backgroundColor: "red"
    },

    container2: {
        flex: 1,
        backgroundColor: "black"
    },

    container3: {
        flex: 2,
        backgroundColor: "yellow"
    }
    })

    nesse caso, o container3 está com flex 2, isso quer dizer que ele vai ter o tamanho do container1 e do container2 juntos, já que somados, dão o mesmo tamanho dele.

outro ex:

    const styles = StyleSheet.create({
    mainContainer: {
        flex: 1,
        backgroundColor: "grey",
    },

    container: {
        height: 100,
        backgroundColor: "red"
    },

    container2: {
        flex: 1,
        backgroundColor: "black"
    },

    container3: {
        backgroundColor: "red",
        height: 100
    }
    })

    nesse caso, container1 e container3 terão 100px, enquanto o container2 tem flex1. Ou seja, nesse espaço que sobrar, todo esse espaço será ocupado pelo container2. Se o flex fosse 0.5, ele ocuparia apenas metade desse espaço