from PyPDF2 import PdfFileMerger
import os
work_dir = 'C:\\Users\\81018590\\Desktop\\Teste_Trabalho'
os.chdir(work_dir)


def consolidando_emails(diretorio,cod_processo):
    os.chdir(diretorio)
    arquivos_tmp = [arquivo for arquivo in os.listdir() if arquivo.endswith('.tmp')]

    for file_tmp in arquivos_tmp:
        file_convertido = file_tmp[:-3] + 'PDF'
        os.rename(file_tmp,file_convertido)

    pdfs = [file for file in os.listdir() if file.upper().endswith('.PDF')]
    pdfs.sort(key=lambda x: os.path.getmtime(x))

    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write(f"Processo_{cod_processo}.pdf")
    merger.close()