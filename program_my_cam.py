#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


def show_webcam(mirror=False):
    # conecta na sua câmera
    cam = cv2.VideoCapture(0)    # câmera id = 0
    while True:
        ret, img = cam.read()
        if ret is False:
            break  # não conseguiu abrir, portanto sai
        if mirror:
            # muitas câmeras leem a imagem espelhada
            # assim se ativar mirror = True
            # fazemos o cv espelhar a imagem
            # mostrando da forma correta
            img = cv2.flip(img, 1)
        cv2.imshow('minha webcam no python', img)
        if cv2.waitKey(1) == 27:
            break    # esc to quit
    cv2.destroyAllWindows()


show_webcam(mirror=True)
