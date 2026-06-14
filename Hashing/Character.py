s = "babfsttsbscbcaliadua"
d = ["a","e","r","u"]

result = []
hash_list = [0]*26
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

for ch in d:
    ascii_value = ord(ch)
    index = ascii_value - 97
    result.append(hash_list[index])

print(result)

ss = 'fjafsggsayuidyuyuiADDHJAJHDJA'
d = ["a","q","u","A","Q"]

result=[]
hash_tab = [0]*42
for ch in ss:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_tab[index] += 1

for ch in d :
    ascii_value = ord(ch)
    index = ascii_value - 97
    result.append(hash_tab[index])


print(result)