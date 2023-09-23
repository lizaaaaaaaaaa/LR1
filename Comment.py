import pyttsx3 #импорт голосового движка
import PyPDF2 #импорт библиотека для извлечения информации и содержимого документов

pdf = open("Andriy_Burkov.pdf", "rb") #создание объекта, содержащего путь к pdf-файлу, rb - чтение двоичного файла

pdfreader = PyPDF2.PdfFileReader(pdf, strict=False) #чтение объекта, содержащего путь к pdf-файлу, без сообщения пользователю при наличии фатальных ошибок во время чтения

pages = pdfreader.numPages #подсчёт количества страниц в файле

dell = pyttsx3.init() #инициализация голосового движка

pages = pdfreader.getPage(7) #указание номера страницы из pdf-файла

text = pages.extractText() #извлечение текста из указанной страницы в переменную text
print(text)

dell.say("Hello How Can I help you") #создание реплики и помещение в очередь
dell.say(text) #создание реплики из извлечённого текста из pdf-файла и помещение в очередь

dell.runAndWait() #воспроизведение списка реплик