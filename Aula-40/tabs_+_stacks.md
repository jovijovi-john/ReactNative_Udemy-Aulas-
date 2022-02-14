Temos a tab navigator, mas vamo supor que estamos na home, mas queremos que essa home seja em formato de stack. Teremos um botao "ir para detalhes" que será outra tela que não estará na tab e quando clicarmos nesse botao, queremos que suba aquela stack e exiba esse componente de detalhes.

Vamos criar uma pasta chamada routes, dentro de src para organizar melhor nosso código

fizemos um arquivo para guardar apenas o stack.navigator com as stacks, e no arquivo de rotas onde pegávamos o home, iremos pegar esse arquivo HomeStack

# App.js
```javascript
import React from "react";

import { NavigationContainer } from "@react-navigation/native";
import Routes from "./src/routes";

export default function App() {
  return(
    <NavigationContainer>
      <Routes />
    </NavigationContainer>
  )
}
```

# src/routes/index.js
```javascript
import React from "react";

import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import { Feather } from "@expo/vector-icons"

import StackRoutes from "./stackRoutes";
import Sobre from "../pages/Sobre";
import Contato from "../pages/Contato";

const Tab = createBottomTabNavigator();

export default function Routes(){
  return(
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
          name="HomeStack"
          component={StackRoutes}
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
  )
}
```

# src/routes/stackRoutes.js
```javascript
import React from "react";

import { createNativeStackNavigator } from "@react-navigation/native-stack"

import Home from "../pages/Home";
import Detalhes from "../pages/Detalhes";

const Stack = createNativeStackNavigator();

export default function StackRoutes() {
    return(
        <Stack.Navigator
        screenOptions={{
            headerShown: false
        }}
        >
            <Stack.Screen
                name="Home"
                component={Home}
            />

            <Stack.Screen 
                name="Detalhes"
                component={Detalhes}
            />
        </Stack.Navigator>
    )
}
```

# src/pages/Home
```javascript
import React from "react";
import {View, Text, StyleSheet, Button} from "react-native";

import { useNavigation } from "@react-navigation/native"

export default function Home(){

    const navigation = useNavigation();

    function navegaDetalhes() {
        navigation.navigate("Detalhes")
    }

    return(
        <View style={styles.container}>
            <Text>Tela home</Text>
            <Button title="Ir para Detalhes" onPress={navegaDetalhes}/>
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

# src/pages/Detalhes
```javascript
import React from "react";
import { View, Text } from "react-native";

export default function Detalhes() {
    return(
        <View style={{flex: 1, alignItems: "center", justifyContent: "center"}}>
            <Text>Página detalhes do usuário</Text>
        </View>
    )
}
```
