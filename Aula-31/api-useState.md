# useState 

Antes fazíamos:

    import React, { Component } from "react";
        
    e criávamos o componente em formato de classe para trabalhar com estados dentro desse componente, ja que em forma de função, não era possível.


=> Importação: 

    import React, { useState } from "react";

Antes, dentro do construtor, tinhamos um this.state = {} e dentro dele tínhamos todos nossos estados.
Com o useState temos de criar um estado específico, um pra cada um.

Exemplo:

    const [nomeDoState, setNomeDoState] = useState(valorDefault);

    // Esse setState é a função que será chamada para alterar o valor do state correspondente

    // queremos criar um estado de nome
    const [nome, setNome] = useState("John Víctor");

    <TouchableOpacity style={styles.btn} onPress={alteraNome}> (Não precisamos usar o this.alteraNome pois não estamos trabalhando com classe)