# Excel Quest

## Problema Educativo
El aprendizaje tradicional de Excel suele ser monótono y teórico, provocando que los estudiantes pierdan el interés o no retengan de manera efectiva los conocimientos prácticos y atajos fundamentales necesarios para su desarrollo académico y profesional. Existe una falta de interactividad que dificulta el aprendizaje basado en la práctica.

## Objetivo General
Desarrollar una aplicación web interactiva y gamificada que permita a los usuarios aprender, practicar y consolidar sus conocimientos de Microsoft Excel a través de misiones prácticas, ejercicios de fórmulas y evaluaciones de progreso en tiempo real.

## Arquitectura de IA
El desarrollo del proyecto se ha apoyado en modelos de lenguaje de Inteligencia Artificial para el diseño de la lógica gamificada, la estructuración del código HTML interactivo, la creación de módulos de pre-test y post-test, y la generación de componentes educativos en Streamlit y Jupyter Notebooks. Esto asegura que los contenidos y la progresión de la dificultad estén alineados con las mejores prácticas pedagógicas.

## Tecnologías Usadas
- **Frontend Interactivo:** HTML5, CSS3 (Tailwind CSS) y JavaScript Vanilla.
- **Landing Page:** Python con **Streamlit** para presentar el proyecto de forma ágil y moderna.
- **Análisis y Documentación:** **Jupyter Notebook** (`.ipynb`) como insumo principal para la estructuración y documentación del desarrollo.

## Instrucciones para ejecutar o abrir el prototipo
1. **Landing Page en Streamlit:**
   - Asegúrate de tener Python instalado junto con la biblioteca Streamlit (`pip install streamlit`).
   - Ejecuta en la terminal desde la carpeta del proyecto:
     ```bash
     streamlit run app/main.py
     ```
   - Se abrirá en tu navegador la presentación del proyecto.
   
2. **Aplicación Gamificada de Excel:**
   - Simplemente abre el archivo `Excel.html` en cualquier navegador web moderno (Chrome, Firefox, Edge). No requiere instalación de un servidor local.

3. **Cuaderno Jupyter:**
   - Instala Jupyter Notebook (`pip install notebook`) o ábrelo en VS Code.
   - Ejecuta `jupyter notebook` y abre `notebooks/Proyecto_Excel.ipynb`.

## Enlace al prototipo publicado
**Landing Page (Streamlit):** [https://excel-quest.streamlit.app/](https://excel-quest.streamlit.app/)
**Simulador (GitHub Pages):** [https://lmarion86.github.io/excel-quest/Excel.html](https://lmarion86.github.io/excel-quest/Excel.html)

## Integrantes
- Rodolfo Colomo, Roberto Carlos Mamani, Lucia Gonzales, Nelson Condori, Abad Bustamante

## Consideraciones Éticas
El proyecto fue diseñado asegurando la accesibilidad y la no discriminación en los ejemplos utilizados. No se recopilan datos personales de los usuarios durante el uso del simulador `Excel.html`, ya que toda la progresión (XP, Niveles) se almacena localmente en el navegador del usuario usando `localStorage`, garantizando la privacidad de la información de aprendizaje.
