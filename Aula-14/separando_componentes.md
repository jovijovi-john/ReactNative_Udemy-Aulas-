vamos separar o componente <pessoa> do nosso App, não é uma boa prática colocar todos os componentes e estilos apenas no arquivo App.js.

Vamos fazer o componente <pessoa> para um arquivo so dele, depois importamos ele no App.js

Uma boa prática é fazer o seguinte:
    ./src/Pessoa/index.js
    pois quando for importar nao vai precisar botar o nome do arquivo, pq por default ele ja vai procurar o index.js
ao invés de:
    ./src/Pessoa/Pessoa.js