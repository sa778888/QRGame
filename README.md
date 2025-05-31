# QR Pong
##  A simple pong game embedded in a qr code.
# QR Pong Game Runner

This project demonstrates how to encode a self-contained Pong game (HTML/JavaScript) into a QR code as a data URI, and provides scripts to decode and launch the game instantly from a QR code image.

---
# Demo
![QR Game Demo](https://github.com/sa778888/QRGame/blob/main/demo.gif?raw=true)


---

## Files Explained

### `qrgame.py`
- **Purpose:** Generates a QR code containing the Pong game as a `data:text/html;base64,...` URI.
- **How it works:** 
  - Reads the HTML/JS Pong game code.
  - Encodes it in base64.
  - Embeds it in a data URI.
  - Generates a QR code with **low error correction** (L) to maximize data capacity.
  - Saves the QR code as `pong_qr.png`.

### `gamerunner.py`
- **Purpose:** Decodes the QR code from an image file and launches the Pong game in your default browser.
- **How it works:** 
  - Loads the QR image.
  - Decodes the QR code using `pyzbar`.
  - If the QR contains a data URI, it opens it as-is; if it contains raw HTML, it encodes it as a data URI.
  - Opens the game in your browser.

### `pong_qr.png`
- **Purpose:** The generated QR code image. When scanned or decoded, it launches the Pong game.
- **Note:** Due to QR code data limits, the HTML must be concise. The error correction level is set to **L (Low)** to allow for maximum data storage at the expense of recoverability.

### `requirements.txt`
- **Purpose:** Lists all Python dependencies required to run the scripts.

---

## QR Encoding Details

- **Encoding:** The Pong game HTML is base64-encoded and embedded as a `data:text/html;base64,...` URI.
- **Error Correction:** `ERROR_CORRECT_L` (Low, ~7% recovery) is used to maximize the amount of data that can fit in the QR code. This means the QR code is less tolerant to damage or distortion but can store more data.
- **Capacity:** With error correction L, a QR code can store up to ~2.9 KB of binary data. The Pong game must be kept minimal for reliable scanning.
- **Compatibility:** Most modern smartphone browsers can open data URIs, but most QR scanners may not support large, complex data URIs directly.

---

## Libraries and Tools Used

- [`qrcode`](https://pypi.org/project/qrcode/): For generating QR codes from data URIs.
- [`Pillow`](https://pypi.org/project/Pillow/): For image handling.
- [`pyzbar`](https://pypi.org/project/pyzbar/): For decoding QR codes from images.
- [`webbrowser`](https://docs.python.org/3/library/webbrowser.html): To open the decoded game in the default browser.
- [`base64`](https://docs.python.org/3/library/base64.html): For encoding HTML as base64.
- [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html): For percent-encoding (if needed).

**System Dependency:**  
- **ZBar shared library** (`libzbar0` on Linux) is required for `pyzbar` to function.

---

## Installation

1. **Install system dependencies:**
```bash
sudo apt-get install libzbar0
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```


---

## Steps to Run

### 1. Generate the QR Code

```bash
python3 qrgame.py
```
- This will create `pong_qr.png`.

### 2. Decode and Run the Game

```bash
python3 gamerunner.py
```
- This will scan the QR code image and open the Pong game in your browser.


---

## Notes & Limitations

- **Error Correction:**  
  Using error correction level L means the QR code can be corrupted by even minor damage. Print and handle with care.
- **Data Size:**  
  The Pong game HTML must be as small as possible. For more complex games, consider hosting the HTML online and encoding only the URL in the QR code.
- **Browser Support:**  
  Most modern browsers support `data:text/html;base64,...` URIs, but some mobile browsers or QR apps may not.
- **ZBar:**  
  On Windows or macOS, you may need to install ZBar via other means (see [pyzbar documentation](https://github.com/NaturalHistoryMuseum/pyzbar)).

---

## Troubleshooting

- **QR code not scanning:**  
  Try increasing the QR code size, improving image quality, or simplifying the HTML.
- **Browser shows code, not game:**  
  Ensure the QR contains a valid `data:text/html;base64,...` URI.
- **ImportError for ZBar:**  
  Install the ZBar shared library as described above.


**Enjoy instant Pong in your browser from a QR code!**

























