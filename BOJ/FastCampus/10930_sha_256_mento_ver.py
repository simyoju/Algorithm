import hashlib

input_data = input()
# 입력 후 바이트 객체를 구하기 위해 encode 함수 사용
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)