def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += (original_length * 8).to_bytes(8, 'little')

    # Chia chuỗi thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        a0, b0, c0, d0 = a, b, c, d

        # Vòng lặp chính của thuật toán MD5
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5*j + 1) % 16
            elif j < 48:
                f = (b ^ c ^ d)
                g = (3*j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7*j) % 16

            # Các hằng số T (không được cung cấp đầy đủ trong ảnh, chỉ có một giá trị mẫu)
            # Bạn sẽ cần một danh sách đầy đủ 64 hằng số T
            T = [
                0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
                0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
                0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
                0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
                0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
                0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc1,
                0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
                0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
                0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
                0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
                0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
                0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
                0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
                0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
                0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
                0x2a67292c, 0xc671d178, 0xfbd7e6fb, 0x453765e8
            ]

            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + T[j] + words[g]) & 0xFFFFFFFF, [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21][j % 16])
            a = temp

        a = (a0 + a) & 0xFFFFFFFF
        b = (b0 + b) & 0xFFFFFFFF
        c = (c0 + c) & 0xFFFFFFFF
        d = (d0 + d) & 0xFFFFFFFF

    md5_hash = '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)
    return md5_hash

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    md5_hash = md5(input_string.encode('utf-8'))
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")