##author: Hao Cheng, Contact : 材料计算学习笔记 公众号


import os

def extract_dump_data(file_path, indices):
    """
    从 LAMMPS dump 文件中提取指定列的数据。
    :param file_path: dump 文件路径
    :param indices: 需要提取的列索引（从0开始）
    :return: 提取的数据列表, 原子数, 帧数
    """
    with open(file_path, 'r') as infile:
        content = infile.readlines()

    result = []
    i = 0
    num_atoms = 0
    frame_count = 0
    atom_lines_per_frame = 0

    while i < len(content):
        if content[i].startswith("ITEM: NUMBER OF ATOMS"):
            num_atoms = int(content[i + 1].strip())
            atom_lines_per_frame = num_atoms
            i += 2
        elif content[i].startswith("ITEM: ATOMS"):
            frame_count += 1
            i += 1
            for j in range(atom_lines_per_frame):
                if i + j < len(content):
                    line_data = content[i + j].strip().split()
                    try:
                        selected = [float(line_data[k]) for k in indices]
                        result.append(selected)
                    except IndexError:
                        print(f"[WARNING] Skipping malformed line {i + j + 1}: {content[i + j].strip()}")
            i += atom_lines_per_frame
        else:
            i += 1

    return result, num_atoms, frame_count

def write_data_pretty(data_list, destination_path):
    """
    将数据写入文件，每列对齐间隔一致。
    """
    with open(destination_path, 'w') as fout:
        for row in data_list:
            formatted = '\t'.join([str(item).ljust(15) for item in row])  # 每列宽15字符
            fout.write(formatted + '\n')

if __name__ == '__main__':
    # 输入和输出文件路径
    input_path = 'C:/Users/26690/Desktop/wendu/dump.txt'
    output_path = 'C:/Users/26690/Desktop/wendu/dumpout.txt'

    # 指定要提取的列索引（从0开始）
    indices_to_get = [0, 1, 2, 3, 4, 5, 6, 7]

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    print("Starting dump file extraction...")
    velocity, natoms, nframes = extract_dump_data(input_path, indices_to_get)

    print(f"\nThe number of atoms in dumpfile is {natoms}")
    print(f"The frame number of the dumpfile is {nframes}\n")

    write_data_pretty(velocity, output_path)
    print(f"Data saved to: {output_path}")
