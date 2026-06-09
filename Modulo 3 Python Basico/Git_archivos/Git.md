
Repositorio
Contiene nuestro codigo

Repositorio local
codigo en nuestra maquina

Repositorio remoto
codigo que queremos compartir

Git = gestiona el control de versiones localmente

Github = subir nuestro codigo a la nube y colaborar con otras personas

Gitlab = llevar repositorios remotos a on site. Ambiente laboral


Etapas:
![[Pasted image 20260523203144.png]]


Working directory -> directorio de trabajo

Staging area -> area de preparacion y decirs, estos son los elementos que quiero

Repository -> hacer comit del cosigo


#m es message
git commit -m "First version of the files manipulation"
//historial de cambios
git log

git add -> agregar los archivos que se trabjaron

git commit - m "Mensaje de los cambios agregados"

git push -> para subir a la nube


BRANCHES

Crear nueva rama y cambiar a ella
git checkout -b nueva-rama

cambiar rama:
git checkout nombre de rama

listar branches:
git branch


![[Pasted image 20260523211504.png]]

|   |   |
|---|---|
|`git init`|Inicia un repositorio local.|
|`git status`|Muestra archivos modificados.|
|`git add nombre-archivo`|Agrega archivos al stage.|
|`git commit -m "mensaje"`|Crea un commit con los archivos en el stage.|
|`git checkout -b nombre-rama`|Crea una nueva rama.|
|`git checkout nombre-rama`|Cambia de rama.|
|`git push`|Envía cambios al repositorio remoto.|
|`git pull`|