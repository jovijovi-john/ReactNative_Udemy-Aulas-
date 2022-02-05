Esse aplicativo vai ter um timer, uma imagem e dois botões (para inicializar e para zerar o timer).

    Como vamos precisar ficar alterando o timer, logo precisaremos usar States

    para colocar alguns numeros após a virgula, basta usar o método toFixed() que recebe como  parametro a quantidade de casas decimais do numero.

    
        <Text style={styles.timer}>{this.state.numero.toFixed(1)}</Text>

    o setInterval serve para executar algo de  tempos em tempos:

        setInterval (() => {
            console.log("sexo")
        }, 100 milisegundos)
    
    precisamos atribuir esse set interval a uma variável, para que consigamos pausar quando quisermos.

    cancelando intervalos: https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals#cancelando_intervalos

    setInterval() continua sua execução para sempre, a menos que você faça algo sobre isso. Você provavelmente quer um jeito de parar tais tarefas, do contrário você pode acabar com error quando o navegador não puder completar outras versões futuras da tarefa, ou se a animação acabar. Você pode fazer isso do mesmo jeito que você para timeouts — passando o identificador retornado por setInterval() para a função clearInterval();

    toda vez que iniciamos o aplicativo o timer ta null. Quando clica no botão ele verifica se o timer ta null, se ta null quer dizer que é pra começar a rodar. Se for diferente de null quer dizer que ja ta rodando então para o timer e seta o timer como null. Se clicar no botão de novo ele vai ta null logo vai voltar a rodar.

    => Agora vamos botar o nome do botão como uma state, ele começará como vai, e quando ele estiver rodando o cronometro vamos trocar essa state para parar

    => Agora guardaremos o ultimo tempo que o usuário fez quando ele clicar em limpar
    
    => Renderização condicional: Mostra isso aqui somente se o ultimo não for null
          {this.state.ultimo > 0 ? 'Ultimo tempo: ' + this.state.ultimo.toFixed(2) + "s" : ''}
            
            se this.state.ultimo for null nao podemos usar this.state.ultimo.toFixed(), pois seria:
                null.toFixed() e isso nao faz sentido.
            
            nesse caso, estamos verificando se o ultimo é maior que 0, se for vai mostrar:
                'Ultimo tempo: ' + this.state.ultimo.toFixed(2) + "s"

            do contrário, nao vai mostrar nada ( '' )