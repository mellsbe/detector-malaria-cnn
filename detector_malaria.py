import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import os

def criar_modelo():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(16,(3,3),activation='relu',input_shape=(128,128,3)),
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1,activation='sigmoid')
    ])
    return model

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_modelo = os.path.join(diretorio_atual, 'modelo_malaria_94acc.h5')
model = criar_modelo()
model.load_weights(caminho_modelo)

def selecionar_e_prever():
    caminho_img = filedialog.askopenfilename()
    if caminho_img:
        img_original = Image.open(caminho_img).convert('RGB')
        img_resized = img_original.resize((128, 128))
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array)[0][0]
        
        if pred < 0.5:
            res, conf, cor = "INFECTADA", (1 - pred) * 100, "#ff4d4d"
        else:
            res, conf, cor = "NÃO INFECTADA", pred * 100, "#2ecc71"
        
        label_result.config(text=f"CÉLULA {res}", fg=cor)
        label_conf.config(text=f"Nível de Confiança: {conf:.1f}%")
        progress['value'] = conf
        
        img_tk = ImageTk.PhotoImage(img_original.resize((220, 220)))
        panel.configure(image=img_tk, borderwidth=2)
        panel.image = img_tk

janela = tk.Tk()
janela.title("Analisador de Malária v1.0")
janela.geometry("450x620")
janela.configure(bg="#2c3e50") 

header = tk.Frame(janela, bg="#34495e", height=80)
header.pack(fill="x")
titulo = tk.Label(header, text="DETECTOR INTELIGENTE DE MALÁRIA", 
                  font=("Segoe UI", 14, "bold"), bg="#34495e", fg="#ecf0f1")
titulo.pack(pady=25)

tk.Label(janela, text="Selecione uma imagem de microscopia para análise:", 
         font=("Segoe UI", 9), bg="#2c3e50", fg="#bdc3c7").pack(pady=10)

btn = tk.Button(janela, text="📂 CARREGAR IMAGEM", command=selecionar_e_prever, 
                bg="#3498db", fg="white", font=("Segoe UI", 10, "bold"), 
                padx=30, pady=12, relief="flat", activebackground="#2980b9", cursor="hand2")
btn.pack(pady=10)

frame_foto = tk.Frame(janela, bg="#2c3e50", highlightbackground="#34495e", highlightthickness=2)
frame_foto.pack(pady=10)
panel = tk.Label(frame_foto, bg="#34495e", width=220, height=220)
panel.pack()

label_result = tk.Label(janela, text="AGUARDANDO ANÁLISE", font=("Segoe UI", 16, "bold"), 
                        bg="#2c3e50", fg="#95a5a6")
label_result.pack(pady=(20, 0))

label_conf = tk.Label(janela, text="", font=("Segoe UI", 10), bg="#2c3e50", fg="#bdc3c7")
label_conf.pack(pady=5)

style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.Horizontal.TProgressbar", troughcolor='#34495e', 
                bordercolor='#2c3e50', background='#3498db', lightcolor='#3498db', darkcolor='#3498db')

progress = ttk.Progressbar(janela, orient="horizontal", length=300, 
                           mode="determinate", style="Custom.Horizontal.TProgressbar")
progress.pack(pady=15)

footer = tk.Label(janela, text="Desenvolvido por Beatriz Melo - LINCE", 
                  font=("Segoe UI", 8, "italic"), bg="#2c3e50", fg="#7f8c8d")
footer.pack(side="bottom", pady=10)

janela.mainloop()