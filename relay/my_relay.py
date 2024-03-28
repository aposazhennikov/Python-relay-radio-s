from flask import Flask, Response
import requests
import os

app = Flask(__name__)

# Список URL-ов для ретрансляции
source_urls = json.loads(os.getenv('RELAY_LINKS_LIST'))

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

