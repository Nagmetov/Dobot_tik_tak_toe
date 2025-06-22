import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt5.QtCore import QTimer, Qt, QRect
from ultralytics import YOLO
import random

class DetectionWindow(QWidget):
    def __init__(self, detected_image, parent_size):
        super().__init__()

        self.detected_label = QLabel(self)
        self.detected_image = cv2.resize(detected_image, (parent_size.width(), parent_size.height()))
        self.update_pixmap()

        vbox = QVBoxLayout()
        vbox.addWidget(self.detected_label)
        self.setLayout(vbox)

        self.setWindowTitle('Detection Result')
        self.resize(parent_size.width(), parent_size.height())
        self.show()

    def update_pixmap(self):
        height, width, channel = self.detected_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(self.detected_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.detected_label.setPixmap(pixmap)

class TicTacToeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.cap = cv2.VideoCapture(0)
        self.image_label = QLabel(self)
        self.detect_button = QPushButton('Detect', self)
        self.detect_button.clicked.connect(self.detect_objects)

        self.easy_button = QPushButton('Easy', self)
        self.easy_button.clicked.connect(lambda: self.set_difficulty('easy'))
        self.medium_button = QPushButton('Medium', self)
        self.medium_button.clicked.connect(lambda: self.set_difficulty('medium'))
        self.hard_button = QPushButton('Hard', self)
        self.hard_button.clicked.connect(lambda: self.set_difficulty('hard'))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)

        hbox = QHBoxLayout()
        hbox.addWidget(self.easy_button)
        hbox.addWidget(self.medium_button)
        hbox.addWidget(self.hard_button)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.image_label)
        self.vbox.addWidget(self.detect_button)
        self.vbox.addLayout(hbox)

        self.setLayout(self.vbox)
        self.setWindowTitle('Tic Tac Toe Robot')
        self.setGeometry(100, 100, 800, 600)
        self.show()

        self.points = []
        self.selected = False
        self.grid_image = None
        self.model = YOLO('best.pt')
        self.difficulty = 'easy'

    def set_difficulty(self, level):
        self.difficulty = level
        print(f'Selected difficulty: {level}')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and len(self.points) < 2:
            self.points.append((event.x(), event.y()))
            if len(self.points) == 2:
                self.selected = True
                self.initialize_game_area()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if len(self.points) > 0:
            painter = QPainter(self)
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            painter.setPen(pen)
            for point in self.points:
                painter.drawEllipse(point[0], point[1], 5, 5)
            if len(self.points) == 2:
                rect = QRect(self.points[0][0], self.points[0][1], self.points[1][0] - self.points[0][0],
                             self.points[1][1] - self.points[0][1])
                painter.drawRect(rect)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            converted_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(converted_image)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.IgnoreAspectRatio))

            if self.selected:
                x1, y1 = self.points[0]
                x2, y2 = self.points[1]

                label_width = self.image_label.width()
                label_height = self.image_label.height()

                scaled_x1 = int(x1 * frame.shape[1] / label_width)
                scaled_y1 = int(y1 * frame.shape[0] / label_height)
                scaled_x2 = int(x2 * frame.shape[1] / label_width)
                scaled_y2 = int(y2 * frame.shape[0] / label_height)

                scaled_x1, scaled_x2 = sorted([scaled_x1, scaled_x2])
                scaled_y1, scaled_y2 = sorted([scaled_y1, scaled_y2])

                scaled_x1 = min(max(scaled_x1, 0), frame.shape[1] - 1)
                scaled_y1 = min(max(scaled_y1, 0), frame.shape[0] - 1)
                scaled_x2 = min(max(scaled_x2, 0), frame.shape[1] - 1)
                scaled_y2 = min(max(scaled_y2, 0), frame.shape[0] - 1)

                roi = frame_rgb[scaled_y1:scaled_y2, scaled_x1:scaled_x2]

                overlay = frame_rgb.copy()
                overlay[scaled_y1:scaled_y2, scaled_x1:scaled_x2] = cv2.addWeighted(
                    self.grid_image[scaled_y1:scaled_y2, scaled_x1:scaled_x2], 0.5, roi, 0.5, 0)
                h, w, ch = overlay.shape
                bytes_per_line = ch * w
                converted_image = QImage(overlay.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.image_label.setPixmap(
                    QPixmap.fromImage(converted_image).scaled(self.image_label.size(), Qt.IgnoreAspectRatio))

    def initialize_game_area(self):
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]

        ret, frame = self.cap.read()
        if not ret:
            print("Unable to capture frame from camera")
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.grid_image = np.zeros_like(frame_rgb)

        label_width = self.image_label.width()
        label_height = self.image_label.height()

        scaled_x1 = int(x1 * frame.shape[1] / label_width)
        scaled_y1 = int(y1 * frame.shape[0] / label_height)
        scaled_x2 = int(x2 * frame.shape[1] / label_width)
        scaled_y2 = int(y2 * frame.shape[0] / label_height)

        scaled_x1, scaled_x2 = sorted([scaled_x1, scaled_x2])
        scaled_y1, scaled_y2 = sorted([scaled_y1, scaled_y2])

        w, h = scaled_x2 - scaled_x1, scaled_y2 - scaled_y1

        scaled_x1 = min(max(scaled_x1, 0), frame.shape[1] - 1)
        scaled_y1 = min(max(scaled_y1, 0), frame.shape[0] - 1)
        w = min(w, frame.shape[1] - scaled_x1)
        h = min(h, frame.shape[0] - scaled_y1)

        for i in range(1, 3):
            cv2.line(self.grid_image, (scaled_x1 + i * w // 3, scaled_y1), (scaled_x1 + i * w // 3, scaled_y1 + h),
                     (255, 255, 255), 2)

        for i in range(1, 3):
            cv2.line(self.grid_image, (scaled_x1, scaled_y1 + i * h // 3), (scaled_x1 + w, scaled_y1 + i * h // 3),
                     (255, 255, 255), 2)

    def detect_objects(self):
        ret, frame = self.cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            if self.selected:
                x1, y1 = self.points[0]
                x2, y2 = self.points[1]

                label_width = self.image_label.width()
                label_height = self.image_label.height()

                scaled_x1 = int(x1 * frame.shape[1] / label_width)
                scaled_y1 = int(y1 * frame.shape[0] / label_height)
                scaled_x2 = int(x2 * frame.shape[1] / label_width)
                scaled_y2 = int(y2 * frame.shape[0] / label_height)

                scaled_x1, scaled_x2 = sorted([scaled_x1, scaled_x2])
                scaled_y1, scaled_y2 = sorted([scaled_y1, scaled_y2])

                scaled_x1 = min(max(scaled_x1, 0), frame.shape[1] - 1)
                scaled_y1 = min(max(scaled_y1, 0), frame.shape[0] - 1)
                scaled_x2 = min(max(scaled_x2, 0), frame.shape[1] - 1)
                scaled_y2 = min(max(scaled_y2, 0), frame.shape[0] - 1)

                roi = frame_rgb[scaled_y1:scaled_y2, scaled_x1:scaled_x2]

                results = self.model.predict(cv2.cvtColor(roi, cv2.COLOR_RGB2BGR))

                detected_objects = results[0].boxes.xyxy.cpu().numpy()
                confidences = results[0].boxes.conf.cpu().numpy()
                labels = results[0].boxes.cls.cpu().numpy()

                grid_matrix = [[0 for _ in range(3)] for _ in range(3)]
                cell_width = roi.shape[1] // 3
                cell_height = roi.shape[0] // 3

                for (x_min, y_min, x_max, y_max), conf, label in zip(detected_objects, confidences, labels):
                    cv2.rectangle(roi, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
                    cv2.putText(roi, f'{conf:.2f}', (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                (0, 255, 0), 2)

                    cell_x = int((x_min + x_max) / 2) // cell_width
                    cell_y = int((y_min + y_max) / 2) // cell_height

                    if label == 0:
                        grid_matrix[cell_y][cell_x] = 2
                    elif label == 1:
                        grid_matrix[cell_y][cell_x] = 1

                print("Grid Matrix:")
                for row in grid_matrix:
                    print(row)

                winner = check_winner(grid_matrix)
                if winner:
                    if winner == 2:
                        print("Победа кружка!")
                        f = open('step.txt', 'w+')
                        f.write('10')
                    else:
                        print("Победа квадрата!")
                        f = open('step.txt', 'w+')
                        f.write('11')
                elif all([cell != 0 for row in grid_matrix for cell in row]):
                    print("Ничья!")
                    f = open('step.txt', 'w+')
                    f.write('0')
                else:
                    next_step = self.next_move(grid_matrix)
                    if next_step:

                        i, j = next_step
                        print(f"Следующий ход: строка {i+1}, столбец {j+1}")

                        f = open('step.txt', 'w+')
                        f.write(str((i * 3) + j + 1))
                        f = open('step.txt', 'r')
                        print(f.read())
                    else:
                        print("Нет возможных ходов.")

                self.detection_window = DetectionWindow(roi, self.image_label.size())
                self.detection_window.show()  # Добавляем вызов show()

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

    def next_move(self, matrix):
        if self.difficulty == 'easy':
            return self.random_move(matrix)
        elif self.difficulty == 'medium':
            return self.medium_move(matrix)
        elif self.difficulty == 'hard':
            return self.minimax_move(matrix)

    def random_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
        return random.choice(empty_cells) if empty_cells else None

    def medium_move(self, board):
        for player in [1, 2]:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = player
                        if check_winner(board) == player:
                            board[i][j] = 0
                            return (i, j)
                        board[i][j] = 0
        return self.random_move(board)

    def minimax_move(self, board):
        def minimax(board, depth, is_maximizing):
            winner = check_winner(board)
            if winner == 1:
                return 10 - depth
            if winner == 2:
                return depth - 10
            if all([board[i][j] != 0 for i in range(3) for j in range(3)]):
                return 0

            if is_maximizing:
                best_score = -float('inf')
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 1
                            score = minimax(board, depth + 1, False)
                            board[i][j] = 0
                            best_score = max(score, best_score)
                return best_score
            else:
                best_score = float('inf')
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 2
                            score = minimax(board, depth + 1, True)
                            board[i][j] = 0
                            best_score = min(score, best_score)
                return best_score

        def can_fork(board, player):
            fork_count = 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = player
                        if check_winner(board) == player:
                            fork_count += 1
                        board[i][j] = 0
            return fork_count > 1

        # Prioritize center if it's free
        if board[1][1] == 0:
            return (1, 1)

        # Check for forks and block them
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    if can_fork(board, 2):
                        board[i][j] = 0
                        return (i, j)
                    board[i][j] = 0

        best_move = None
        best_score = -float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    move_score = minimax(board, 0, False)
                    board[i][j] = 0
                    if move_score > best_score:
                        best_score = move_score
                        best_move = (i, j)

        return best_move


def check_winner(board):
    for i in range(3):
        if all([board[i][j] == 1 for j in range(3)]) or all([board[j][i] == 1 for j in range(3)]):
            return 1
        if all([board[i][j] == 2 for j in range(3)]) or all([board[j][i] == 2 for j in range(3)]):
            return 2
    if all([board[i][i] == 1 for i in range(3)]) or all([board[i][2-i] == 1 for i in range(3)]):
        return 1
    if all([board[i][i] == 2 for i in range(3)]) or all([board[i][2-i] == 2 for i in range(3)]):
        return 2
    return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToeApp()
    sys.exit(app.exec_())
