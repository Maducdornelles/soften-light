const int pinoBotao = 6;
const int pinoLDR = A0;
const int pinoLedVerde = 7;
const int pinoLedVermelho = 8;
const int pinoBuzzer = 9;

bool sistemaAtivo = false;
int valorLDR = 0;
const int limiteLuz = 600;

unsigned long tempoAnterior = 0;
const unsigned long intervaloLeitura = 500;

bool estadoBotaoAnterior = HIGH;

void setup() {
  pinMode(pinoBotao, INPUT_PULLUP);
  pinMode(pinoLedVerde, OUTPUT);
  pinMode(pinoLedVermelho, OUTPUT);
  pinMode(pinoBuzzer, OUTPUT);

  digitalWrite(pinoLedVerde, LOW);
  digitalWrite(pinoLedVermelho, LOW);
  digitalWrite(pinoBuzzer, LOW);

  Serial.begin(9600);
}

void loop() {
  bool estadoBotaoAtual = digitalRead(pinoBotao);

  if (estadoBotaoAnterior == HIGH && estadoBotaoAtual == LOW) {
    sistemaAtivo = !sistemaAtivo;
    if (!sistemaAtivo) {
      digitalWrite(pinoLedVerde, LOW);
      digitalWrite(pinoLedVermelho, LOW);
      digitalWrite(pinoBuzzer, LOW);
    }
    delay(200);
  }

  estadoBotaoAnterior = estadoBotaoAtual;

  if (sistemaAtivo) {
    unsigned long tempoAtual = millis();

    if (tempoAtual - tempoAnterior >= intervaloLeitura) {
      tempoAnterior = tempoAtual;

      valorLDR = analogRead(pinoLDR);

      if (valorLDR > limiteLuz) {
        digitalWrite(pinoLedVerde, LOW);
        digitalWrite(pinoLedVermelho, HIGH);
        digitalWrite(pinoBuzzer, HIGH);
        Serial.println("ALERTA");
      } else {
        digitalWrite(pinoLedVerde, HIGH);
        digitalWrite(pinoLedVermelho, LOW);
        digitalWrite(pinoBuzzer, LOW);
        Serial.println("OK");
      }
    }
  }
}
