# Telematica-Lab2
## Autor: Catalina López Roldán
## Descripción
En este laboratorio se puede evidenciar el manejo del protocolo HTTP y de arquitectura cliente/servidor por medio de un chat grupal, donde dos clientes o mas se van a poder comunicar siempre y cuando el servidor este corriendo. 
Se puede evidenciar el uso de algunos métodos del protocolo como lo son el GET(Traer información) y el POST(Enviar inforación), ademas del los codigos de estado las transacciones realizadas durante el envio de mensajes.

## Instalación
Se debe instanciar tres o mas instancias EC2 en AWS, una de esta sera el servidor y las otras los clientes que se van a comunicar en el chat grupal. 
Estas instancias deben tener dos grupos de seguridad (SG) diferentes, el SG del Servidor debe tener el puerto seleccionado para TCP (ej. 3550), abierto para cualquir IP. Por otro lado el puesto TCP del SG de los clientes, que va con el mismo numero, debe estar solo abierto para la IP publica del Servidor. Hay que tener en cuenta que la instancia del Servidor debe llevar una IP elastica asociada.

Todas las instancias deben contra con python 3, ademas de git y un edito de texto de preferencia, se pueden instalar con los siguientes comandos:
<pre><code> $ sudo yum install git
 $ sudo yum install emacs 
 $ sudo yum install python3
</code></pre>

Ademas se debe installar la biblioteca de requests con el siguiente comando:
<pre><code> $ python3 -m pip install requests
</code></pre>

## Ejecución
Para ejecutar el programa se debe acceder a las instancias por medio de ssh y clonar el repositorio.
Luego de verificar esto se debe correr en la instancia servidor el archivo Server.py de la siguiente manera:
<pre><code> $ python3 Server.py 0.0.0.0 [PUERTO]
</code></pre>
Luego de tener el servidor corriendo se puede poner a correr los clientes que se desee de la siente manera:
<pre><code> $ python3 Client1.py [PUBLIC_IP_SERVER] [PUERTO]
</code></pre>
PUBLIC_IP_SERVER: La IP publica de la instancia que funciona como servidor. <br />
PUERTO: El puerto previamente seleccionado y abierto para TCP.

## Referencias
- https://gist.github.com/junian/99e402db918cbe150002dc8c6736feb6
- https://github.com/Shiroke-013/TET_LABS/blob/b29a91ebc31742a55285cf6fb8bf536a5241b9bb/Lab2/Chat_Server.py (threading)
- https://www.geeksforgeeks.org/http-request-methods-python-requests/
- https://www.codegrepper.com/code-examples/python/python+get+public+ip+address
