import qrcode
import base64

html = """<!DOCTYPE html><html><body style="margin:0;overflow:hidden"><canvas id="c"></canvas><script>
let c = document.getElementById("c"), x = c.getContext("2d");
let w = c.width = innerWidth, h = c.height = innerHeight;
let px = w / 2 - 50, py = h - 20, pw = 100, ph = 10;
let bx = w / 2, by = h / 2, br = 10, dx = 4, dy = -4;
document.onmousemove = e => px = e.clientX - pw / 2;
function draw() {
  x.clearRect(0, 0, w, h);
  x.fillRect(px, py, pw, ph);
  x.beginPath(); x.arc(bx, by, br, 0, Math.PI * 2); x.fill();
  bx += dx; by += dy;
  if (bx < br || bx > w - br) dx = -dx;
  if (by < br) dy = -dy;
  if (by > py - br && bx > px && bx < px + pw) dy = -dy;
  if (by > h) alert("Game Over");
  requestAnimationFrame(draw);
}
draw();
</script></body></html>"""

data_uri = f"data:text/html;base64,{base64.b64encode(html.encode()).decode()}"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)  # Reduced error correction
qr.add_data(data_uri)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("pong_qr_reduced_error_correction.png")
