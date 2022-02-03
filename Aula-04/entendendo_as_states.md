Nessa aula estudaremos sobre states(estados) dentro dos nossos componentes


=> Vimos como passar props e como usá-las, so que se eu receber uma prop e eu quiser que mude essa prop eu não consigo. 

    !-> Isso porque as props são estáticas (não mudam de valor)

=> Para resolver isso temos as states, que são mutáveis, logo podemos trocar o valor de variáveis por meio delas
=> para termos estados dentro de um componente, temos que criar meio que uma variável, mas precisamos criar de uma maneira diferente.

=> Dentro da classe, precisamos crir um construtor:

    constructor(props) {
     super(props);

     this.state = {
      nome: "Jovi"
     };
  }

  <!-- dentro de this.states, teremos todas as states que queremos criar -->

=> para usar um botão basta, importar:
    import {Button} from 'react-native';

    export default class App extends Component {
        render(){
            return(
                <View>
                    <Button/>
                </View>
            );
        };
    };

    <!-- no botão temos um evento de press (onPress), nele podemos passar uma função que será executada sempre que o botão for pressionado. Essa função pode ser arrow function ou mesmo uma função externa -->

        export default class App extends Component {
        
        entrar(){

        }

        render(){
            return(
                <View>
                    <Button onPress={this.entrar}/>
                </View>
            );
        };
    };

    !!! Quando criamos uma função e queremos acessar as propriedades da classe, necessitamos dar um bind nessa função. Como assim?

        no construtor, basta fazer isso:
        
        constructor(props) {
            super(props);
            this.state = {
                nome: "Jovi Jovi"
            };

            this.entrar = this.entrar.bind(this);
        }

        fazendo isso nós permitimos com que a função possa acessar todas as propriedades/states para alterar o valor.

=> Não podemos fazer isso:

    entrar(){
        this.state.nome = "José";
    }

=> O certo seria assim:

    entrar(){
        this.setState({
            nome: "José"
        })
    }

=> Não podemos fazer isso:

    <Button onPress={this.entrar("Zed")} />

    Isso porque quando o app é renderizado, ele ta chamando a função direto. Pra gente nao deixar ele executar toda vez e executar só quando eu quero, devemos fazer uma função anônima

    <Button onPress={() => this.entrar("Zed")} />
