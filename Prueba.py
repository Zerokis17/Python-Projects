print("Hola, este programa te ayudará a calcular el IMC")
numeroPersonas = int(input("\n¿Cuántas personas vas a calcular? "))

for vc in range(numeroPersonas):
    print(f"\nIngrese los siguientes datos para la persona {vc+1}:")
    nombre = input("Nombre: ")
    apellido = input("Ingrese su apellido: ")
    peso = float(input("Ingrese su peso en kilogramos: "))
    estatura = float(input("Ingrese su estatura en metros: "))

    imc = peso / (estatura ** 2)

    nombre_completo = f"{nombre} {apellido}"
    print(f"Nombres completos: {nombre_completo}")
    print(f"Índice de masa corporal: {imc:.1f}")

    if imc <= 18.5:
        print("Delgado. Toca echarle huevito al arroz.")
    elif 18.5 < imc <= 24.9:
        print("Aceptable. Estás en buena forma.")
    elif 25 <= imc <= 29.9:
        print("Sobrepeso. Quizás deberías cuidar un poco la dieta.")
    elif 30 <= imc <= 34.9:
        print("Obesidad leve. Es un buen momento para revisar tus hábitos alimenticios.")
    elif 35 <= imc <= 39.9:
        print("Obesidad moderada. Recuerda que la salud es lo primero, ¡consulta a un profesional!")
    else:
        print("Obesidad severa. Es crucial buscar orientación médica y establecer un plan de salud.")