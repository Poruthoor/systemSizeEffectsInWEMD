import argparse
from pathlib import Path

def add_offset_to_column(data_file, offset):

    output_file = Path(data_file).stem + '.dat'
    #  output_file = Path(data_file).stem + '_offset.dat'

    with open(data_file, 'r') as file:
        header = file.readline().strip()  # Read the header
        with open(output_file, 'w') as out_file:
            out_file.write(header + ' OFFSETTED\n')  # Write header to the new file
            for line in file:
                if not line.startswith('#'):
                    columns = line.strip().split()  # Assuming space-delimited
                    columns[1] = str(float(columns[1]) + offset) # Add offset to second column
                    out_file.write(' '.join(columns) + '\n')  # Write modified line to new file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add an offset value to the second column of a data file.')
    parser.add_argument('data_file', type=str, help='Path to the data file')
    parser.add_argument('offset', type=float, help='Offset value to add to the second column')
    args = parser.parse_args()
    add_offset_to_column(args.data_file, args.offset)
