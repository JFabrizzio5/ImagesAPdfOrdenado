import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

def obtener_ruta_script():
    return os.path.dirname(os.path.realpath(__file__))

def convertir_imagenes_a_pdf(imagenes, nombre_salida):
    c = canvas.Canvas(nombre_salida, pagesize=landscape(letter))

    for imagen in imagenes:
        c.drawImage(imagen, 0, 0, width=letter[1], height=letter[0])  # Invierte el ancho y alto para orientación horizontal
        c.showPage()

    c.save()

def obtener_imagenes_en_carpeta(carpeta):
    imagenes = [archivo for archivo in os.listdir(carpeta) if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    return sorted(imagenes, key=lambda x: int(x.split('-')[0]))

if __name__ == "__main__":
    script_dir = obtener_ruta_script()
    carpeta_imagenes = script_dir
    pdf_output_path = os.path.join(script_dir, "output_horizontal.pdf")

    imagenes = obtener_imagenes_en_carpeta(carpeta_imagenes)

    if imagenes:
        pdf_output_path = os.path.join(script_dir, "output_horizontal.pdf")
        convertir_imagenes_a_pdf(imagenes, pdf_output_path)
        print(f"Proceso completado. Nuevo PDF horizontal creado en: {pdf_output_path}")
    else:
        print("No se encontraron imágenes en la carpeta.")
