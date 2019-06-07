import tkinter as tkt 
import tkinter.filedialog
import tkinter.messagebox
import py_crypto as pc

def main():
    root  = tkt.Tk(className=' AES-128 Encryption')
    #input label
    input_label = tkt.Label(root,text='input')
    input_label.grid(row=0,column=0)

    #input entry
    input_entry = tkt.Entry(root, width=50, textvariable='i am a student,you are a pig')
    input_entry.grid(row=0,column=1)

    #key label
    key_label = tkt.Label(root, text='key') 
    key_label.grid(row=1, column=0)

    #key entry
    key_entry = tkt.Entry(root, width=50, textvariable='ilikechinesebest')
    key_entry.grid(row=1, column=1)

    #encrypt label
    encrypt_label = tkt.Label(root,text='encrypted')
    encrypt_label.grid(row=2, column=0)

    #encrypt entry
    encrypt_entry = tkt.Entry(root, width=50)
    encrypt_entry.grid(row=2, column=1)

    #decrypt label
    decrypt_label = tkt.Label(root, text='decrypted')
    decrypt_label.grid(row=3, column=0)

    #decrypt entry
    decrypt_entry = tkt.Entry(root, width=50)
    decrypt_entry.grid(row=3, column=1)

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
    en_but = tkt.Button(root, text='encrypt', width=15, command=encrypt_callback)
    en_but.grid(row=0, column=2)

    #decrypt button
    def decrypt_callback():
        key = key_entry.get()
        if key == '':
            tkt.messagebox.showerror('error','key is empty')
        encrypt_text = encrypt_entry.get() 
        decrypt = pc.Pycrypto(key).decrypt(encrypt_text)
        decrypt_entry.delete(0, tkt.END)
        decrypt_entry.insert(0, decrypt)
    de_but = tkt.Button(root, text='decrypt',width=15, command=decrypt_callback)
    de_but.grid(row=3, column=2)

    #import encrypt button
    def import_encrypt_callback():
        filename = tkt.filedialog.askopenfilename()
        if filename != '':
            encrypt_entry.delete(0,tkt.END)
            encrypt_entry.insert(0,pc.Pycrypto().read_cipher(filename))
    import_encrypt_but = tkt.Button(root,text='import encrypt',width=15, command=import_encrypt_callback)
    import_encrypt_but.grid(row=2, column=2)

    #save encrypt button
    def save_encrypt_callback():
        encrypt_file_name = tkt.filedialog.askopenfilename()
        if encrypt_file_name != '':
            with open(encrypt_file_name, 'w') as f:
                f.write(encrypt_entry.get())
    save_encrypt_but = tkt.Button(root, text='save encrypt', width=15, command=save_encrypt_callback)
    save_encrypt_but.grid(row=2, column=3)

    #import key button
    def import_key_callback():
        key_file_name = tkt.filedialog.askopenfilename()
        if key_file_name != '':
            key_entry.delete(0, tkt.END)
            key_entry.insert(0, pc.Pycrypto().read_cipher(key_file_name)) 
    import_key_but = tkt.Button(root, text='import key', width=15, command=import_key_callback)
    import_key_but.grid(row=1, column=2)

    #save key button
    def save_key_callback():
        key_file_name = tkt.filedialog.askopenfilename()
        if key_file_name != '':
            with open(key_file_name, 'w') as f:
                f.write(key_entry.get())
    save_key_but = tkt.Button(root, text='save key', width=15, command=save_key_callback)
    save_key_but.grid(row=1, column=3) 

    root.mainloop()

   

main()