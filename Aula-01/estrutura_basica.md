=> em um projeto startado apenas com react-native init, sem expo, o primeiro arquivo chamado é o index.js. Como não temos o index.js aqui, veja como seria:

    /**
    * @format
    */

    import {AppRegistry} from 'react-native';
    import App from './App';
    import {name as appName} from './app.json';

    AppRegistry.registerComponent(appName, () => App);

=> esse index.js registra esse aplicativo e chama o App que é o componente principal. Registra um componente e registra o App como primeiro componente a ser exibido quando abrimos o aplicativo

=> o que é retornado no App é um jsx

* podemos criar o app em forma de função: *

    -> exportando diretamente na função:

        import React from "react";
        import { View } from "react-native"

        export default function App() {
            return (
                <View>

                </View>
            );
        }

    -> exportando fora da função:

        import React from "react";
        import { View } from "react-native"

        function App() {
            return (
                <View>

                </View>
            );
        }

        export default App;
        
* Podemos escrever componentes em forma de classes: *
    
    !!! é importante comentar, que para isso precisamos importar o Component do React:
        import {Component} from "react"

    import React, { Component } from "react";
    import { View, Text} from "react-native";

    class App extends Component {
    
        render(){
        
            return(
                <View>
                    <Text>Olá mundo!</Text>
                    <Text>Hello World</Text>
                </View>
            );
        };
    };

    export default App;