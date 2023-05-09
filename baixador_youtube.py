import pytube
import pyinputplus as pyip

# URL do vídeo do YouTube
url = pyip.inputStr("Digite a URL do vídeo do YouTube: ")

# Cria uma instância do objeto YouTube
yt = pytube.YouTube(url)

# Mostra as opções de formato disponíveis para o usuário
print("Selecione o formato de arquivo que deseja baixar:")
print("[1] MP3 (somente áudio)")
print("[2] MP4 (vídeo com áudio)")

# Obtem a escolha do usuário
format_choice = pyip.inputInt("Opção: ", min=1, max=2)

# Seleciona o stream de áudio e o stream de maior resolução para download, de acordo com a escolha do usuário
if format_choice == 1:
    stream = yt.streams.filter(only_audio=True).first()
    file_extension = "mp3"
else:
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    file_extension = "mp4"

# Faz o download do arquivo
file_name = f"{yt.title}.{file_extension}"
stream.download(filename=file_name)

# Mostra a mensagem de conclusão do download
print(f"\nArquivo {file_name} baixado com sucesso!")

