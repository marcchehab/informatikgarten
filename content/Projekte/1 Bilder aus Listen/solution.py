import turtle
eva = turtle.Turtle()
px = 3
eva.width(px)
def paint(bild):
    for zeile in bild:
        for farbe in zeile:
            eva.color(farbe)
            eva.forward(px)
        eva.penup()
        eva.back(len(bild[0]*px))
        eva.right(90)
        eva.forward(px)
        eva.left(90)
        eva.pendown()

bild = [["#feffff", "#ffffff", "#ffffff", "#fefffe", "#fefeff", "#fffefe", "#ffffff", "#fffffe", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#feffff", "#cfcfcf", "#bfbebe", "#bebfbf", "#bfbfbf", "#bfbfbf", "#cfcfcf", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#fefeff", "#ffffff", "#feffff", "#fffffe"],
["#feffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#fffeff", "#ffffff", "#9f9f9f", "#4f4d3a", "#000000", "#1f1d0d", "#3e3a0e", "#3e3a0b", "#3e3a0b", "#3e3a0f", "#1f1d0c", "#000000", "#4f4d3a", "#9f9e9f", "#ffffff", "#fffffe", "#feffff", "#ffffff", "#fffffe", "#ffffff", "#fffffe", "#ffffff", "#fffeff", "#ffffff"],
["#fffffe", "#fffeff", "#fffffe", "#ffffff", "#fefeff", "#ffffff", "#ffffff", "#ffffff", "#8e8e88", "#0f0e09", "#2e2b0a", "#9d921b", "#dccd26", "#fcea2b", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#dccd27", "#9d921b", "#2e2b0a", "#0f0e09", "#7f7f79", "#ffffff", "#feffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#cfcfcf", "#2f2e20", "#2e2b0a", "#bdaf20", "#fcea2a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#bdaf20", "#2f2b0a", "#2e2e20", "#cfcfcf", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#fffeff"],
["#feffff", "#ffffff", "#ffffff", "#ffffff", "#fffeff", "#afafaf", "#0f0e07", "#7e7515", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#7e7515", "#0f0e06", "#afafaf", "#ffffff", "#ffffff", "#ffffff", "#fffeff", "#ffffff"],
["#fffefe", "#ffffff", "#ffffff", "#ffffff", "#afaeaf", "#000000", "#9d921b", "#fcea2a", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#9d921b", "#000000", "#afafaf", "#ffffff", "#ffffff", "#ffffff", "#fffffe"],
["#ffffff", "#ffffff", "#ffffff", "#cfcfcf", "#0f0e07", "#9c921b", "#fceb2b", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdeb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#9d921b", "#0f0e07", "#cfcfcf", "#fffffe", "#ffffff", "#ffffff"],
["#feffff", "#ffffff", "#ffffff", "#2f2e20", "#7f7515", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fdea2a", "#fcea2b", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#7e7515", "#2f2e20", "#ffffff", "#ffffff", "#feffff"],
["#ffffff", "#ffffff", "#7f7f79", "#2e2b0a", "#fcea2b", "#fceb2b", "#fceb2b", "#fcea2b", "#fcea2b", "#ecdb28", "#cdbe23", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fceb2b", "#fcea2b", "#fdea2b", "#fcea2b", "#cdbe23", "#ecdb28", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#2e2b0a", "#8f8e88", "#fffffe", "#ffffff"],
["#ffffff", "#ffffff", "#0e0e09", "#bdaf20", "#9d921b", "#332f09", "#080701", "#000000", "#000000", "#000000", "#1f1c05", "#000000", "#000000", "#1d1b05", "#a2961b", "#fcea2b", "#dccd26", "#847b16", "#1d1b05", "#000100", "#000000", "#1f1d05", "#000000", "#000000", "#000000", "#080701", "#332f09", "#9d931b", "#bdae20", "#0f0f09", "#ffffff", "#ffffff"],
["#fffeff", "#9f9f9f", "#2e2b0a", "#fcea2b", "#6e6613", "#0c0a02", "#59530f", "#eddb28", "#fcea2b", "#cdbe23", "#bdaf20", "#fcea2b", "#dccd26", "#2f2b08", "#111003", "#000100", "#000000", "#0b0b03", "#2f2b08", "#cec124", "#fcea2a", "#bdaf20", "#cdbe23", "#fcea2b", "#ecdb28", "#59530f", "#0c0a02", "#6e6613", "#fcea2b", "#2e2b0a", "#9f9f9f", "#ffffff"],
["#ffffff", "#4f4d3a", "#9d921b", "#fcea2b", "#56500f", "#0f0e02", "#fcea2a", "#fcea2a", "#7e7515", "#000000", "#000000", "#2e2b08", "#fcea2b", "#dccd26", "#070601", "#060601", "#131203", "#090902", "#dccd26", "#fcea2b", "#2e2b08", "#000000", "#000000", "#7e7515", "#fcea2b", "#fcea2b", "#171504", "#56500f", "#fcea2b", "#9d921b", "#4f4d3a", "#ffffff"],
["#feffff", "#010000", "#dccd26", "#fcea2b", "#665f11", "#524c0e", "#fcea2b", "#fcea2b", "#3e3a0b", "#000000", "#000000", "#010000", "#bdaf20", "#fcea2b", "#000000", "#252306", "#252306", "#000000", "#fcea2b", "#bdaf20", "#000000", "#000100", "#000000", "#3e3a0b", "#fcea2a", "#fceb2a", "#524c0e", "#665f11", "#fcea2b", "#dccd26", "#000000", "#ffffff"],
["#cfcfcf", "#1f1d0c", "#fcea2b", "#fcea2b", "#7e7515", "#6f6613", "#fcea2b", "#fcea2b", "#4e480d", "#000000", "#000100", "#000000", "#dccd26", "#ecdb28", "#000000", "#ecdb28", "#ecdb28", "#010000", "#ecdb28", "#dccd26", "#000000", "#000000", "#000000", "#4e480d", "#fcea2b", "#fcea2b", "#6e6613", "#7e7415", "#fcea2b", "#fcea2b", "#1f1d0c", "#cfcfcf"],
["#bfbfbf", "#3e3b0e", "#fcea2b", "#fcea2b", "#bdaf20", "#2e2b08", "#fcea2b", "#fcea2b", "#cdbe23", "#4e480d", "#3e3a0b", "#9d921b", "#fdea2b", "#9d921b", "#2e2b08", "#fcea2b", "#fcea2b", "#2e2b08", "#9d921b", "#fcea2b", "#9d921b", "#3e3a0b", "#4e480d", "#cdbe22", "#fcea2b", "#fcea2b", "#2e2b08", "#bdaf20", "#fcea2b", "#fcea2b", "#3e3a0e", "#bfbfbf"],
["#bfbebf", "#3e3a0b", "#fcea2b", "#fcea2b", "#ecdb28", "#0f0e03", "#cdbe23", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#ecdb29", "#1f1c05", "#9d921b", "#fcea2b", "#fcea2b", "#9d921b", "#1f1c05", "#eddb28", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#cdbe23", "#0f0e03", "#ecdb28", "#fcea2b", "#fcea2b", "#3e3a0b", "#bfbebf"],
["#bfbebe", "#3f3a0a", "#fcea2a", "#fcea2b", "#fdea2b", "#8d8318", "#0f0e03", "#ada01e", "#fcea2b", "#fcea2b", "#cdbe23", "#9d921a", "#1f1c05", "#5e5710", "#fcea2b", "#fcea2a", "#fceb2b", "#fcea2b", "#5e5710", "#1f1c05", "#9d921b", "#dccd26", "#fcea2b", "#fcea2b", "#ada11e", "#0f0e03", "#8d8318", "#fcea2b", "#fcea2b", "#fcea2a", "#3e3a0b", "#bfbfbf"],
["#bebebf", "#3e3b0e", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#9c921b", "#1f1c05", "#000000", "#000100", "#0f0e02", "#4e480d", "#9d921b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#ada11e", "#4e480d", "#0f0e03", "#000000", "#000000", "#1f1c05", "#9d921b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#3e3a0e", "#bfbfbf"],
["#cfcfcf", "#1f1d0c", "#fceb2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#1f1d0c", "#cfcfcf"],
["#fefffe", "#000100", "#dccd26", "#fcea2b", "#fcea2b", "#fdea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2a", "#fdea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#dccd26", "#000000", "#fffeff"],
["#fffefe", "#4f4d3a", "#9d921a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#8d8318", "#4f4d3b", "#ffffff"],
["#fffeff", "#9f9f9f", "#2e2a0a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2a", "#6e6612", "#7e7415", "#fdea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fceb2b", "#ecdb28", "#7e7515", "#6e6613", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#2e2b0a", "#9f9f9f", "#feffff"],
["#ffffff", "#ffffff", "#0f0e09", "#bdaf20", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#bdaf20", "#3e3a0b", "#0f0e03", "#6e6613", "#ada11e", "#cdbe23", "#fcea2b", "#ecdb28", "#bcaf20", "#8c8318", "#4e480d", "#000000", "#4e480d", "#bdaf20", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#bdaf20", "#0f0e09", "#ffffff", "#ffffff"],
["#ffffff", "#ffffff", "#8f8e88", "#2e2b0a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#cdbe23", "#7e7515", "#100f0a", "#1e1e19", "#000000", "#000000", "#3f3e32", "#17170f", "#9d921b", "#dccd26", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#2e2b0a", "#8f8e88", "#ffffff", "#ffffff"],
["#ffffff", "#ffffff", "#ffffff", "#2e2e20", "#7e7515", "#fcea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#000000", "#ffffff", "#3f3f3f", "#3f3f3f", "#ffffff", "#000000", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#7e7515", "#2f2e20", "#ffffff", "#feffff", "#ffffff"],
["#ffffff", "#ffffff", "#fefffe", "#cfcfcf", "#0f0e07", "#9d921b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#fceb2b", "#fcea2b", "#fcea2b", "#1f1e11", "#8f8f8f", "#3f3f3f", "#3f3e3f", "#8f8e8f", "#1f1e11", "#fceb2a", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#9d921b", "#0f0e07", "#cfcfcf", "#ffffff", "#ffffff", "#feffff"],
["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#afafaf", "#000000", "#9d921b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#cdbe23", "#2f2d19", "#090906", "#090905", "#2f2c19", "#cdbe23", "#fcea2b", "#fcea2a", "#fceb2b", "#fcea2a", "#fcea2b", "#fcea2b", "#9d921b", "#000000", "#afafaf", "#ffffff", "#ffffff", "#ffffff", "#fffffe"],
["#ffffff", "#ffffff", "#ffffff", "#feffff", "#ffffff", "#afafaf", "#0f0f07", "#7e7515", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdeb2b", "#7e7515", "#0f0e07", "#afafaf", "#feffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
["#ffffff", "#feffff", "#ffffff", "#fffffe", "#ffffff", "#ffffff", "#cfcfcf", "#2f2e21", "#2e2b0a", "#bdaf20", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fcea2b", "#fdea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#bdaf20", "#2e2b0a", "#2e2e20", "#cfcfcf", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
["#ffffff", "#ffffff", "#ffffff", "#fffeff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#8f8e88", "#0f0e09", "#2e2b0b", "#9d921b", "#dccd26", "#fcea2b", "#fcea2b", "#fcea2a", "#fcea2b", "#fcea2b", "#fcea2b", "#dccd27", "#9d921b", "#2e2b0a", "#0f0e09", "#8f8e88", "#ffffff", "#ffffff", "#ffffff", "#feffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
["#ffffff", "#ffffff", "#ffffff", "#fffffe", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#9f9f9f", "#4f4d3a", "#000000", "#1f1d0c", "#3e3a0e", "#3e3a0b", "#3e3a0b", "#3e3a0e", "#1f1d0c", "#010000", "#4f4d3a", "#9e9f9f", "#ffffff", "#ffffff", "#ffffff", "#fffffe", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
["#fffffe", "#ffffff", "#ffffff", "#ffffff", "#fffffe", "#ffffff", "#ffffff", "#fffeff", "#ffffff", "#ffffff", "#feffff", "#ffffff", "#ffffff", "#cfcfcf", "#bfbfbf", "#bfbfbf", "#bfbebf", "#bfbfbf", "#cfcfcf", "#ffffff", "#fffeff", "#fffffe", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#fffeff", "#ffffff", "#ffffff", "#ffffff", "#fffffe", "#fffeff"]]

paint(bild)