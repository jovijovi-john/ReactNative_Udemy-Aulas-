# Icones: Aula 51

Vamos aprender a usar uma biblioteca para icones SVG


> o SVG é mais leve e mais facil de utilizar que png ou jpg, por exemplo.

* Vector Icons: 
    
    cli:    yarn add react-native-vector-icons

            => import FontAwesome from "react-native-vector-icons/FontAwesome"
            => documentação: https://github.com/oblador/react-native-vector-icons
            => biblioteca de icones: https://oblador.github.io/react-native-vector-icons/
            => recomendações: Feather, FontAwesome, MaterialCommunityIcons




    expo:   já vem instalado por npm insalll default

            => import { Ionicons } from '@expo/vector-icons';
            => documentação: https://docs.expo.dev/guides/icons/
            => biblioteca de icones: https://icons.expo.fyi/

            {...}
            import { Ionicons, FontAwesome, Feather } from '@expo/vector-icons';

            export default function App() {
              return(
                <View style={styles.container}>
                  <Text>Sujeito Programador</Text>


                  <Ionicons name="md-checkmark-circle" size={32} color="green" />
                  <FontAwesome name="whatsapp" size={32} color="green" />
                  <Feather name="x" size={24} color="black" />
                
                </View>
              )
            }

# App.js: 

    import React from "react";
    import {
      View,
      Text,
      StyleSheet,
      TouchableOpacity
    } from "react-native";
    import { Ionicons, FontAwesome, Feather } from '@expo/vector-icons';
    
    export default function App() {
      return(
        <View style={styles.container}>
          
          <Text>Sujeito Programador</Text>
          
          <Ionicons 
            name="md-checkmark-circle" 
            size={32} 
            color="green" 
          />
    
          <FontAwesome 
            name="whatsapp" 
            size={32} 
            color="green" 
          />
          
          <Feather 
            name="x" 
            size={32} 
            color="green" 
          />
    
          <TouchableOpacity style={styles.btnYoutube}>
            <FontAwesome 
              name="youtube"
              size={25}
              color="#fff"
            /> 
            <Text style={styles.btnText}>Acessar canal</Text>
          </TouchableOpacity>
        </View>
      )
    }
    
    const styles = StyleSheet.create({
      container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center"
      },
    
      btnYoutube: {
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        padding: 12,
        backgroundColor: "#f00",
        borderRadius: 5
      },
    
      btnText: {
        color: "#fff",
        paddingLeft: 10,
        fontWeight: "bold"
      }
    })