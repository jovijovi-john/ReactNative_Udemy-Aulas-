Picker é um componente que podemos utilizar em formulários, buscas, etc. Veremos como utilizá-lo nessa aula.

=> Instalação:

    Para instalar o picker pelo expo: expo install @react-native-picker/picker

=> Documentação:

    https://docs.expo.dev/versions/latest/sdk/picker/

=> Importação:

    import {Picker} from '@react-native-picker/picker';

=> Uso:

    Picker.Item é um item dentro daquele picker

=> Props:

    - style
    - selectedValue
    - onValueChange
    - testId
    - enabled
    - promp
    - itemStyle
    - mode

=> mão na massa:

    <Picker.Item key={} value={} label=""/>

    key => para diferenciar cada item, um identificador único
    value => valor que vai ter quando alguem selecionar
    label => o que vai aparecer
    
        <Picker>
          <Picker.Item key={1} value={1} label="Calabresa" />
          <Picker.Item key={2} value={2} label="Brigadeiro" />
          <Picker.Item key={3} value={3} label="Mussarela" />
          <Picker.Item key={4} value={4} label="Frango com Catupiry" />
          <Picker.Item key={5} value={5} label="4 Queijos" />
          <Picker.Item key={6} value={6} label="Portuguesa" />
          <Picker.Item key={7} value={7} label="Camarão" />
        </Picker>
    
    entretanto, quando selecionarmos qualquer uma dessas opções, não vai mudar. Precisamos fazer algumas alterações NO PICKER

    <Picker selectedValue={}>
        o selectedValue vai pegar lá do nosso state

    o selectedValue vai setar como selecionado a key que for passada para ele

      <Picker 
          selectedValue={this.state.pizza}
          onValueChange={ (itemValue, itemIndex) => this.setState({
            pizza: itemValue
          })}
        >
          <Picker.Item key={1} value={1} label="Calabresa" />
          <Picker.Item key={2} value={2} label="Brigadeiro" />
          <Picker.Item key={3} value={3} label="Mussarela" />
          <Picker.Item key={4} value={4} label="Frango com Catupiry" />
          <Picker.Item key={5} value={5} label="4 Queijos" />
          <Picker.Item key={6} value={6} label="Portuguesa" />
          <Picker.Item key={7} value={7} label="Camarão" />
        </Picker>

        <Text style={styles.pizzas}>Você escolheu: Pizza Calabresa</Text>
        <Text style={styles.pizzas}>R$: 59,90</Text>
        <Text style={{fontSize: 30}}>{this.state.pizza}</Text>

    => Renderização dinâmica / Renderização mapeada:

