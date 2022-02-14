* Passar informações entre páginas 

    function navegaSobre() {
        navigation.navigate("Sobre", { nome: "John", email: "Johnvictor@gmail.com"})
    }   

    em Sobre, passamos o parametro {route}, ele vai conter essas informações passadas no navigate

    ```javascript 
        export default function Sobre({ route }) {
            return (
                <View style={styles.container}>
                    <Text>Página sobre</Text>
                    <Text>{route.params?.nome}</Text>
                    <Text>{route.params?.email}</Text>
                </View>
            )
        }
    ```

    esse route.params? é para casos em que a propriedade nao foi passada (exemplo: email), assim ele não vai crashar a aplicação e sim vai definir apenas como vazio

Temos um Hook para facilitar isso (useRoute)

    ```javascript 

        import { useRoute } from "@react-navigation/native";
        
        const route = useRoute();

        export default function Sobre() {
            return (
                <View style={styles.container}>
                    <Text>Página sobre</Text>
                    <Text>{route.params?.nome}</Text>
                    <Text>{route.params?.email}</Text>
                </View>
            )
        }
    ```

# Manipular o título do header

por enquanto, no App.js ele ta passando o titulo so que fixo. Imagine se quisermos navegar, so que queremos na nossa tela receber aquele parametro e colocar o parametro do nome no header. Para isso, precisamos importar o hook { useLayoutEffect } do react.

o useLayoutEffect é bem parecido com o useEffect. Quando abre o app ele chama a função quando o componente é montado. A diferença entre os dois, é que o useLayoutEffect é síncrono.

```javascript
useLayoutEffect(() => {
    navigation.setOptions({
        title: route.params?.nome === "" ? "Página Sobre" : route.params?.nome
    })
}, [navigation])
// passamos o navigation pois a propriedade que queremos manipular está dentro dele, que é o titulo
```

Agora faremos uma função para voltar uma tela atrás
    > navigation.goBack()

Agora vamos criar um botao que volta tudo pra home e zera a pilha de navegação.
    para isso, é necessário importar o StackActions para podermos mexer na pilha de navegação

    ```javascript
    function handleHome() {
        // .pop() volta uma pra trás
        navigation.dispatch(StackActions.pop()) 
    }
    ```

    ```javascript
    function handleHome() {
        // .popToTop() volta pro topo da pilha (primeira screen)
        navigation.dispatch(StackActions.pop()) 
    }
    ```
    

# App.js
```javascript

import React from "react";

import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Home from "./src/pages/Home";
import Sobre from "./src/pages/Sobre";
import Contato from "./src/pages/Contato";

const Stack = createNativeStackNavigator(); 


export default function App(){
  return(
    <NavigationContainer>
      <Stack.Navigator>

        <Stack.Screen 
          name="Home"
          component={Home}
          options={{
            title: "Tela início",
            headerStyle: {
              backgroundColor: "#121212"
            },
            
            headerTintColor: "#fff",
            headerShown: false
          }}
        />

        <Stack.Screen
          name="Sobre"
          component={Sobre}
        />

        <Stack.Screen
          name="Contato"
          component={Contato}
        />
      
      </Stack.Navigator>
    </NavigationContainer>
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

    function navegaSobre() {
        navigation.navigate("Sobre", { nome: "Laís Vitória", email: "Johnvictor@gmail.com"})
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
        alignItems: "center"
    }
})
ah
```

# src/pages/Sobre
```javascript

import React, { useLayoutEffect } from "react";
import {
    View,
    Text,
    StyleSheet,
    Button
} from "react-native";

import { useRoute, useNavigation } from "@react-navigation/native";

export default function Sobre() {
    
    const route = useRoute();
    const navigation = useNavigation();
    
    useLayoutEffect(() => {
        navigation.setOptions({
            title: route.params?.nome === "" ? "Página Sobre" : route.params?.nome
        })
    }, [navigation])

    return (
        <View style={styles.container}>
            <Text>Página sobre</Text>
            <Text>{route.params?.nome}</Text>
            <Text>{route.params?.email}</Text>

            <Button title="Tela contatos" onPress={() => navigation.navigate("Contato")}/>
            <Button title="Voltar tela" onPress={() => navigation.goBack()}/>
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

# src/pages/Contato
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
            <Button title="VOLTAR HOME" onPress={handleHome}/>
        </View>
    )
}

```