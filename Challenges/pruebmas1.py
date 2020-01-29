a = 'ghaqjdrmnegmrlrlfpjmnnngpwalzknsencuzwsnhfltwohdgbmvfuwtquosrnyerucntxxkfqehjqygcarxogvcfkljzbzutxphpyykapncjfclnhndzxghelyvzpylazhuutmcquusexzbhsfsmbnlvnlemzvfqbfzwquairhpylnbvyhiyamztlhfchhbwrqddmuzsprfdwuqqchcpeakkexackwwzihkfenwzwckynymgqydvjtovaoezkjjurylqcuonsujycziobnfnmuwnoxcdtahpituykvgpyyshvukrstcbmnsqtjseflwywnslmvnqrtnzkyaddkjamrezprqgoenzsdryygbkeahfiduozpwkrgmatszaxmwodsqiocvagbvxyqotpaujnqvqgjmfxnxhfbwqjpgodlxdrxpjpmzeabpgqrzpxomniknjkdiwtfgyvwvekrnoupwkcbtmpcfamzrghgrznuedkybmfwctdghcfawajlxfkzhdamuygjbcwnyglkjlfmpxfdtovkqbshhrfrnyjrgxgiozsuuncnwofkqzsypwgeikpfbhryhpszegdfajzvqlwwqlnvdtdiuckcvvosrdweohnmawqonjbxyjjhlccuteeshfrxxdhzgakwjqbymnaeudcmibsytyajsgdpfvrutcpglzxdevenevmkgalcrpknuvcrnkuboennhyzirfwvtozzijujsckbxqpocakzrbwgpqgjjmsrtwmvhwyraukbuxfvebeylfpipzwjdzlmgslbtwzataxgqpasrssnfwndldwkdutdqcmcpyanrbdsxrvcvpsywjambtbzlcrvzesuhvyvwwuwwdznigxjxknfajpknqutfvvqynkpvkzgypasevrpxofbymdzcitoqolwqegocuyqsexhumzmckzuuwkamolbltlifongpvkcnrnnuplftqbxpdnegdqlymftqyrxcnzmu'
# i = len(a)
# sum = 0
# largo = 0
# symbol = 'abcdefghijklmnopqrstuvwxyz'
# for key in symbol:
#     if a.count(key) > 1:
#         sum = a.count(key) + sum
#     # print(key, a.count(key))
#     while i > 0:
#         largo = i + largo
#         i -= 1
# sum = sum // 2
# print(sum)
# print(largo - sum)



lean_head_string = len(a)
list_substring = []
count = 1
while lean_head_string >= 1:
    for i in range(0, len(a)):
        if a[:i+1] not in list_substring:
            list_substring.append(a[:i+1])
    lean_head_string -= 1
    a = a[count:]
print(len(list_substring))
