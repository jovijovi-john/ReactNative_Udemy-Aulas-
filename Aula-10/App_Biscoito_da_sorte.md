teremos uma imagem de biscoito da sorte e teremos várias frases. Iremos sortear a frase, e cada vez que clicar no botão sorteará uma frase diferente e exibi-la na tela.

Além disso, serão duas imagens, uma de biscoito fechado e outra de biscoito aberto, ai quando clicar ela vai mudar.

Criaremos a pasta src e colocaremos essas fotos lá.

No source da imagem, ao inves de chamar o uri, que servia para importar uma imagem da internet, como temos essa imagem localmente, precisamos fazer o seguinte:

    <Image
        source={require("./src/biscoito.png")}
    />
utilizaremos um novo tipo de botão, o TouchableOpacity

    <TouchableOpacity>
        <View>
            <Text>Abrir biscoito!</Text>
        </View>
    </TouchableOpacity>
     
igual ao button normal, o TouchableOpacity também tem a propriedade de evento onPress. Dentro de abreBiscoito, teremos que pegar uma frase aleatoria e atualizar o textoFrase come essa frase sorteada.

para gerar um número aleatório:

    let randomNumber = Math.floor(Math.random() * this.frases.length)
    math.random gera um numero no intervalo [0, 1[, multiplicando por 7 que é a quantidade de frases. Quando arredondar pra baixo, nunca vai dar 7, pois so daria 7 se o intervalo fosse fechado a direita, o que não é o caso. Logo nunca será 1 * 7, no maximo será 0.999999 * 7 que vai dar 6.99999, que com o floor vai ficar 6. o array vai de 0 a 6, logo nunca teremos a posição 7.