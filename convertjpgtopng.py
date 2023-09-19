from PIL import Image
import os


def convert_jpgs_to_pngs(input_folder, output_folder):
    try:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # List all files in the input folder
        files = os.listdir(input_folder)

        for file in files:
            if file.lower().endswith(".jpg"):
                input_path = os.path.join(input_folder, file)
                output_path = os.path.join(
                    output_folder, os.path.splitext(file)[0] + ".png")

                # Open the JPG image
                image = Image.open(input_path)

                # Save it as PNG
                image.save(output_path, "PNG")

                print(f"Conversion successful: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Replace with the path to your folder containing JPG images
    input_folder = "/Users/gokuljs/work-docs/script/class/brime/"
    # Replace with the desired output folder for PNG images
    output_folder = "/Users/gokuljs/work-docs/script/png/   "

    convert_jpgs_to_pngs(input_folder, output_folder)
