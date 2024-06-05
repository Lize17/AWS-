## 📚 Revisão - Modelo de Responsabilidade Compartilhada da AWS
Categorias de Serviços em Nuvem
Introdução à AWS e Computação em Nuvem

AWS: Amazon Web Services.
Maior provedora de serviços de computação em nuvem do mundo.
Oferece mais de 200 serviços para armazenar, processar, analisar e gerenciar dados na internet.

## 📍 Categorias de Serviços na AWS

### Infraestrutura como Serviço (IaaS).
### Plataforma como Serviço (PaaS).
### Software como Serviço (SaaS).

## ♦ Infraestrutura como Serviço (IaaS)
◼ Nível mais baixo de abstração.

◼ Cliente tem acesso direto aos recursos de computação, armazenamento e rede da nuvem.
#### Exemplo: Amazon EC2 - criação e execução de máquinas virtuais na nuvem.

## ♦ Plataforma como Serviço (PaaS)
◼ Nível intermediário de abstração.

◼ Cliente foca apenas na plataforma para desenvolver e executar aplicações.
#### Exemplo: AWS Lambda - criação e execução de funções na nuvem sem gerenciar servidores.

## ♦ Software como Serviço (SaaS)
◼ Nível mais alto de abstração.

◼ Cliente foca apenas no software para realizar suas tarefas.
#### Exemplo: Amazon S3 - armazenamento e recuperação de dados na nuvem sem gerenciar servidores ou bancos de dados.

O Modelo de Responsabilidade Compartilhada
Definição do Modelo

Responsabilidades da AWS e do cliente na proteção de recursos e dados na nuvem.
Segurança na nuvem é uma responsabilidade compartilhada.
Divisão clara entre segurança da nuvem e segurança na nuvem.
Analogia: Aluguel de Apartamento
Duas partes envolvidas.
Proprietário do apartamento: fornecer o apartamento em boas condições.
Inquilino: cuidar do apartamento.
Responsabilidades da AWS

Fornecer serviços de nuvem em boas condições.
Manter infraestrutura, sistemas operacionais e plataformas funcionando.
Garantir segurança física da infraestrutura.
Responsabilidades do Cliente

Cuidar dos recursos e dados na nuvem.
Manter proteção e organização dos dados.
Pagar as contas em dia e não causar danos aos serviços.
Responsabilidades Compartilhadas

Criptografia de dados.
Gestão de identidade e acesso.
Configuração de firewalls.
Ideia geral do Modelo

Divisão de responsabilidades entre AWS e cliente.
Segurança da nuvem vs. segurança na nuvem.
Segurança da Nuvem (Responsabilidade da AWS)

Proteção da infraestrutura da nuvem.
Hardware, software, redes e instalações.
Conformidade com padrões do setor.
Segurança na Nuvem (Responsabilidade do Cliente)

Proteção de recursos e dados utilizados na nuvem.
Sistema operacional, softwares, configurações de rede, dados armazenados.
Garantia de conformidade com leis e regulamentos.
Exemplos Explorando IaaS, PaaS e SaaS
Infraestrutura como Serviço (IaaS)

Maior controle e responsabilidade para o cliente.
Cliente gerencia sistema operacional, softwares, configurações de rede, permissões de acesso, dados.
AWS protege infraestrutura física, redes, instalações.
Plataforma como Serviço (PaaS)

Controle e responsabilidade intermediários.
Cliente gerencia código das aplicações, configurações de rede, permissões de acesso, dados.
AWS protege infraestrutura física, redes, instalações, sistemas operacionais, plataformas.
Software como Serviço (SaaS)

Menor controle e responsabilidade para o cliente.
Cliente gerencia dados (incluindo criptografia) e permissões de acesso.
AWS protege infraestrutura física, redes, instalações, sistemas operacionais, plataformas, software.
Variação das Responsabilidades

Abstração do serviço influencia a distribuição das responsabilidades.
Serviços mais abstratos implicam em menor responsabilidade para o cliente.
Escolha do serviço deve considerar segurança, desempenho, custo e flexibilidade.
Conclusão

Modelo de responsabilidade compartilhada garante segurança na nuvem.
AWS responsável pela segurança da infraestrutura.
Cliente responsável pela segurança dos recursos e dados.
Responsabilidade varia conforme o tipo de serviço: maior para IaaS, intermediária para PaaS e menor para SaaS.

## 📚 Revisão - Segurança, Governança e Conformidade na Nuvem AWS
- Iniciando com AWS Artifact
- Introdução ao AWS Artifact

Recurso indispensável para conformidade na nuvem AWS.
Oferece acesso a relatórios e acordos de associados.
Facilita entendimento e demonstração da conformidade.
Relatórios de Auditoria

Auxiliam na avaliação da conformidade com padrões específicos.
Exemplos: SOC 1, SOC 2, PCI DSS.
Cruciais para diversas indústrias.
Acordos de Associados de Negócios

