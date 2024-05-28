# import requests

# # Fungsi untuk mendapatkan seluruh komentar dari postingan Instagram
# def get_all_comments(media_id, access_token):
#     base_url = f"https://graph.instagram.com/{media_id}/comments"
#     params = {
#         'access_token': access_token,
#         'limit': 100   # Jumlah komentar yang diambil per permintaan, maksimal 100
#     }
#     all_comments = []

#     # Lakukan loop sampai tidak ada komentar lagi
#     while True:
#         response = requests.get(base_url, params=params)
#         data = response.json()
        
#         if 'data' in data:
#             comments = data['data']
#             all_comments.extend(comments)

#             # Cek apakah masih ada komentar selanjutnya
#             if 'paging' in data and 'next' in data['paging']:
#                 # Mengatur parameter 'next' untuk mengambil halaman komentar berikutnya
#                 next_page = data['paging']['next']
#                 next_page_params = next_page.split("?")[1]
#                 params = dict(item.split("=") for item in next_page_params.split("&"))
#             else:
#                 break
#         else:
#             break

#     return all_comments

# # Contoh penggunaan
# media_id = "17877475003596600"
# access_token = "IGQWRPWm5BLXFUX1hTcENnLWdjWlBxU3U1emVUZAEZAJRk9Mc042MktLbHZAwbUpMVU9XRnA2c0VqWTBXODJRbDY2dENDZAW5fcUZAYRnoySWdDbUhvOEQ1VnliZAHFuNGRnLTlQcFlaOXVaWm9LLVVQYUJvbFAxVXJ1M3cZD"
# comments = get_all_comments(media_id, access_token)

# # Tampilkan komentar
# for comment in comments:
#      print("1")
#      print(comment['text'])
# print("ini test 4")


# import requests

# # Ganti YOUR_ACCESS_TOKEN dengan access token yang Anda dapatkan
# access_token = "IGQWRPWm5BLXFUX1hTcENnLWdjWlBxU3U1emVUZAEZAJRk9Mc042MktLbHZAwbUpMVU9XRnA2c0VqWTBXODJRbDY2dENDZAW5fcUZAYRnoySWdDbUhvOEQ1VnliZAHFuNGRnLTlQcFlaOXVaWm9LLVVQYUJvbFAxVXJ1M3cZD"
# url = f"https://graph.instagram.com/me/media?access_token={access_token}"

# response = requests.get(url)
# data = response.json()

# # Sekarang data berisi informasi tentang media dari akun Anda
# print(data)

import requests

def get_user_media(access_token):
    # URL endpoint untuk mendapatkan semua media dari pengguna
    url = f"https://graph.instagram.com/me/media"
    params = {
        'access_token': access_token,
        'fields': 'id'  # Hanya ambil ID dari setiap postingan
    }

    # List untuk menyimpan semua media pengguna
    all_media = []

    try:
        while True:
            response = requests.get(url, params=params)
            data = response.json()

            # Memeriksa apakah ada data media dalam respons
            if 'data' in data:
                media = data['data']
                all_media.extend(media)

                # Memeriksa apakah ada halaman selanjutnya
                if 'paging' in data and 'next' in data['paging']:
                    # Jika ada, atur ulang URL dengan parameter 'next' untuk halaman selanjutnya
                    url = data['paging']['next']
                else:
                    break
            else:
                print("Tidak ada media.")
                break
    except requests.exceptions.RequestException as e:
        print("Gagal mengambil media:", e)

    return all_media

def get_all_comments(access_token, media_id):
    # URL endpoint untuk mendapatkan semua komentar dari suatu postingan
    url = f"https://graph.facebook.com/v19.0/{media_id}/comments"
    params = {
        'access_token': access_token
    }
    all_comments = []

    try:
        while True:
            response = requests.get(url, params=params)
            data = response.json()
            print("Respons API:", data)

            # Memeriksa apakah ada data komentar dalam respons
            if 'data' in data:
                comments = data['data']
                all_comments.extend(comments)

                # Memeriksa apakah ada halaman selanjutnya
                if 'paging' in data and 'next' in data['paging']:
                    # Jika ada, atur ulang URL dengan parameter 'next' untuk halaman selanjutnya
                    url = data['paging']['next']
                else:
                    break
            else:
                print("Tidak ada komentar.")
                break
    except requests.exceptions.RequestException as e:
        print("Gagal mengambil komentar:", e)

    return all_comments

# Ganti dengan access token Anda
access_token = "IGQWRPWm5BLXFUX1hTcENnLWdjWlBxU3U1emVUZAEZAJRk9Mc042MktLbHZAwbUpMVU9XRnA2c0VqWTBXODJRbDY2dENDZAW5fcUZAYRnoySWdDbUhvOEQ1VnliZAHFuNGRnLTlQcFlaOXVaWm9LLVVQYUJvbFAxVXJ1M3cZD"

# Dapatkan semua media pengguna
user_media = get_user_media(access_token)

# List untuk menyimpan semua komentar dari semua postingan
all_comments = []

# Dapatkan komentar dari setiap media
for media in user_media:
    media_id = media['id']
    comments = get_all_comments(access_token, media_id)
    all_comments.extend(comments)

# Menampilkan komentar dari semua postingan
if all_comments:
    for comment in all_comments:
        print(comment['text'])

print("tessss2")
