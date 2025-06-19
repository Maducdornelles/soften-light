import serial
import asyncio
import websockets

# Ajuste a porta conforme sua máquina:
arduino = serial.Serial('/dev/ttyACM0', 9600)

clientes = set()

async def envia_websocket():
    async with websockets.serve(handle_cliente, "0.0.0.0", 6789):
        print("Servidor WebSocket ativo na porta 6789 (modo Arduino)...")
        while True:
            if arduino.in_waiting:
                dado = arduino.readline().decode().strip()
                print(f"Recebido do Arduino: {dado}")

                if "|" in dado:
                    status, valor_str = dado.split("|", 1)
                    try:
                        valor = int(valor_str)
                        # Você pode opcionalmente validar status aqui, mas não é obrigatório
                        mensagem = f"{status}|{valor}"
                        await broadcast(mensagem)
                    except ValueError:
                        print(f"Valor inválido vindo do Arduino: {valor_str}")
                else:
                    print(f"Dado inválido vindo do Arduino: {dado}")

            await asyncio.sleep(0.1)

async def handle_cliente(websocket):
    clientes.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        clientes.remove(websocket)

async def broadcast(mensagem):
    if clientes:
        await asyncio.gather(*(cliente.send(mensagem) for cliente in clientes))

asyncio.run(envia_websocket())
