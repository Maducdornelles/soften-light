
# Soften Light – Monitoramento de Luminosidade para Ambientes Clínicos

## Descrição do Projeto

O **Soften Light** é um sistema de monitoramento em tempo real da intensidade luminosa em ambientes sensíveis à luz, especialmente voltado para uso em clínicas e consultórios onde o conforto visual e a proteção do paciente são essenciais. 

O sistema visa garantir que a iluminação esteja dentro dos níveis adequados para o conforto e segurança dos pacientes com fotossensibilidade, alertando imediatamente sempre que a luminosidade ultrapassar o limite definido.

Este sistema integra:

- Um circuito com **Arduino**, utilizando um sensor de luminosidade LDR, leds indicadores e buzzer para feedback local.
- Um servidor desenvolvido em **Python**, que lê os dados do Arduino via serial e transmite em tempo real via protocolo **WebSocket**.
- Uma interface web responsiva que exibe o status atual, histórico de leituras e gráfico da evolução da luminosidade em tempo real.

---

## Componentes de Hardware Utilizados no Arduino

- **Sensor LDR (Light Dependent Resistor):** Mede o nível de luminosidade do ambiente.
- **Botão:** Permite ativar ou desativar o sistema manualmente.
- **LED Verde:** Indica que a luminosidade está dentro do limite seguro.
- **LED Vermelho:** Indica que a luminosidade ultrapassou o limite definido.
- **Buzzer:** Emite alerta sonoro em caso de luminosidade alta.

---

## Funcionamento

- O sistema é ativado/desativado manualmente pelo botão.
- A cada 500ms, o Arduino realiza uma leitura do sensor LDR.
- Se a luminosidade estiver acima do limite configurado, o LED vermelho e o buzzer são acionados, e um alerta é enviado via serial.
- Caso contrário, o LED verde fica aceso indicando condição segura.
- O servidor Python lê esses dados e os transmite em tempo real para o painel web, que atualiza status, histórico e gráfico.

---

## Como Executar

1. Faça o clone do repositório para sua máquina local:

```bash
git clone https://github.com/Maducdornelles/soften-light.git
```

2. Acesse a pasta do projeto:

```bash
cd soften-light
```

3. Abra a IDE do Arduino, carregue o código presente no arquivo `.ino` e faça o upload para o microcontrolador.

4. Crie um ambiente virtual Python para o servidor:

```bash
python3 -m venv venv
```

5. Ative o ambiente virtual:

- No Linux/macOS:

```bash
source venv/bin/activate
```

- No Windows:

```bash
venv\Scripts\activate
```

6. Instale as dependências necessárias manualmente:

```bash
pip install websockets pyserial
```

7. Ajuste, se necessário, a porta serial do Arduino no arquivo `servidor.py`:

```python
arduino = serial.Serial('/dev/ttyACM0', 9600)
```
Exemplo: `/dev/ttyACM0` pela porta correta no seu sistema, `COM3` no Windows

8. Execute o servidor Python para iniciar a transmissão via WebSocket:

```bash
python servidor.py
```

9. Abra o arquivo `painel.html` diretamente no navegador ou sirva via servidor HTTP local para visualizar os dados em tempo real:

```bash
python3 -m http.server 8000
```

Acesse em: [http://localhost:8000/painel.html](http://localhost:8000/painel.html)

---

## Aplicações

Este sistema é ideal para ambientes clínicos que exigem controle rigoroso da iluminação para proteger pacientes com fotosensibilidade, tais como:

- Consultórios de oftalmologia e odontologia.
- Clínicas de psicologia.
- Salas de exame e ambientes hospitalares.
- Ambulatórios e clínicas de fisioterapia.

---



- Maria Dornelles – [@Maducdornelles](https://github.com/Maducdornelles)
