# Análisis Financiero con Python 📈

Proyecto basado en Python que permite, desde un ejemplo básico, aplicar automatización de búsqueda de datos, extracción de información importante y análisis de acciones. Permite conocer el comportamiento de un activo en un periodo de tiempo específico, resaltando su precio máximo, mínimo y valor medio — una herramienta que le permite a una compañía, a un corredor de bolsa o a un inversor tener información más precisa para la toma de decisiones. Finalmente, esta información es enviada de forma automatizada mediante correo preestablecido.

## 🚀 Funcionalidades

- Descarga de datos históricos de cualquier activo financiero ingresado por el usuario.
- Cálculo de precio máximo, mínimo y valor medio en el periodo analizado.
- Visualización gráfica del comportamiento del activo.
- Automatización del envío de resultados por correo electrónico.

## 🛠️ Tecnologías y librerías utilizadas

- **Python 3**
- [`yfinance`](https://pypi.org/project/yfinance/) — extracción de datos financieros
- `matplotlib` — visualización gráfica de los datos
- `pyautogui` — automatización de acciones en pantalla
- `pyperclip` — manejo del portapapeles
- `webbrowser` — apertura automática de páginas/correo

## ▶️ Cómo ejecutarlo

1. Cloná o descargá este repositorio.
2. Instalá las librerías necesarias:
```bash
   pip install yfinance matplotlib pyautogui pyperclip
```
3. Abrí el archivo `Análisis.ipynb` en Jupyter Notebook o en VS Code.
4. Ejecutá las celdas en orden e ingresá el ticker del activo que quieras analizar (ej: `AAPL`, `TSLA`, `MSFT`).

## 📌 Notas

Este proyecto fue desarrollado como parte de un seminario práctico de Python aplicado a análisis financiero.
