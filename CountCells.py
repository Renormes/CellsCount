import pyautogui
import os
import time
import PySimpleGUI as sg
import cv2




layout = [[sg.Text("Comece subindo suas imagens")], [sg.Button("subir imagens")]]


window = sg.Window("Demo", layout)


while True:
    event, values = window.read()
   
    if event == "subir imagens":
       os.startfile("C:/CountCells/images/4x")
       time.sleep(3)
       window.close()
    if event == sg.WIN_CLOSED:  
       exit()
    break   


file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Escolha a imagem de corte clicando em Browse:"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Cortar Imagem"),
        ],
        [
            sg.Text("Assim que terminar de cortar todas as imagens, clique em converter:"),
            sg.Button("Converter e contar imagens cortadas"),
        ],
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == "Cortar Imagem":
            filename = values["-FILE-"]
            os.startfile(filename)
            time.sleep(2)
            pyautogui.hotkey("ctrl", "e")
        if event == "Converter e contar imagens cortadas":
            window.close()
            for dirname in os.listdir("C:/CountCells/images/"):

             for filename in os.listdir("C:/CountCells/images/" + dirname + "/"):
              ft = cv2.imread("C:/CountCells/images/" + dirname + "/" + filename)
              hsv = cv2.cvtColor(ft, cv2.COLOR_BGR2HSV)
              mask1= cv2.inRange(hsv, (0, 40, 0), (20, 255, 200))
              mask2= cv2.inRange(hsv, (160, 40, 0), (180, 255, 200))
              mask = cv2.bitwise_or(mask1, mask2)
              path = 'C:/CountCells/convertImages/conversions'
              cv2.imwrite(os.path.join(path , filename), mask)
            time.sleep(5)
            for dirname in os.listdir("convertImages/"):

             for filename in os.listdir("convertImages/" + dirname + "/"):

        
              img = cv2.imread("convertImages/" + dirname + "/" + filename, 0)
       

              denoisedImg = cv2.fastNlMeansDenoising(img)
        

              kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        

              morphImg = cv2.morphologyEx(denoisedImg, cv2.MORPH_CLOSE, kernel, iterations = 2)
        
        
              contours, hierarchy = cv2.findContours(morphImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        

              contoursImg = cv2.cvtColor(morphImg, cv2.COLOR_GRAY2RGB)
        

              saves = cv2.drawContours(contoursImg, contours, -1, (255,100,0), 3)
              path = 'C:/CountCells/contoursImages'
              cv2.imwrite(os.path.join(path , filename), saves)
              

              cv2.imwrite("results/" + dirname + "/" + filename + "_result.tif", contoursImg)
              textFile = open("results/results.txt","a")
              textFile.write(filename + " Dots number: {}".format(len(contours)) + "\n")
              textFile.close()
              
                     
if __name__ == "__main__":
    main()


