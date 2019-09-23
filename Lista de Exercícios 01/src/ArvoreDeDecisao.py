import os
from Dados import *
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# Instanciando arquivos para listas
script_dir = os.path.dirname(__file__)                  # Diretório absoluto
rel_path1 = "../frases/peace.txt"                       # Diretório relativo
rel_path2 = "../frases/silence.txt"                     # Diretório relativo
rel_path3 = "../frases/success.txt"                     # Diretório relativo
abs_file_path1 = os.path.join(script_dir, rel_path1)    # Diretório final
abs_file_path2 = os.path.join(script_dir, rel_path2)    # Diretório final
abs_file_path3 = os.path.join(script_dir, rel_path3)    # Diretório final

#instanciando Listas de dados
treinoFrase = []
treinoClass = []

testeFrase = []
testeClass = []

#instanciando classe de dados
dados = Dados()
dados.importarDados(abs_file_path1, abs_file_path2, abs_file_path1, "Peace", "Silence", "Success")

#pegando os dados e separando nas listas instanciadas acima
for k in range(len(dados.treino)):
    treinoFrase.append(dados.treino[k][0])
    treinoClass.append(dados.treino[k][1])

for k in range(len(dados.teste)):
    testeFrase.append(dados.teste[k][0])
    testeClass.append(dados.teste[k][1])

x = CountVectorizer()
treinoFrase  = x.fit_transform(treinoFrase).toarray()       #transforma treinoFrase em uma matriz de numeros por palavra

bagOfWords = x.vocabulary_                                  #cria a bagOfWords

y_vect = CountVectorizer(vocabulary = bagOfWords)           #adiciona a bagOfWords a nova variavel
bagOfWords = y_vect.fit_transform(testeFrase).toarray()     #coloca todas as frases na nova bagOfWords

arvore = tree.DecisionTreeClassifier()                      #cria arvore
arvore.fit(treinoFrase, treinoClass)                        #treina arvore

#mostra score
print("A precisão é de", str(arvore.score(bagOfWords, testeClass) * 100) + "%")
