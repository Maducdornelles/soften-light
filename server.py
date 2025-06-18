import serial
import asyncio
import websockets
import smtplib
from email.mime.text import MIMEText

# Ajuste a porta conforme sua máquina:
arduino = serial.Serial('/dev/ttyACM0', 9600)

email_enviado = False
clientes = set()

async def envia_websocket():
    global email_enviado
    async with websockets.serve(handle_cliente, "0.0.0.0", 6789):
        print("Servidor WebSocket ativo na porta 6789 (modo Arduino)...")
        while True:
            if arduino.in_waiting:
                dado = arduino.readline().decode().strip()
                print(f"Recebido do Arduino: {dado}")

                if dado == "OK" and not email_enviado:
                    enviar_email()
                    email_enviado = True

                await broadcast(dado)
            await asyncio.sleep(0.1)  # Pequeno delay para evitar sobrecarga

async def handle_cliente(websocket):
    clientes.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        clientes.remove(websocket)

async def broadcast(mensagem):
    if clientes:
        await asyncio.gather(*(cliente.send(mensagem) for cliente in clientes))

def enviar_email():
    msg = MIMEText("Ambiente está estável para início do atendimento (Arduino).")
    msg['Subject'] = "Status: Ambiente Estável (Arduino)"
    msg['From'] = "1134791@atitus.edu.br"
    msg['To'] = "1134791@atitus.edu.br"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("1134791@atitus.edu.br", "qwzc waea pivp momd")
            server.send_message(msg)
        print("E-mail enviado! (Arduino)")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

asyncio.run(envia_websocket())

