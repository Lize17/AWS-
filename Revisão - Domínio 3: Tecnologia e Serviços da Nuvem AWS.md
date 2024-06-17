## Revisão - Métodos de Implantação e Operação na Nuvem AWS
Diferentes Formas de Provisionamento e Operação na AWS
Provisionamento

Provisionamento Manual:
Configuração manual de instâncias EC2, grupos de segurança, buckets S3, etc.
Adequado para casos simples ou experimentais.
Trabalhoso e propenso a erros em ambientes complexos.
Provisionamento Automatizado:
Ferramentas como AWS CloudFormation, AWS Elastic Beanstalk e AWS OpsWorks.
CloudFormation: Define infraestrutura como código.
Elastic Beanstalk e OpsWorks: Plataformas gerenciadas para implantação e operação de aplicativos.
Operação

Monitoramento e Gerenciamento de Recursos:
Amazon CloudWatch: Monitora métricas de desempenho e logs de aplicativos.
Define alarmes para ações automáticas em eventos indesejados.
AWS Config: Avalia e audita a conformidade da infraestrutura com políticas de segurança e governança.
Automatização de Tarefas:

AWS Lambda: Executa código sem a necessidade de provisionar ou gerenciar servidores.
Ideal para tarefas de processamento de eventos em resposta a gatilhos.
AWS Step Functions: Coordenam e orquestram fluxos de trabalho complexos em serviços da AWS.
Diferentes Formas de Acessar os Serviços da AWS
Acesso Programático

Acesso via APIs, SDKs e CLI:
Interação com os serviços da AWS de forma programática.
Automatização e integração com aplicativos e sistemas.
AWS SDKs:
Disponíveis em várias linguagens de programação.
Simplificam o desenvolvimento de aplicativos que interagem com os serviços da AWS.
AWS CLI:
Ferramenta de linha de comando para interagir com serviços da AWS.
Interface simples e consistente para várias tarefas.
Console de Gerenciamento da AWS

Interface Web:

Experiência visual para provisionar e gerenciar recursos.
Interface intuitiva e fácil de usar.
Suporte a Multiusuários:
Configuração de contas de usuário e permissões com IAM.
Controle de acesso e ações permitidas.
Infraestrutura como Código (IaC)

AWS CloudFormation:
Define infraestrutura da AWS em formato de código YAML ou JSON.
Facilita criação, atualização e exclusão de recursos de forma automatizada.
AWS CDK (Cloud Development Kit):
Permite escrever código para provisionar recursos na AWS de maneira programática.
Abstração sobre o CloudFormation para expressar a infraestrutura como código.
Tipos de Modelos de Implantação na Nuvem
Nuvem Pública

Características:
Recursos disponibilizados por um provedor de serviços em nuvem.
Elasticidade e compartilhamento de recursos.
Elasticidade:
Dimensionamento automático conforme demanda.
Redução ou aumento de recursos sem provisionamento manual.
Compartilhamento de Recursos:
Economias de escala.
Pagamento apenas pelo que é utilizado.
Nuvem Privada

Características:
Recursos provisionados exclusivamente para uma única organização.
Controle total e customização.
Controle Total:
Implementação de políticas de segurança e governança personalizadas.
Atendimento a requisitos específicos de conformidade e privacidade.
Customização:
Personalização da infraestrutura de acordo com as necessidades específicas da organização.
Seleção de hardware, software e configurações de rede personalizadas.
Nuvem Híbrida

Características:
Combinação de nuvem pública e privada.
Flexibilidade e integração com infraestrutura existente.
Flexibilidade:
Otimização de custos e desempenho.
Alocando recursos onde são mais necessários.
Integração com Infraestrutura Existente:
Facilidade de integração com sistemas legados.
Migração gradual para a computação em nuvem.
On-Premises

Características:
Operação exclusiva em data centers locais.
Controle total, mas requer investimento em infraestrutura física.
Controle Total:
Importante para requisitos rigorosos de segurança e conformidade.
Investimento em Infraestrutura Física:
Custos iniciais significativos.
Necessidade de uma equipe técnica dedicada para gerenciar a infraestrutura.
Analogia: Escolha de um local para morar
Nuvem Pública:
Morar em um apartamento compartilhado, com acesso a serviços convenientes e flexibilidade de espaço.
Nuvem Privada:
Ter uma casa exclusiva, com controle total sobre quem acessa e customização completa.
Nuvem Híbrida:
Morar em uma casa com jardim, mas com acesso a serviços compartilhados em um condomínio fechado.
Opções de Conectividade na AWS
AWS VPN (Virtual Private Network)

Conexão Segura:
Estabelece túneis criptografados sobre a Internet pública.
Conexão Site-to-Site:
Túnel VPN entre a rede local e a VPC da AWS.
Comunicação segura e transparente entre recursos locais e na nuvem.
Conexão Cliente-para-Site:
Usuários remotos se conectam à VPC da AWS de forma segura.
Acesso a recursos na nuvem de qualquer lugar e a qualquer momento.
AWS Direct Connect

Conexão Dedicada:
Conexões físicas diretas entre data center local e pontos de presença da AWS.
Desempenho consistente e baixa latência.
Redução de Custo de Rede:
Evita taxas de transferência sobre a Internet pública.
Redução significativa nos custos de rede para grandes volumes de tráfego.
Internet Pública

Acessibilidade Universal:
Acesso aos serviços da AWS de qualquer lugar com conexão à Internet.
Segurança:
Exposição a ameaças de segurança, como ataques DDoS.
Necessidade de medidas de segurança, como firewalls e criptografia.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Revisão - Infraestrutura Global e Conectividade na AWS
### Regiões AWS - O que são Regiões AWS?

- Locais geográficos onde a AWS opera centros de dados.
- Cada Região hospeda múltiplas Zonas de Disponibilidade (AZs).
- Redundância e resiliência geográfica para aplicações críticas.
- 
## Importância da Escolha Estratégica

- Reduzir a latência ao hospedar aplicações em Regiões específicas.
- Melhorar a experiência do usuário.
- Otimizar a performance em aplicações que demandam interações rápidas.

# Zonas de Disponibilidade

## O que são Zonas de Disponibilidade (AZs)?

Centros de dados individuais com redundância e isolamento.
Garantem resiliência a falhas de sistema e desastres naturais.
Distribuição de aplicações entre AZs assegura alta disponibilidade.
Estratégias de Distribuição entre Múltiplas AZs

Distribuir aplicações entre múltiplas AZs dentro de uma Região.
Assegurar que suas aplicações permaneçam disponíveis e resilientes.
Garantir a continuidade dos negócios e uma excelente experiência do usuário.
Locais de Borda e Zonas Wavelength
Reduzem latência e melhoram performance para usuários finais.
Posicionam conteúdo e aplicações fisicamente próximos aos usuários.
Cruciais para aplicações que exigem resposta em tempo real.
Zonas Locais da AWS
Estendem a infraestrutura AWS para áreas metropolitanas.
Permitem latências ultra-baixas para aplicações específicas.
Benefícios para indústrias que demandam processamento de dados próximo.
Alcançando Alta Disponibilidade
Utilização de múltiplas AZs garante continuidade de serviços.
Vital para aplicações de missão crítica.
Componentes essenciais para serviços de nuvem seguros e confiáveis.
