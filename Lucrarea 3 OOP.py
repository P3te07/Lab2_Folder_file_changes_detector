import os
from datetime import datetime
import threading
import time
import json

class File:
    def __init__(self, folder):
        self.folder = folder
        self.snapshot = set()
        self.snapshot_file = os.path.join(folder, "snapshot.json")
        self.load_snapshot()
        self.snapshot_time = None
        self.update_event = threading.Event()
        self.update_thread = threading.Thread(target=self.update_snapshot, daemon=True)

    def load_snapshot(self):
        if os.path.exists(self.snapshot_file):
            with open(self.snapshot_file, "r") as f:
                self.snapshot = set(json.load(f))

    def save_snapshot(self):
        with open(self.snapshot_file, "w") as f:
            json.dump(list(self.snapshot), f)

    def update_snapshot(self):
        while not self.update_event.is_set():
            current_files = set(os.listdir(self.folder))
            new_files = current_files - self.snapshot
            deleted_files = self.snapshot - current_files
            if new_files or deleted_files:
                print("Changes detected at", datetime.now())
                if new_files:
                    print("New files added:", new_files)
                if deleted_files:
                    print("Files deleted:", deleted_files)
                
                save_thread = threading.Thread(target=self.save_snapshot)
                save_thread.start()
                
            self.snapshot = current_files
            time.sleep(5) 

    def start_update_thread(self):
        self.update_thread.start()

    def stop_update_thread(self):
        self.update_event.set()
        self.update_thread.join()

    def update(self):
        update_thread = threading.Thread(target=self.update_snapshot)
        update_thread.start()
        print("Manual update initiated.")

class Info(File):
    def list_files_and_changes(self):
        files = os.listdir(self.folder)
        for file in files:
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                print(f"File: {file},\t\t Size: {file_size} bytes")

class Status(File):
    def check_status(self):
        if self.snapshot_time:
            print("Snapshot Time:", self.snapshot_time)
        else:
            print("Snapshot has not been updated.")
        
        files = os.listdir(self.folder)
        for file in files:
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path):
                last_modified_time = os.path.getmtime(file_path)
                last_modified_time_str = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                print(f"File: {file},\t\t Last Modified Time: {last_modified_time_str}")

folder_path = r"C:\Users\Admin\Desktop\TOTALLY_NOT_GTA6_Leaks"
info = Info(folder_path)
status = Status(folder_path)
update = File(folder_path)
update.start_update_thread()

while True:
    action = input("Enter the action you want to perform: Update / Info / Status (or type 'exit' to quit): ").lower()
    if action == "update":
        update.update()
    elif action == "info":
        info.list_files_and_changes()
    elif action == "status":
        status.check_status()
    elif action == "exit":
        print("Exiting the program...")
        update.stop_update_thread()
        break
    else:
        print("Invalid action. Please try again.")
