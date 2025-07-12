# 🚀 Hướng dẫn Deploy lên Vercel (Từng bước)

## Bước 1: Tải xuống file

1. **Tải file zip**: `discord_tts_web_dashboard_20250712_190533.zip`
2. **Giải nén** file zip ra thư mục trên máy tính

## Bước 2: Tạo GitHub Repository

1. **Vào GitHub**: https://github.com
2. **Đăng nhập** (tạo tài khoản nếu chưa có)
3. **Tạo repository mới**:
   - Nhấn nút "+" góc trên bên phải
   - Chọn "New repository"
   - Tên repository: `discord-tts-web-dashboard`
   - Chọn "Public"
   - Nhấn "Create repository"

## Bước 3: Upload code lên GitHub

**Cách 1 - Dễ nhất (dùng web):**
1. Trong repository mới, nhấn "uploading an existing file"
2. Kéo thả tất cả file từ thư mục đã giải nén
3. Nhấn "Commit changes"

**Cách 2 - Dùng Git:**
```bash
git clone https://github.com/your-username/discord-tts-web-dashboard.git
cd discord-tts-web-dashboard
# Copy all files from extracted folder to here
git add .
git commit -m "Initial commit"
git push origin main
```

## Bước 4: Deploy lên Vercel

1. **Vào Vercel**: https://vercel.com
2. **Đăng nhập bằng GitHub**
3. **Import Project**:
   - Nhấn "New Project"
   - Chọn repository `discord-tts-web-dashboard`
   - Nhấn "Import"
4. **Deploy**:
   - Vercel sẽ tự động detect Python
   - Nhấn "Deploy"
   - Đợi 1-2 phút

## Bước 5: Hoàn thành!

✅ **Kết quả:**
- Web dashboard có URL: `https://discord-tts-web-dashboard.vercel.app`
- Chạy 24/7 miễn phí
- Tự động có SSL/HTTPS
- Có thể tìm kiếm trên Google

## Các file đã được chuẩn bị:

```
📁 discord_tts_web_dashboard_20250712_190533/
├── app.py                    # Web application chính
├── requirements.txt          # Python dependencies
├── Procfile                 # Heroku config
├── runtime.txt              # Python version
├── vercel.json              # Vercel config
├── DEPLOY_GUIDE.md          # Hướng dẫn chi tiết
├── deploy_instructions.txt  # Hướng dẫn ngắn
├── README.md                # Hướng dẫn project
└── templates/
    ├── public_dashboard.html # Giao diện dashboard
    └── setup.html           # Trang setup
```

## Tính năng web dashboard:

✅ **Giao diện tiếng Việt**
- Dashboard thống kê bot
- Số lượng server, thành viên
- Thống kê lệnh TTS
- Thời gian hoạt động

✅ **Responsive Design**
- Tự động điều chỉnh với mobile
- Giao diện đẹp mắt
- Cập nhật realtime

✅ **Tính năng đầy đủ**
- Nút thêm bot vào Discord
- Hướng dẫn sử dụng
- API endpoints
- Health check

## Lưu ý quan trọng:

1. **Miễn phí vĩnh viễn** trên Vercel
2. **Tự động deploy** khi có thay đổi code
3. **Custom domain** có thể thêm miễn phí
4. **Analytics** có sẵn trong dashboard Vercel

## Nếu gặp lỗi:

1. **Kiểm tra logs** trong Vercel dashboard
2. **Đảm bảo** tất cả file đã upload đúng
3. **Liên hệ** Vercel support nếu cần

🎉 **Chúc mừng! Web dashboard của bạn đã online vĩnh viễn!**