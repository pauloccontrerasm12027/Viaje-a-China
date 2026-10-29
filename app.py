import streamlit as st
import docx
import os

st.set_page_config(page_title="Mapa Interactivo de China", layout="wide")

st.markdown("""
<style>
    /* Color de fondo suave para toda la página */
    .stApp {
        background-color: #fdfbf7;
        color: #2c3e50;
    }

    /* Color rojo para el título principal */
    h1 {
        color: #c0392b !important;
    }

    /* Color para los subtítulos */
    h2, h3 {
        color: #8e44ad !important;
    }
</style>
""", unsafe_allow_html=True)


st.title("Mapa Interactivo de China")
st.write("Guía para explorar tu viaje en China.")

# Pestañas principales
tab1, tab2 = st.tabs(["📖 Documentos Word", "🗺️ Mapa Interactivo de China"])

with tab1:
    st.header("Itinerario de Viaje a China")
    
    # Nombre del archivo que tienes subido en tu repositorio
    nombre_archivo = "Itinerario_Viaje_China_15_Dias_Visa (2).docx"
    
    if os.path.exists(nombre_archivo):
        doc = docx.Document(nombre_archivo)
        for parrafo in doc.paragraphs:
            texto = parrafo.text.strip()
            if texto:
                # Estilo para títulos de sección o encabezados
                if parrafo.style.name.startswith("Heading") or (len(texto) > 0 and texto[0].isdigit() and "." in texto[:3]):
                    st.subheader(texto)
                else:
                    st.write(texto)
                    
        st.divider()
        # Botón para que los visitantes puedan descargar una copia si lo desean
        with open(nombre_archivo, "rb") as f:
            st.download_button(
                label="📥 Descargar archivo Word",
                data=f,
                file_name="Itinerario_Viaje_China.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.warning(f"No se encontró el archivo '{nombre_archivo}' en el repositorio.")

with tab2:
    st.header("Mapa Interactivo de China")
    st.write("Ubicaciones principales del itinerario:")
    
    # Coordenadas de ejemplo (Pekín, Xi'an, Shanghái)
    ciudades = {
        "latitude": [39.9042, 34.3416, 31.2304],
        "longitude": [116.4074, 108.9398, 121.4737]
    }
    st.map(ciudades)
