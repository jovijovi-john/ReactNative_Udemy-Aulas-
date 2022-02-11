Animated.loop()

    Só podemos passar UMA animação
    Então colocamos uma sequencia, e dentro dela colocamos duas animações:
        - Indo ate 200
        - Voltando ate 150

# App.js
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
          altAnimada: new Animated.Value(35)
        };
    
        Animated.loop(
          Animated.sequence([
          
            Animated.timing(
              this.state.largAnimada,
              {
                toValue:  200,
                duration: 700 
              }
            ),
    
            Animated.timing(
              this.state.largAnimada,
              {
                toValue: 150,
                duration: 700
              }
            )
          ])
        ).start()
      }
    
      render() {
        return(
          <View  style={styles.container}>
            <Animated.View style={{width: this.state.largAnimada, 
                          height: this.state.altAnimada, 
                          backgroundColor: "#4169e1", 
                          justifyContent:"center",
                          borderRadius: 25
            }}>
    
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
    
    