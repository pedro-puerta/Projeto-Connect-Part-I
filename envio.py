import smtplib
import email.message

def novos_clientes(destinatario):  
    corpo_email = """
    <p>Obrigado por escolher a Sixconnect</p>
    <p>Seja bem-vindo</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Teste"
    msg['From'] = 'adaltospjr@gmail.com'
    msg['To'] = f'{destinatario}'
    password = 'eioovtdnuvpclftj' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def clientes_antigo(destinatario):  
    corpo_email = """
    <p>Aguardamos o seu retorno</p>
    <p>Até a próxima</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Teste"
    msg['From'] = 'adaltospjr@gmail.com'
    msg['To'] = f'{destinatario}'
    password = 'eioovtdnuvpclftj' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email cliente antigo enviado')
