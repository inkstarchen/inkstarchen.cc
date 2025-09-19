import os

def rename_files_in_assets(root="."):
    for dirpath, dirnames, filenames in os.walk(root):
        # 只处理路径中包含 assets 的目录
        if os.path.basename(dirpath) == "assets":
            for filename in filenames:
                if " " in filename:
                    old_path = os.path.join(dirpath, filename)
                    new_filename = filename.replace("%", "_")
                    new_path = os.path.join(dirpath, new_filename)

                    os.rename(old_path, new_path)
                    print(f"已重命名: {old_path} -> {new_path}")

if __name__ == "__main__":
    rename_files_in_assets(".")
