O Claude que fez o README.md da API Calculadora. Estava com preguiça

# 🧮 API Calculadora

API REST simples que recebe dois números e um tipo de operação, retornando o resultado em JSON.

---
O servidor estará disponível em: `http://localhost:6969

( ͡° ͜ʖ ͡°)`

---

## 📌 Endpoints

### `GET /`
Mensagem de boas-vindas da API.

**Resposta:**
```json
{
  "mensagem": "API Calculadora - Acesse /calcular via POST ou /operacoes via GET."
}
```

---

### `GET /operacoes`
Lista todas as operações disponíveis.

**Resposta:**
```json
{
  "operacoes_disponiveis": ["soma", "subtracao", "multiplicacao", "divisao"]
}
```

---

### `POST /calcular`
Realiza o cálculo entre dois números.

**Content-Type:** `application/json`

#### Corpo da requisição

| Campo      | Tipo   | Obrigatório | Descrição                                          |
|------------|--------|-------------|-----------------------------------------------------|
| `num1`     | number | ✅ Sim      | Primeiro número                                     |
| `num2`     | number | ✅ Sim      | Segundo número                                      |
| `operacao` | string | ✅ Sim      | Tipo de operação: `soma`, `subtracao`, `multiplicacao`, `divisao` |

#### Exemplos de requisição

**Soma:**
```json
{
  "num1": 10,
  "num2": 5,
  "operacao": "soma"
}
```

**Subtração:**
```json
{
  "num1": 10,
  "num2": 5,
  "operacao": "subtracao"
}
```

**Multiplicação:**
```json
{
  "num1": 10,
  "num2": 5,
  "operacao": "multiplicacao"
}
```

**Divisão:**
```json
{
  "num1": 10,
  "num2": 5,
  "operacao": "divisao"
}
```

---

#### Resposta de sucesso (`200 OK`)

```json
{
  "sucesso": true,
  "num1": 10.0,
  "num2": 5.0,
  "operacao": "soma",
  "resultado": 15.0
}
```

#### Respostas de erro

**Campo ausente (`400 Bad Request`):**
```json
{
  "sucesso": false,
  "erro": "Campo obrigatório ausente: 'num1'"
}
```

**Operação inválida (`400 Bad Request`):**
```json
{
  "sucesso": false,
  "erro": "Operação inválida. Use: soma, subtracao, multiplicacao, divisao"
}
```

**Divisão por zero (`400 Bad Request`):**
```json
{
  "sucesso": false,
  "erro": "Divisão por zero não é permitida."
}
```

**Tipo inválido (`400 Bad Request`):**
```json
{
  "sucesso": false,
  "erro": "Os campos 'num1' e 'num2' devem ser números."
}
```

---

## 🛠️ Testando com cURL

```bash
# Soma
curl -X POST http://localhost:5000/calcular \
  -H "Content-Type: application/json" \
  -d '{"num1": 10, "num2": 5, "operacao": "soma"}'

# Divisão
curl -X POST http://localhost:5000/calcular \
  -H "Content-Type: application/json" \
  -d '{"num1": 10, "num2": 2, "operacao": "divisao"}'
```

---

## 🗂️ Estrutura do projeto

```
.
├── app.py       # Código principal da API
└── README.md    # Documentação
```

---

## 📋 Operações suportadas

| Operação        | Campo na requisição | Exemplo (10 e 5) | Resultado |
|-----------------|---------------------|------------------|-----------|
| Soma            | `soma`              | 10 + 5           | 15        |
| Subtração       | `subtracao`         | 10 - 5           | 5         |
| Multiplicação   | `multiplicacao`     | 10 × 5           | 50        |
| Divisão         | `divisao`           | 10 ÷ 5           | 2         |
