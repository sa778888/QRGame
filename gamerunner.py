from PIL import Image
from pyzbar.pyzbar import decode
import webbrowser

def open_game_from_qr_image(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        if data.startswith('data:text/html;base64,'):
            data_uri = data
        else:
            # If it's just raw HTML, you could encode as needed (not the case here)
            import urllib.parse
            data_uri = 'data:text/html,' + urllib.parse.quote(data)
        print("Opening game in browser...")
        webbrowser.open(data_uri)

# Example usage
open_game_from_qr_image('pong_qr.png')
