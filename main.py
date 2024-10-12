import flet as ft # Importa a biblioteca Flet

# Função principal
def main(page):
    page_title = ft.Text(value="HashZap") # Título da página

    # Função que inicializa o chat em um tunel de comunicação
    def initialize_chat_channel(message):
        chat.controls.append(ft.Text(value=message)) # Adiciona a mensagem à coluna que armazena as mensagens
        page.update() # Atualiza a página

    page.pubsub.subscribe(initialize_chat_channel) # Cria um tunel de comunicação

    # Função que envia a mensagem
    def send_message(event):
        message = f'{alert_dialog_content.value}: {input_message.value}' # Mensagem que será enviada com o nome do usuário e o texto digitado por ele
        page.pubsub.send_all(message) # Envia a mensagem para todos os usuários conectados ao tunel de comunicação
        input_message.value = "" # Limpa o campo de texto
        page.update() # Atualiza a página

    input_message = ft.TextField(label="Digite sua mensagem:", on_submit=send_message) # Campo de texto para digitar a mensagem

    send_message_button = ft.ElevatedButton(text="Enviar", on_click=send_message) # Botão para enviar a mensagem

    row = ft.Row([input_message, send_message_button]) # Linha com o campo de texto e o botão

    chat = ft.Column([]) # Coluna que armazena as mensagens

    alert_dialog_title = ft.Text(value="Bem-vindo ao HashZap!") # Título do modal
    alert_dialog_content = ft.TextField(label="Digite seu nome:") # Campo de texto do modal

    # Função que entra no chat
    def enter_chat(event):
        alert_dialog.open = False # Fecha o modal
        page.remove(page_title) # Remove o título da página
        page.remove(modal_open_button) # Remove o botão de abrir o modal da página
        page.add(chat) # Adiciona a coluna que armazena as mensagens à página
        page.add(row) # Adiciona a linha com o campo de texto e o botão de enviar mensagem à página
        message = f'{alert_dialog_content.value} entrou no chat.' # Mensagem de entrada do usuário
        page.pubsub.send_all(message)
        page.update() # Atualiza a página

    alert_dialog_button = ft.ElevatedButton(text="Entrar no Chat", on_click=enter_chat) # Botão do modal

    alert_dialog = ft.AlertDialog(title=alert_dialog_title, content=alert_dialog_content, actions=[alert_dialog_button]) # Modal

    # Função que abre o modal
    def open_alert_dialog(event):
        page.overlay.append(alert_dialog) # Adiciona o modal à página
        alert_dialog.open = True # Abre o modal
        page.update() # Atualiza a página

    modal_open_button = ft.ElevatedButton(text="Iniciar Chat", on_click=open_alert_dialog) # Botão que abre o modal

    page.add(page_title) # Adiciona o título à página
    page.add(modal_open_button) # Adiciona o botão à página

ft.app(main) # Executa a aplicação