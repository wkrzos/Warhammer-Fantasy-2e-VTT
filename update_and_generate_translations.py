import os
import subprocess

# Define the paths
frontend_dir = 'frontend'
translations_dir = 'translations'

# List of languages
languages = ['en', 'pl', 'de']

# Gather all Python files in the frontend directory
py_files = []
for root, dirs, files in os.walk(frontend_dir):
    for file in files:
        if file.endswith('.py'):
            py_files.append(os.path.join(root, file))

# Join the files into a single string
py_files_str = ' '.join(py_files)

# Run pyside6-lupdate for each language to update .ts files
for lang in languages:
    ts_file = os.path.join(translations_dir, f'{lang}.ts')
    command = f'pyside6-lupdate {py_files_str} -ts {ts_file}'
    subprocess.run(command, shell=True)
    print(f'Updated {ts_file}')

# Run pyside6-lrelease for each language to generate .qm files
for lang in languages:
    ts_file = os.path.join(translations_dir, f'{lang}.ts')
    qm_file = os.path.join(translations_dir, f'{lang}.qm')
    command = f'pyside6-lrelease {ts_file} -qm {qm_file}'
    subprocess.run(command, shell=True)
    print(f'Generated {qm_file}')

print("Translation files updated and .qm files generated successfully.")
