#simple pdf merger

import os
import sys
import PyPDF2

folder_path = input("Insira aqui o caminho até com os PDFs: ")

merger = PyPDF2.PdfMerger()

for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        file_path = os.path.join(folder_path, file)
        print(f"Unindo {file}")
        merger.append(file_path)

output_path = os.path.join(folder_path, "PDF_Unido.pdf")
merger.write(output_path)
merger.close()

print(f"Arquivos PDF unidos com sucesso e salvos na pasta:: {output_path}")
        
