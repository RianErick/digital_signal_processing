# Processamento Digital de Imagens – PDS

Este repositório contém a resolução da **Atividade Avaliativa 1** da disciplina de **Processamento Digital de Imagens**, utilizando **Python + OpenCV + NumPy + Matplotlib**.

## Atividade
A atividade foi dividida em duas questões principais:

### Questão 1 – Filtros Passa-Baixa (Suavização)
- Adição de **ruído sal e pimenta** em imagens em tons de cinza.
- Aplicação de diferentes filtros de suavização:
  - **Filtro da Média (Box)**
  - **Filtro da Mediana**
  - **Filtro Triangular (Bartlett)**
- Avaliação com janelas de **3x3, 5x5 e 7x7**.
- Comparação dos resultados quanto à remoção de ruído e preservação de detalhes.

### Questão 2 – Filtros Passa-Alta (Detecção de Bordas com Sobel)
- Aplicação do **filtro de Sobel** nas direções:
  - Horizontal
  - Vertical
  - Magnitude do gradiente
- Avaliação em:
  - Imagem original
  - Imagem com ruído
  - Imagens suavizadas
- Discussão sobre as diferenças entre os resultados e influência da suavização.