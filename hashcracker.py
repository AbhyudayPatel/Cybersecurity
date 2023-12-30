import hashlib
def read(filepath):
    with open(filepath,'r') as file:
        return [line.strip() for line in file]
def crack(targethash,dictionary):
    for i in dictionary :
        if hashlib.sha256(i.encode()).hexdigest() == targethash:
            return i
    else:
        return None
if __name__== '__main__':
    targethash = 'e23c9d920c3cc58becb9540027754506eb209e88c5271efab2d6d2cab77f76a8'
    filepath = r'C:\Users\Abhyuday Patel\Desktop\code playground\random projects\dict.txt'
    dictionary = read(filepath)
    crack = crack(targethash,dictionary)
    if crack :
        print("password found ",crack)
    else:
        print("not found")