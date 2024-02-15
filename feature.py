from flask import Flask

FAI = Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return '<center><marquee>Hai This is my Karim"s First Flask Project</marquee></h1></center>'


@FAI.route('/secondStringResponse')
def secondStringResponse():
    return '<center><h1 style="color :red">Hello World...!!</h1></center>'


if __name__ == '__main__':
    FAI.run(debug = True)


