import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

file = r'C:\Users\sigab\OneDrive\Área de Trabalho\machine\arvoredecisao\dados_tubarao_binario.xlsx'
df = pd.read_excel(file)

df["Risco"] = np.where(
    (df["temperatura_agua"] == 1) & 
    (df["hora_dia"] == 2) & 
    (df["profundidade_agua"] == 0) & 
    (df["distancia_costa"] == 0) & 
    (df["turbidez_agua"] == 1) & 
    (df["atividade_presas"] == 1),
    "Alto",  
    "Baixo"  
)

resultado = df["Risco"].value_counts()["Alto"]
resultado2 = df["Risco"].value_counts()["Baixo"]

print(resultado)
print(resultado2)

X = df[["temperatura_agua", "hora_dia", "profundidade_agua", "distancia_costa", "turbidez_agua", "atividade_presas"]]
y = df["Risco"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)

acuracia = accuracy_score(y_test, previsoes)
print(f"Acurácia: {acuracia:.2f}")
print(classification_report(y_test, previsoes))

plt.figure(figsize=(12,8))
plot_tree(modelo, filled=True, feature_names=X.columns, class_names=modelo.classes_, rounded=True)
plt.show()