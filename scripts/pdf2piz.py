import sys
import zipfile

def main():
    arguments = sys.argv[1:]

    for file in arguments:
        if 'pdf' != file.split('.')[-1]:
            print(f'"{file}" is not .pdf file')
            continue

        file_name = '.'.join(file.split('.')[:-1])

        with zipfile.ZipFile(f'{file_name}.zip', 'w') as zip_file:
            zip_file.write(file)

        file = f'{file_name}.zip'

        try:
            with open(file, 'rb') as bin_file:
                print(bin_file)
                data = bin_file.read()

                reversed_data = data[::-1]
                piz_file = f'{file_name}.piz'

                with open(piz_file, 'wb') as out:
                    out.write(reversed_data)

        except FileNotFoundError as e:
            print(f'Skipping file "{file}":', e)


# specify pdf files in arguments

if __name__ == '__main__':
    main()