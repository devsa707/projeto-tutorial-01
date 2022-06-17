init python:
    def EscolherFundo():
        global locations
        global ImagemFundo
        ImagemFundo = location.lower()
        ImagemFundo = ImagemFundo.replace(" ", "_")
        ImagemFundo = "places/" + ImagemFundo + ".png"
