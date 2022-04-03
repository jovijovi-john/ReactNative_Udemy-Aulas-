Aplicando Styled Components

    Ele nos possibilita, ao invés de usar o StyleSheet.create(), usar um css padrão
    -> é opcional
    -> traz dinamismo
    -> podemos passar propriedades para o estilo de forma mais dinâmica
        conforme ocorra algum evento na aplicação, um click, mudar a cor de fundo ou alguma coisa desse tipo, é muito mais fácil usando o StyledComponents 

Instalação:

    yarn add styled-components

Importação:

    import styled from "styled-components/native";

App.js:
```javascript
import { View, Text } from 'react-native';
import React from 'react';

import { Container, Titulo, Nome, BotaoSujeito, BotaoText} from './src/styles';

export default function App() {
  return (
    <Container>
      <Titulo tamanho="35">Bem Vindo,</Titulo>
      <Nome cor="#ff0000" tamanho="20">Zed</Nome>

      <BotaoSujeito onPress={() => {
          alert("Entrando");
      }}>
          <BotaoText>
                Entrar
          </BotaoText>
      </BotaoSujeito>

    </Container>
  )
}

```

src/styles.js:
```javascript
import styled from 'styled-components/native';

export const Container = styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
    background-color: #111;
`; 

export const Titulo = styled.Text`
    font-size: ${props => props.tamanho}px;
    color: #fff;
`;

export const Nome = styled.Text`
    color: ${props => props.cor};
    font-size: ${props => props.tamanho}px;
`;

export const BotaoSujeito = styled.TouchableOpacity`
    background-color: #ddd;
    padding: 5px
    font-size: 20px;
    border-radius: 5px;
    width: 90%;
    align-items: center;
    justify-content: center;
`;

export const BotaoText = styled.Text`
    color: #000;
    font-size: 20;
`;
```

off: baixar dracula clean