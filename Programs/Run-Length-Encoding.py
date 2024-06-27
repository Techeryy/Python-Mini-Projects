# A simple run length encoding compression algorithm,
# part of Techeryy/Python-Mini-Projects
# Programmed By: Stephen Adams

def rleCompression(string,count=1,encode=''):
    value = string[0]
    for i in range(len(string)-1):
        if string[i+1] == value:
            count += 1
        else:
            encode += (str(count) + string[i])
            value = string[i+1]
            count = 1
    encode += (str(count) + string[-1:])
    return encode

print(rleCompression(input('Enter String: ')))