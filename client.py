import socket 
import cv2
import pickle
import struct
import imutils 

camera = True
if camera == True:
	vid = cv2.VideoCapture(0)
else:
	vid = cv2.VideoCapture('videos/mario.mp4')
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = "Server's IP" # Here according to your server ip write the address

port = 9999
client_socket.connect((host_ip,port))

if client_socket: 
	while (vid.isOpened()):
		try:
			img, frame = vid.read()
			frame = imutils.resize(frame,width=380)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			cv2.imshow(f"TO: {host_ip}",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				client_socket.close()
		except:
			print('VIDEO FINISHED!')
			break