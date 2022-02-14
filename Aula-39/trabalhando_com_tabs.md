Vamos aprender sobre bottom tabs, que é um outro tipo de navegação:

# Bottom Tabs Navigator

* Instalação:
    
    CLI:
        
        npm install @react-navigation/bottom-tabs
    
    Expo:

        expo install @react-navigation/bottom-tabs

Independente do tipo de navegação, o navigation container sempre vai ficar por volta de todos.

Importação:
    
    import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";


Para tirar o header de todas as tabs devemos fazer a configuração no Tab.Navigator
    <Tab.Navigator
        screenOptions={{
            headerShown: false,
            tabBarHideOnKeyboard: true,        
            tabBarShowLabel: false
        }}
    >
    
    o tabBarHideOnKeyboard serve pra não mostrar a tabBar quando abrir o teclado, pra ela nao ficar por cima. Ai quando o teclado fechar, ela volta a aparecer

    o tabBarShowLabel serve pra mostrar ou não aquele texto embaixo dos icones

renderizando Icones dinamicamente: 
```javascript
 screenOptions={({ route })=> ({

    tabBarIcon: ({ focused, color, size }) => {

        let iconName;

        if (route.name === "Home") {
            iconName = "home"
        } else if (route.name === "Sobre"){
            iconName = "file-text"
        } else  if (route.name === "Contato") {
            iconName = "phone-call"
        }

        return <Feather name={iconName} size={size} color={color} />;
    },
    headerShown: false,
    tabBarHideOnKeyboard: true,
    tabBarShowLabel: false,
    tabBarActiveTintColor: "#f00",
    tabBarStyle: {
        backgroundColor: "#05f",
        borderTopWidth: 0
    }
})}
```

renderizando Icones estaticamente: 
```javascript
    <Tab.Screen 
        name="Home"
        component={Home}
        options={{
            tabBarIcon: ({color, size}) => {
                return <Feather name="home" color={color} size={size}/>
            }}
        }
    />
```

> Personalizando tabBar: https://www.jonataoliveira.com.br/tabbar-personalizada-em-react-native/

# App.js
```javascript
import React from "react";

import { NavigationContainer, StyleSheet } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import { Ionicons, Feather, FontAwesome, MaterialCommunityIcons } from "@expo/vector-icons"

import Home from "./src/pages/Home";
import Sobre from "./src/pages/Sobre";
import Contato from "./src/pages/Contato";

const Tab = createBottomTabNavigator();

export default function App(){
  return(
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={{
          headerShown: false,
          tabBarHideOnKeyboard: true,
          tabBarShowLabel: false,
          tabBarActiveTintColor: "#c00",
          tabBarStyle: {
            backgroundColor: "#111",
            borderTopWidth: 0,
            height: 55
          }
        }}
      >

        <Tab.Screen 
          name="Home"
          component={Home}
          options={{

            tabBarIcon: ({color, size}) => {
              return <Feather name="home" color={color} size={size}/>
            }
          }}
        />

        <Tab.Screen 
          name="Sobre"
          component={Sobre}
          options={{
            tabBarIcon: ({color, size}) => {
              return <Feather name="file-text" color={color} size={size}/>
            }
          }}
        />

        <Tab.Screen 
          name="Contato"
          component={Contato}
          options={{
            headerShown: false, 
            tabBarIcon: ({color, size}) => {
              return <Feather name="phone-call" color={color} size={size}/>
            }
          }}
        />

      </Tab.Navigator>
    </NavigationContainer>
  )
}
```

# ./src/pages/Home
```javascript
import React from "react";
import {View, Text, StyleSheet, Button} from "react-native";

import { useNavigation } from "@react-navigation/native"

export default function Home(){

    const navigation = useNavigation();

    function navegaSobre() {
        navigation.navigate("Sobre")
    }

    return(
        <View style={styles.container}>
            <Text>Tela home</Text>
            <Button title="Ir para sobre" onPress={navegaSobre}/>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "red"
    }
})
```

# ./src/pages/Contato
```javascript
import React from "react";
import { View, Text, Button } from "react-native";

import { useNavigation, StackActions } from "@react-navigation/native";

export default function Contato(){
    
    const navigation = useNavigation();

    function handleHome() {
        navigation.dispatch(StackActions.popToTop())
    }
    
    return (
        <View>
            <Text>Página Contato</Text>
        </View>
    )
}
```

# ./src/pages/Sobre
```javascript
import React, { useLayoutEffect } from "react";
import {
    View,
    Text,
    StyleSheet,
    Button
} from "react-native";

export default function Sobre() {
    

    return (
        <View style={styles.container}>
            <Text>Página sobre</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center"
    }
})
```