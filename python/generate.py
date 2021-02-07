from db import Base, engine


def generate():
  Base.metadata.create_all(engine)


if __name__ == '__main__':
  print("Start database generation")
  generate()
