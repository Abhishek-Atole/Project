import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from main import process_file  # Import your main processing function

class MCQProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MCQ Processor")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create layout
        self.layout = QVBoxLayout()

        # Add a label
        self.label = QLabel("Select a file to process:")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Add a button to select a file
        self.select_file_button = QPushButton("Select File")
        self.select_file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_file_button)

        # Add a label to show the status
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.status_label)

        # Set the layout
        self.central_widget.setLayout(self.layout)

    def select_file(self):
        # Open a file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*.*)")
        if file_path:
            self.status_label.setText(f"Processing: {file_path}")
            QApplication.processEvents()  # Update the GUI immediately

            # Call the process_file function
            try:
                process_file(file_path, "input_files", "output_files")
                self.status_label.setText("Processing complete! Check the output_files directory.")
            except Exception as e:
                self.status_label.setText(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MCQProcessorApp()
    window.show()
    sys.exit(app.exec_())