# Solicitar ao usuário o nome da branch
$nome_da_branch = Read-Host -Prompt "Digite o nome da branch"

# Obter a data e hora atual no formato AAAA-MM-DD-HH-MM
$data_atual = Get-Date -Format "yyyy-MM-dd-HH-mm"

# Criar o nome do diretório de build
$diretorio_build = "build\$nome_da_branch-$data_atual"

# Criar o diretório de build
New-Item -Path $diretorio_build -ItemType Directory

# Copiar os arquivos necessários para o diretório de build
Copy-Item -Path "main.py" -Destination $diretorio_build
Copy-Item -Path "dolar.jpg" -Destination $diretorio_build

# Mudar para o diretório de build
Set-Location -Path $diretorio_build

# Rodar o pyinstaller para gerar o .exe
# Vamos incluir o 'dolar.jpg' como recurso com o parâmetro --add-data
pyinstaller --onefile --add-data "dolar.jpg;." main.py

# Aguardar o processo finalizar
Write-Host "Build concluído. O arquivo .exe foi gerado no diretório 'dist'."