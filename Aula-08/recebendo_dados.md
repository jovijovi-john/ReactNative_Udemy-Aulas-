=> Para importar a caixinha de texto (input de texto):

    import { TextInput } from "react-native"

    !queremos que o texto que for escrito pelo usuário apareça logo em baixo num componente de texto. Como esse texto vai ser mutável, logo precisaremos utilizar states.

=> para escrever um texto dentro do input (placeholder), basta adicionar essa propriedade ao inputText:
    
    <TextInput
        style={styles.input}
        placeholder="Digite seu nome: "
    />

=> para deixar uma linhazinha em baixo do que o usuário está digitando (disponível apenas no android):

    <TextInput
        style={styles.input}
        placeholder="Digite seu nome: "
        underlineColorAndroid="red"
    />

=> O TextInput tem um evento/prop onChangeText que é chamada toda vez que o texto dentro do input é modificado.
    lógica: precisamos pegar o que o usuário digitou e alterar o estado com o que ele digitou
    
    queremos apresentar o "bem vindo" apenas quando o usuário digitar alguma coisa: 

        logo, tiraremos o bem vindo do componente de texto. Caso o usuário digite qualquer coisa, o bem vindo será concatenado com o que ele digitou e será apresentado na tela. Caso não tenha nada digitado(seja porque ainda nao digitou nada ou porque apagou tudo) o nome passado será vazio, assim não terá mensagem de bem vindo.

App.js:

    import React, { Component } from "react";
    import { 
        View,
        Text,
        TextInput,
        StyleSheet
    } from "react-native";


    class App extends Component {

        constructor(props) {
            super(props);
            this.state = {
                nome: ''
            };

            this.getNome = this.getNome.bind(this);
        }

        getNome(texto) {

            if (texto.length > 0) {
                this.setState({nome: "Bem vindo " + texto});
            } else {
                this.setState({nome: ""});
            }
        };
        
        render(){
            
            return(
                <View style={styles.container}>
                    <TextInput
                        style={styles.input}
                        placeholder="Digite seu nome: "
                        underlineColorAndroid="transparent"
                        onChangeText={this.getNome}
                    />

                    <Text style={styles.texto}>{this.state.nome}</Text>
                </View>
            );
        };
    };

    const styles = StyleSheet.create({
        container: {
            flex: 1,
            justifyContent: "center"
        },

        input: {
            height: 45,
            borderWidth: 1,
            borderColor: "#222",
            margin: 10,
            fontSize: 20,
            padding: 10
        },

        texto: {
            textAlign: "center",
            fontSize: 25
        }
    })
    export default App;