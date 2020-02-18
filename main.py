import ctypes
from datetime import datetime

wallpaper1 = "C:/Uni/lake_mountains_forest.jpg"
wallpaper2 = "C:/Uni/573224.jpg"
#wallpaperW = str.decode(r"C:\Uni\lake_forest_mountains_148683_3840x2160.jpg")



def timed_wallpaper(wallpaper_path,planned_time):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if(planned_time == current_time):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)


#i need a cron job
timed_wallpaper(wallpaper2,"22:34")
