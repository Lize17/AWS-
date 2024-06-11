## Desafio 1 
entrada = input()

def escolher_categoria(afirmacao):
    if "nivel mais baixo de abstracao" in afirmacao:
        return "iaas"

    elif "nivel intermediario de abstracao" in afirmacao:
        return "paas"
        
    elif "nivel mais alto de abstracao" in afirmacao:
        return "saas"
        
    elif "acesso direto aos recursos de computacao" in afirmacao:
        return "iaas"
        
print(escolher_categoria(entrada))

## Desafio 2
entrada = input()

def indicar_responsavel(responsabilidade):
    if "seguranca da nuvem" in responsabilidade:
        return "AWS"

    elif "seguranca na nuvem" in responsabilidade:
        return "cliente"
        
    elif "garantir que os dados estejam em conformidade com as leis" in responsabilidade:
        return "cliente"
        
    elif "proteger a infraestrutura que executa todos os servicos" in responsabilidade:
        return "AWS"
        
print(indicar_responsavel(entrada))

#Desafio 3 

entrada = input()

def determinar_mecanismo_controle(cenario):
    if "uma aplicacao precisa permitir o trafego apenas na porta 80" in cenario:
        return "grupo de seguranca"
        
    elif "uma sub-rede precisa bloquear todo o trafego de entrada" in cenario:
        return "ACL de rede"
        
    elif "bloquear trafego externo para instancias em uma sub-rede privada" in cenario:
        return "ACL de rede"
        
    elif "permitir acesso SSH a uma instancia somente para um endereço IP" in cenario:
        return "grupo de seguranca"
        
print(determinar_mecanismo_controle(entrada))
