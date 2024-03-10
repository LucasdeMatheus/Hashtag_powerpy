# tittle 
# botão de iniciar chat
    # popup
        # "Bem, vindo ao hashzap"
        # "seu nomer input"
        # entrar no chat
# chat
    # campo para digitar
    # enviar
# import framework
import flet as ft

# função principal
def main(pagina):
    texto = ft.Text("zapzap")


    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(f"{nome_usuario.value}: {mensagem}")
        chat.controls.append(texto_mensagem)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    # função de enviar mensagem
    def enviar_mensagem(evento):
        pagina.pubsub.send_all(campo_mensagem.value)
        
        
        campo_mensagem.value = ""

        pagina.update()
    
    # escreve e enviar a mensagem
    campo_mensagem = ft.TextField(label="ESCREVA AQUI TA AKAJHAHAHAHHAHA")
    botao_enviar = ft.ElevatedButton("enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    # função para iniciar chat
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botão_iniciar)
        pagina.remove(texto)
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.add(linha_enviar)
        pagina.update()

    # popup para o nome do usuario
    titulo_popup = ft.Text("Bem vindo ao ZAP HAHAAHHAHA")
    nome_usuario = ft.TextField(label="Escreva seu nome caba")
    botao_entrar = ft.ElevatedButton("Entrar", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False, 
        modal=True,title= titulo_popup, 
        content=nome_usuario,
        actions=[botao_entrar])

    # função para abrir o popup
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    # botão para iniciar
    botão_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    pagina.add(texto)
    pagina.add(botão_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)