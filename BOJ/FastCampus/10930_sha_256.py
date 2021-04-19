import hashlib

before = input()
after = before.encode('utf-8')
# after_after = ''

hash_pwd = hashlib.new('sha256')
hash_pwd.update(after)
print(hash_pwd.hexdigest())