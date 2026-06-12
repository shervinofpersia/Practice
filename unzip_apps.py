import zipfile
import os
import urllib.request

def main():
    # 1. Define file paths
    zip_url = "https://github.com/shervinofpersia/Practice/raw/refs/heads/main/apps.zip"
    zip_path = "apps.zip"
    extract_dir = "apps"

    # 2. Download the zip file from the raw GitHub URL
    print(f"Downloading {zip_url} ...")
    urllib.request.urlretrieve(zip_url, zip_path)
    print("Download completed.")

    # 3. Create extraction directory if it doesn't exist
    os.makedirs(extract_dir, exist_ok=True)

    # 4. Unzip all contents into the 'apps' folder
    print(f"Extracting to '{extract_dir}'...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("Extraction complete.")

    # 5. Clean up the downloaded zip file
    os.remove(zip_path)
    print("Temporary zip file removed.")

if __name__ == "__main__":
    main()
