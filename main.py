import os
import re
import zipfile
import shutil
from tqdm import tqdm

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
TEMP_DIR = "./data"
COMMAND_REGEX = re.compile(r"^\s*([a-z_]+)(?=[\s{])")

def add_minecraft_prefix_to_command(line: str) -> str:
    match = COMMAND_REGEX.match(line)
    if match:
        command = match.group(1)
        if not command.startswith("minecraft:") and ":" not in command:
            line = line.replace(command, f"minecraft:{command}", 1)
    return line

def process_mcfunction_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = [add_minecraft_prefix_to_command(line) for line in lines]
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def get_all_mcfunction_files(root_path: str):
    mcfunction_files = []
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith(".mcfunction"):
                mcfunction_files.append(os.path.join(root, file))
    return mcfunction_files

def extract_zip(input_zip, extract_to):
    with zipfile.ZipFile(input_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def create_zip_from_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, folder_path)
                zipf.write(abs_path, rel_path)

if __name__ == "__main__":
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True)

    zip_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".zip")]
    if not zip_files:
        print("❌ Keine ZIP-Datei im Ordner 'input' gefunden!")
        exit(1)

    input_zip = os.path.join(INPUT_DIR, zip_files[0])
    print(f"📦 Verwende ZIP-Datei: {zip_files[0]}")

    print("📂 Entpacke Datapack...")
    extract_zip(input_zip, TEMP_DIR)

    mcfunction_files = get_all_mcfunction_files(TEMP_DIR)
    if not mcfunction_files:
        print("❌ Keine .mcfunction-Dateien gefunden!")
    else:
        print(f"🔍 {len(mcfunction_files)} .mcfunction-Dateien gefunden.\n")
        for file_path in tqdm(mcfunction_files, desc="Bearbeite Dateien", unit="Datei"):
            process_mcfunction_file(file_path)

        input_name = os.path.splitext(zip_files[0])[0]
        output_name = f"{input_name}_converted.zip"
        output_zip = os.path.join(OUTPUT_DIR, output_name)

        print("\n📦 Erstelle neue ZIP-Datei...")
        create_zip_from_folder(TEMP_DIR, output_zip)
        print(f"✅ Fertig! Neue Datei gespeichert unter: {output_zip}")

    shutil.rmtree(TEMP_DIR)
    print("🧹 Temporäre Dateien entfernt.")
