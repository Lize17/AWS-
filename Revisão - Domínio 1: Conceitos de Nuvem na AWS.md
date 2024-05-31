# 📚 Revisão - AWS Cloud Adoption Framework (AWS CAF)
O que é o AWS Cloud Adoption Framework (AWS CAF)?
Introdução ao AWS Cloud Adoption Framework (AWS CAF)

AWS Cloud Adoption Framework (AWS CAF) como modelo para guiar a transformação digital na AWS.
Benefícios do AWS CAF

Redução do Risco Comercial: Orquestração de iniciativas de nuvem, maximizando benefícios organizacionais e minimizando riscos.
Melhoria do Desempenho em ESG: Alinhamento com princípios de ESG para redução da pegada de carbono e promoção da inclusão.
Aumento da Receita: Aceleração da transformação digital e resultados de negócios, aumentando agilidade e inovação.
Aumento da Eficiência Operacional: Construção de uma plataforma de nuvem híbrida escalável e modernização de workloads.
Domínios de Transformação do AWS CAF

Transformação Tecnológica: Migração e modernização de infraestrutura, aplicações e plataformas de dados e análises.
Transformação de Processos: Digitalização, automação e otimização das operações de negócios.
Transformação Organizacional: Reimaginação do modelo operacional e organização de equipes em torno de produtos e valor.
Transformação de Produtos: Reimaginação do modelo de negócios, criação de novas propostas de valor e modelos de receita.
Perspectivas do AWS CAF

Perspectiva de Negócios: Alinhamento dos investimentos em nuvem com as ambições de transformação digital.
Perspectiva de Pessoas: Evolução para uma cultura de crescimento e aprendizado contínuos.
Perspectiva de Governança: Orquestração de iniciativas de nuvem e minimização de riscos.
Perspectiva de Plataforma: Criação de uma plataforma de nuvem híbrida escalável.
Perspectiva de Segurança: Garantia da confidencialidade, integridade e disponibilidade dos dados.
Perspectiva de Operações: Garantia da entrega de serviços de nuvem atendendo às necessidades da empresa.
Conclusão

Destaque para a importância do AWS CAF como guia para transformação digital na AWS.
Abordagem abrangente do AWS CAF, cobrindo aspectos tecnológicos, organizacionais e operacionais.
Estratégias de Migração Para a Nuvem AWS
Introdução às Estratégias de Migração para a Nuvem AWS

Definição de estratégias de migração como métodos para planejar, executar e validar a migração de workloads para a nuvem AWS.
Destaque para a importância da escolha da estratégia adequada e seu impacto no tempo, custo, risco e benefício da migração.
As Sete Estratégias de Migração para a Nuvem (7 Rs)

Retire (Retirada): Migração de aplicativos a serem descomissionados ou arquivados.
Retain (Reter): Estratégia para manter aplicativos no ambiente de origem ou adiar a migração.
Rehost (Rehospedar): Mover aplicativos para a nuvem sem modificá-los (lift and shift).
Relocate (Realocar): Transferir servidores ou instâncias para outra plataforma na nuvem.
Repurchase (Recompra): Substituir o aplicativo por uma versão ou produto diferente.
Replatform (Realocação de plataformas): Mover aplicativos para a nuvem e otimizá-los para reduzir custos ou melhorar o desempenho.
Refactor or Re-architect (Refatorar ou Rearquitetar): Modificar a arquitetura do aplicativo ao movê-lo para a nuvem, aproveitando os recursos nativos para melhorar agilidade, desempenho e escalabilidade.
Fatores na Escolha da Estratégia de Migração

Tipo, complexidade e criticidade dos workloads.
Objetivos, requisitos e restrições de negócios.
Tempo, custo e risco da migração.
Nível de maturidade e prontidão para a nuvem.
Ferramentas e Serviços AWS para Migração

AWS Migration Hub: Central de controle para monitorar e gerenciar migrações.
AWS Application Discovery Service: Descoberta automatizada de workloads para planejamento de migração.
AWS Server Migration Service: Migração de servidores para a nuvem.
AWS Database Migration Service: Migração de bancos de dados para a nuvem.
AWS CloudEndure Migration: Replicação de workloads em tempo real para a nuvem.
AWS Snow Family: Dispositivos físicos para transferência de dados em massa para a nuvem.
Conclusão e Próximos Passos

