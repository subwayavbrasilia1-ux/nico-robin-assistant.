import sys

# Personalidade da Nico Robin integrada com funções do JARVIS
def responder_robin(comando):
    comando = comando.lower()
    
    if "email" in comando or "mensagens" in comando:
        return "Fufu... Deixe-me examinar suas correspondências recentes. Seria uma conspiração ou apenas correspondência trivial? Vou verificar seus e-mails agora."
    
    elif "abrir" in comando:
        app = comando.replace("abrir", "").strip()
        return f"Desbravando o sistema... Abrindo o aplicativo {app} para você. Não se perca no caminho."
    
    elif "bateria" in comando or "status" in comando:
        return "Analisando os signos vitais deste dispositivo... A energia está estável, capitão."
    
    else:
        return "Compreendido. Vou pesquisar sobre isso nos registros antigos do Século Vazio."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        print(responder_robin(entrada))
