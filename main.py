from rocketry import Rocketry


app = Rocketry()


@app.task('minutely')
def do_things():
    print('hola')


if __name__ == "__main__":
    app.run()
