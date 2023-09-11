meses = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

entrada = int(input())

# Verificar se a entrada é válida
if entrada in meses:
    mes_em_ingles = meses[entrada]
    print(f"O mês correspondente ao número {entrada} é {mes_em_ingles}.")
else:
    print("Número inválido. Por favor, insira um número de 1 a 12.")