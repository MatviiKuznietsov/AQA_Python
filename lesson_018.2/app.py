from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

upload_directory = './uploads'
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)


@app.route('/')
def index():
    return jsonify({
        'message': 'Image Upload API',
        'endpoints': {
            'upload': 'POST /upload - Upload an image',
            'get_image': 'GET /image/<filename> - Get image info or file',
            'delete': 'DELETE /delete/<filename> - Delete an image'
        }
    })


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Безопасное сохранение файла
    filename = os.path.join(upload_directory, image.filename)
    image.save(filename)

    return jsonify({'image_url': request.host_url + 'uploads/' + image.filename}), 201


@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    # Получаем заголовок Accept
    accept_header = request.headers.get('Accept', '')
    filepath = os.path.join(upload_directory, filename)

    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404

    # Если клиент запрашивает текстовый ответ
    if 'text/plain' in accept_header:
        return jsonify({'image_url': request.host_url + 'uploads/' + filename}), 200

    # По умолчанию возвращаем изображение
    return send_from_directory(upload_directory, filename)


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    filepath = os.path.join(upload_directory, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404

    os.remove(filepath)
    return jsonify({'message': f'Image {filename} deleted'}), 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)