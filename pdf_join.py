from PyPDF2 import PdfFileMerger
from pdfrw import PdfReader, PdfWriter
import os
work_dir = 'C:\\Users\\81018590\\Desktop\\TESTE\\FILE'
os.chdir(work_dir)


def consolidando_emails(diretorio,cod_processo):
    os.chdir(diretorio)
    arquivos_tmp = [arquivo for arquivo in os.listdir() if arquivo.endswith('.tmp')]
    arquivos_tmp.sort(key=lambda x: os.path.getmtime(x))

    for file_tmp in arquivos_tmp:
        file_convertido = file_tmp[:-3] + 'PDF'
        os.rename(file_tmp,file_convertido)
    n = 0

    arquivos_pdf = [arquivo for arquivo in os.listdir() if arquivo.upper().endswith(".PDF")]
    arquivos_pdf.sort(key=lambda x: os.path.getmtime(x))
    for file in arquivos_pdf:
        n += 1
        file_convertido = str(n) + "_" + file
        os.rename(file,file_convertido)

    pdfs = [file for file in os.listdir() if file.upper().endswith('.PDF')]
    pdfs.sort(key=lambda x: os.path.getmtime(x))

    m = 0
    writer = PdfWriter()
    for pdf in pdfs:
        try:
            writer.addpages(PdfReader(pdf).pages)
            print(f"Sucesso - {pdf}")
        except Exception as err:
            print(f"ERRO - {pdf}")
    writer.write(f"Processo_{cod_processo}.pdf")

