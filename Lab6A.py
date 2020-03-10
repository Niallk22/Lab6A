import hashlib
firstString = 'ecsc' ; hash_value = 'c89aa2ffb9edcc6604005196b5f0e0e4'
def hash(s):
    figure = hashlib.md5(s.encode())
    output = figure.hexdigest()
    return output
while firstString != 'c89aa2ffb9edcc6604005196b5f0e0e4':
    firstString = hash(firstString)
    print(firstString)
