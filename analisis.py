import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
""" Grafico 1 """
df = pd.read_csv("csv/data_organizado.csv")

def grafico1():
    def categorize_age(age):
            if age < 18:
                return 'Menor de 18'
            elif age < 25:
                return '18-24'
            elif age < 35:
                return '25-34'
            elif age < 45:
                return '35-44'
            elif age < 55:
                return '45-54'
            elif age < 65:
                return '55-64'
            else:
                return '65+'

    df['Edad_cat'] = df['Edad'].apply(categorize_age)
    orden_edades = ['Menor de 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    df['Edad_cat'] = pd.Categorical(df['Edad_cat'], categories=orden_edades, ordered=True)

 
    conteo = df.groupby(['Edad_cat', 'MBTI'], observed=False).size().unstack(fill_value=0)

    # Convertir a proporciones (por fila)
    proporciones = conteo.div(conteo.sum(axis=1), axis=0)

    # Colores para MBTI
    palette = sns.color_palette("tab20", n_colors=16)

    # Gráfico apilado horizontal
    proporciones.plot(kind='barh', stacked=True, color=palette, figsize=(14, 8))

    plt.title('Proporción de Tipos de MBTI por Categoría de Edad', fontsize=18, fontweight='bold')
    plt.xlabel('Proporción')
    plt.ylabel('Categoría de Edad')
    plt.legend(title='Tipo MBTI', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title_fontsize=12)
        
    plt.tight_layout()


    """ Creador de imagen """
    plt.savefig('static/images/grafico1.png')
    plt.close()

def grafico2():
    orden_mbti = df['MBTI'].value_counts().index.tolist()
    sns.set(style="whitegrid")
    palette_vibrante = sns.color_palette("Spectral", n_colors=2)
    # Crear gráfico de barras
    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=df,
        x='MBTI',
        hue='Género',
        order=orden_mbti,
        palette=palette_vibrante,
        edgecolor="black"
        )
    # Títulos y etiquetas
    plt.title("Distribución de Tipos MBTI por Género", fontsize=16, fontweight='bold')
    plt.xlabel("Tipo de Personalidad MBTI", fontsize=12)
    plt.ylabel("Cantidad de Personas", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Género')
    plt.tight_layout()
    
    """ Creador de imagen """
    plt.savefig('static/images/grafico2.png')
    plt.close()

def grafico3():
    sns.set(style="whitegrid", palette="pastel", font_scale=1.1)
    # Crear gráfico de conteo por interés, MBTI y educación
    g = sns.catplot(
        data=df,
        x="Interés",
        hue="MBTI",
        col="Educación_cat",
        kind="count",
        height=6,
        aspect=1.2,
        palette="Set2"
        )
    # Ajustes visuales
    g.set_titles("Nivel educativo: {col_name}")
    g.set_axis_labels("Interés", "Cantidad")
    g.set_xticklabels(rotation=45)
    g._legend.set_title("Tipo MBTI")

    plt.subplots_adjust(top=0.85)
    g.fig.suptitle("Distribución de Tipos MBTI por Interés y Nivel Educativo", fontsize=16)
    
    plt.savefig('static/images/grafico3.png')
    plt.close()

