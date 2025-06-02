
# 🤖 SUPER BOT – TRỢ LÝ QUẢN TRỊ DISCORD TOÀN DIỆN

## 🚀 Phiên bản chính thức 1.0

Super Bot là một công cụ quản trị Discord mạnh mẽ, mã nguồn mở, được thiết kế dành cho các admin bận rộn nhưng vẫn mong muốn server gọn gàng, an toàn và dễ kiểm soát.

---

## 🛡️ Vì sao chọn Super Bot?

- **Mã nguồn mở**: Tự chạy, không gửi dữ liệu ra ngoài.
- **Toàn quyền kiểm soát**: Không phụ thuộc bot lạ, bạn kiểm soát hoàn toàn hành vi và token.
- **Dễ sử dụng**: Quản lý quyền, kênh, và tin nhắn chỉ bằng vài lệnh đơn giản.
- **Hỗ trợ đa bot**: Chạy nhiều bot cùng lúc chỉ bằng `tokens.txt`.

---

## ✨ Tính năng nổi bật

- 🎯 **Quản lý quyền**: Chỉnh hàng loạt quyền role trên nhiều kênh.
- 🧹 **Dọn dẹp tin nhắn**: Xóa toàn bộ tin nhắn trong kênh cực nhanh.
- 📢 **Gửi tin tự động**: 30 phút/lần gửi tin “Mình đang online nè 👀”.
- 📎 **Phản hồi khi được tag**: Trả lời thân thiện khi được nhắc tên.
- 💬 **Chức năng vui vẻ**: Phản hồi ngẫu nhiên khi bị gọi “bot gay”, “bot ngu”.
- 🛠️ **fix.py tích hợp (hoặc `!fix`)**: Sửa lỗi quyền kênh nhanh chóng.
- 🚨 **`!fixfull`**: Cấp full quyền khẩn cấp cho toàn bộ role (ngoại trừ @everyone).

---

## 🧠 Cách hoạt động

- Đọc các token từ `tokens.txt`.
- Mỗi token khởi tạo một bot riêng.
- Mỗi bot phản hồi, kiểm tra, gửi tin nhắn định kỳ và thực thi các lệnh.

---

## ⚙️ Hướng dẫn sử dụng

### 1. Cài đặt thư viện
```
pip install discord.py
````

### 2. Tạo `tokens.txt`

Mỗi dòng một token bot:

```
token_bot_1
token_bot_2
...
```

### 3. Chạy bot

```
python super_bot.py
```


## 📌 Các lệnh chính

| Lệnh                               | Mô tả                                    |
| ---------------------------------- | ---------------------------------------- |
| `!chat <#kênh hoặc ID> <nội dung>` | Gửi tin nhắn đến kênh chỉ định           |
| `!setup`                           | Thiết lập quyền hàng loạt theo role/kênh |
| `!delete`                          | Xóa toàn bộ tin nhắn trong một kênh      |
| `!fix`                             | Khôi phục quyền xem lịch sử tin nhắn     |
| `!fixfull`                         | Cấp full quyền cho tất cả roles          |
| `!fun`                             | Gửi câu nói ngẫu nhiên dễ thương         |
| `!version`                         | Xem phiên bản bot hiện tại               |

---

## 🔧 Sử dụng lệnh `!setup` như thế nào?

1. Bot gửi danh sách role và channel để chọn.
2. Nhập số tương ứng với role và kênh bạn muốn chỉnh (cách nhau bằng dấu phẩy).
3. Chọn chế độ:

   * `1`: Chỉ xem + react.
   * `2`: Full chat.
   * `3`: Ẩn kênh với role đó.
4. Bot tự động thiết lập trong vài giây.

---

## 🆘 Cứu hộ: `!fix` hoặc `fix.py`

Nếu lỡ tay phá quyền, không còn thấy được kênh nào:

* Dùng lệnh `!fix` trong server có bot.
* Hoặc:

```
python fix.py
```
Bot sẽ tự động khôi phục quyền cơ bản cho mọi role trên các kênh.

## ❓ Câu hỏi thường gặp (FAQ)

### 🔹 Bot có lưu dữ liệu không?

❌ Không. Mọi thao tác đều real-time và không lưu trữ.

### 🔹 Có dùng được nhiều bot không?

✅ Có! Chỉ cần thêm nhiều dòng vào `tokens.txt`.

### 🔹 Bot không gửi được tin nhắn?

* Kiểm tra quyền gửi tin của bot.
* Kiểm tra token có đúng không.
* Server có kick bot không?

## 👨‍💻 Tác giả

Phát triển bởi **Wuys** – đam mê tiện ích và tự động hóa.

### Công nghệ:

* Ngôn ngữ: Python 3.8+
* Thư viện: `discord.py`

## ✅ Tổng kết

* ✨ Dễ dùng – Không cần biết code
* 🚀 Nhanh gọn – Thiết lập trong vài giây
* 🤝 Đáng tin cậy – Mã nguồn mở minh bạch

📬 Liên hệ tác giả để mở rộng thêm AI, database hoặc chức năng cao cấp khác.

**Nếu bạn lỡ phá quyền?** Yên tâm, đã có `!fix` hoặc `fix.py` lo hết! ✌️

