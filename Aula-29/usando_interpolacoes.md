para fazer uma interpolação, por exemplo, de 0% ate 100%:

    dentro do render => 

    let porcentagemAnimada = this.state.animatedWidth.interpolate({
        inputRange: [0, 100],
        outputRange: ["0%", "100%"]
    }) 

## App.js:
    
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
          animatedWidth: new Animated.Value(0),
          animatedHeight: new Animated.Value(0)
        };
    
          Animated.timing(
            this.state.animatedWidth,
            {
              toValue: 100,
              duration: 5000,
            }
          ).start()
      }
    
    
      render() {
      
        let porcentagemAnimada = this.state.animatedWidth.interpolate({
          inputRange: [0, 100],
          outputRange: ["0%", "100%"]
        }) 
    
        
    
        return(
          <View  style={styles.container}>
           
    
            <Animated.View style={{backgroundColor: "#4169e1",
                          width: porcentagemAnimada,
                          height: 25              
            }}></Animated.View>
    
          </View>
        )
      };
    };
    
    const styles = StyleSheet.create({
      container: { 
        flex: 1,
        alignItems: "flex-start",
        justifyContent: "center"
      }
      ,
    })
    
    export default App;

