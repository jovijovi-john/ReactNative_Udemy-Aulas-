->> todos os textos devem estar renderizados dentro de um componente de texto

->> Os componentes podem ter props (propriedades), estilos, métodos, etc

    <Text style={{ color: "red" }}></Text>

=> em rn nao trabalhamos com px, esses estilos são com pontos e não pixels

=> componente de imagem: <Image>
    
    esse componente tem duas propriedades obrigatórias,
    o source{{uri: "https://urlDaImagem"}} e o
    style={{width: , height: }}. Do contrário, a imagem não será renderizada
    
    exemplo:
        <Image source={{uri: "https://github.com/jovijovi-john.png"}} style={{width: 80, height: 80}}/>

    quando quiser puxar imagem da internet, a url precisa estar no protocolo https

=> podemos criar variáveis, assim como no JS. Para chamar essa variável dentro do componente é necessário o uso de chaves

    render(){
    
    let nome = "John";

    return(
      <View>
        <Text>{nome}</Text>
        <Image source={{uri: "https://github.com/jovijovi-john.png"}} style={{width: 80, height: 80}}/>
      </View>
    );
  };