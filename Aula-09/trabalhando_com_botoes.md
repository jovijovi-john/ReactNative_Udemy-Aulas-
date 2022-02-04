Supondo que agora nós queiramos que apareça a mensagem de bem vindo apenas após clicar no botão:

    => O componente Button tem a propriedade de title que define o texto apresentado no botão:

        <Button title="texto do botão"/>
    
    => O componente também tem a propriedade de evento onPress que chama uma função sempre que o usuário pressionar o botão

    if (this.state.input === '') {
        alert("Digite seu nome!!!")
        return;
    }  
    // o return nesse caso impede o restante da execução da função, logo não precisaríamos de um else aí.