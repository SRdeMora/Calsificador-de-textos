<div align="center">
  <h1 align="center">
    📰 Clasificador de Noticias por Categoría
  </h1>
  <p align="center">
    <strong>Un proyecto de Machine Learning para clasificar automáticamente noticias en diferentes categorías (Deportes, Economía, etc.) utilizando modelos clásicos de NLP y Scikit-learn.</strong>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/NLTK-3776AB?style=for-the-badge" alt="NLTK">
  <img src="https://img.shields.io/badge/Matplotlib-010101?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
</p>

---

## 📜 Descripción del Proyecto

Este repositorio contiene un notebook de Jupyter que detalla el proceso completo para construir y evaluar un **clasificador de textos multiclase**. El objetivo es entrenar un modelo de Machine Learning capaz de leer el contenido de una noticia y asignarle automáticamente una de las siguientes categorías:

-   **Deportes**
-   **Economía**
-   **Entretenimiento**
-   **Ciencia y Tecnología**
-   **Salud**

El proyecto abarca desde el preprocesamiento del texto hasta el entrenamiento, la evaluación comparativa de varios algoritmos y la visualización de sus resultados.

---

## ⚙️ Pipeline del Proyecto

El flujo de trabajo implementado en el notebook sigue los pasos estándar de un proyecto de Procesamiento del Lenguaje Natural (NLP):

### 1. Carga y Exploración de Datos

-   Se carga el dataset de noticias desde un archivo CSV.
-   Se realiza un análisis exploratorio inicial para entender la distribución de las categorías y la estructura de los datos.

### 2. Preprocesamiento del Texto

Para preparar los datos para el modelado, se aplica una serie de técnicas de limpieza y normalización:
-   **Limpieza de Ruido:** Eliminación de caracteres no alfabéticos y puntuación.
-   **Conversión a Minúsculas:** Estandarización del texto.
-   **Tokenización:** División de los textos en palabras individuales (`tokens`) usando **NLTK**.
-   **Eliminación de Stopwords:** Filtrado de palabras comunes que no aportan significado (ej. "el", "la", "de").

### 3. Vectorización de Texto

Los textos limpios se convierten en vectores numéricos para que los modelos de Machine Learning puedan procesarlos. Se utiliza la técnica **TF-IDF (Term Frequency-Inverse Document Frequency)**, que asigna un peso a cada palabra en función de su importancia en el documento y en el corpus completo.

### 4. Entrenamiento y Evaluación de Modelos

Se entrenan y evalúan cinco modelos de clasificación diferentes de la librería **Scikit-learn** para comparar su rendimiento:
-   `LogisticRegression` (Regresión Logística)
-   `MultinomialNB` (Naive Bayes)
-   `SVC` (Support Vector Classifier)
-   `LinearSVC` (Linear Support Vector Classifier)
-   `DecisionTreeClassifier` (Árbol de Decisión)

Para cada modelo, se calcula su **precisión (accuracy)** en el conjunto de prueba.

### 5. Análisis de Resultados

-   Se comparan las métricas de precisión de todos los modelos para identificar el de mejor rendimiento.
-   Se utiliza una **matriz de confusión** para analizar en detalle los aciertos y errores del mejor modelo (`LinearSVC`), permitiendo visualizar qué categorías son más difíciles de predecir.
-   Los resultados se visualizan mediante gráficos de barras generados con **Matplotlib**.

---

## 📊 Resultados

Tras la evaluación, el modelo **Linear Support Vector Classifier (LinearSVC)** demostró ser el más preciso para esta tarea, alcanzando una **precisión superior al 95%** en la clasificación de noticias.

<div align="center">
  <!-- Recomiendo hacer una captura de pantalla de tus gráficos y subirla al repo -->
  <img src="URL_DE_TUS_GRAFICOS.png" alt="Gráfico de Comparación de Modelos" width="700"/>
  <p><em>Comparativa de la precisión de los modelos entrenados.</em></p>
</div>

---

## 🚀 Cómo Utilizar este Notebook

1.  **Clona el repositorio:**
    ```sh
    git clone https://github.com/SRdeMora/Calsificador-de-textos.git
    cd Calsificador-de-textos
    ```

2.  **Crea un entorno virtual e instala las dependencias:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    pip install -r requirements.txt 
    ```
    *(Nota: Asegúrate de crear un archivo `requirements.txt` en tu repositorio con `pip freeze > requirements.txt`)*

3.  **Inicia Jupyter Notebook:**
    ```sh
    jupyter notebook
    ```

4.  **Abre el archivo `Clasificador de textos.ipynb`** y ejecuta las celdas para replicar el análisis.