Especificam as responsabilidades e obrigações de cada parte na gestão de dados.
Exemplo: BAA da HIPAA.
Importantes para gestão de dados de saúde.
Simplificação do Processo de Conformidade

Facilita acesso à documentação.
Simplifica o processo de auditoria.
Permite foco em inovação ao reduzir burocracia.
Analogia: AWS Artifact como Guia na Jornada da Conformidade
Oferece orientação com detalhes e requisitos.
Ajuda a navegar pelos complexos padrões de conformidade.
Garante uma exploração segura no mundo regulatório.
Navegando pela Conformidade Geográfica e Setorial
Estratégias de Conformidade da AWS

Específicas para o GDPR: Proteção e privacidade dos dados na Europa.
Implementações focadas no LGPD: Atendimento às exigências de proteção de dados no Brasil.
Adoção de abordagem global para garantir conformidade em diferentes regiões e setores.
Benefícios da Abordagem Global

Permite que empresas globais operem com eficiência em diferentes cenários regulatórios.
Facilita a navegação pelas complexidades da conformidade.
Adaptação fácil às mudanças legislativas e normativas.
Analogia do Quebra-Cabeça
Conformidade como um quebra-cabeça que varia por localização e setor.
AWS como um conjunto de peças pré-montadas.
Peças ajustáveis às exigências regulatórias globais, como GDPR e LGPD, facilitando a conformidade empresarial.
Protegendo Recursos com Ferramentas AWS
Segurança Multifacetada

Proteção de dados.
Defesa contra ataques cibernéticos.
Conjunto de ferramentas para salvaguardar seus recursos.
Ferramentas Chave de Segurança na AWS

Amazon Inspector: Avaliação automatizada de segurança e recomendações para remediação de vulnerabilidades.
AWS Security Hub: Consolidação de alertas de segurança e gestão simplificada da postura de segurança.
Amazon GuardDuty: Monitoramento de atividades suspeitas e maliciosas com detecção baseada em inteligência artificial.
AWS Shield: Proteção contra ataques DDoS com serviço gerenciado ativado automaticamente.
Benefícios da Implementação das Ferramentas de Segurança

Fortalecimento da postura de segurança dos clientes AWS.
Alertas automatizados e proteção proativa contra diversas ameaças cibernéticas.
Foco em inovação e crescimento com a segurança garantida pela AWS.
Analogia: Castelo Medieval
Segurança dos recursos na AWS como a construção e manutenção de um castelo medieval.
Ferramentas de segurança como diferentes camadas de defesa do castelo.
Cada componente tem um papel específico em proteger os dados dos clientes, garantindo sua segurança.
Dominando a Criptografia na AWS
Importância da Criptografia na AWS

Protege dados em trânsito e em repouso.
Assegura confidencialidade e integridade dos dados.
Vital para a segurança das informações em ambientes digitais.
Soluções de Criptografia na AWS

AWS Key Management Service (KMS): Cria e controla chaves de criptografia.
AWS CloudHSM: Oferece ambiente dedicado para gerenciamento de chaves.
Flexíveis e escaláveis para atender diversas necessidades.
Flexibilidade e Escalabilidade

Atende organizações de todos os tamanhos.
Proporciona soluções acessíveis e eficazes.
Adaptável às exigências específicas de cada empresa.
Analogia: Cofre Pessoal
AWS KMS e AWS CloudHSM como cofres sofisticados para dados valiosos.
Oferece diferentes níveis de segurança e chaves personalizadas.
Garante acesso apenas a pessoas autorizadas.
Governança e Conformidade com Monitoramento e Auditoria
Ferramentas Essenciais para Governança e Conformidade

Amazon CloudWatch: Fornece métricas detalhadas e monitoramento em tempo real.
AWS CloudTrail: Registra eventos e ações, crucial para a auditoria e análise forense.
AWS Audit Manager: Simplifica a coleta de evidências de conformidade.
AWS Config: Avalia as configurações de recursos em relação aos padrões desejados.
Visão Contínua da Conformidade

Permitem ajustes em tempo real.
Asseguram a aplicação rigorosa das políticas de governança.
Otimizam os recursos e a detecção proativa de potenciais vulnerabilidades.
Analogia: Capitão de um Navio
Monitorar e auditar sua infraestrutura na AWS é como ser o capitão de um navio em uma longa jornada pelo oceano.
Amazon CloudWatch e AWS CloudTrail são como o mapa estelar e o compasso, ajudando a navegar.
AWS Audit Manager e AWS Config são como o diário de bordo e as verificações regulares do navio, garantindo conformidade e segurança.
Compreendendo a Variedade de Requisitos de Conformidade
Variação nos Requisitos de Conformidade

Reconhecimento das diferenças nos requisitos.
Adaptação das estratégias conforme necessário.
Estratégias Específicas para Cada Serviço

Adaptação do uso dos serviços AWS às necessidades de conformidade específicas.
Personalização das estratégias conforme o projeto ou a indústria. 

## 📚 Revisão - Recursos de Gerenciamento de Acesso da AWS


