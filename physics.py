g = 2500
FRICTION = 1000

class Physics:
    def get_friction():
        return FRICTION

    def set_friction(new):
        global FRICTION
        FRICTION = new

    def get_gravity():
        return g

    def set_gravity(new):
        global g
        g = new