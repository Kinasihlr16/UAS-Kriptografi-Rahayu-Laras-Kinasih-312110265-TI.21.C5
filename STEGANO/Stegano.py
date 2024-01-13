from stegano import lsb
secret = lsb.hide("download.jpeg", "RAHAYU LARAS KINASIH")
secret.save("here.png")
print(lsb.reveal("here.png"))