import os
import subprocess

# List of your source files
source_files = [
    'action_panel_ui.py',
    'chat_view_ui.py',
    'creatures_view_ui.py',
    'items_view_ui.py',
    'map_view_ui.py',
    'music_player_ui.py',
    'options_view_ui.py',
    'character_sheet.py',
    'main_window_view.py'
]

# Join the source files into a single string
source_files_str = ' '.join(source_files)

# List of translation files
translations = ['en.ts', 'pl.ts', 'de.ts']

# Generate the .ts files
for ts_file in translations:
    lupdate_command = f'pyside6-lupdate {source_files_str} -ts {ts_file}'
    print(f"Running: {lupdate_command}")
    subprocess.run(lupdate_command, shell=True, check=True)

# Generate the .qm files from the .ts files
for ts_file in translations:
    qm_file = ts_file.replace('.ts', '.qm')
    lrelease_command = f'pyside6-lrelease {ts_file} -qm {qm_file}'
    print(f"Running: {lrelease_command}")
    subprocess.run(lrelease_command, shell=True, check=True)
