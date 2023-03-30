import streamlit as st
import pandas as pd 
import pickle
import plotly.graph_objects as go
import plotly.figure_factory as ff

st.set_page_config(
    layout="wide"
)

st.title("Ternarys")


# Importar el diccionario desde el archivo binario
with open('deploy/distribucion_multinomial_grafico.pickle', 'rb') as handle:
    distribucion_multinomial_grafico = pickle.load(handle)


options = st.multiselect(
        'Seleccione una o varias zonas para visualizar sus gráficos',
        ['Zona1', 'Zona2', 'Zona3', 'Zona4', 'Zona5', 'Zona6', 'Zona7'], )

intervalos = ["4-6", "7-9", "10-12", "13-15", "16-18", "19-22", "noche"]
zonas = ['Zona1', 'Zona2', 'Zona3', 'Zona4', 'Zona5', 'Zona6', 'Zona7']

# Definir los datos de los ejes
axis_labels = ['JAM', 'ACCIDENT', 'WEATHERHAZARD']

# Definir el diagrama ternario
ternary_data = {
    'sum': 1,
    'aaxis': {'title': axis_labels[0]},
    'baxis': {'title': axis_labels[1]},
    'caxis': {'title': axis_labels[2]}
}

# Generar los gráficos para cada zona y cada intervalo
for zona in zonas:
    if zona in options:
        st.write(f"<p style='font-size: 35px; font-weight: bold; font-family: 'Gill Sans Extrabold';'>{zona}</p>", unsafe_allow_html=True)

        if zona == "Zona1":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1Sy6NudejAYU1wJh8zV0sz93PLWxII64&ehbc=2E312F" 
                                width="40%" height="500"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona2":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1vIk58ZxKqKTRMQN9cLHUlXAv8dNBQX0&ehbc=2E312F" 
                                width="50%" height="700"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona3":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=17p9dYkCsekb5GZic9yUmNBlHpWtbnPg&ehbc=2E312F" 
                                width="50%" height="700"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona4":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1jdd7v34eaAK_Ae3vXgT8JtD6BTZQYtA&ehbc=2E312F" 
                                width="50%" height="700"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona5":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1D9bcjMKJcJLLV5szZVKR6MtlbDh6CSE&ehbc=2E312F" 
                                width="50%" height="700"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona6":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1QY-LXpGLTse42nu_lJMiI5kxaD8TYns&ehbc=2E312F" 
                                width="50%" height="700"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona7":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1cEHIvkKq_ByU02EOxDjH2e2K8MPkM1w&ehbc=2E312F" 
                                width="40%" height="500"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        
        st.write("___________________________________________________________________________________")
        # Crear dos columnas en el contenedor
        col1, col2 = st.columns(2)

        for intervalo in intervalos:
            #nombre del dataframe actual
            nombre_df = f"{zona}_{intervalo}"
            #Dataframe actual 
            df = distribucion_multinomial_grafico[nombre_df]
            # Crear el gráfico
            fig = go.Figure()
            # Añadir el diagrama ternario
            fig.add_trace(go.Scatterternary({
                'mode': 'markers',
                'a': df['JAM'],
                'b': df['ACCIDENT'],
                'c': df['WEATHERHAZARD'],
                'marker': {
                    'color': df['JAM'],
                    'colorscale': 'YlOrRd',
                    'size': 10,
                    'colorscale': 'Hot',
                    'line': {
                        'width': 1,
                        'color': 'black'

                    },
                    'colorbar': {'title': 'JAM', 'len': 1, 'y': 0.6}
                },
                'name': 'Puntos'
            }))
            # Configurar el layout
            fig.update_layout({
                'title': f'Ternary Heatmap para - {nombre_df}',
                'ternary': ternary_data,
                'showlegend': False,
                'width': 500
            })
            # Mostrar el gráfico en la columna correspondiente


            if intervalo in ["4-6", "7-9", "10-12"]:
                
                col1.plotly_chart(fig, use_container_width=True)
            else:
                col2.plotly_chart(fig, use_container_width=True)
    


