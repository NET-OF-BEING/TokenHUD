#!/usr/bin/env python3
"""
Token Count HUD Widget
Displays live token usage for Claude Code sessions
"""

import tkinter as tk
from tkinter import ttk
import json
import os
from pathlib import Path
import time

class TokenHUD:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Token HUD")

        # Window properties
        self.root.attributes('-topmost', True)  # Always on top
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-alpha', 0.9)  # Slight transparency

        # Position in top-right corner
        screen_width = self.root.winfo_screenwidth()
        window_width = 300
        window_height = 120
        x_position = screen_width - window_width - 20
        y_position = 20
        self.root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

        # Make window draggable
        self.root.bind('<Button-1>', self.start_move)
        self.root.bind('<B1-Motion>', self.on_move)

        # Status file path
        self.status_file = Path.home() / '.claude' / 'token_status.json'
        self.status_file.parent.mkdir(parents=True, exist_ok=True)

        # Initialize with default values
        self.token_data = {
            'used': 0,
            'total': 200000,
            'remaining': 200000,
            'percentage': 100.0
        }

        self.create_widgets()
        self.update_display()
        self.auto_update()

    def create_widgets(self):
        # Main frame with dark theme
        main_frame = tk.Frame(self.root, bg='#1e1e1e', padx=15, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title bar with close button
        title_frame = tk.Frame(main_frame, bg='#1e1e1e')
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(
            title_frame,
            text="Claude Code Tokens",
            font=('Segoe UI', 10, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        )
        title_label.pack(side=tk.LEFT)

        close_btn = tk.Button(
            title_frame,
            text="×",
            command=self.root.quit,
            font=('Segoe UI', 12, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff',
            bd=0,
            padx=5,
            activebackground='#ff0000',
            activeforeground='#ffffff'
        )
        close_btn.pack(side=tk.RIGHT)

        # Separator
        separator = tk.Frame(main_frame, height=1, bg='#3e3e3e')
        separator.pack(fill=tk.X, pady=(5, 10))

        # Token count display
        self.remaining_label = tk.Label(
            main_frame,
            text="0",
            font=('Segoe UI', 24, 'bold'),
            bg='#1e1e1e',
            fg='#4ec9b0'
        )
        self.remaining_label.pack()

        self.subtitle_label = tk.Label(
            main_frame,
            text="tokens remaining",
            font=('Segoe UI', 9),
            bg='#1e1e1e',
            fg='#808080'
        )
        self.subtitle_label.pack()

        # Progress bar
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "Token.Horizontal.TProgressbar",
            troughcolor='#2d2d2d',
            background='#4ec9b0',
            bordercolor='#1e1e1e',
            lightcolor='#4ec9b0',
            darkcolor='#4ec9b0'
        )

        self.progress = ttk.Progressbar(
            main_frame,
            style="Token.Horizontal.TProgressbar",
            length=270,
            mode='determinate'
        )
        self.progress.pack(pady=(10, 5))

        # Usage stats
        self.stats_label = tk.Label(
            main_frame,
            text="0 / 200,000 (100%)",
            font=('Segoe UI', 8),
            bg='#1e1e1e',
            fg='#808080'
        )
        self.stats_label.pack()

    def update_display(self):
        """Update the display with current token data"""
        remaining = self.token_data['remaining']
        used = self.token_data['used']
        total = self.token_data['total']
        percentage = self.token_data['percentage']

        # Update main label with formatted number
        self.remaining_label.config(text=f"{remaining:,}")

        # Update stats label
        self.stats_label.config(text=f"{used:,} / {total:,} ({percentage:.1f}%)")

        # Update progress bar
        self.progress['value'] = percentage

        # Change color based on remaining percentage
        if percentage < 10:
            color = '#ff5555'  # Red
        elif percentage < 25:
            color = '#ffaa00'  # Orange
        else:
            color = '#4ec9b0'  # Teal

        self.remaining_label.config(fg=color)
        style = ttk.Style()
        style.configure("Token.Horizontal.TProgressbar", background=color)

    def load_token_data(self):
        """Load token data from status file"""
        try:
            if self.status_file.exists():
                with open(self.status_file, 'r') as f:
                    data = json.load(f)
                    self.token_data.update(data)
        except Exception as e:
            print(f"Error loading token data: {e}")

    def auto_update(self):
        """Automatically update display every second"""
        self.load_token_data()
        self.update_display()
        self.root.after(1000, self.auto_update)  # Update every 1 second

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def run(self):
        self.root.mainloop()

def main():
    hud = TokenHUD()
    hud.run()

if __name__ == '__main__':
    main()
