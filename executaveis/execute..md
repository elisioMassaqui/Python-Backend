Aplicativos e Utilitários do Sistema no Windows
Bloco de Notas (Notepad)

Nome de Execução: notepad.exe
Calculadora

Nome de Execução: calc.exe
Microsoft Word

Nome de Execução: "C:\\Program Files\\Microsoft Office\\root\\OfficeXX\\WINWORD.EXE" (o caminho pode variar com base na versão do Office)
Explorador de Arquivos (Windows Explorer)

Nome de Execução: explorer.exe
Paint

Nome de Execução: mspaint.exe
Prompt de Comando

Nome de Execução: cmd.exe
PowerShell

Nome de Execução: powershell.exe
Gerenciador de Tarefas

Nome de Execução: taskmgr.exe
Editor de Registro

Nome de Execução: regedit.exe
Configurações do Windows

Nome de Execução: ms-settings:
Painel de Controle

Nome de Execução: control.exe
Internet Explorer

Nome de Execução: iexplore.exe
Microsoft Edge

Nome de Execução: msedge.exe (ou microsoft-edge: para abrir uma URL no Edge)
Gerenciador de Dispositivos

Nome de Execução: devmgmt.msc
Ferramenta de Diagnóstico de Desempenho

Nome de Execução: perfmon.exe
Editor de Texto do Windows

Nome de Execução: write.exe (em algumas versões do Windows, o Bloco de Notas também pode ser usado para este propósito)
Aplicativos do Microsoft Store

Nome de Execução: Variável, normalmente usando start ms-windows-store: ou comandos específicos baseados na aplicação
Executando Aplicativos com subprocess
Aqui estão exemplos de como você pode usar o módulo subprocess para abrir alguns desses aplicativos:

python
Copiar código
import subprocess

# Abrir o Bloco de Notas
subprocess.Popen(['notepad.exe'])

# Abrir a Calculadora
subprocess.Popen(['calc.exe'])

# Abrir o Gerenciador de Tarefas
subprocess.Popen(['taskmgr.exe'])

# Abrir o Editor de Registro
subprocess.Popen(['regedit.exe'])
Observações
Caminho de Execução: Para alguns aplicativos, pode ser necessário fornecer o caminho absoluto do executável, especialmente se não estiver no PATH do sistema.
Permissões: Certifique-se de ter as permissões necessárias para iniciar esses aplicativos.
Variabilidade: O nome de execução pode variar dependendo da versão do Windows e das configurações do sistema.
Se precisar de mais detalhes ou tiver outras perguntas, estou aqui para ajudar!