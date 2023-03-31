
def create_file_info(file, index):
  first_part_end = 0
  number_part_end = 0
  file_length = len(file)
  for i in range(file_length):
    if '0' <= file[i] <= '9':
      first_part_end = i - 1
      break
  number = ''
  for i in range(first_part_end + 1, file_length):
    if '0' <= file[i] <= '9':
      number += file[i]
    else:
      number_part_end = i - 1
      break
  number = int(number)
  last_part = ''
  if number_part_end != 0:
    last_part = file[number_part_end + 1:file_length]


  return [file[0:first_part_end + 1].lower(), number, last_part.lower(), index]


def create_file_infos(files, file_infos):
  for i, file in enumerate(files):
    file_infos.append(create_file_info(file, i))


def sort_file_infos(file_infos):
  file_infos.sort(key=lambda x: (x[0], x[1], x[3]))


def solution(files):
  answer = []
  file_infos = []
  create_file_infos(files, file_infos)
  sort_file_infos(file_infos)
  for file_info in file_infos:
    index = file_info[3]
    answer.append(files[index])
  return answer