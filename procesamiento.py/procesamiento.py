import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def limpiar_nombres_columnas(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

def eliminar_columnas_repetidas(df):
    df = df.loc[:, ~df.columns.duplicated()]
    df = df.loc[:, ~df.columns.duplicated(keep='first')]

def limpiar_dispositivo_legal(df):
    df['dispositivo_legal'] = df['dispositivo_legal'].replace(',', '', regex=True)

def dolarizar_valores(df, valor_dolar):
    df['monto_inversion_dolarizado'] = df['monto_inversion'] / valor_dolar
    df['monto_transferencia_dolarizado'] = df['monto_transferencia'] / valor_dolar

def actualizar_estado(df):
    df['estado'] = df['estado'].map({'ActosPrevios': 'Actos Previos', 'Ejecucion': 'Ejecución'})

def puntuar_estado(df):
    df['puntuacion_estado'] = df['estado'].map({'Actos Previos': 1, 'Resuelto': 0, 'Ejecución': 2, 'Concluido': 3})

def obtener_valor_dolar_desde_api():
    # Implementa la obtención del valor del dólar desde la API de sunat
    # Sustituye este valor con la lógica real de obtención
    return 3.65

def almacenar_en_base_de_datos(tabla_ubigeos):
    # Implementa la lógica para almacenar en la base de datos
    # Sustituye este código con la lógica real
    engine = create_engine('sqlite:///ubigeos.db', echo=True)
    tabla_ubigeos.to_sql('ubigeos', con=engine, if_exists='replace', index=False)

def generar_excel_top5_costo_por_region(df):
    # Implementa la generación de Excel por región con el top 5 de costo de inversión
    # Sustituye este código con la lógica real
    writer = pd.ExcelWriter('top5_costo_por_region.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()

def enviar_correo(mensaje):
    # Implementa la lógica de envío de correo
    # Sustituye este código con la lógica real
    from_email = 'tu_correo@gmail.com'
    to_email = 'destinatario@gmail.com'
    password = 'tu_contraseña'

    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def generar_reportes_y_almacenar():
    df = pd.read_excel('datos/reactiva.xlsx')

    # Aplicar funciones de limpieza
    limpiar_nombres_columnas(df)
    eliminar_columnas_repetidas(df)
    limpiar_dispositivo_legal(df)

    # Emplear API de sunat (sustituir 'valor_dolar' con el valor actual)
    valor_dolar = obtener_valor_dolar_desde_api()

    # Dolarizar valores
    dolarizar_valores(df, valor_dolar)

    # Actualizar y puntuar estado
    actualizar_estado(df)
    puntuar_estado(df)

    # Almacenar en base de datos tabla de ubigeos sin duplicados
    tabla_ubigeos = df[['ubigeo', 'region', 'provincia', 'distrito']].drop_duplicates()
    almacenar_en_base_de_datos(tabla_ubigeos)

    # Generar Excel por región con top 5 costo inversión de obras de tipo Urbano en estado 1,2,3
    generar_excel_top5_costo_por_region(df)

    # Envío de correo
    enviar_correo('¡Proceso finalizado!')

if __name__ == "__main__":
    generar_reportes_y_almacenar()