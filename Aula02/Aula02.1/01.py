letra = input("escolha uma letra")

match letra.lower:
    case "a"|"e"|"i"|"o"|"u":
        print(f"A letra {letra} é uma vogal")
    case _:
        print(f"A letra {letra} sera um consoante")