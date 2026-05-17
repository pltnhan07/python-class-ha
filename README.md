### **1. Cài đặt Anaconda**
- Truy cập đường dẫn: https://www.anaconda.com/download
- Đăng nhập bằng Gmail
- Chọn tải Anaconda Distribution hoặc Miniconda (nếu cấu hình máy thấp).
- Chạy file .exe vừa tải về để cài đặt.
- Để biết cài đặt thành công, tìm kiếm app `Anaconda Prompt` trong máy.

### **2. Thiết lập môi trường Conda ảo (Conda Virtual Environment)**
- Lý do cần:
    - Mỗi môi trường ảo --> Khu vực làm việc riêng cho từng mục đích/dự án
    - Tránh xung đột các thư viện
    - Quản lý và chuyển đổi các phiên bản Python
- Cài đặt một môi trường ảo:
    - Mở `Anaconda Prompt`
    - Cú pháp khởi tạo: ```conda create -n [env-name] [python-version]```
        VD: conda create -n py_class python=3.10

### **3. Cài đặt Jupyter Notebook**
- Kích hoạt môi trường ảo vừa tạo:
    ```conda activate py_class```
- Cài đặt Jupyter Notebook:
    ```conda install notebook```

### **4. Hướng dẫn sử dụng Git trong quá trình học**
Tải git repo về máy:
```git clone https://github.com/pltnhan07/python-class-ha.git```
(Chỉ thực hiện 1 lần duy nhất)

**1. Cấu trúc Git Repo:**

Nhánh `main`:
```
├── lectures/
│   ├── lecture_1.ipynb
│   └── ...
├── practice/
│   ├── practice_1.ipynb
│   └── ...
├── README.md 
```
Nhánh `main` là nơi lưu trữ tài liệu học tập. Học sinh không được cấp quyền chỉnh sửa/cập nhật tài liệu lên nhánh `main`.

**2. Các thao tác mỗi ngày**
- B1: Mở code folder và cập nhật tài liệu mới
    1. Mở Git Bash trong VS code
    2. Chuyển về nhánh main:

        ``` git checkout main```
    3. Kéo tài liệu mới nhất từ server về máy:

        ```git pull origin main``` (nếu là lần đầu tiên thực hiện lệnh pull)

        hoặc ```git pull``` (cho các lần pull tiếp theo)
- B2: Tạo nhánh (branch) riêng để làm bài

    ```git checkout -b solution```
- B3: Làm bài tập
    1. Bật môi trường conda đã cài đặt:

        ```conda activate py_class```
    2. Copy file bài tập `practice_*.ipynb` từ `\practice` về `\solution` và làm bài tập.
- B4: Nộp bài
    1. Đưa tất cả các file đã sửa vào trạng thái chuẩn bị lưu:
        
        ```git add .```
    2. Đóng gói và ghi chú:

        ```git commit -m "Submit solution 1"```
    3. Nộp bài lên server:

        ```git push origin solution``` (push file bài làm lên nhánh solution)
    4. Tạo pull request:
        - Truy cập: https://github.com/pltnhan07/python-class-ha
        - Có một thông báo màu vàng/xanh báo rằng nhánh `solution` vừa được cập nhật. Bấm nút `Compare & pull request`.
        - Bấm `Create pull request`.

