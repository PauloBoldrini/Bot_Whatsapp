#Necessário selenium instalado
from selenium import webdriver
import time


class whatsappbot:
    #Base inicio
    def __init__(self):
        self.mensagem = "Bom dia pessoal, acessem a página: https://pauloboldrini.github.io/portfolio/"
        self.grupos = ["Recados importantes"] #Grupos ou pessoas
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver', chrome_options=options)


    #Enviar mensagem
    def envio_mensagens(self): 
        #<span dir="auto" title="Recados importantes" class="_35k-1 _1adfa _3-8er">Recados importantes</span>
        #<div tabindex="-1" class="_1JAUF _2x4bz"> Precisa da classe Escrever mensagem
        #<span data-icon="send" class=""   Botão de envio

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        #FOR repetição para vários grupos ou pessoas caso seja necessário
        #Necessário tempo entre as ações para não sobrecarregar o sistema
        for grupo in self.grupos: 
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()

            caixa_mensagem = self.driver.find_element_by_class_name('_2x4bz')
            time.sleep(3)
            caixa_mensagem.click()

            caixa_mensagem.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = whatsappbot()
bot.envio_mensagens()


