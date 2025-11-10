#American Standard Code for Information Interchange, or ASCII. This standard maps a
#number to a letter. The number 90 is Z, which in bits is 1011010, which gets mapped to the ASCII table
#inside the computer.


##>>> 0b1011010
#>>> ord('Z')
#>>> chr(90)


raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
raw_bytes.decode()

'文言'

utf_string = '文言'
utf_string.encode()

b'\xe6\x96\x87\xe8\xa8\x80'

raw_bytes == utf_string.encode()
True

utf_string == raw_bytes.decode()
True



#The way to remember this (even though I look it up almost every time) is to remember the mnemonic
#“DBES,” which stands for “Decode Bytes Encode Strings.” I say “dee bess” in my head when I have to
#convert bytes and strings. When you have bytes and need a string, “Decode Bytes.” When you have
#a string and need bytes, “Encode Strings.”