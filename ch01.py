encoded_text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq '\
               'ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw '\
               'rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq '\
               'pcamkkclbcb. lmu ynnjw ml rfc spj.'

def decode(text):               
    import string
    mapping_table = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    return ''.join(
        [mapping_table[ord(c)-ord('a')] if c.isalpha() else c for c in text])
        
print decode(encoded_text)

print decode('map')
# output: ocr
# next: http://www.pythonchallenge.com/pc/def/ocr.html