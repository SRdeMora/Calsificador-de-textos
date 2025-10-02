<div align="center">
  <h1 align="center">
    📰 Clasificador de Noticias por Categoría
  </h1>
  <p align="center">
    <strong>Un proyecto de Machine Learning con una interfaz web para clasificar noticias en 5 categorías utilizando un modelo pre-entrenado de Scikit-learn.</strong>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

---

## 📜 Descripción del Proyecto

Este repositorio contiene un clasificador de textos multiclase entrenado con técnicas de Procesamiento de Lenguaje Natural (NLP). El sistema toma un texto (por ejemplo, el titular o cuerpo de una noticia) y lo asigna a una de las siguientes categorías:

-   ⚽ **Deportes**
-   💰 **Economía**
-   🎬 **Entretenimiento**
-   🔬 **Ciencia y Tecnología**
-   ⚕️ **Salud**

El proyecto está listo para usar e incluye tanto el **modelo de Machine Learning ya entrenado** como una **interfaz web sencilla** para probar su funcionamiento en tiempo real.

---

## ⚙️ Componentes del Repositorio

-   `clasificadortexto.py`: Script principal en Python (usando Flask) que carga el modelo y el vectorizador para servir las predicciones.
-   `modelo.pkl`: Archivo del modelo de Machine Learning ya entrenado (`LinearSVC`).
-   `vectorizador.pkl`: Archivo del vectorizador TF-IDF pre-ajustado, necesario para transformar los nuevos textos.
-   `index.html`: Estructura de la interfaz web para que el usuario pueda ingresar un texto.
-   `script.js`: Lógica en JavaScript que se encarga de enviar el texto al backend y mostrar la clasificación recibida.
-   `requirements.txt`: Lista de todas las dependencias de Python necesarias para ejecutar el proyecto.

---

## 🚀 Cómo Empezar

Sigue estos pasos para ejecutar el clasificador en tu máquina local.

### 1. Prerrequisitos

-   Python 3.8 o superior
-   Git

### 2. Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/SRdeMora/Calsificador-de-textos.git
    cd Calsificador-de-textos
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Ejecución

1.  **Inicia el servidor de Flask:**
    ```bash
    python clasificadortexto.py
    ```
2.  **Abre tu navegador** y ve a la siguiente dirección:
    ```
    http://127.0.0.1:5000
    ```
3.  ¡Listo! Ya puedes escribir un texto en la interfaz y ver cómo lo clasifica el modelo.
