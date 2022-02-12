=> O que são Hooks?

    São funções que nos permitem usar os estados e os ciclos de vida de um componente de classe em um componente funcional.

=> Importante:

    Hooks não funcionam com classes

=> Componentes funcionais no react são normalmente chamados de componentes funcionais sem estado (stateless component)
    
    Agora não mais! Anteriormente apenas um componente de classe permitia-nos ter um estado local e ciclo de vida gerenciáveis

=> Então um componente funcioncional que era conhecido como 'stateless component' agora passa a ser chamado de 'stateful component'

=> Vantagens:

    * Poder utilizar componentes funcionais para guardar estados e gerenciar o ciclo de vida do componente

    * A natureza do Javascript está atrelada à programação funcional, usar componentes funcionais nos aproxima desta natureza.

    * Isso elimina a necessidade de utilizar o operador this, que é usado para classes e é pouco intuitivo no javascript

    * Não precisamos utilizar métodos especiais como componentDidMount, componentDidUpdate, ... para acessar o ciclo de vida de um componente

