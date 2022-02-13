aprenderemos a trabalhar com TabNavigator, StackNavigator, Drawer, etc...

primeiramente temos que instalar o react-navigation

    Docs: https://reactnavigation.org/

* #Instalação:
    
    npm install @react-navigation/native

* => Dependencias:

    * CLI:
            => npm install react-native-screens react-native-safe-area-context
    * Expo:
            => expo install react-native-screens react-native-safe-area-context

=> Stack Navigator:

    * docs: https://reactnavigation.org/docs/hello-react-navigation
    * instalação: 
        CLI: npm install @react-navigation/native-stack
        Expo: expo install @react-navigation/native-stack

    Vamos criar dois componentes que vão ser as páginas do nosso app

    !!! O app.js vai ser o responsável pela nossa react-navigation, pelas rotas

primeira coisa que devemos importar:
        
    import {NavigationContainer} from "@react-navigation/native";
    \\ depois importamos o tipo de navegação que queremos
    import { createNativeStackNavigator } from "react-navigation/native-stack";

*const tipoDeNavegacao = createNativeStackNavigator();

quando formos fazer o return, dentro do app.js, nao retornarmos uma view. Retornamos um NavigationContainer,
e dentro dele, teremos o nosso tipo de navegação, e dentro disso, teremos nossas screens.

no Stack.Screen, devemos passar o nome da tela e o componente que será renderizado naquela screen

```javascript
  <NavigationContainer>
      <Stack.Navigator>

        <Stack.Screen 
          name="Home"
          component={Home}
        />

        <Stack.Screen
          name="Sobre"
          component={Sobre}
        />
      
      </Stack.Navigator>
    </NavigationContainer>
```

para poder navegar o usuário, precisamos importar, nas telas, um hook (useNavigation)

    import { useNavigation } from "@react-navigation/native";

uso: 
```javascript
    export default function Home(){

        const navigation = useNavigation();

        return(
            <View style={styles.container}>
                <Text>Tela home</Text>
                <Button title="Ir para sobre" onPress={ () => navigation.navigate("Sobre") }/>
            </View>
        )
    }
```
O navigation vai guardar nosso hook de navegação, e .navigate(<nameScreen>) recebe o name da screen que ele vai navegar 

# Personalizando o header das telas

    <Stack.Screen
        name="Home"
        component={Home}
        options: {{
        }}
    />

    ```javascript
        options={{
            title: "Tela início", //Título da tela
            headerStyle: { // personalizando o header
              backgroundColor: "#121212"
            },
            
            headerTintColor: "#fff", // cor do titulo do header
            headerShown: false // exibir ou ocultar o header
        }}
    ```

# App.js

```javascript

```

# src/pages/Home
# src/pages/Sobre