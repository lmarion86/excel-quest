import streamlit as st

st.set_page_config(
    page_title="Excel Quest | Landing Page",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para una estética moderna y oscura
st.markdown("""
<style>
    .main {
        background-color: #080d0b;
        color: #e8f0ec;
    }
    h1, h2, h3 {
        color: #00e676;
        font-family: 'Courier New', Courier, monospace;
    }
    .hero {
        text-align: center;
        padding: 50px 20px;
        background: linear-gradient(135deg, #0a120e, #0f1a15);
        border-radius: 15px;
        border: 1px solid #1a2e24;
        box-shadow: 0 0 20px rgba(0, 230, 118, 0.2);
        margin-bottom: 30px;
    }
    .btn-play {
        display: inline-block;
        background: linear-gradient(135deg, #00c853, #00e676);
        color: #080d0b !important;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        text-decoration: none;
        border-radius: 10px;
        transition: transform 0.2s, box-shadow 0.2s;
        margin-top: 20px;
    }
    .btn-play:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(0, 230, 118, 0.4);
    }
    .feature-card {
        background: #0f1a15;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #1a2e24;
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Sección Hero
st.markdown("""
<div class="hero">
    <h1 style="font-size: 3em;">Excel Quest</h1>
    <h3 style="color: #e8f0ec; font-weight: 300;">El Dominio de la Hoja de Cálculo</h3>
    <p style="margin-top: 20px; font-size: 1.2em; color: #5a7d6c;">Aprende Excel de forma gamificada, domina fórmulas, atajos y conviértete en un experto.</p>
    <br>
    <a href="http://localhost:8000/Excel.html" target="_blank" class="btn-play">▶ Iniciar Aventura (Requiere servidor local)</a>
</div>
""", unsafe_allow_html=True)

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Misiones Prácticas</h3>
        <p>Completa ejercicios reales en una interfaz simulada. Escribe fórmulas, domina referencias absolutas y aprende haciendo.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>⭐ Gana Experiencia (XP)</h3>
        <p>Sube de nivel a medida que adquieres nuevas habilidades. Desbloquea niveles más avanzados y domina el uso del programa.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Pre y Post Test</h3>
        <p>Mide tu nivel de conocimiento antes de comenzar y comprueba cuánto has aprendido al finalizar todas las misiones.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.subheader("Acerca del Proyecto")
st.write("""
Este proyecto fue diseñado para abordar el problema educativo del aprendizaje tradicional de Microsoft Excel. 
Al integrar mecánicas de gamificación, logramos retener la atención del estudiante y potenciar su retención de información y atajos.
""")
