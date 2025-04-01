import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout,
    QWidget, QProgressBar, QMessageBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from main import process_file  # Import your main processing function


class FileProcessorThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        try:
            # Simulate progress (replace with actual processing logic)
            for i in range(1, 101):
                self.progress.emit(i)
                self.msleep(20)  # Simulate work

            # Call the process_file function
            process_file(self.file_path, "input_files", "output_files")
            self.finished.emit("Processing complete! Check the output_files directory.")
        except Exception as e:
            self.error.emit(str(e))


class MCQProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MCQ Processor")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Title Label
        self.title_label = QLabel("MCQ Processor", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.title_label)

        # Instruction Label
        self.instruction_label = QLabel("Select a file to process:", self)
        self.instruction_label.setAlignment(Qt.AlignCenter)
        self.instruction_label.setStyleSheet("font-size: 16px; color: #555;")
        self.layout.addWidget(self.instruction_label)

        # Select File Button
        self.select_file_button = QPushButton("Select File", self)
        self.select_file_button.setStyleSheet(
            "background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 5px;"
        )
        self.select_file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_file_button)

        # Progress Bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet(
            "QProgressBar { border: 1px solid #bbb; border-radius: 5px; text-align: center; }"
            "QProgressBar::chunk { background-color: #4CAF50; width: 20px; }"
        )
        self.layout.addWidget(self.progress_bar)

        # Status Label
        self.status_label = QLabel("", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 14px; color: #777;")
        self.layout.addWidget(self.status_label)

    def select_file(self):
        # Open a file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*.*)")
        if file_path:
            self.status_label.setText(f"Processing: {file_path}")
            self.progress_bar.setValue(0)

            # Start the file processing thread
            self.thread = FileProcessorThread(file_path)
            self.thread.progress.connect(self.progress_bar.setValue)
            self.thread.finished.connect(self.on_processing_finished)
            self.thread.error.connect(self.on_processing_error)
            self.thread.start()

    def on_processing_finished(self, message):
        self.status_label.setText(message)
        QMessageBox.information(self, "Success", message)

    def on_processing_error(self, error_message):
        self.status_label.setText("Error occurred!")
        QMessageBox.critical(self, "Error", error_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MCQProcessorApp()
    window.show()
    sys.exit(app.exec_())
