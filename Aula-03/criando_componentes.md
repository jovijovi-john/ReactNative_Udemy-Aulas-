!!! Boa prática: PascalCase em nomes de componentes

=> supondo que eu queira criar um componente onde este componente seja responsável por mostrar só essa imagem (a minha do github no caso).

=> Podemos criar esse novo componente dentro do próprio App.js

    ex:


        class App extends Component {
        };

        class John extends Component {
            render(){
                return(
                   <Image/>
                );
            }
        };

        export default App;


        // nesse caso não colocamos uma <View> por volta da imagem. Por quê?
            -> Quando colocamos apenas um componente não é necessário retorná-lo envolvido numa view

=> Quando queremos usar o componente John, por exemplo, dentro do componente App e eles estão no mesmo arquivo, não é 
   necessário importar o componente John

=> supondo que no componente App eu queira chamar o componente John passando propriedades de largura e altura dessa maneira:    <John largura={200} altura={200}/>

    como eu faria no componente John para receber essas propriedades?
    assim:
        class John extends Component {
            render(){
                
                let imagem = "https://github.com/jovijovi-john.png";

                return(
                    <Image  
                        source={{ uri: imagem }} 
                        style={{ width: this.props.largura, height: this.props.altura }}
                    />
                );
            }
        };

        // ou seja, devemos acessar as propriedades passadas via this.props, pois this referencia o proprio elemento e props as suas propriedades
        