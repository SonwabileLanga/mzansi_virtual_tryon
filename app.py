from flask import Flask, render_template, request, redirect, url_for
import base64
import os

app = Flask(__name__)

# URL mapping for redirecting users to specific clothing categories on the store
SHOP_URLS = {
    0: 'https://www.zando.co.za/men',
    1: 'https://www.zando.co.za/men/trousers',
    2: 'https://www.zando.co.za/men/sweaters',
    3: 'https://www.zando.co.za/women/dresses',
    4: 'https://www.zando.co.za/men/coats',
    5: 'https://www.zando.co.za/women/sandals',
    6: 'https://www.zando.co.za/men/shirts',
    7: 'https://www.zando.co.za/men/sneakers',
    8: 'https://www.zando.co.za/men/bags',
    9: 'https://www.zando.co.za/men/boots',
}

# Ensure the upload directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    image_data = request.form['image']

    # Remove the data:image/png;base64, part from the base64 string
    image_data = image_data.replace('data:image/png;base64,', '')

    # Decode the image data
    image_data = base64.b64decode(image_data)

    # Save the image as a file
    image_filename = os.path.join('uploads', 'captured_image.png')
    with open(image_filename, 'wb') as f:
        f.write(image_data)

    # Mock result image (this is where your virtual try-on processing would go)
    result_image_url = image_filename

    # Redirect to a clothing store (mock link for now)
    shop_url = SHOP_URLS.get(0, '#')

    return render_template('result.html', image_url=result_image_url, shop_url=shop_url)

if __name__ == '__main__':
    app.run(debug=True)
