Observações:

O código foi inteiramente desenvolvido em Python 3.10.12


As bibliotecas utilizadas foram
	Numpy 
	Matplotlib
	Scipy


O Visual Studio Code não reconhece arquivos .au, sendo assim é necessário algumas conversões.

	(Caso não haja instalado ffmpeg)

	No Linux, para distros baseadas em Debian, abra o terminal (Ctrl+Alt+T) e digite:
	sudo apt update
	sudo apt install ffmpeg 

	Em seguida, com o projeto aberto no VS Code

	Abra o terminal (Ctrl+Shift+´) e digite:
	ffmpeg -i bluewhale.au.au bluewhale.wav

	Dessa forma, bluewhale.au.au será convertido para .wav



