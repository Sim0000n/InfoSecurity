import tkinter as tkt 
import py_crypto as pc

def main():
    root  = tkt.Tk()
    #input label
    input_label = tkt.Label(root,text='input')
    input_label.grid(row=0,column=0)

    #input entry
    input_entry = tkt.Entry(root, textvariable='i am a student,you are a pig')
    input_entry.grid(row=0,column=5)

    #key label
    key_label = tkt.Label(root, text='key') 
    key_label.grid(row=1, column=0)

    #key entry
    key_entry = tkt.Entry(root, textvariable='ilikechinesebest')
    key_entry.grid(row=1, column=5)

    #encrypt label
    encrypt_label = tkt.Label(root,text='encrypted')
    encrypt_label.grid(row=2, column=0)

    #encrypt entry
    encrypt_entry = tkt.Entry(root)
    encrypt_entry.grid(row=2, column=5)

    #decrypt label
    decrypt_label = tkt.Label(root, text='decrypt')
    decrypt_label.grid(row=3, column=0)

    #decrypt entry
    decrypt_entry = tkt.Entry(root)
    decrypt_entry.grid(row=3, column=5)

    #encrypt button
    def encrypt_callback():
        print('callback')
        # global input_entry, key_entry, decrypt_entry
        text = input_entry.get()
        key = key_entry.get()
        print(text)
        print(key)
        encrypt = pc.Pycrypto(key).encrypt(text) 
        encrypt_entry.delete(0, tkt.END)
        encrypt_entry.insert(0, encrypt)   #encrypt button
    en_but = tkt.Button(root, text='encrypt', width=10, command=encrypt_callback)
    en_but.grid(row=4, column=0)

    #decrypt button
    def decrypt_callback():
        key = key_entry.get()
        encrypt_text = pc.Pycrypto(key).read_cipher()
        decrypt = pc.Pycrypto(key).decrypt(encrypt_text)
        decrypt_entry.delete(0, tkt.END)
        decrypt_entry.insert(0, decrypt)
    de_but = tkt.Button(root, text='decrypt',width=10, command=decrypt_callback)
    de_but.grid(row=4, column=3)



 
    
    

    root.mainloop()

   

main()