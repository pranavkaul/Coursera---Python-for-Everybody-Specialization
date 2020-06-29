text = "X-DSPAM-Confidence:    0.8475"
found = text.find('0.8475')
final = text[found:]
type_change = float(final)
print(type_change)
