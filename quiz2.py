
str1 = "X-DSPAM-Confidence:0.8475"

n = str1.find(':')

m = str1[n + 1:]
float_convert= float(m)
print(float_convert)
