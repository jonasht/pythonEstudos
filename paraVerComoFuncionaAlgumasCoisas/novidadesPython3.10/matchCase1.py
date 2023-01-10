from colorama.ansi import Fore as f
error = ''



match error:
    case '404':
        print(f.RED+'pagina na encontrada'+f.RESET)
    case '401':
        print(f.RED+'acesso nao autorizado'+f.RESET)
    case '500':
        print(f.RED+'erro no servidor'+f.RESET)

    case outra_coisa:
        print(f.GREEN+f'outro valor'+f.RESET)