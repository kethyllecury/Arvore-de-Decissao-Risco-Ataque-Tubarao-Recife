# Modelo de Previsão de Ataques de Tubarão nas Praias de Recife

## Descrição
Este modelo utiliza uma árvore de decisão para prever as chances de um ataque de tubarão em diversas praias de Recife, com base em uma série de fatores ambientais. O objetivo é fornecer uma previsão do risco para banhistas, permitindo que autoridades locais e cidadãos tomem decisões mais informadas sobre segurança nas praias.

## Características dos Dados
O modelo é alimentado por dados ambientais, transformados conforme as regras descritas abaixo:

- **Temperatura da água (°C)**:
  - **0** → Temperatura abaixo ou igual à mediana
  - **1** → Temperatura acima da mediana
- **Hora do dia**:
  - **0** → Manhã
  - **1** → Tarde
  - **2** → Noite
- **Profundidade da água (m)**:
  - **0** → Profundidade abaixo ou igual à mediana
  - **1** → Profundidade acima da mediana
- **Distância da costa (m)**:
  - **0** → Distância da costa abaixo ou igual à mediana
  - **1** → Distância da costa acima da mediana
- **Turbidez da água (NTU)**:
  - **0** → Turbidez abaixo ou igual à mediana
  - **1** → Turbidez acima da mediana
- **Atividade das presas (cardumes/km²)**:
  - **0** → Baixa quantidade de presas na região
  - **1** → Alta quantidade de presas na região

## Exemplo de Dados Usados no Modelo:
| Temperatura da Água | Hora do Dia | Profundidade (m) | Distância da Costa (m) | Turbidez (NTU) | Atividade das Presas (cardumes/km²) | Risco |
|---------------------|-------------|-------------------|------------------------|----------------|-------------------------------------|-------|
| 1 (quente)          | 2 (noite)   | 0 (raso)          | 0 (perto)              | 1 (turva)      | 1 (muitas presas)    | ALTO  |

## Resultados do Modelo:
- **Acurácia**: 90%
- **Precision (Precisão)**:
  - **Alto**: 85%
  - **Baixo**: 100%
- **Recall (Revocação)**:
  - **Alto**: 100%
  - **Baixo**: 80%
- **F1-Score**:
  - **Alto**: 0.92
  - **Baixo**: 0.89

## Métricas de Avaliação:
O modelo foi avaliado usando a métrica de **acurácia**, **precisão**, **recall** e **F1-score**, com as seguintes observações:

- O modelo apresenta uma boa capacidade de prever os casos de risco **Alto** (100% de recall).
- A classe **Baixo** possui uma boa precisão, mas poderia ser melhorada no recall (80%).

## Como Usar:
1. **Obter Dados Atualizados**: Para usar o modelo em tempo real, é necessário coletar dados diários de temperatura da água, hora do dia, profundidade, distância da costa, turbidez e atividade das presas nas praias de Recife.
   
2. **Aplicar o Modelo**: Use os dados coletados como entrada para a árvore de decisão treinada. O modelo irá prever se o risco de ataque é **Alto** ou **Baixo** com base nas condições ambientais.

3. **Tomada de Decisão**: Com base na previsão do modelo, é possível tomar medidas preventivas, como alertas aos banhistas e ajustes nas políticas de segurança nas praias.

## Tecnologias Usadas:
- **Python**: Linguagem de programação utilizada para construir e treinar o modelo.
- **Scikit-learn**: Biblioteca usada para a criação da árvore de decisão e as métricas de avaliação.
- **Matplotlib**: Usado para visualizar a árvore de decisão.

## Possíveis Melhorias:
- **Ajustes no Modelo**: O modelo pode ser melhorado ajustando os parâmetros da árvore de decisão, como profundidade máxima e número mínimo de amostras por folha.
- **Dados Adicionais**: Incluir mais variáveis, como o histórico de ataques de tubarão e o comportamento do mar (ondas, correnteza), pode melhorar a precisão do modelo.
- **Balanceamento de Dados**: Técnicas como SMOTE podem ser aplicadas para balancear melhor as classes **Alto** e **Baixo**, melhorando o recall da classe "Baixo".

## Conclusão
Este modelo fornece uma ferramenta útil para prever a segurança nas praias de Recife, ajudando a reduzir os riscos de ataques de tubarão. Embora o modelo apresente bons resultados, ele pode ser continuamente melhorado com a adição de mais dados e ajustes no processo de treinamento.
