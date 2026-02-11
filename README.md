# Detector de Malária com Deep Learning

Este projeto utiliza uma **Rede Neural Convolucional (CNN)** para identificar automaticamente células sanguíneas infectadas com o parasita da malária. O sistema foi desenvolvido para auxiliar na triagem rápida de lâminas de microscopia.

## Resultados do Modelo
O modelo foi treinado no Kaggle e alcançou métricas de alto desempenho:
* **Acurácia Geral:** 94%.
* **Precisão (Infectados):** 97%.
* **Sensibilidade (Recall):** 91%.

## Interface do Usuário
Desenvolvi uma aplicação desktop amigável em **Python (Tkinter)** que permite:
1. Realizar o upload de imagens de células.
2. Obter um diagnóstico instantâneo.
3. Verificar o nível de confiança da predição através de uma barra de progresso visual.

## Tecnologias Utilizadas
* Python
* TensorFlow / Keras
* NumPy
* Pillow (PIL)
* Tkinter (Interface Gráfica)
