import tkinter as tk

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
CELL_SIZE = 40
ERASER_SIZE = 30
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 80

class EraserCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        # Set up canvas
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        # Draw grid of blue cells
        self.cells = []
        self.create_grid()

        # Create buttons for drawing and clearing
        self.create_buttons()

        # Set up the eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='red', outline='red')
        self.drawing = False

        # Bind mouse events
        self.canvas.bind("<Motion>", self.move_eraser)
        self.canvas.bind("<Button-1>", self.on_click)

    def create_grid(self):
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")
                self.cells.append(cell)

    def create_buttons(self):
        self.draw_button = tk.Button(self.root, text="Draw", command=self.toggle_drawing)
        self.draw_button.place(x=10, y=CANVAS_HEIGHT - BUTTON_HEIGHT - 10, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.place(x=100, y=CANVAS_HEIGHT - BUTTON_HEIGHT - 10, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    def toggle_drawing(self):
        self.drawing = not self.drawing
        self.draw_button.config(text="Drawing" if self.drawing else "Draw")

    def clear_canvas(self):
        for cell in self.cells:
            self.canvas.itemconfig(cell, fill="blue")

    def move_eraser(self, event):
        if self.drawing:
            return

        mouse_x = event.x
        mouse_y = event.y
        self.canvas.coords(self.eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
        self.erase_cells(mouse_x, mouse_y)

    def on_click(self, event):
        if self.drawing:
            self.draw_cells(event.x, event.y)

    def erase_cells(self, mouse_x, mouse_y):
        # Erase all blue cells that the eraser touches
        overlapping_items = self.canvas.find_overlapping(mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
        for item in overlapping_items:
            if item in self.cells:
                self.canvas.itemconfig(item, fill='white')

    def draw_cells(self, mouse_x, mouse_y):
        # Draw blue cells if the "Draw" mode is active
        col = (mouse_x // CELL_SIZE) * CELL_SIZE
        row = (mouse_y // CELL_SIZE) * CELL_SIZE
        self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue')

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserCanvasApp(root)
    root.mainloop()
