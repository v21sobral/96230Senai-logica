import os
os.system("clear")

print("Calcule seu Índice de Massa Corpóreo(IMC)")
altura_usuario = float(input("Digite sua altura em cm: " ))
peso_usuario = float(input("Digite seu peso em kg: "))
print("""Digite para sexo masculino      Digite para sexo feminino
             M                                 F""")
genero_usuario = input("Digite seu sexo: ").upper()
print(genero_usuario)

match genero_usuario:
    case "M":
       imc_m = (peso_usuario) / (altura_usuario * altura_usuario)
       if imc_m > 18.4 and imc_m < 25:
          print(f"O seu índice de massa corpóreo é {imc_m:.1f} e está no peso ideal.")
       if imc_m > 25 and imc_m < 30:
          print(f"O seu índice de massa corpóreo é {imc_m:.1f} e você está com sobrepeso.")
       if imc_m >= 30:
          print(f"O seu índice de massa corpóreo é {imc_m:.1f} e você está obeso.")
       if imc_m <= 18.4:
          print(f"O seu índice de massa corpóreo é {imc_m:.1f} e você está abaixo do peso.")

    case "F":
      imc_m = (peso_usuario) / (altura_usuario * altura_usuario)
      if imc_m > 18.5 and imc_m < 25:
         print(f"O seu índice de massa corpóreo é {imc_m:.1f} e está no peso ideal.")
      if imc_m > 24.9 and imc_m < 30:
         print(f"O seu índice de massa corpóreo é {imc_m:.1f} e você está com sobrepeso.")
      if imc_m >= 30:
         print(f"O seu índice de massa corpóreo é {imc_m:.1f} e você está obeso.")
      if imc_m <= 18.5:
         print(f"O seu índice de massa corpóreo é {imc_m:.1f} e você está abaixo do peso.")

    case _:
      print("Opção inválida!")
      
            
        

