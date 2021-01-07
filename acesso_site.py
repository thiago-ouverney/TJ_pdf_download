from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import win32com.client as win32
from datetime import date
import pandas as pd, numpy as np
import time, os, logging , shutil


# profile["plugin.scan.plid.all"] = false
# profile["plugin.scan.Acrobat"] = "99.0"
# profile["pdfjs.disabled"] = true

def preferencia_download_firefox(dir_trabalho):
    arquivos = "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,aplication/pdf"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir",dir_trabalho)
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/pdf')
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    profile.set_preference("browser.download.manager.useWindow", False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.openFile",  'application/pdf')
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.download.manager.showAlertOnComplete", False)
    profile.set_preference("browser.download.manager.closeWhenDone", True)
    profile.set_preference("pdfjs.disabled", True)
    profile.set_preference("plugin.scan.Acrobat","99.0")
    profile.set_preference("plugin.scan.plid.all", False)
    return profile


def inicializador_webdriver(mostra_na_tela,dir_trabalho):
    """Come essa função iremos iniciar o webdriver Firefox mostrando ou não o output na tela.
    """
    #Definindo preferencias selenium
    preferencias = preferencia_download_firefox(dir_trabalho)
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = False
    ##My Driver
    driver = webdriver.Firefox(firefox_profile=preferencias,
                                capabilities=cap
                                )
    if mostra_na_tela == False:
        driver.set_window_position(-2000,0)

    return driver


def robo_download_email(dir_trabalho,link,pagina_inicial,pagina_final):
    # dir_trabalho = 'C:\\Users\\81018590\\Desktop\\Teste_Trabalho'
    driver = inicializador_webdriver(mostra_na_tela = True,
                                     dir_trabalho = dir_trabalho
                                     )


    #Entrando site já logado
    # link = 'http://www1.tjrj.jus.br/gedvisaweb/frmFramenavegador.aspx?id=33FAC503470D4846'
    driver.get(link)
    time.sleep(2)


    #Expandindo Todos arquivos
    css_botao_expandir = '#btnExpandir > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)'
    clicando_botao_expandir = driver.find_element_by_css_selector(css_botao_expandir).click()
    time.sleep(2)


    for indicador in range(pagina_inicial,pagina_final):
        arquivo = str(indicador).zfill(7)
        time.sleep(0.5)
        if driver.find_element_by_partial_link_text(arquivo):
            try:
                driver.find_element_by_partial_link_text(arquivo).click()
                print(f"{arquivo} impresso com sucesso")
            except:
                print(f"{arquivo} não impresso com sucesso")
        else:
            print(f"{arquivo} não encontrado")


        try:
            meu_arquivo = driver.find_element_by_partial_link_text(arquivo)
            meu_arquivo.click()
            print(f"{arquivo} impresso com sucesso")
        except Exception as err:
            # print(err)
            print(f"{arquivo} com problema")



#https://yizeng.me/2014/05/23/download-pdf-files-automatically-in-firefox-using-selenium-webdriver/