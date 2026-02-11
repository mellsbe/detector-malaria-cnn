# Detector Inteligente de Malária com Deep Learning

Este projeto utiliza uma **Rede Neural Convolucional (CNN)** para identificar automaticamente células sanguíneas infectadas com o parasita da malária. O sistema foi desenvolvido para auxiliar na triagem rápida de lâminas de microscopia de forma eficiente e acessível.

## Interface do Usuário (Software)
Desenvolvi uma aplicação desktop amigável em **Python (Tkinter)**. O usuário carrega uma imagem de microscopia e recebe o diagnóstico instantâneo com o nível de confiança.

<p align="center">
<img width="448" height="653" alt="Captura de tela 2026-02-11 141949" src="https://github.com/user-attachments/assets/279401d2-e124-4184-87a4-69683d95b00d" />
<img width="448" height="652" alt="Captura de tela 2026-02-11 142028" src="https://github.com/user-attachments/assets/de5746ce-fba6-4a31-ad23-7316463dc42b" />
</p>

## Desempenho e Métricas
O modelo foi treinado e validado apresentando alta confiabilidade estatística:

* **Acurácia Geral:** 94%
* **Precisão (Infectados):** 97% (Alta confiabilidade na detecção da doença)
* **Sensibilidade (Recall):** 91% (Capacidade de identificar doentes reais)

### Matriz de Confusão
Abaixo, a distribuição dos acertos do modelo em um conjunto de dados de 5.510 imagens nunca vistas antes:

<p align="center">
<img width="473" height="387" alt="MatrizDeConfusao_CNN_Final" src="https://github.com/user-attachments/assets/57ba2627-c478-4a75-a36b-d5f730d3372b" />
</p>

## Tecnologias Utilizadas
* **Linguagem:** Python
* **IA:** TensorFlow e Keras
* **Interface:** Tkinter
* **Processamento:** NumPy e Pillow (PIL)

---
Desenvolvido por **Beatriz Melo** – Focando em tecnologia aplicada à saúde.
