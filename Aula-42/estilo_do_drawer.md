Vamos personalizar o estilo do nosso drawer, assim como fizemos com o tabs e com o stack

# src/pages/Home

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
        headerShown: false,
        drawerStyle: {
          backgroundColor: "#121212",
        },
        
        drawerActiveTintColor: "#fff",
        drawerActiveBackgroundColor: "#d00",
        drawerInactiveBackgroundColor: "#400",
        drawerInactiveTintColor: "#fff"

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