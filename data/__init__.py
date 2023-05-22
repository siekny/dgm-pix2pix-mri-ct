# import os
# import re
# import tqdm
# import shutil

# dir = '/home/edgpu/edgpu41/edgpu41_assignment/data/data/test'
# mri_files = os.listdir(f'{dir}/MRI/')
# ct_files = os.listdir(f'{dir}/CT/')

# count = 0
# for i, mri_file in tqdm.tqdm(enumerate(mri_files)):
#     for j, ct_file in enumerate(ct_files):
#     # num = re.findall(r'\d+', file)
#         if re.findall(r'\d+', mri_file.split('.')[0]) == re.findall(r'\d+', ct_file.split('.')[0]):
#             shutil.copy(f'{dir}/MRI/{mri_file}', f'{dir}/mri/{count}.png')
#             shutil.copy(f'{dir}/CT/{ct_file}', f'{dir}/ct/{count}.png')
#             count += 1