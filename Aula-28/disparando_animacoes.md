# App:

    import React, { Component } from "react";
    import { 
      View, 
      StyleSheet, 
      Text,
      Animated,
      TouchableOpacity
    } from "react-native";

    class App extends Component {

      constructor(props){
        super(props);
        this.state = {
          largAnimada: new Animated.Value(150),
          altAnimada: new Animated.Value(35),
          opAnimada: new Animated.Value(0),
          textVisible: false
        };

        this.carregarGrafico = this.carregarGrafico.bind(this);
      }
    
      carregarGrafico() { 
        Animated.sequence([
          Animated.timing(
            this.state.opAnimada,
            {
              toValue: 1,
              duration: 400
            }
          ),
          Animated.timing(
            this.state.altAnimada,
            {
              toValue: 300, 
              duration: 1000
            }
          )
        ]).start()

        setTimeout(() => {
          this.setState({
            text: true
          })
        }, 1400)

      }

      render() {

        return(
          // View global
          <View  style={{flex: 1}}>

            {/* Header */}
            <View style={{height: 120, 
                    alignItems: "center", 
                    justifyContent: "center", 
                    flexDirection: "row",
                    backgroundColor: "#4169e1"
            }}>

              <TouchableOpacity style={{marginTop: 25}} onPress={() => {
                  this.carregarGrafico()
                  }}>
                <Text style={{color: "#fff", fontSize: 25}}>Gerar gráfico</Text>
              </TouchableOpacity>
            </View>

            {/* View do carregando */}
            <View style={{flex: 1, 
                          flexDirection: "column", 
                          justifyContent: "flex-end", 
                          alignItems:"center"
            }}>

              <Text>{this.state.text ? "Vendas" : ""}</Text>  

              <Animated.View style={{width: this.state.largAnimada, 
                            height: this.state.altAnimada, 
                            backgroundColor: "#ff0000",
                            justifyContent:"center",
                            opacity: this.state.opAnimada
              }}>

                <Text style={{color: "#fff", 
                              fontSize: 22, 
                              textAlign: "center"}}>
                  R$ 150,00
                </Text>
              </Animated.View>
            </View>

          </View>
        )
      };
    };

    const styles = StyleSheet.create({

    })

    export default App;