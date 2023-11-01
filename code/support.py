"""import game assets"""
from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    """importing CSV and implement it into list"""
    terrain_map = []
    with open(path, encoding='utf-8') as level_map:
        layout=reader(level_map, delimiter= ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    """importing img files implement it into list"""
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            list(full_path).sort()
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
