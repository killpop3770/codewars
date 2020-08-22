#Программа для обработки голосовых сообщений? Yandex SpeechKit Cloud? 
#Импорт библиотек
import xml.etree.ElementTree as XmlElementTree #для чтения и встраивания xml древа

import httplib2 #http клиент

import uuid #для генерирования случайных объектов в качестве идентификаторов

from config import *** #конфиг

 
#Объявление и инициализация констант
***_HOST = '***'

***_PATH = '/***_xml'

CHUNK_SIZE = 1024 ** 2

 
#Объявление функции
def speech_to_text(filename=None, bytes=None, request_id=uuid.uuid4().hex, topic='notes', lang='ru-RU',

                       key=***_API_KEY):

 

        if filename:

            with open(filename, 'br') as file: #открытие файла в двоичном режиме

                bytes = file.read()

        if not bytes: #Обработка исключения 

            raise Exception('Neither file name nor bytes provided.')

 

 
        #конвертация байт в формат PCM 16000 Гц, 16 бит
        bytes = convert_to_pcm16b16000r(in_bytes=bytes)

 

        
        #инициализация URL запроса
        url = ***_PATH + '?uuid=%s&key=%s&topic=%s&lang=%s' % (

            request_id,

            key,

            topic,

            lang

        )

 

        
        #чтение байт, (аудиозаписи) 
        chunks = read_chunks(CHUNK_SIZE, bytes)

 

        
        #установка соединения 
        connection = httplib2.HTTPConnectionWithTimeout(***_HOST)

 
        #формирование запроса
        connection.connect()

        connection.putrequest('POST', url)

        connection.putheader('Transfer-Encoding', 'chunked')

        connection.putheader('Content-Type', 'audio/x-pcm;bit=16;rate=16000')

        connection.endheaders()

 

 
        #отправление байт (аудиозаписи), частями
        for chunk in chunks:

            connection.send(('%s\r\n' % hex(len(chunk))[2:]).encode())

            connection.send(chunk)

            connection.send('\r\n'.encode())

 

        connection.send('0\r\n\r\n'.encode())

        response = connection.getresponse()

 

        
        #обработка ответа сервера
        if response.code == 200:

            response_text = response.read()

            xml = XmlElementTree.fromstring(response_text)

 
            #если атрибут success равен 1, инициализируем переменную с максимальным доверием 
            if int(xml.attrib['success']) == 1:

                max_confidence = - float("inf")

                text = ''

 
                #в любом случае, кроме ошибки, атрибут confidence будет больше max_confidence
                for child in xml:

                    if float(child.attrib['confidence']) > max_confidence:

                        text = child.text

                        max_confidence = float(child.attrib['confidence'])

 
                #следовательно, будет возвращен текст
                if max_confidence != - float("inf"):

                    return text
                #иначе будет выброшено исключение 
                else:

                    

                    raise SpeechException('No text found.\n\nResponse:\n%s' % (response_text))

            else:

                raise SpeechException('No text found.\n\nResponse:\n%s' % (response_text))

        else:

            raise SpeechException('Unknown error.\nCode: %s\n\n%s' % (response.code, response.read()))

 
#создание исключения
сlass SpeechException(Exception):

        pass
