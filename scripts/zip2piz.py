import sys

def main():
    arguments = sys.argv[1:]

    for file in arguments:
        if 'zip' != file.split('.')[-1]:
            print(f'"{file}" is not .zip file')
            continue

        file_name = '.'.join(file.split('.')[:-1])
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


# specify zip files in 

if __name__ == '__main__':
    main()