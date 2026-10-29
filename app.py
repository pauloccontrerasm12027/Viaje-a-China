import streamlit as st
import docx

st.set_page_config(page_title="Mapa Interactivo de China", layout="wide")

# Título y subtítulo principal
st.title("Mapa Interactivo de China")
st.write("Guía para explorar tu viaje en China.")

# Pestañas superiores
tab1, tab2 = st.tabs(["📖 Documentos Word", "🗺️ Mapa Interactivo de China"])

with tab1:
    st.header("Visor de Documentos Word (.docx)")
    
    # Campo para cargar el archivo
    archivo_subido = st.file_uploader("Sube tu archivo Word (.docx)", type=["docx"])
    
    if archivo_subido is not None:
        st.success(f"Archivo '{archivo_subido.name}' cargado con éxito.")
        st.divider()
        
        # Leer y mostrar el contenido del documento
        doc = docx.Document(archivo_subido)
        for parrafo in doc.paragraphs:
            texto = parrafo.text.strip()
            if texto:
                if parrafo.style.name.startswith("Heading") or (len(texto) > 0 and texto[0].isdigit() and "." in texto[:3]):
                    st.subheader(texto)
                else:
                    st.write(texto)
    else:
        st.info("Sube tu archivo .docx para visualizar su contenido aquí.")

with tab2:
    st.header("Mapa Interactivo de China")
    st.write("Ubicaciones principales del recorrido:")
    
    # Coordenadas aproximadas de ejemplo (Pekín, Xi'an, Shanghái)
    coordenadas = {
        "latitude": [39.9042, 34.3416, 31.2304],
        "longitude": [116.4074, 108.9398, 121.4737]
    }
    st.map(coordenadas)
