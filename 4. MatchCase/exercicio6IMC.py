import os
os.system("clear")

print("Calcule seu Índice de Massa Corpóreo(IMC)")
altura_usuario = float(input("\nDigite sua altura em m: " ))
print(f"{altura_usuario} m")
peso_usuario = float(input("Digite seu peso em kg: "))
print(f"{peso_usuario} Kg")
print("""Digite para sexo masculino      Digite para sexo feminino
             M                                 F""")
genero_usuario = input("Digite seu sexo: ").upper()


match genero_usuario:
    case "M"  :
       print("Masculino")
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
      print("Feminino")
      imc_f = (peso_usuario) / (altura_usuario * altura_usuario)
      if imc_f > 18.5 and imc_f < 25:
         print(f"O seu índice de massa corpóreo é {imc_f:.1f} e está no peso ideal.")
      if imc_f > 24.9 and imc_f < 30:
         print(f"O seu índice de massa corpóreo é {imc_f:.1f} e você está com sobrepeso.")
      if imc_f >= 30:
         print(f"O seu índice de massa corpóreo é {imc_f:.1f} e você está obeso.")
      if imc_f <= 18.5:
         print(f"O seu índice de massa corpóreo é {imc_f:.1f} e você está abaixo do peso.")

    case _:
      print("Opção inválida!")
      
      
            
        

