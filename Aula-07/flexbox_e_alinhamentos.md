Veremos quais são os tipos de alinhamento e como podemos alinhar os conteúdos na tela.

=> Para colocar os elementos dispostos um ao lado do outro:

    flexDirection: "row"
    por default vem "column", deixando um abaixo do outro

    {
        => No flexDirection: "row"

            justifyContent: -> para alinhar com base no eixo x
            alignItems -> para alinhar com base no eixo y

        => No flexDirection: "column"

            justifyContent -> para alinhar com base no eixo y
            alignItems -> para alinhar com base no eixo x

        valores possíveis para justifyContent:

            flex-start-> alinha no começo
            flex-end-> alinha no final
            center-> alinha ao centro
            space-around -> deixa o mesmo espaço entre os elementos, e um espaço no começo e no fim do container
            space-between -> Cola os elementos nas bordas e deixa um espaço identico entre eles

        valores possíveis para alignItems:
            flex-start-> alinha no começo
            flex-end-> alinha no final
            center-> alinha ao centro

    !!!Importante: Independente do flexDirection, os valores possíveis para justifyContent e alignItems são sempre os mesmos.
    }