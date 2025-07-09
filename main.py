import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from nesting_canvas import NestingCanvas
from dxf_parser import DXFParser

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NestCraft v0.1‑beta")
        self.canvas = NestingCanvas()
        self.setCentralWidget(self.canvas)
        self._create_menu()

    def _create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        imp = QAction("Import DXF", self)
        imp.triggered.connect(self.import_dxf)
        file_menu.addAction(imp)

        exp = QAction("Export Layout (PNG)", self)
        exp.triggered.connect(self.canvas.export_image)
        file_menu.addAction(exp)

    def import_dxf(self):
        fn, _ = QFileDialog.getOpenFileName(self, "Open DXF", "", "DXF Files (*.dxf)")
        if fn:
            parts = DXFParser.load(fn)
            self.canvas.add_parts(parts)

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()# NestCraft-
