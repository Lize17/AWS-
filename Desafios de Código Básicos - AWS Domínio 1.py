* Desafio - 1 / 3 - Benefícios da Nuvem AWS *
- Entrada
A entrada consistirá na vantagem da arquitetura em nuvem para a qual você deve retornar a descrição. Nesse contexto, as seguintes vantagens são consideradas válidas para este desafio de código:

"economia de custos"
"infraestrutura global"
"alta disponibilidade"
"elasticidade"
"agilidade"

- Saída
A saída esperada é a descrição associada à vantagem fornecida como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"garantia de que os recursos estejam sempre disponiveis"
"capacidade de dimensionar recursos conforme a demanda"
"otimizacao de gastos por meio de modelos de precos flexiveis"
"capacidade de desenvolver, testar e implantar rapidamente"
"fornecer recursos eficientemente em qualquer lugar do mundo"

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "economia de custos":
        return "otimizacao de gastos por meio de modelos de precos flexiveis"
        
    # TODO: Preencha corretamente a descrição de cada vantagem, considerando as condições abaixo e Saídas possíveis:
    
    elif vantagem == "infraestrutura global":
        return "fornecer recursos eficientemente em qualquer lugar do mundo"
        
    elif vantagem == "alta disponibilidade":
        return "garantia de que os recursos estejam sempre disponiveis"
        
    elif vantagem == "elasticidade":
        return "capacidade de dimensionar recursos conforme a demanda"
        
    elif  vantagem == "agilidade":
        return "capacidade de desenvolver, testar e implantar rapidamente"
 
# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem".
print(descrever_vantagem(entrada))

* Desafio - 2 / 3 - Os Pilares do AWS Well-Architected Framework * 

- Entrada
A entrada consistirá no pilar do AWS Well-Architected Framework para o qual você deve retornar a descrição. Nesse contexto, os seguintes pilares são considerados válidos para este desafio de código:

"excelencia operacional"
"seguranca"
"confiabilidade"
"eficiencia de performance"
"otimizacao de custos"
"sustentabilidade"

- Saída
A saída esperada é a descrição associada ao pilar fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"capacidade dos sistemas de executar as funcoes pretendidas"
"execucao e monitoramento de sistemas e melhoria continua"
"reducao do impacto ambiental dos sistemas na nuvem"
"protecao de informacoes e sistemas"
"alocacao eficaz e otimizada de recursos de TI e computacao"
"obtencao do melhor retorno sobre o investimento em recursos"

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um pilar e retornar sua respectiva descrição.
def descrever_pilar(pilar):
    if pilar == "excelencia operacional":
        return "execucao e monitoramento de sistemas e melhoria continua"
        
    # TODO: Preencha corretamente a descrição de cada pilar, considerando as condições abaixo e Saídas possíveis:
    
    elif pilar == "seguranca":
        return "protecao de informacoes e sistemas"
        
    elif pilar == "confiabilidade":
        return "capacidade dos sistemas de executar as funcoes pretendidas"
        
    elif pilar == "eficiencia de performance":
        return "alocacao eficaz e otimizada de recursos de TI e computacao"
        
    elif pilar == "otimizacao de custos":
        return "obtencao do melhor retorno sobre o investimento em recursos"
        
    elif pilar == "sustentabilidade":
        return "reducao do impacto ambiental dos sistemas na nuvem"
 
# Imprime a descrição do pilar recebido na "entrada" através da função "descrever_pilar".
print(descrever_pilar(entrada))

* Dasafio - 3 / 3 - Escolhendo a Estratégia de Migração * 

- Entrada
A entrada consistirá em um cenário de migração, descrevendo brevemente o aplicativo ou sistema a ser migrado. Nesse contexto, os seguintes cenários são considerados válidos para este desafio de código:

"transicao de aplicativo sem valor comercial"
"aplicativo com necessidade de adiar sua migracao para a nuvem"
"substituir o aplicativo por uma versao ou produto diferente"
"modificar a arquitetura do aplicativo"
"mover aplicativos para a nuvem sem modifica-los"
"introduzir otimizacoes no aplicativo para opera-lo de forma eficiente"
"transferir servidores ou instancias para outra plataforma na nuvem"

- Saída
A saída esperada é a estratégia de migração mais apropriada para o cenário fornecido como entrada, escolhida entre as 7 Rs. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"relocate"
"retire"
"refactor or re-architect"
"retain"
"repurchase"
"rehost"
"replatform"

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um cenário e retornar a estratégia indicada.
def escolher_estrategia(cenario):
    if "aplicativo a ser descomissionado" in cenario or "sem valor comercial" in cenario:
        return "retire"
        
    # TODO: Preencha corretamente a estrátegia indicada para cada cenário, considerando as condições abaixo e Saídas possíveis:

    elif "manter aplicativos no ambiente de origem" in cenario or "adiar sua migracao para a nuvem" in cenario:
        return "retain"
        
    elif "mover aplicativos para a nuvem sem modifica-los" in cenario or "lift and shift" in cenario:
        return "rehost"
        
    elif "transferir servidores ou instancias para outra plataforma na nuvem" in cenario:
        return "relocate"
        
    elif "substituir o aplicativo por uma versao ou produto diferente" in cenario:
        return "repurchase"
        
    elif "mover o aplicativo para a nuvem" in cenario or "introduzir otimizacoes para opera-lo de forma eficiente" in cenario:
        return "replatform"
        
    elif "modificar a arquitetura do aplicativo" in cenario or "aproveitar os recursos nativos para melhorar agilidade" in cenario:
        return "refactor or re-architect"
        
# Imprime a estratégia indicada para o cenário recebido na "entrada" através da função "escolher_estrategia".
print(escolher_estrategia(entrada))
