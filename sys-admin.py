#importamos el sistemas de archivos y os de linux
import os 
#importamos los subprocesos
import subprocess

#aqui mandamos a llamar la funcion system y le pasamos el comando ls
os.system("ls")

subprocess.run(["ls", "-l"])

subprocess.run(["ls","-l","README.md"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])