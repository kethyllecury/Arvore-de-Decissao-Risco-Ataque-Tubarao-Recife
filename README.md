# Modelo de Previsão de Ataques de Tubarão nas Praias de Recife

## Descrição
Este modelo utiliza uma árvore de decisão para prever as chances de um ataque de tubarão em diversas praias de Recife, com base em uma série de fatores ambientais. O objetivo é fornecer uma previsão do risco para banhistas, permitindo que autoridades locais e cidadãos tomem decisões mais informadas sobre segurança nas praias.

## Características dos Dados
O modelo é alimentado por dados ambientais, como:

- **Temperatura da água (°C)**: Indica a temperatura da água do mar. Tubarões têm maior atividade em águas mais quentes.
- **Hora do dia**: A hora em que o banhista está na praia. As chances de ataque podem ser maiores à noite.
- **Profundidade da água (m)**: A profundidade onde o banhista está. Águas rasas podem ser mais perigosas devido à maior proximidade com os tubarões.
- **Distância da costa (m)**: A distância entre o banhista e a costa. Quanto mais perto da costa, maior a chance de interação com tubarões.
- **Turbidez da água (NTU)**: A clareza da água. Águas turvas dificultam a visualização, aumentando o risco de ataques acidentais.
- **Atividade das presas (cardumes/km²)**: A quantidade de presas na área. Uma maior presença de cardumes pode atrair tubarões para a região.

## Previsão de Risco
O modelo classifica o risco de ataque em duas categorias:

- **Alto**: Quando as condições são mais favoráveis a ataques de tubarões.
- **Baixo**: Quando as condições são mais seguras e não indicam alto risco de ataques.

## Exemplo de Dados Usados no Modelo:
| Temperatura da Água (°C) | Hora do Dia | Profundidade (m) | Distância da Costa (m) | Turbidez (NTU) | Atividade das Presas (cardumes/km²) | Risco |
|--------------------------|-------------|------------------|------------------------|----------------|-------------------------------------|-------|
| 28                       | Noite       | 0 (Raso)         | 0 (Perto)              | 1 (Turva)      | 1 (Alta)                           | Alto  |
| 24                       | Tarde       | 1 (Profunda)     | 50 (Distante)          | 0 (Clara)      | 0 (Baixa)                          | Baixo |

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
