from flask import Flask, Response
import requests

app = Flask(__name__)

# Список URL-ов для ретрансляции
source_urls = os.getenv('RELAY_LINKS_LIST', [
    "http://server.audiopedia.su:8000/ices128", # Staroe radio 0
    "https://lk.castnow.ru:8100/oldbrief-320.mp3",  # old brief radio 1
    "https://umnoe.amgradio.ru/Umnoe",    # umnoe radio  2
    "https://icecast-zvezda.mediacdn.ru/radio/zvezda/zvezda_128", # radio zvezda 3
    "https://listen6.myradio24.com/55699", #Radio Fantastika 4
    "https://c6.radioboss.fm:18096/stream", # Donat FM 5
    "https://stream05.pcradio.ru/dan_brown-med", # Dan Brown 6
    "https://5.restream.one/1465_1", # Model Dlya Sborki 7
    "https://5.restream.one/1464_1", # Literaturnoe radio 8
    "https://radio-soyuz.ru:1045/stream", # Kniga v Sluh 9
    "https://storyfm.hostingradio.ru:8031/storyfm128.mp3", # Story FM 10
    "https://stream.cassiopeia-station.ru:5125/stream" # Cassiopeya 11
])

# Перенаправление потока
@app.route('/audio_stream/<int:index>')
def audio_stream(index):
    if 0 <= index < len(source_urls):
        source_url = source_urls[index]
        r = requests.get(source_url, stream=True)
        return Response(r.iter_content(chunk_size=1024), content_type=r.headers['content-type'])
    else:
        return "Invalid index"

if __name__ == '__main__':
    port = os.getenv('PORT', 8001)  # Значение по умолчанию - 80
    app.run(host='0.0.0.0', port=int(port))  # Запуск сервера на полученном из переменной окружения порту

