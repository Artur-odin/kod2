from zipfile import ZipFile

d = {"B": 0, "KB": 1, "MB": 2, "GB": 3}
# B = 1024**0, KB = 1024**1, MB = 1024**2, GB = 1024**3
with ZipFile("desktop.zip", mode="r") as zip_file:
    info = zip_file.infolist()

    for i in info:
        spl_i = i.filename.split("/")
        dir = i.is_dir()

        maks_size = min(filter(lambda x: x[0] >= 1, [[i.file_size / 1024 ** value, " " + key] for key, value in d.items()]), key=lambda x: x[0]) if not dir else ["", ""]

        print(f"{((len(spl_i) - dir - 1) * 2) * ' '}{spl_i[-2 if dir else -1]} {str(round(maks_size[0]) if not dir else "") + maks_size[1]}")