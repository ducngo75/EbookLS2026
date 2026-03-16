import base64
import os

glb_path = r"l:\Đào tạo AI\Sách Ebook\SGK Lịch sử - Địa lý 5 (4)\files\pageConfig\trongdong.glb"
out_path = r"l:\Đào tạo AI\Sách Ebook\SGK Lịch sử - Địa lý 5 (4)\files\pageConfig\trongdong_base64.js"

with open(glb_path, "rb") as f:
    glb_data = f.read()

b64_data = base64.b64encode(glb_data).decode("utf-8")
js_content = f"const trongdong_b64 = 'data:application/octet-stream;base64,{b64_data}';"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Base64 generated at {out_path}")
