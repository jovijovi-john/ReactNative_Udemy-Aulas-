fizemos animações tanto de largura quanto de altura só que a gente fez uma OU outra, a gente não fez em sequencia nem em parallelo

    => Sequencia:   

        
        Animated.sequence([

        ]);

        o Animated.sequence vai fazer a primeira coisa do array, depois a segunda, e assim vai. Nao vai fazer todas ao mesmo tempo


        assim:

            Animated.sequence([
                Animated.timing(
                    this.state.largAnimada,
                    {
                        toValue: 250,
                        duration: 2000
                    }
                ),
            
                Animated.timing(
                    this.state.altAnimada,
                    {
                        toValue: 200,
                        duration: 2000
                    }
                )
            ]).start()

    => Paralelo

        
        Animated.parallel([

        ]);

        o Animated.parallel vai fazer a primeira coisa do array ao mesmo tempo que faz a segunda, a terceira, e assim vai. 

        assim:

            Animated.parallel([
                Animated.timing(
                    this.state.largAnimada,
                    {
                        toValue: 250,
                        duration: 2000
                    }
                ),
            
                Animated.timing(
                    this.state.altAnimada,
                    {
                        toValue: 200,
                        duration: 2000
                    }
                )
            ]).start()

Animação de fade:


    constructor(props){
        super(props);
        this.state = {
            largAnimada: new Animated.Value(150),
            altAnimada: new Animated.Value(50), 
            opacidadeAnimada: new Animated.Value(1)
        };

        Animated.parallel([
        Animated.timing(
            this.state.largAnimada,
            {
                toValue: 250,
                duration: 2000
            }
        ),
    
        Animated.timing(
            this.state.altAnimada,
            {
                toValue: 200,
                duration: 2000
            }
        ),

        Animated.timing(
            this.state.opacidadeAnimada,
            {
                toValue: 0,
                duration: 2000
            }
        )
        ]).start()
    }

Dá para fazer animações aninhadas!!!:

    Animated.sequence([
      Animated.timing(
        this.state.opacidadeAnimada,
        {
          toValue: 1,
          duration: 1500
        }
      ),

      Animated.parallel([
        Animated.timing(
          this.state.largAnimada,
          {
            toValue: 300,
            duration: 2000
          }
        ) ,
      
        Animated.timing(
          this.state.altAnimada,
          {
            toValue: 200,
            duration: 500
          }
        )
      ]),

      Animated.timing(
        this.state.opacidadeAnimada,
        {
          toValue: 0,
          duration: 1500
        }
      )

    ]).start()

# App.js:

    import React, { Component } from "react";
    import { 
        View, 
        StyleSheet, 
        Text,
        ActivityIndicator,
        Animated
    } from "react-native";

    class App extends Component {

    constructor(props){
        super(props);
        this.state = {
            largAnimada: new Animated.Value(150),
            altAnimada: new Animated.Value(50), 
            opacidadeAnimada: new Animated.Value(0)
        };

        Animated.sequence([
        Animated.timing(
            this.state.opacidadeAnimada,
            {
                toValue: 1,
                duration: 1500
            }
        ),

        Animated.parallel([
            Animated.timing(
            this.state.largAnimada,
            {
                toValue: 300,
                duration: 2000
            }
            ) ,
        
            Animated.timing(
            this.state.altAnimada,
            {
                toValue: 200,
                duration: 500
            }
            )
        ]),

        Animated.timing(
            this.state.opacidadeAnimada,
            {
                toValue: 0,
                duration: 1500
            }
        )

        ]).start()
    }

    render() {
        return(
        <View  style={styles.container}>
            <Animated.View style={{width: this.state.largAnimada, 
                        height: this.state.altAnimada, 
                        backgroundColor: "#4169e1", 
                        justifyContent:"center",
                        opacity: this.state.opacidadeAnimada
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

