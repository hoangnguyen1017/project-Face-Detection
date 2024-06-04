import hashlib
h = hashlib.new("SHA256")
h.update("tun1".encode())

print(h.hexdigest())