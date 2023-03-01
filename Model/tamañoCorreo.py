import imaplib

# # Conexión al servidor de correo
# mail = imaplib.IMAP4_SSL('imap.gmail.com')
# mail.login('agustin.amaya.g21@gmail.com', 'amaya.soza8')
# mail.select('inbox')

# # Obtención del tamaño del correo
# typ, msg_data = mail.fetch('<63ff21fb.a70a0220.f882e.5844SMTPIN_ADDED_BROKEN@mx.google.com>', '(RFC822.SIZE)')
# mail_size = int(msg_data[0].split()[-1])

# # Conversión a megabytes
# mail_size_mb = mail_size / (1024**2)

# print(f"Tamaño del correo en megabytes: {mail_size_mb}")