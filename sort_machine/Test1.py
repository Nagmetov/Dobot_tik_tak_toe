import sys
import cv2
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from ultralytics import YOLO
import numpy as np

class DetectionThread(QThread):
    result_ready = pyqtSignal(QImage)

    def __init__(self, frame, model, listb):
        super().__init__()
        self.frame = frame
        self.model = model
        self.listb = listb
        print("DetectionThread initialized")

    def run(self):
        try:
            print("DetectionThread started")
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            results = self.model.predict(cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
            print("Prediction completed")

            detected_objects = results[0].boxes.xyxy.cpu().numpy()
            confidences = results[0].boxes.conf.cpu().numpy()
            labels = results[0].boxes.cls.cpu().numpy()
            print("Detection results processed")

            # Sort detected objects by their x_min coordinate (left to right)
            sorted_objects = sorted(zip(detected_objects, confidences, labels), key=lambda x: x[0][0])

            print('Order of detected classes from left to right:')
            lista = [0, 1, 2, 3, 4]
            listb = self.listb.copy()
            listb = [i-1 for i in listb]
            listc = {}
            k = 0
            for (x_min, y_min, x_max, y_max), conf, label in sorted_objects:
                print(f'Class: {int(label)}, Confidence: {conf:.2f}')
                if label not in listc:
                    k += 1
                    listc[label] = k
                cv2.rectangle(self.frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
                cv2.putText(self.frame, f'{int(label)}: {conf:.2f}', (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (0, 255, 0), 2)
            shlu = []
            for i in range(len(lista)):
                if i in listb:
                    if lista[i] in listc:
                        shlu.append(listc[lista[i]])
                    else:
                        print(f"Warning: Label {lista[i]} not detected in the frame.")

            # Save listc to file
            shlu.append(6)
            print(shlu)
            with open('C:\\Users\\ADMIN\\PycharmProjects\\DOBOT\\sort_machine\\numbers.txt', 'w') as f:
                f.write(', '.join([str(z) for z in shlu]))

            # Convert to QImage to display
            frame_bgr = self.frame.copy()
            height, width, channel = frame_bgr.shape
            step = channel * width
            qImg = QImage(frame_bgr.data, width, height, step, QImage.Format_BGR888)
            self.result_ready.emit(qImg)
            print("DetectionThread finished successfully")
        except Exception as e:
            print(f'Error in DetectionThread: {e}')

class WebcamApp(QWidget):
    def __init__(self):
        super().__init__()

        try:
            self.initUI()
            self.model = YOLO('yeah.pt')
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            print("Frame updated successfully")
            self.cap = cv2.VideoCapture(0)
            print(1)
            self.timer.start(10)  # Update every 10 ms
            print("WebcamApp initialized successfully")
        except Exception as e:
            print(f'Error in WebcamApp initialization: {e}')

    def initUI(self):
        try:
            self.image_label = QLabel(self)
            self.image_label.resize(640, 480)

            self.result_label = QLabel(self)
            self.result_label.resize(640, 480)

            self.input_line = QLineEdit(self)
            self.input_line.setPlaceholderText('Введите числа от 1 до 5 (например, 1 2 3)')

            self.detect_button = QPushButton('Detect', self)
            self.detect_button.clicked.connect(self.detect_objects)

            input_layout = QHBoxLayout()
            input_layout.addWidget(self.input_line)
            input_layout.addWidget(self.detect_button)

            layout = QVBoxLayout()
            layout.addWidget(self.image_label)
            layout.addLayout(input_layout)
            layout.addWidget(self.result_label)
            self.setLayout(layout)

            self.setWindowTitle('Webcam')
            self.setGeometry(100, 100, 1280, 960)
            self.show()
            print("UI initialized successfully")
        except Exception as e:
            print(f'Error in initUI: {e}')

    def update_frame(self):
        try:
            ret, frame = self.cap.read()
            if ret:
                self.current_frame = frame
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame_rgb.shape
                step = channel * width
                qImg = QImage(frame_rgb.data, width, height, step, QImage.Format_RGB888)
                self.image_label.setPixmap(QPixmap.fromImage(qImg))

        except Exception as e:
            print(f'Error in update_frame: {e}')

    def detect_objects(self):
        try:
            if hasattr(self, 'current_frame'):
                input_text = self.input_line.text()
                try:
                    listb = [int(i) for i in input_text.split() if 1 <= int(i) <= 5]
                    if len(listb) > 0:  # Проверяем наличие элементов
                        self.detect_button.setEnabled(False)
                        self.thread = DetectionThread(self.current_frame.copy(), self.model, listb)
                        self.thread.result_ready.connect(self.show_detection_result)
                        self.thread.finished.connect(self.on_thread_finished)
                        self.thread.start()
                        print("Detection started")
                    else:
                        QMessageBox.critical(self, 'Error', 'Invalid input. Please enter numbers between 1 and 5.')
                        self.detect_button.setEnabled(True)
                        print("Invalid input: No valid numbers entered")
                except ValueError:
                    QMessageBox.critical(self, 'Error', 'Invalid input. Please enter numbers between 1 and 5.')
                    self.detect_button.setEnabled(True)
                    print("ValueError in detect_objects: Invalid input")
            else:
                QMessageBox.critical(self, 'Error', 'Failed to capture image from webcam')
                print("No frame captured in detect_objects")
        except Exception as e:
            print(f'Error in detect_objects: {e}')

    def on_thread_finished(self):
        try:
            self.detect_button.setEnabled(True)
            print("Thread finished")
        except Exception as e:
            print(f'Error in on_thread_finished: {e}')

    def show_detection_result(self, qImg):
        try:
            print("Displaying detection result")
            self.result_label.setPixmap(QPixmap.fromImage(qImg))
            print("Detection result displayed")
        except Exception as e:
            print(f'Error in show_detection_result: {e}')

    def closeEvent(self, event):
        try:
            self.cap.release()
            if hasattr(self, 'thread') and self.thread.isRunning():
                self.thread.quit()
                self.thread.wait()
            print("WebcamApp closed successfully")
        except Exception as e:
            print(f'Error in closeEvent: {e}')

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = WebcamApp()
        sys.exit(app.exec_())
    except Exception as e:
        print(f'Error in main: {e}')

