import smtplib
import email.message

def novos_clientes(destinatario):  
    corpo_email = """
    <h1>BEM VINDO!</h1>
    <p>Obrigado por se juntar a nós! Estamos muito felizes de ter você como cliente.</p>
    <p>Atenciosamente,</p>
    <p>SixConnect.</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "SixConnect"
    msg['From'] = 'adaltospjr@gmail.com'
    msg['To'] = f'{destinatario}'
    password = 'eioovtdnuvpclftj' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

def clientes_antigo(destinatario):  
    corpo_email = """
    <p>Olá caro cliente.</p>
    <p>Recebemos a informação que você não faz mais parte dos clientes da Sixconnect. É uma pena mas esperamos que você possa voltar a ser nosso cliente.</p>
    <p>Atenciosamente,</p>
    <p>SixConnect.</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "SixConnect"
    msg['From'] = 'adaltospjr@gmail.com'
    msg['To'] = f'{destinatario}'
    password = 'eioovtdnuvpclftj' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
