def read_songs(path):
    with open(path, 'r', encoding='utf-8') as song:
        lines = song.readlines()
    lines.sort()
    for number, line in enumerate(lines, start=1):
        print(f"Line {number}: {line.strip()}")
    return lines

def songs_append(input_path, output_path):
    lines = read_songs(input_path)
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line.strip() + '\n')

songs_append('quijote.txt', 'new songs.txt')
