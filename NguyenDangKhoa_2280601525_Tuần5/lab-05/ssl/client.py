import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    """
    Hàm này được chạy trong một luồng riêng để nhận dữ liệu từ server.
    """
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                # Nếu không còn dữ liệu, server đã đóng kết nối
                break
            print("Nhận:", data.decode('utf-8'))
    except:
        # Xử lý ngoại lệ (ví dụ: mất kết nối đột ngột)
        pass
    finally:
        # Đảm bảo socket được đóng khi vòng lặp kết thúc hoặc có lỗi
        ssl_socket.close()
        print("Kết nối đã đóng.")

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS) # Theo hình ảnh

# Cấu hình chế độ xác minh (thay đổi nếu cần thiết cho môi trường sản phẩm)
context.verify_mode = ssl.CERT_NONE # Thay đổi điều này tùy theo nhu cầu của bạn
context.check_hostname = False # Thay đổi điều này tùy theo nhu cầu của bạn

# Thiết lập kết nối SSL
# client_hostname được sử dụng để xác minh chứng chỉ của server (nếu verify_mode không phải CERT_NONE)
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost') # Theo hình ảnh

# Kết nối đến server
ssl_socket.connect(server_address)

# Bắt đầu một luồng để nhận dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi dữ liệu lên server
try:
    while True:
        message = input("Nhập tin nhắn: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    # Xử lý khi người dùng nhấn Ctrl+C
    pass
finally:
    # Đảm bảo socket được đóng khi chương trình kết thúc
    ssl_socket.close()