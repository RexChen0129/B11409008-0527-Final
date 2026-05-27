import os
import json

FILE_NAME = "lib_data.json"  # 改用 JSON 格式儲存資料

def load_library_data():
    """從檔案載入圖書資料"""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)  # 使用 JSON 解析檔案
            except json.JSONDecodeError:
                print("檔案格式錯誤，無法載入資料")
                return []
    return []

def save_library_data(library_data):
    """將圖書資料儲存到檔案"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(library_data, file, ensure_ascii=False, indent=4)

def isbn_exists(library_data, isbn):
    """檢查指定 ISBN 是否存在於圖書資料中"""
    return any(book['isbn'] == isbn for book in library_data)

def main():
    library_data = load_library_data()  # 載入圖書資料
    print("=== 圖書管理系統 v0.1 (Refactored) ===")
    
    while True:
        op = input("> ").strip()
        
        if op == "exit":
            save_library_data(library_data)  # 儲存圖書資料
            print("系統關閉")
            break
            
        elif op.startswith("add "):
            raw = op[4:].split("/")
            if len(raw) == 3:
                title, isbn, status = raw
                if not isbn_exists(library_data, isbn):
                    library_data.append({"title": title, "isbn": isbn, "status": status})
                    print("Success")
                else:
                    print("ISBN 已存在")
            else:
                print("格式錯誤，請使用: add 書名/ISBN/狀態")
                
        elif op == "show":
            for book in library_data:
                print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")
                
        elif op.startswith("borrow "):
            target_isbn = op[7:]
            for book in library_data:
                if book['isbn'] == target_isbn:
                    if book['status'] != "borrowed":
                        book['status'] = "borrowed"
                        print("已更新狀態為借出")
                    else:
                        print("此書已被借出")
                    break
            else:
                print("找不到指定的 ISBN")
        else:
            print("未知指令")

if __name__ == "__main__":
    main()