Enfatizar a importância da escolha da estratégia correta para uma migração bem-sucedida.
Encorajar os participantes a explorar as ferramentas e serviços AWS para planejar e executar suas migrações com sucesso.
Exemplos de Estratégias de Migração para a Nuvem AWS
Exemplo de Rehosting: Replicação de Banco de Dados
Estratégia: Rehosting

Mover workloads para a nuvem sem alterações significativas.
Exemplo Prático: Replicação de Banco de Dados

Copiar dados de um banco local para um na nuvem AWS, mantendo a estrutura.
Utilização do AWS Database Migration Service (AWS DMS).
Migração rápida, segura e confiável.
Conclusão e Próximos Passos

Recapitulação do exemplo prático de rehosting com replicação de banco de dados.
Encorajamento para explorar mais sobre o AWS DMS e outras estratégias de migração nos documentos da AWS para uma migração bem-sucedida para a nuvem AWS.
Exemplo de Replatforming: Uso do AWS Snowball
Exemplo de Replatforming: Uso do AWS Snowball

Estratégia: Replatforming
Modificar workloads antes da migração para a nuvem AWS.
Exemplo Prático: Uso do AWS Snowball
Dispositivo físico para transferir grandes volumes de dados para a nuvem AWS.
Evita limitações de largura de banda, tempo ou segurança da internet.
AWS Snowball em Ação

Processo de Utilização:
Solicitação pelo console da AWS.
Transferência de dados para o dispositivo.
Envio do dispositivo de volta para a AWS.
Carregamento dos dados para o Amazon S3 e exclusão dos dados do dispositivo.
Benefícios:
Criptografia, compressão e otimização dos dados.
Transferência rápida e segura de grandes volumes de dados.
Exemplo de Refactoring: Uso do Amazon Lambda
Exemplo de Refactoring: Uso do Amazon Lambda

Estratégia: Refactoring
Redesenhar workloads para se adaptarem aos recursos nativos da nuvem AWS.
Exemplo Prático: Uso do Amazon Lambda
Serviço para executar código sem provisionar ou gerenciar servidores.
Benefícios do Amazon Lambda:
Escalabilidade, performance e custo otimizado.
Aplicações do Amazon Lambda

Cenário de Uso:
Processamento de imagens no Amazon S3.
Aplicação de filtros, redimensionamento ou marcas d’água.
Funcionamento:
Execução do código da função em resposta a eventos (e.g., upload de imagem).
Pagamento apenas pelo tempo de computação consumido.

# 📚 Revisão - Aspectos Econômicos da Nuvem AWS * 

Custos Fixos vs Custos Variáveis
Custos Fixos: não mudam independentemente do uso ou demanda.
Exemplo: Servidor físico na empresa.
Custos Variáveis: dependem do uso ou demanda.
Exemplo: Serviço de streaming de vídeo.
Vantagens dos Custos Variáveis:
Economia e eficiência.
Flexibilidade e escalabilidade.
Custos On-Premises vs Custos na Nuvem
Ambientes On-Premises vs Ambientes na Nuvem
On-Premises: infraestrutura mantida internamente.
Nuvem: infraestrutura fornecida por provedor de serviços.
Vantagens da Nuvem:
Redução do TCO (Total Cost of Ownership).
Foco no negócio, sem preocupações com infraestrutura.
Estratégias de Licenciamento
Bring-Your-Own-License (BYOL) vs Licenças Incluídas
BYOL: uso de licenças existentes na nuvem.
Licenças Incluídas: pagamento pelo uso do software na nuvem.
Melhor Estratégia de Licenciamento:
Depende de fatores como tipo de software e custo.
Ferramentas como AWS License Manager podem ajudar na decisão.
Dimensionamento Correto
Conceito de Dimensionamento Correto:
Ajuste do tamanho e tipo de recursos conforme demanda.
Otimização de custos e desempenho.
Ferramentas da AWS para Dimensionamento Correto:
AWS Compute Optimizer.
AWS Cost Explorer.
Automação
Benefícios da Automação:
Redução de custos e aumento da eficiência.
Execução de tarefas sem intervenção humana.
Serviços Gerenciados pela AWS:
Amazon RDS, Amazon ECS, Amazon EKS, Amazon DynamoDB.
Ferramentas para Automação:
AWS Systems Manager, AWS Budgets.
