from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular(num1: float, num2: float, operacao: str) -> tuple:
    operacoes = {
        "soma": lambda a, b: a + b,
        "subtracao": lambda a, b: a - b,
        "multiplicacao": lambda a, b: a * b,
        "divisao": lambda a, b: a / b
    }

    if operacao not in operacoes:
        return None, f"Operação inválida. Use: {', '.join(operacoes.keys())}"

    if operacao == "divisao" and num2 == 0:
        return None, "Divisão por zero não é permitida."

    resultado = operacoes[operacao](num1, num2)
    return resultado, None

@app.route("/calcular", methods=["POST"])
def calcular_route():
    # JSON não serve para tudo kkkkk
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"sucesso": False, "erro": "O corpo da requisição deve ser um JSON válido."}), 400

    # Validação de campos ausentes
    campos_obrigatorios = ["num1", "num2", "operacao"]
    campos_ausentes = [campo for campo in campos_obrigatorios if campo not in dados]

    if campos_ausentes:
        return jsonify({
            "sucesso": False,
            "erro": f"Campos obrigatórios ausentes: {', '.join(campos_ausentes)}"
        }), 400

    # Validação dos tipos
    try:
        num1 = float(dados["num1"])
        num2 = float(dados["num2"])
    except (ValueError, TypeError):
        return jsonify({"sucesso": False, "erro": "Os campos 'num1' e 'num2' devem ser números."}), 400

    operacao = str(dados["operacao"]).lower().strip()
    resultado, erro = calcular(num1, num2, operacao)

    if erro:
        return jsonify({"sucesso": False, "erro": erro}), 400

    return jsonify({
        "sucesso": True,
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado
    }), 200

@app.route("/operacoes", methods=["GET"])
def listar_operacoes():
    return jsonify({"operacoes_disponiveis": ["soma", "subtracao", "multiplicacao", "divisao"]}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API Calculadora - Acesse /calcular via POST ou /operacoes via GET."}), 200

if __name__ == "__main__":
    app.run(debug=True, port=6969) # ( ͡° ͜ʖ ͡°)
