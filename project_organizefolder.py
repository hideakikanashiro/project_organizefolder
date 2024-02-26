import os
from tkinter.filedialog import askdirectory

# Passo 1 = Abre uma pop-up e o usuário seleciona uma pasta. O caminho dessa pasta será salvo na variável directory.
directory = askdirectory (title="Please, select one folder.")

# Passo 2 = os.listdir irá mostrar os arquivos que tem dentro do parâmetro passado do Passo 1.
list_files = os.listdir(directory)

# Passo 3 = Aqui foi feito um dicionário, para depois criar uma pasta onde serão jogados os arquivos com cada extensão especificada.
local_drop = {
    "image": [".png", ".jpg", ".jpeg"],
    "pdf": [".pdf"],
    "notas": [".txt"],
    "office": [".xlsx", ".word", ".docx", ".csv"],
    "audio e video": [".mp3" , ".mp4", ".mov", ".mp5"],
    "Adobe": [".psd", ".eps", ".svg", ".ai"]
}

# Passo 4 = Dentro do for com a função os.path.split estamos informando o caminho do diretório + extensão do arquivo. Ele irá percorrer por toda a pasta informando o diretório e os arquivos dentro dele.
for file in list_files:
    name_folder, extension = os.path.splitext (f"{directory}/{file}")
  
    # Passo 5 = Para cada pasta dentro de local_drop, faça.. (OBS: ele irá percorrer somente pelas chaves do dicionário, ou seja, image, pdf, txt, office. Ele não lê os valores dentro)
    for folder in local_drop:
        # Esse if irá criar uma pasta caso ela não exista.
        if extension in local_drop [folder]:
            if not os.path.exists(f"{directory}/{folder}"):
                # Foi criado uma nova pasta.
                os.mkdir(f"{directory}/{folder}")
                # Com a pasta criada, temos que mover o file para dentro desta nova pasta.
            os.rename (f"{directory}/{file}", f"{directory}/{folder}/{file}")