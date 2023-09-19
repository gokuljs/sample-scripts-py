import os


def rename_files_in_directory(directory_path):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(
        os.path.join(directory_path, f))]

    # Sort files to keep the original order (if required)
    files.sort()

    counter = 1
    for file in files:
        # Extract the file extension
        file_extension = os.path.splitext(file)[1]

        # Create the new name
        new_name = "image" + str(counter) + file_extension

        # Rename the file
        os.rename(os.path.join(directory_path, file),
                  os.path.join(directory_path, new_name))
        counter += 1

    print("Files renamed successfully!")


if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    rename_files_in_directory(directory_path)
