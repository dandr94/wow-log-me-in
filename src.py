import tkinter as tk
from tkinter.filedialog import askopenfile
import pyautogui as pg
import time
from datetime import datetime
import os


class Application(tk.Tk):
    DIRECTORY_NAME_LABEL: str = 'Dir:'
    TIME_NAME_LABEL: str = 'Time:'
    TABS_NAME_LABEL: str = 'Tabs:'
    TITLE_NAME: str = 'wow Login Schedular'
    BROWSE_BTN_NAME: str = 'Browse'
    LAUNCH_BTN_NAME: str = 'Launch'
    BTN_BG: str = 'yellow'
    SLEEP_TIME: int = 15
    BROWSE_FIELD_TITLE: str = 'Please select your path to your WoW Classic exe'
    HOUR_FIELD_PLACEHOLDER: str = 'H'
    MINUTES_FIELD_PLACEHOLDER: str = 'M'
    DIR_ENTRY_STATE: str = 'disabled'
    JUSTIFY_CONTENT: str = 'center'
    GEOMETRY_SIZE: str = '570x300'
    RESIZABLE: bool = False

    def __init__(self):
        super().__init__(className=self.TITLE_NAME)
        self.browse_label = tk.Label(self, text=self.DIRECTORY_NAME_LABEL, width=10)
        self.time_label = tk.Label(self, text=self.TIME_NAME_LABEL, width=10)
        self.tabs_label = tk.Label(self, text=self.TABS_NAME_LABEL, width=10)
        self.dir_text = tk.StringVar(value=self.BROWSE_FIELD_TITLE)
        self.hour_text = tk.StringVar(value=self.HOUR_FIELD_PLACEHOLDER)
        self.minutes_text = tk.StringVar(value=self.MINUTES_FIELD_PLACEHOLDER)
        self.dir_entry = tk.Entry(self, textvariable=self.dir_text, width=60, state=self.DIR_ENTRY_STATE)
        self.hour_entry = tk.Entry(self, textvariable=self.hour_text, width=5, justify=self.JUSTIFY_CONTENT)
        self.minutes_entry = tk.Entry(self, textvariable=self.minutes_text, width=5, justify=self.JUSTIFY_CONTENT)
        self.tabs_entry = tk.Entry(self, width=5, justify=self.JUSTIFY_CONTENT)
        self.browse_btn = tk.Button(self, text=self.BROWSE_BTN_NAME, width=8, bg=self.BTN_BG,
                                    command=lambda: self.browse())
        self.launch_btn = tk.Button(self, text=self.LAUNCH_BTN_NAME, width=8, bg=self.BTN_BG,
                                    command=lambda: self.launch())

        self.geometry(self.GEOMETRY_SIZE)
        self.resizable(self.RESIZABLE, self.RESIZABLE)

        self.browse_label.grid(row=1, column=1, padx=10, pady=30)
        self.time_label.grid(row=2, column=1, padx=1, pady=30)
        self.tabs_label.grid(row=3, column=1, padx=1, pady=30)

        self.dir_entry.grid(row=1, column=2)

        self.browse_btn.grid(row=1, column=3)

        self.hour_entry.grid(row=2, column=2)

        self.minutes_entry.grid(row=2, column=3)

        self.tabs_entry.grid(row=3, column=2)

        self.launch_btn.grid(row=4, column=2)

    @property
    def get_hour(self) -> str:
        return self.hour_entry.get()

    @property
    def get_minutes(self) -> str:
        return self.minutes_entry.get()

    @property
    def get_tabs(self) -> str:
        return self.tabs_entry.get()

    def _valid_parameters(self, h, m, tabs, path) -> bool:
        if h.isdigit() \
                and m.isdigit() \
                and (0 <= int(h) <= 24) and (0 <= int(m) <= 60) \
                and path != self.BROWSE_FIELD_TITLE \
                and tabs \
                and tabs.isdigit():
            return True

        return False

    def browse(self):
        file = askopenfile(parent=self, mode='rb', title=self.BROWSE_FIELD_TITLE)
        if file:
            file_dir = file.name
            self.dir_text.set(file_dir)

    def launch(self):
        h = self.get_hour
        m = self.get_minutes
        tabs = self.get_tabs
        dir_path = self.dir_text.get()

        if self._valid_parameters(h, m, tabs, dir_path):
            launch_time = f'{h}:{m}'
            while True:
                current_time = datetime.now().strftime('%H:%M')
                if current_time == launch_time:
                    os.startfile(dir_path)
                    time.sleep(self.SLEEP_TIME)
                    pg.press("tab", int(tabs), 0.3)
                    pg.press('space')
                    break
                else:
                    time.sleep(5)


def main():
    app = Application()
    app.mainloop()


if __name__ == '__main__':
    main()
