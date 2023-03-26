def remove_and_split(string,word):
    newstr=string.replace(word, "")
    return newstr.strip()


this = "  harry is a good boy   "
#print(this)
#print(this.strip())
n = remove_and_split(this,"harry")
print(n)
