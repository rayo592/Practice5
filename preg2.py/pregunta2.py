import pandas as pd

wine_df = pd.read_csv('preg2.py/winemag-data-130k-v2.csv',sep=',')

print("Exploración del DataFrame:")
print(wine_df.head())
print("\nInformación del DataFrame:")
print(wine_df.info())
print("\nEstadísticas descriptivas del DataFrame:")
print(wine_df.describe())


if 'points' not in wine_df.columns or 'price' not in wine_df.columns:
    print("Error: Las columnas 'points' o 'price' no están presentes en el conjunto de datos.")
else:

    wine_df.rename(columns={'points': 'wine_points', 'price': 'wine_price', 'variety': 'wine_variety', 'winery': 'wine_winery'}, inplace=True)

    wine_df['price_range'] = pd.cut(wine_df['wine_price'], bins=[0, 20, 50, 100, float('inf')], labels=['0-20', '20-50', '50-100', '100+'])
    wine_df['is_high_rated'] = wine_df['wine_points'] >= 90
    wine_df['points_price_ratio'] = wine_df['wine_points'] / wine_df['wine_price']

    # Reportes por agrupamiento de datos
    report1 = wine_df.groupby('country')['wine_points'].mean().sort_values(ascending=False).head(10)
    report2 = wine_df.groupby('wine_variety')['wine_price'].mean().sort_values(ascending=False).head(10)
    report3 = wine_df.groupby('price_range')['wine_points'].mean().sort_index()
    report4 = wine_df.groupby(['province', 'price_range'])['wine_variety'].count().unstack()

    # Almacenar un dato agrupado en un archivo Excel
    report4.to_excel('/workspaces/PC5/wine_report.xlsx')

    print("\nReporte 1: Promedio de puntos por país (Top 10):")
    print(report1)
    print("\nReporte 2: Precio promedio por variedad (Top 10):")
    print(report2)
    print("\nReporte 3: Promedio de puntos por rango de precio:")
    print(report3)
    print("\nReporte 4: Cantidad de vinos por provincia y rango de precio:")
    print(report4)
    print("\nDatos agrupados almacenados en 'wine_report.xlsx'")