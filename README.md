
# 🤖 SUPER BOT – TRỢ LÝ QUẢN TRỊ DISCORD TOÀN DIỆN

## 😰 Bạn có sợ dùng những con bot "không rõ nguồn gốc"?

* Bot lạ mời vào server, không biết **nó có làm gì sau lưng mình không**?
* Bot không rõ ai viết, **ẩn mã nguồn**, có thể **đọc, ghi, hoặc theo dõi** các kênh quan trọng?
* Giao toàn bộ quyền quản trị cho một thứ **không kiểm soát được**?

🛡️ **Super Bot là mã nguồn mở, hoàn toàn minh bạch, do chính bạn tự chạy.**
Không gửi dữ liệu ra ngoài, không theo dõi, không lưu trữ. Bạn **toàn quyền kiểm soát**, từ token đến hành vi của bot.

## 😫 Bạn đau khổ vì phải tự chỉnh quyền từng kênh bằng tay?

* Bạn mệt mỏi khi phải **chỉnh quyền thủ công cho từng role trên từng kênh**?
* Server của bạn quá lớn và việc **gửi thông báo đồng loạt trở nên rối rắm**?
* Bạn muốn **ẩn kênh, mở kênh**, hoặc **gửi tin nhắn tự động** nhưng không muốn code phức tạp?
* Mỗi lần dọn dẹp kênh chat lại phải **xóa tin nhắn từng dòng thủ công**?

🎉 **Đừng lo! Super Bot có thể giúp bạn giải quyết tất cả chỉ với vài lệnh đơn giản.**
Dành cho những admin bận rộn nhưng vẫn muốn server chuyên nghiệp, gọn gàng và dễ quản lý.

## 🧠 Super Bot hoạt động như thế nào?

Super Bot được thiết kế để chạy **đa bot**, **tự động hóa cao**, với khả năng quản lý và phản hồi cực kỳ nhanh chóng:

* **Đa bot:** Tự động khởi tạo nhiều bot từ file `tokens.txt`.
* **Tự động phản hồi:** Khi được nhắc tên (@mention), bot lập tức trả lời lại một cách thân thiện.
* **Gửi tin định kỳ:** Mỗi 30 phút, bot gửi một tin nhắn `"Mình đang online nè 👀"` để duy trì tương tác.
* **Thao tác quyền:** Chỉnh sửa quyền truy cập của nhiều role trên nhiều kênh trong vài giây.
* **Dọn dẹp kênh:** Xóa toàn bộ tin nhắn trong một kênh bằng một dòng lệnh duy nhất.

## 🛠️ Hướng dẫn tạo bot Discord

### 1. Tạo ứng dụng và bot

1. Vào trang: [Discord Developer Portal](https://discord.com/developers/applications)
2. Nhấn **“New Application”**, đặt tên bot.
3. Vào tab **“Bot”**, chọn **“Add Bot”** → xác nhận.

### 2. Lấy token bot

* Trong tab **Bot**, nhấn nút **“Copy”** ở phần **Token**.
* Dán vào file `tokens.txt` (mỗi dòng một token nếu bạn dùng nhiều bot).

### 3. Cấp quyền cho bot vào server

Vào tab **OAuth2 > URL Generator**:

* Tick: `bot`, `applications.commands`
* Tick các quyền: `Send Messages`, `Manage Channels`, `Manage Roles`, `Read Messages`, `Add Reactions`, `Attach Files`, v.v...
* Copy URL → Dán vào trình duyệt → Mời bot vào server.


## ▶️ Cài đặt & chạy bot

### 1. Cài thư viện cần thiết

```bash
pip install discord.py
```

### 2. Tạo file `tokens.txt`

* Mỗi dòng là một token bot bạn muốn chạy.

### 3. Chạy bot

```bash
python super_bot.py
```


## ⚙️ Lệnh điều khiển bot

### `!chat <#kênh hoặc ID> <nội dung>`

Gửi tin nhắn đến kênh được chỉ định.

> Ví dụ: `!chat #general Chào mọi người!`


### `!setup`

Thiết lập quyền hàng loạt:

1. Chọn **role** cần áp dụng.
2. Chọn **kênh** muốn chỉnh.
3. Chọn chế độ:

   * `1`: Chỉ xem + react.
   * `2`: Full chat.
   * `3`: Ẩn kênh với role đó.

---

### `!delete`

Xóa toàn bộ tin nhắn trong kênh (qua chọn danh sách hoặc tag kênh trực tiếp).


## ❓ CÂU HỎI THƯỜNG GẶP (FAQ)

### 🔹 Bot có lưu dữ liệu không?

Không. Mọi thao tác được xử lý thời gian thực, không lưu trữ.

### 🔹 Có thể dùng nhiều bot một lúc không?

Có. Chỉ cần thêm token mới vào `tokens.txt`.

### 🔹 Tại sao bot không gửi được tin nhắn?

Kiểm tra:

* Bot có quyền gửi tin ở kênh đó không?
* Token có hợp lệ không?
* Server có kick bot không?

## 👨‍💻 Được lập trình bởi **Wuys**

Super Bot được phát triển bởi **Wuys** – một lập trình viên đam mê sự tiện dụng và tự động hóa.

### 🧩 Công nghệ:

* **Ngôn ngữ:** Python 3.8+
* **Thư viện:** [`discord.py`](https://pypi.org/project/discord.py/)

### 📐 Cấu trúc thông minh:

* `setup_bot(token)`: Khởi tạo bot theo từng token.
* `on_ready()`: Đặt trạng thái, tự gửi tin định kỳ.
* `on_message()`: Phản hồi khi được tag.
* `!setup`, `!chat`, `!delete`: Những công cụ quản trị cực nhanh và tiện.

## ✅ Tổng kết

**Super Bot** là công cụ lý tưởng cho mọi quản trị viên Discord:

> ✨ Dễ dùng – Không cần biết code
> 🚀 Nhanh gọn – Thiết lập mọi thứ chỉ trong vài giây
> 🤝 Đáng tin cậy – Mã nguồn mở, không ẩn ý

📬 **Liên hệ Wuys nếu bạn muốn mở rộng thêm AI, tích hợp cơ sở dữ liệu hoặc các tính năng nâng cao.**

