Quando trabalhamos com animações no react native, nunca pedimos diretamente no componente. Nos fazemos através de propriedades.

Ex: Passamos as propriedades no view e fazemos as animações fora do render

Importar animated:

    import { Animated } from "react-native"

    uso:

        Sem animated: <View></View>
        Com animated: <Animated.View></Animated.View>

        nos states:

            ao invés de:

                largura: 150,
                altura: 150,

            faça:

                largura: new Animated.Value(valorInicial),
                altura: new Animated.Value(valorInicial)

        
        constructor(props){
        super(props);
        this.state = {
            largAnimada: new Animated.Value(150),
            altAnimada: new Animated.Value(50), 
        };

        Animated.timing(
          this.state.largAnimada,
          {
              toValue: 300,
              duration: 2000 //em MS
          }
        ).start();
    }

=> TODA ANIMAÇÃO DEVE SER STARTADA

#App.js:

    import React, { Component } from "react";
    import { 
    View, 
        StyleSheet, 
        Text,
        Animated
    } from "react-native";

    class App extends Component {

        constructor(props){
            super(props);
            this.state = {
                largAnimada: new Animated.Value(150),
                altAnimada: new Animated.Value(50), 
            };

            Animated.timing(
                this.state.largAnimada,{
                    toValue: 250,
                    duration: 2000
                }
                
            ).start();

            Animated.timing(
                this.state.altAnimada,
                {
                    toValue: 250,
                    duration: 2000
                }
            ).start();
        }

        render() {
            return(
            <View  style={styles.container}>
                <Animated.View style={{width: this.state.largAnimada, 
                            height: this.state.altAnimada, 
                            backgroundColor: "#4169e1", 
                            justifyContent:"center"}}>

                <Text style={{color: "#fff", 
                                fontSize: 22, 
                                textAlign: "center"}}>
                    Carregando...
                </Text>
                </Animated.View>
            </View>
            )
        };
    };

    const styles = StyleSheet.create({
        container: {
            flex: 1,
            alignItems :"center",
            justifyContent: 'center',
        }
    })

    export default App;

