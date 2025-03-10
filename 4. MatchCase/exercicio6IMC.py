import os
os.system("clear")

print("Calcule seu Índice de Massa Corpóreo(IMC)")
altura_usuario = float(input("\nDigite sua altura em m: " ))
print(f"{altura_usuario} m")
print("""Digite para sexo masculino      Digite para sexo feminino
             M                                 F""")
genero_usuario = input("Digite seu sexo: ").upper()


match genero_usuario:
    case "M" | "m" :
       print("Masculino")
       peso_ideal = (72.7 * (altura_usuario) -58)
       print(f"O peso ideal para homens de {altura_usuario} m é  {peso_ideal:.1f} kg ")


    case "F" | "f":
      print("Feminino ")
      peso_ideal = (62.1 * (altura_usuario) - 44.7)
      print(f"O peso ideal para mulheres de {altura_usuario} m é {peso_ideal:.1f} kg ")
      

    case _:
      print("Opção inválida!")
      
      
            
        

