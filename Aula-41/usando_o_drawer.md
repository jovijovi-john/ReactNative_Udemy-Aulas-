# Drawer Navigator

Vai seguir o mesmo esquema/principio do Tabs Navigator e do Stack Navigator
VEJA A AULA ATE O FINAL ANTES DE SAIR INSTALANDO QUALQUER COISA

Instalação:

    CLI:
    
        npm install @react-navigation/drawer
        Dependencias: npm install react-native-gesture-handler react-native-reanimated
    
    Expo:

        expo install @react-navigation/drawer
        Dependencias: expo install react-native-gesture-handler react-native-reanimated

O gesture-handler e o reac-native-reanimated são para reconhecimento de gestos e animações.

*!!! IMPORTANTE:*

No App.js, é necessário fazer o seguinte comando:
    
    import 'react-native-gesture-handler';

Do contrário, a aplicação irá crashar

o reanimated que funcionou foi o da versão 2.3.1

Tive alguns problemas com o Reanimated, então veja a documentação e alguns sites/comandos:
    https://docs.expo.dev/versions/latest/sdk/reanimated/#installation
    https://pt.stackoverflow.com/questions/175372/instalar-vers%C3%A3o-espec%C3%ADfica-de-uma-biblioteca-com-npm
    expo install react-native-reanimated@2.3.1

# App.js

```javascript
import 'react-native-gesture-handler';
  
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

# routes
```javascript
import React from "react";

import { createDrawerNavigator } from "@react-navigation/drawer";
import { Feather } from "@expo/vector-icons";

import StackRoutes from "./stackRoutes";
import Sobre from "../pages/Sobre";
import Contato from "../pages/Contato";

const Drawer = createDrawerNavigator();

export default function Routes(){
  return(
    <Drawer.Navigator
      screenOptions={{
        headerShown: false
      }}
    >
      <Drawer.Screen
        name="HomeStack"
        component={StackRoutes}
      />

      <Drawer.Screen 
        name="Sobre"
        component={Sobre}
      />
      
      <Drawer.Screen 
        name="Contato"
        component={Contato}
      />

    </Drawer.Navigator>     
  )
}
```

# Home
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
            <Button title="Abrir Drower" onPress={() => navigation.openDrawer()}/>
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