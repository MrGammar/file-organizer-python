import os
import shutil

folder_to_clean = 'C:/Users/dawid/Desktop/ExampleFileSegregation'

file_categories = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Photos': ['.jpg', '.png', '.jpeg'],
    'Installers': ['.exe', '.msi'],
    'Archives': ['.rar', '.zip', '.7z']
}

# Iterate through every element
for file in os.listdir(folder_to_clean):
    print(f'Found file: {file}')  # Display the found element in the console

    # Concatenate the folder path with the filename to get the full path
    full_path = os.path.join(folder_to_clean, file)

    # Check if the element is a file, skipping folders
    if os.path.isfile(full_path):

        # Extract the file extension and convert to lowercase
        extension = os.path.splitext(file)[1].lower()

        # Iterate through the defined categories in the dictionary
        for category, extensions in file_categories.items():
            if extension in extensions:  # Check if the file extension matches the current category list
                target_folder = os.path.join(
                    folder_to_clean, category)  # Define path

                # Create the category folder if it doesn't exist
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(
                    target_folder, file))  # Move the file to its designated folder
                break
