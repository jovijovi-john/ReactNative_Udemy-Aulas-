O CustomDrawer vai ser nosso componente personalizado. Para isso, dentro do Drawer.Navigator fora do screen options a gente tem uma propriedade chamada drower content. para essa propriedade nós podemos passar o componente que queremos renderizar.

Quando usamos o drawerContent, ele envia algumas propriedades para nosso componente:
    Qual que ta ativo, qual cor que ta ativa, qual cor que não ta ativa, etc...

# CustomDrawer.js

```javascript
import React from "react";
import { View, Text, Image } from "react-native";

import { DrawerContentScrollView, DrawerItemList } from "@react-navigation/drawer"

export default function CustomDrawer(props){
    return(
        <DrawerContentScrollView {...props}>
            <View style={{
                width: "100%",
                height: 85,
                justifyContent: "center",
                alignItems: "center",
                marginTop: 30
            }}>

                <Image 
                    source={require("../assets/perfil.png")}
                    style={{width: 65, height: 65}}
                />

                <Text style={{color: "#000", marginTop: 5, marginBottom: 35, fontSize: 17}}>
                    Bem vindo 
                </Text>

            </View>

            <DrawerItemList {...props}/>
        </DrawerContentScrollView>
    )
}
```

# routes/index.js

```javascript
import React from "react";

import { createDrawerNavigator } from "@react-navigation/drawer";
import { Feather } from "@expo/vector-icons";

import StackRoutes from "./stackRoutes";
import Sobre from "../pages/Sobre";
import Contato from "../pages/Contato";

import CustomDrawer from "../components/CustomDrawer";

const Drawer = createDrawerNavigator();

export default function Routes(){
  return(
    <Drawer.Navigator
      drawerContent={CustomDrawer}
      screenOptions={{
        headerShown: false,
        
        drawerActiveTintColor: "#fff",
        drawerActiveBackgroundColor: "#0de",
        drawerInactiveBackgroundColor: "#eee",
        drawerInactiveTintColor: "#000"

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